"""
Main orchestrator — runs all analyses and generates visualizations.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data.technology_data import get_all_datasets, impact_matrix
from analysis.trend_analysis import run_all_trend_analyses
from analysis.clustering_analysis import run_clustering_analysis
from analysis.convergence_model import run_convergence_analysis
from visualizations.generate_charts import generate_all_charts

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')


def main():
    print("=" * 60)
    print("THE HARD TECH REVOLUTION — Analysis Pipeline")
    print("=" * 60)

    # 1. Load datasets
    print("\n[1/4] Loading curated datasets...")
    datasets = get_all_datasets()
    print(f"  Loaded {len(datasets)} datasets")

    # 2. Trend analysis
    print("\n[2/4] Running trend analyses (regression, curve fitting)...")
    analyzer, trend_results = run_all_trend_analyses(datasets)
    for name, res in trend_results.items():
        if isinstance(res, dict) and 'r2' in res:
            print(f"  {name}: R² = {res['r2']:.4f}")

    # 3. Clustering analysis
    print("\n[3/4] Running clustering analysis (K-Means + PCA)...")
    cluster_results = run_clustering_analysis(impact_matrix)
    print(f"  Silhouette Score: {cluster_results['silhouette_score']:.4f}")
    print(f"  PCA Explained Variance: {cluster_results['pca_explained_variance']}")
    print(f"  Cluster assignments:")
    for _, row in cluster_results['summary'].iterrows():
        print(f"    {row['technology']:25s} -> {row['cluster_name']}")

    # 4. Convergence analysis (PyTorch)
    print("\n[4/4] Training convergence neural network (PyTorch)...")
    convergence_results = run_convergence_analysis(impact_matrix)
    print(f"  Final training loss: {convergence_results['final_loss']:.6f}")
    print(f"  Top convergent pairs:")
    for _, row in convergence_results['top_pairs'].head(5).iterrows():
        print(f"    {row['tech_1']} × {row['tech_2']}: {row['convergence_score']:.3f}")

    # 5. Generate charts
    print("\n[5/5] Generating publication-quality visualizations...")
    chart_paths = generate_all_charts(datasets, cluster_results, convergence_results, OUTPUT_DIR)
    for name, path in chart_paths.items():
        print(f"  ✓ {name}: {path}")

    print("\n" + "=" * 60)
    print("Analysis complete. All outputs saved to:", OUTPUT_DIR)
    print("=" * 60)

    return datasets, trend_results, cluster_results, convergence_results, chart_paths


if __name__ == '__main__':
    main()
