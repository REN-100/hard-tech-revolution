"""
Convergence Model — PyTorch neural network that scores technology convergence potential.
Uses a Multi-Layer Perceptron to model cross-sector synergy scores.
"""

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import MinMaxScaler


class ConvergenceNet(nn.Module):
    """Neural network for scoring technology convergence potential."""

    def __init__(self, input_dim=5, hidden_dims=[64, 32, 16]):
        super(ConvergenceNet, self).__init__()

        layers = []
        prev_dim = input_dim
        for h_dim in hidden_dims:
            layers.append(nn.Linear(prev_dim, h_dim))
            layers.append(nn.BatchNorm1d(h_dim))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(0.2))
            prev_dim = h_dim
        layers.append(nn.Linear(prev_dim, 1))
        layers.append(nn.Sigmoid())

        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)


class ConvergenceAnalyzer:
    """Analyzes cross-sector convergence potential using a neural network."""

    def __init__(self):
        self.model = None
        self.scaler = MinMaxScaler()
        self.convergence_matrix = None

    def _create_pairwise_features(self, impact_matrix):
        """Create feature vectors for each pair of technologies."""
        n = len(impact_matrix)
        pairs = []
        pair_labels = []

        for i in range(n):
            for j in range(i + 1, n):
                row_i = impact_matrix.iloc[i]
                row_j = impact_matrix.iloc[j]

                # Features: avg readiness, readiness gap, avg potential,
                #           market size ratio, combined growth
                avg_readiness = (row_i['readiness_level'] + row_j['readiness_level']) / 2
                readiness_gap = abs(row_i['readiness_level'] - row_j['readiness_level'])
                avg_potential = (row_i['societal_potential'] + row_j['societal_potential']) / 2
                market_ratio = min(row_i['current_market_B'], row_j['current_market_B']) / \
                              (max(row_i['current_market_B'], row_j['current_market_B']) + 1e-6)
                combined_growth = (row_i['projected_2035_B'] / (row_i['current_market_B'] + 1) +
                                  row_j['projected_2035_B'] / (row_j['current_market_B'] + 1)) / 2

                pairs.append([avg_readiness, readiness_gap, avg_potential,
                             market_ratio, combined_growth])
                pair_labels.append((row_i['technology'], row_j['technology']))

        return np.array(pairs), pair_labels

    def _generate_synthetic_targets(self, features):
        """
        Generate convergence scores based on domain knowledge heuristics.
        Higher scores for: high readiness, low readiness gap, high potential,
        balanced market sizes, and high growth.
        """
        scores = np.zeros(len(features))
        for i, feat in enumerate(features):
            avg_readiness, readiness_gap, avg_potential, market_ratio, combined_growth = feat
            # Weighted heuristic scoring
            score = (0.25 * avg_readiness / 10 +
                    0.15 * (1 - readiness_gap / 10) +
                    0.30 * avg_potential / 10 +
                    0.10 * market_ratio +
                    0.20 * min(combined_growth / 20, 1))
            # Add noise for training
            scores[i] = np.clip(score + np.random.normal(0, 0.05), 0, 1)
        return scores

    def train_model(self, impact_matrix, epochs=200, lr=0.001):
        """Train the convergence neural network."""
        features, pair_labels = self._create_pairwise_features(impact_matrix)
        targets = self._generate_synthetic_targets(features)

        # Scale features
        features_scaled = self.scaler.fit_transform(features)

        # Convert to tensors
        X = torch.FloatTensor(features_scaled)
        y = torch.FloatTensor(targets).unsqueeze(1)

        # Initialize model
        self.model = ConvergenceNet(input_dim=features.shape[1])
        optimizer = optim.Adam(self.model.parameters(), lr=lr)
        criterion = nn.MSELoss()

        # Training loop
        self.model.train()
        losses = []
        for epoch in range(epochs):
            optimizer.zero_grad()
            output = self.model(X)
            loss = criterion(output, y)
            loss.backward()
            optimizer.step()
            losses.append(loss.item())

        return losses, pair_labels

    def predict_convergence(self, impact_matrix):
        """Generate convergence score matrix for all technology pairs."""
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")

        features, pair_labels = self._create_pairwise_features(impact_matrix)
        features_scaled = self.scaler.transform(features)

        self.model.eval()
        with torch.no_grad():
            X = torch.FloatTensor(features_scaled)
            scores = self.model(X).numpy().flatten()

        # Build symmetric matrix
        n = len(impact_matrix)
        matrix = np.eye(n)
        idx = 0
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i, j] = scores[idx]
                matrix[j, i] = scores[idx]
                idx += 1

        techs = impact_matrix['technology'].values
        self.convergence_matrix = pd.DataFrame(matrix, index=techs, columns=techs)

        return self.convergence_matrix, pair_labels, scores

    def get_top_convergences(self, n=10):
        """Get the top N most convergent technology pairs."""
        if self.convergence_matrix is None:
            raise ValueError("Must run predict_convergence() first.")

        matrix = self.convergence_matrix.values
        techs = self.convergence_matrix.index
        n_tech = len(techs)

        pairs = []
        for i in range(n_tech):
            for j in range(i + 1, n_tech):
                pairs.append({
                    'tech_1': techs[i],
                    'tech_2': techs[j],
                    'convergence_score': matrix[i, j]
                })

        df = pd.DataFrame(pairs).sort_values('convergence_score', ascending=False)
        return df.head(n)


def run_convergence_analysis(impact_matrix):
    """Execute full convergence analysis."""
    analyzer = ConvergenceAnalyzer()

    # Train the model
    torch.manual_seed(42)
    np.random.seed(42)
    losses, pair_labels = analyzer.train_model(impact_matrix, epochs=300)

    # Generate convergence predictions
    conv_matrix, _, scores = analyzer.predict_convergence(impact_matrix)

    # Get top convergent pairs
    top_pairs = analyzer.get_top_convergences(n=15)

    return {
        'analyzer': analyzer,
        'training_losses': losses,
        'convergence_matrix': conv_matrix,
        'top_pairs': top_pairs,
        'final_loss': losses[-1],
    }
