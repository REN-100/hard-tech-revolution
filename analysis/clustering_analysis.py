"""
Clustering Analysis Module — K-Means clustering and PCA for technology landscape.
Groups technologies by readiness and societal impact to generate the Impact Matrix.
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score


class TechnologyClusterer:
    """Clusters technologies by readiness level and societal potential."""

    def __init__(self):
        self.scaler = StandardScaler()
        self.kmeans = None
        self.pca = None
        self.labels = None
        self.cluster_centers = None

    def prepare_features(self, impact_matrix):
        """Prepare feature matrix from impact data."""
        features = impact_matrix[['readiness_level', 'societal_potential',
                                   'current_market_B', 'projected_2035_B']].copy()
        # Log-transform market sizes to reduce skew
        features['current_market_log'] = np.log1p(features['current_market_B'])
        features['projected_2035_log'] = np.log1p(features['projected_2035_B'])
        features['growth_ratio'] = features['projected_2035_B'] / (features['current_market_B'] + 1)

        feature_cols = ['readiness_level', 'societal_potential',
                       'current_market_log', 'projected_2035_log', 'growth_ratio']
        X = features[feature_cols].values
        X_scaled = self.scaler.fit_transform(X)
        return X_scaled, feature_cols

    def cluster(self, impact_matrix, n_clusters=4):
        """Perform K-Means clustering on technology features."""
        X_scaled, feature_cols = self.prepare_features(impact_matrix)

        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.labels = self.kmeans.fit_predict(X_scaled)
        self.cluster_centers = self.kmeans.cluster_centers_

        sil_score = silhouette_score(X_scaled, self.labels)

        # Map cluster labels to meaningful names
        cluster_names = self._name_clusters(impact_matrix, self.labels, n_clusters)

        return self.labels, sil_score, cluster_names

    def _name_clusters(self, impact_matrix, labels, n_clusters):
        """Assign descriptive names to clusters based on characteristics."""
        names = {}
        for i in range(n_clusters):
            mask = labels == i
            avg_readiness = impact_matrix.loc[mask, 'readiness_level'].mean()
            avg_potential = impact_matrix.loc[mask, 'societal_potential'].mean()

            if avg_readiness >= 6 and avg_potential >= 8:
                names[i] = 'Ready & Transformative'
            elif avg_readiness >= 6 and avg_potential < 8:
                names[i] = 'Commercially Maturing'
            elif avg_readiness < 6 and avg_potential >= 8:
                names[i] = 'High-Potential Frontier'
            else:
                names[i] = 'Emerging Research'
        return names

    def reduce_dimensions(self, impact_matrix, n_components=2):
        """Apply PCA for 2D visualization of the technology landscape."""
        X_scaled, _ = self.prepare_features(impact_matrix)

        self.pca = PCA(n_components=n_components, random_state=42)
        X_pca = self.pca.fit_transform(X_scaled)

        explained_var = self.pca.explained_variance_ratio_

        return X_pca, explained_var

    def get_cluster_summary(self, impact_matrix):
        """Generate a summary table of cluster assignments."""
        if self.labels is None:
            raise ValueError("Must run cluster() first")

        df = impact_matrix.copy()
        df['cluster'] = self.labels
        _, _, cluster_names = self.cluster(impact_matrix)
        df['cluster_name'] = df['cluster'].map(cluster_names)

        return df[['technology', 'readiness_level', 'societal_potential',
                   'current_market_B', 'cluster_name']]


def run_clustering_analysis(impact_matrix):
    """Execute full clustering analysis and return results."""
    clusterer = TechnologyClusterer()

    # K-Means clustering
    labels, sil_score, cluster_names = clusterer.cluster(impact_matrix, n_clusters=4)

    # PCA dimensionality reduction
    X_pca, explained_var = clusterer.reduce_dimensions(impact_matrix)

    # Summary
    summary = clusterer.get_cluster_summary(impact_matrix)

    return {
        'clusterer': clusterer,
        'labels': labels,
        'silhouette_score': sil_score,
        'cluster_names': cluster_names,
        'pca_coords': X_pca,
        'pca_explained_variance': explained_var,
        'summary': summary,
    }
