"""
Trend Analysis Module — Regression models for technology trajectories.
Uses sklearn for polynomial/exponential regression and scipy for curve fitting.
Generates forecasts with confidence intervals.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error
from scipy.optimize import curve_fit
from scipy.stats import t as t_dist
import warnings
warnings.filterwarnings('ignore')


def exponential_decay(x, a, b, c):
    """Exponential decay: y = a * exp(-b * x) + c"""
    return a * np.exp(-b * x) + c


def exponential_growth(x, a, b, c):
    """Exponential growth: y = a * exp(b * x) + c"""
    return a * np.exp(b * x) + c


def logistic_growth(x, L, k, x0, b):
    """Logistic growth: y = L / (1 + exp(-k*(x-x0))) + b"""
    return L / (1 + np.exp(-k * (x - x0))) + b


class TrendAnalyzer:
    """Performs trend analysis on technology datasets."""

    def __init__(self):
        self.models = {}
        self.results = {}

    def fit_polynomial(self, x, y, degree=2, name='model'):
        """Fit polynomial regression and store results."""
        x_arr = np.array(x).reshape(-1, 1)
        y_arr = np.array(y)

        poly = PolynomialFeatures(degree=degree)
        x_poly = poly.fit_transform(x_arr)

        model = LinearRegression()
        model.fit(x_poly, y_arr)

        y_pred = model.predict(x_poly)
        r2 = r2_score(y_arr, y_pred)
        rmse = np.sqrt(mean_squared_error(y_arr, y_pred))

        self.models[name] = {'model': model, 'poly': poly, 'degree': degree}
        self.results[name] = {'r2': r2, 'rmse': rmse, 'coefficients': model.coef_}

        return model, poly, r2, rmse

    def predict_polynomial(self, name, x_future):
        """Generate predictions from a fitted polynomial model."""
        x_arr = np.array(x_future).reshape(-1, 1)
        poly = self.models[name]['poly']
        model = self.models[name]['model']
        x_poly = poly.transform(x_arr)
        return model.predict(x_poly)

    def fit_exponential_decay(self, x, y, name='decay_model'):
        """Fit exponential decay curve (e.g., for cost reduction)."""
        x_arr = np.array(x, dtype=float)
        y_arr = np.array(y, dtype=float)

        # Normalize x to start from 0
        x_norm = x_arr - x_arr.min()

        try:
            popt, pcov = curve_fit(exponential_decay, x_norm, y_arr,
                                   p0=[y_arr.max(), 0.1, y_arr.min()],
                                   maxfev=10000)
            y_pred = exponential_decay(x_norm, *popt)
            r2 = r2_score(y_arr, y_pred)

            self.models[name] = {
                'params': popt, 'cov': pcov, 'x_min': x_arr.min(), 'type': 'decay'
            }
            self.results[name] = {'r2': r2, 'params': popt}
            return popt, r2
        except RuntimeError:
            return None, 0.0

    def fit_exponential_growth(self, x, y, name='growth_model'):
        """Fit exponential growth curve (e.g., for market expansion)."""
        x_arr = np.array(x, dtype=float)
        y_arr = np.array(y, dtype=float)
        x_norm = x_arr - x_arr.min()

        try:
            popt, pcov = curve_fit(exponential_growth, x_norm, y_arr,
                                   p0=[y_arr.min(), 0.1, 0],
                                   maxfev=10000)
            y_pred = exponential_growth(x_norm, *popt)
            r2 = r2_score(y_arr, y_pred)

            self.models[name] = {
                'params': popt, 'cov': pcov, 'x_min': x_arr.min(), 'type': 'growth'
            }
            self.results[name] = {'r2': r2, 'params': popt}
            return popt, r2
        except RuntimeError:
            return None, 0.0

    def predict_exponential(self, name, x_future):
        """Predict using fitted exponential model."""
        model_info = self.models[name]
        x_norm = np.array(x_future, dtype=float) - model_info['x_min']
        if model_info['type'] == 'decay':
            return exponential_decay(x_norm, *model_info['params'])
        else:
            return exponential_growth(x_norm, *model_info['params'])

    def compute_cagr(self, start_value, end_value, years):
        """Compute Compound Annual Growth Rate."""
        if start_value <= 0 or end_value <= 0 or years <= 0:
            return 0.0
        return (end_value / start_value) ** (1 / years) - 1

    def generate_confidence_interval(self, y_pred, y_actual, x_future_len, confidence=0.95):
        """Generate confidence intervals for predictions."""
        n = len(y_actual)
        residuals = y_actual - y_pred[:n] if len(y_pred) >= n else y_actual - y_pred
        se = np.std(residuals)
        t_val = t_dist.ppf((1 + confidence) / 2, df=max(n - 2, 1))
        margin = t_val * se
        return margin


def run_all_trend_analyses(datasets):
    """Run trend analyses on all technology datasets. Returns analyzer and results dict."""
    analyzer = TrendAnalyzer()
    results = {}

    # 1. Battery energy density — polynomial regression
    batt = datasets['battery_data'].dropna(subset=['solid_state_Wh_kg'])
    analyzer.fit_polynomial(batt['year'], batt['solid_state_Wh_kg'], degree=2, name='battery_density')
    future_years = np.arange(2026, 2036)
    batt_pred = analyzer.predict_polynomial('battery_density', future_years)
    results['battery_density'] = {
        'future_years': future_years, 'predictions': batt_pred,
        'r2': analyzer.results['battery_density']['r2']
    }

    # 2. Space launch cost — exponential decay
    space = datasets['space_data']
    popt, r2 = analyzer.fit_exponential_decay(space['year'], space['launch_cost_per_kg'], name='launch_cost')
    future_years_space = np.arange(2026, 2036)
    launch_pred = analyzer.predict_exponential('launch_cost', future_years_space)
    results['launch_cost'] = {
        'future_years': future_years_space, 'predictions': np.maximum(launch_pred, 50),
        'r2': r2
    }

    # 3. DAC cost — exponential decay
    dac = datasets['dac_data']
    popt_dac, r2_dac = analyzer.fit_exponential_decay(dac['year'], dac['cost_per_ton_usd'], name='dac_cost')
    future_dac = np.arange(2026, 2040)
    dac_pred = analyzer.predict_exponential('dac_cost', future_dac)
    results['dac_cost'] = {
        'future_years': future_dac, 'predictions': np.maximum(dac_pred, 50),
        'r2': r2_dac
    }

    # 4. Gene editing trials — polynomial growth
    gene = datasets['gene_editing_data']
    analyzer.fit_polynomial(gene['year'], gene['active_clinical_trials'], degree=2, name='gene_trials')
    future_gene = np.arange(2026, 2036)
    gene_pred = analyzer.predict_polynomial('gene_trials', future_gene)
    results['gene_trials'] = {
        'future_years': future_gene, 'predictions': gene_pred,
        'r2': analyzer.results['gene_trials']['r2']
    }

    # 5. Synthetic biology market — exponential growth
    synbio = datasets['synbio_data']
    popt_syn, r2_syn = analyzer.fit_exponential_growth(synbio['year'], synbio['market_size_B'], name='synbio_market')
    results['synbio_market'] = {'r2': r2_syn}

    # 6. BCI error rate — exponential decay
    bci = datasets['bci_data']
    popt_bci, r2_bci = analyzer.fit_exponential_decay(bci['year'], bci['error_rate_pct'], name='bci_error')
    results['bci_error'] = {'r2': r2_bci}

    # Compute CAGRs for key markets
    cagrs = {}
    for name, df, col in [
        ('synbio', synbio, 'market_size_B'),
        ('batteries', datasets['battery_market'], 'market_size_B'),
    ]:
        start_idx, end_idx = 0, len(df) - 1
        cagrs[name] = analyzer.compute_cagr(
            df[col].iloc[start_idx], df[col].iloc[end_idx],
            df['year'].iloc[end_idx] - df['year'].iloc[start_idx]
        )
    results['cagrs'] = cagrs

    return analyzer, results
