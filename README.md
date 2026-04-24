# The Hard Tech Revolution: What Actually Comes After the AI Boom

An evidence-based analysis of the 12 technologies defining the next physical chapter of human progress. This repository contains the data, ML/DL analysis code, and publication-quality visualizations for the research paper.

## Overview

The AI boom was Chapter One. The physical revolution — **The Hard Tech Revolution** — is Chapter Two. This project analyzes 12 transformative technologies across four domains using machine learning and deep learning techniques.

## Technologies Analyzed

| Domain | Technologies |
|--------|-------------|
| **Energy Bedrock** | Nuclear Fusion, Next-Gen Batteries, Direct Air Capture |
| **Biological Rewrite** | Gene Editing (CRISPR), Synthetic Biology, Regenerative Biotech |
| **Atomic/Compute Edge** | Nanotechnology, Advanced Materials, Quantum Computing, BCI |
| **New Infrastructure** | Space Infrastructure, DePIN / DLT |

## ML/DL Methods

- **Polynomial & Exponential Regression** (sklearn, scipy) — Trend forecasting for cost curves, market growth, and clinical trial expansion
- **K-Means Clustering + PCA** (sklearn) — Technology landscape clustering and dimensionality reduction
- **PyTorch Neural Network** — Multi-layer perceptron for cross-sector convergence scoring
- **Confidence Intervals** — Statistical uncertainty quantification for all forecasts

## Data Sources

| Domain | Sources |
|--------|---------|
| Energy | IEA State of Energy Innovation 2026, Fusion Industry Association |
| Batteries | IEA, Electrive, Bonnenbatteries, Fortune Business Insights |
| DAC | Climeworks, US DOE, Fortune Business Insights |
| Gene Editing | ClinicalTrials.gov, Innovative Genomics Institute, CRISPR Therapeutics |
| Synthetic Biology | Grand View Research, Coherent Market Insights, BioSpace |
| Regen Biotech | Mordor Intelligence, Technavio, IMARC Group |
| Nanotech | Mordor Intelligence, NovaOne Advisor |
| Materials | GM Insights, IDTechEx, Precedence Research |
| Quantum | IBM Research, Google Quantum AI |
| BCI | SNS Insider, Neuralink, Economic Times |
| Space | Precedence Research, Goldman Sachs, Morgan Stanley |
| DePIN | KuCoin Research, Binance Research, Messari |
| VC Trends | PitchBook, Dealroom, Celesta VC |

## Setup & Usage

```bash
pip install -r requirements.txt
python main.py                # Run all analyses + generate charts
python generate_document.py   # Generate the Word document
```

## Output

- `output/` — 15 publication-quality PNG charts
- `Friday Lintspace.docx` — Full ~4,000 word research paper (saved to Desktop)

## Project Structure

```
hard-tech-revolution/
├── data/
│   └── technology_data.py      # Curated datasets (12 technologies)
├── analysis/
│   ├── trend_analysis.py       # Regression & curve fitting
│   ├── clustering_analysis.py  # K-Means + PCA
│   └── convergence_model.py    # PyTorch neural network
├── visualizations/
│   └── generate_charts.py      # 15 publication-quality charts
├── output/                     # Generated charts (PNG)
├── main.py                     # Analysis orchestrator
├── generate_document.py        # Word document generator
├── requirements.txt
└── README.md
```

## License

MIT
