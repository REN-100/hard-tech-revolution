"""
Chart generation module — 13 publication-quality visualizations.
Uses matplotlib and seaborn with a dark academic theme.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np
import pandas as pd
import os

# Global style
plt.rcParams.update({
    'figure.facecolor': '#0d1117', 'axes.facecolor': '#161b22',
    'axes.edgecolor': '#30363d', 'axes.labelcolor': '#c9d1d9',
    'text.color': '#c9d1d9', 'xtick.color': '#8b949e', 'ytick.color': '#8b949e',
    'grid.color': '#21262d', 'grid.alpha': 0.6,
    'font.family': 'sans-serif', 'font.size': 11,
    'figure.dpi': 150, 'savefig.dpi': 200, 'savefig.bbox': 'tight',
    'savefig.facecolor': '#0d1117',
})

COLORS = ['#58a6ff', '#3fb950', '#f0883e', '#bc8cff', '#f778ba',
          '#ff7b72', '#79c0ff', '#7ee787', '#ffa657', '#d2a8ff', '#56d364', '#e3b341']


def _save(fig, output_dir, name):
    path = os.path.join(output_dir, f'{name}.png')
    fig.savefig(path, dpi=200, bbox_inches='tight', facecolor='#0d1117')
    plt.close(fig)
    return path


def chart_01_fusion(datasets, output_dir):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    d = datasets['fusion_investment']
    ax1.bar(d['year'], d['cumulative_private_investment_B'], color=COLORS[0], alpha=0.7, label='Cumulative Investment ($B)')
    ax1.set_xlabel('Year'); ax1.set_ylabel('Cumulative Investment ($B)', color=COLORS[0])
    ax2 = ax1.twinx()
    ax2.plot(d['year'], d['num_companies'], color=COLORS[1], linewidth=2.5, marker='o', label='Active Companies')
    ax2.set_ylabel('Number of Companies', color=COLORS[1])
    # Milestones
    ms = datasets['fusion_milestones']
    for _, row in ms[ms['year'] <= 2026].iterrows():
        ax1.axvline(x=row['year'], color=COLORS[3], alpha=0.3, linestyle='--')
    ax1.set_title('Nuclear Fusion: Private Investment & Industry Growth', fontsize=14, fontweight='bold', pad=15)
    ax1.legend(loc='upper left'); ax2.legend(loc='lower right')
    ax1.grid(True, alpha=0.3)
    return _save(fig, output_dir, '01_nuclear_fusion')


def chart_02_batteries(datasets, output_dir):
    fig, ax = plt.subplots(figsize=(12, 6))
    d = datasets['battery_data']
    ax.plot(d['year'], d['li_ion_Wh_kg'], color=COLORS[0], linewidth=2.5, marker='s', label='Li-ion (Wh/kg)')
    mask = d['solid_state_Wh_kg'].notna()
    ax.plot(d.loc[mask, 'year'], d.loc[mask, 'solid_state_Wh_kg'], color=COLORS[1], linewidth=2.5, marker='D', label='Solid-State (Wh/kg)')
    ax.fill_between(d.loc[mask, 'year'], d.loc[mask, 'li_ion_Wh_kg'], d.loc[mask, 'solid_state_Wh_kg'], alpha=0.15, color=COLORS[1])
    ax.axhline(y=500, color=COLORS[2], linestyle='--', alpha=0.5, label='Commercial SSB Target (500 Wh/kg)')
    ax.set_xlabel('Year'); ax.set_ylabel('Energy Density (Wh/kg)')
    ax.set_title('Battery Energy Density: Li-ion vs Solid-State Trajectory', fontsize=14, fontweight='bold', pad=15)
    ax.legend(); ax.grid(True, alpha=0.3)
    return _save(fig, output_dir, '02_batteries')


def chart_03_dac(datasets, output_dir):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    d = datasets['dac_data']
    ax1.plot(d['year'], d['cost_per_ton_usd'], color=COLORS[2], linewidth=2.5, marker='o', label='Cost per ton CO₂ ($)')
    ax1.set_ylabel('Cost per Ton CO₂ ($)', color=COLORS[2]); ax1.set_xlabel('Year')
    ax1.axhline(y=200, color=COLORS[5], linestyle='--', alpha=0.5, label='Viability Target ($200/ton)')
    ax2 = ax1.twinx()
    ax2.fill_between(d['year'], d['installed_capacity_kt_yr'], alpha=0.3, color=COLORS[0], label='Installed Capacity (kt/yr)')
    ax2.set_ylabel('Installed Capacity (kt CO₂/yr)', color=COLORS[0])
    ax2.set_yscale('log')
    ax1.set_title('Direct Air Capture: Cost Decline & Capacity Scaling', fontsize=14, fontweight='bold', pad=15)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right')
    ax1.grid(True, alpha=0.3)
    return _save(fig, output_dir, '03_dac')


def chart_04_gene_editing(datasets, output_dir):
    fig, ax = plt.subplots(figsize=(12, 6))
    d = datasets['gene_editing_data']
    bars = ax.bar(d['year'], d['active_clinical_trials'], color=COLORS[3], alpha=0.8)
    for bar, approved in zip(bars, d['fda_approved_therapies']):
        if approved > 0:
            bar.set_edgecolor(COLORS[1]); bar.set_linewidth(3)
    ax.plot(d['year'], d['market_size_B'] * 10, color=COLORS[1], linewidth=2, marker='D', label='Market Size ($B × 10)')
    ax.set_xlabel('Year'); ax.set_ylabel('Active Clinical Trials')
    ax.set_title('Gene Editing: Clinical Trial Pipeline Expansion', fontsize=14, fontweight='bold', pad=15)
    ax.legend(); ax.grid(True, alpha=0.3)
    return _save(fig, output_dir, '04_gene_editing')


def chart_05_synbio(datasets, output_dir):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})
    d = datasets['synbio_data']
    ax1.bar(d['year'], d['market_size_B'], color=COLORS[4], alpha=0.8)
    ax1.plot(d['year'], d['market_size_B'], color='white', linewidth=1.5, alpha=0.5)
    ax1.set_xlabel('Year'); ax1.set_ylabel('Market Size ($B)')
    ax1.set_title('Synthetic Biology Market Growth', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    seg = datasets['synbio_segments']
    ax2.barh(seg['segment'], seg['share_2026_pct'], color=COLORS[:len(seg)])
    ax2.set_xlabel('2026 Market Share (%)'); ax2.set_title('Segment Breakdown', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    return _save(fig, output_dir, '05_synthetic_biology')


def chart_06_regen(datasets, output_dir):
    fig, ax = plt.subplots(figsize=(12, 6))
    d = datasets['regen_data']
    ax.stackplot(d['year'], d['regen_medicine_B'], d['longevity_biotech_B'], d['organ_replacement_B'],
                 labels=['Regenerative Medicine', 'Longevity Biotech', 'Organ Replacement'],
                 colors=[COLORS[3], COLORS[4], COLORS[5]], alpha=0.8)
    ax.set_xlabel('Year'); ax.set_ylabel('Market Size ($B)')
    ax.set_title('Regenerative Biotech: Market Segment Growth', fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper left'); ax.grid(True, alpha=0.3)
    return _save(fig, output_dir, '06_regenerative_biotech')


def chart_07_nanotech(datasets, output_dir):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [1.5, 1]})
    d = datasets['nanotech_data']
    ax1.fill_between(d['year'], d['market_size_B'], alpha=0.4, color=COLORS[6])
    ax1.plot(d['year'], d['market_size_B'], color=COLORS[6], linewidth=2.5, marker='o')
    ax1.set_xlabel('Year'); ax1.set_ylabel('Market Size ($B)')
    ax1.set_title('Nanotechnology Market Growth', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    sec = datasets['nanotech_sectors']
    wedges, texts, autotexts = ax2.pie(sec['share_pct'], labels=sec['sector'], autopct='%1.0f%%',
                                        colors=COLORS[:len(sec)], textprops={'fontsize': 8, 'color': '#c9d1d9'})
    ax2.set_title('Sector Distribution (2026)', fontsize=13, fontweight='bold')
    plt.tight_layout()
    return _save(fig, output_dir, '07_nanotechnology')


def chart_08_materials(datasets, output_dir):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    g = datasets['graphene_data']
    m = datasets['metamaterials_data']
    ax1.plot(g['year'], g['market_size_B'], color=COLORS[1], linewidth=2.5, marker='o', label='Graphene Market ($B)')
    ax1.plot(m['year'], m['market_size_B'], color=COLORS[8], linewidth=2.5, marker='s', label='Metamaterials Market ($B)')
    ax1.set_xlabel('Year'); ax1.set_ylabel('Market Size ($B)')
    ax2 = ax1.twinx()
    ax2.bar(g['year'], g['production_tons'], alpha=0.2, color=COLORS[1], label='Graphene Production (tons)')
    ax2.set_ylabel('Graphene Production (tons)', color=COLORS[1])
    ax1.set_title('Advanced Materials: Manufacturing Scale-Up', fontsize=14, fontweight='bold', pad=15)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    ax1.grid(True, alpha=0.3)
    return _save(fig, output_dir, '08_advanced_materials')


def chart_09_quantum(datasets, output_dir):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    d = datasets['quantum_data']
    ax1.semilogy(d['year'], d['physical_qubits_best'], color=COLORS[0], linewidth=2.5, marker='o', label='Physical Qubits')
    mask = d['logical_qubits'] > 0
    ax1.semilogy(d.loc[mask, 'year'], d.loc[mask, 'logical_qubits'], color=COLORS[1], linewidth=2.5, marker='D', label='Logical Qubits')
    ax1.set_xlabel('Year'); ax1.set_ylabel('Qubit Count (log scale)')
    ms = datasets['quantum_milestones']
    for _, row in ms.iterrows():
        ax1.annotate(row['milestone'][:35] + '...', xy=(row['year'], 100),
                    fontsize=7, rotation=45, alpha=0.7, color=COLORS[3])
    ax1.set_title('Quantum Computing: Qubit Scaling Roadmap', fontsize=14, fontweight='bold', pad=15)
    ax1.legend(); ax1.grid(True, alpha=0.3)
    return _save(fig, output_dir, '09_quantum_computing')


def chart_10_bci(datasets, output_dir):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    d = datasets['bci_data']
    ax1.bar(d['year'], d['clinical_trial_participants'], color=COLORS[3], alpha=0.7, label='Trial Participants')
    ax1.set_xlabel('Year'); ax1.set_ylabel('Clinical Trial Participants', color=COLORS[3])
    ax2 = ax1.twinx()
    ax2.plot(d['year'], d['error_rate_pct'], color=COLORS[5], linewidth=2.5, marker='v', label='Error Rate (%)')
    ax2.plot(d['year'], d['typing_speed_wpm'], color=COLORS[1], linewidth=2.5, marker='^', label='Typing Speed (WPM)')
    ax2.set_ylabel('Error Rate (%) / Speed (WPM)')
    ax1.set_title('Brain-Computer Interfaces: Clinical Progress', fontsize=14, fontweight='bold', pad=15)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='center left')
    ax1.grid(True, alpha=0.3)
    return _save(fig, output_dir, '10_bci')


def chart_11_space(datasets, output_dir):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    d = datasets['space_data']
    ax1.semilogy(d['year'], d['launch_cost_per_kg'], color=COLORS[5], linewidth=2.5, marker='o', label='Launch Cost ($/kg)')
    ax1.set_xlabel('Year'); ax1.set_ylabel('Launch Cost $/kg (log)', color=COLORS[5])
    ax1.axhline(y=100, color=COLORS[2], linestyle='--', alpha=0.5, label='Starship Target ($100/kg)')
    ax2 = ax1.twinx()
    ax2.fill_between(d['year'], d['space_economy_B'], alpha=0.2, color=COLORS[0])
    ax2.plot(d['year'], d['space_economy_B'], color=COLORS[0], linewidth=2, label='Space Economy ($B)')
    ax2.set_ylabel('Space Economy ($B)', color=COLORS[0])
    ax1.set_title('Space Infrastructure: Launch Cost Decay vs Orbital Revenue', fontsize=14, fontweight='bold', pad=15)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right')
    ax1.grid(True, alpha=0.3)
    return _save(fig, output_dir, '11_space_infrastructure')


def chart_12_depin(datasets, output_dir):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})
    d = datasets['depin_data']
    ax1.bar(d['year'], d['market_cap_B'], color=COLORS[8], alpha=0.7, label='Market Cap ($B)')
    ax1b = ax1.twinx()
    ax1b.plot(d['year'], d['monthly_onchain_revenue_M'], color=COLORS[1], linewidth=2.5, marker='D', label='Monthly On-chain Revenue ($M)')
    ax1.set_xlabel('Year'); ax1.set_ylabel('Market Cap ($B)', color=COLORS[8])
    ax1b.set_ylabel('Monthly Revenue ($M)', color=COLORS[1])
    ax1.set_title('DePIN: Market Cap & Revenue Growth', fontsize=13, fontweight='bold')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax1b.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    ax1.grid(True, alpha=0.3)
    seg = datasets['depin_segments']
    ax2.barh(seg['segment'], seg['share_2026_pct'], color=COLORS[:len(seg)])
    ax2.set_xlabel('2026 Share (%)'); ax2.set_title('DePIN Segments', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    return _save(fig, output_dir, '12_depin_dlt')


def chart_13_impact_matrix(impact_matrix, cluster_results, output_dir):
    fig, ax = plt.subplots(figsize=(12, 8))
    labels = cluster_results['labels']
    sizes = np.sqrt(impact_matrix['current_market_B'].values) * 8
    for i, (_, row) in enumerate(impact_matrix.iterrows()):
        ax.scatter(row['readiness_level'], row['societal_potential'],
                  s=sizes[i], c=COLORS[labels[i]], alpha=0.7, edgecolors='white', linewidth=1.5)
        ax.annotate(row['technology'], (row['readiness_level'], row['societal_potential']),
                   textcoords='offset points', xytext=(8, 5), fontsize=8, color='#c9d1d9')
    ax.set_xlabel('Readiness Level (1-10)', fontsize=12)
    ax.set_ylabel('Societal Potential (1-10)', fontsize=12)
    ax.set_title('Technology Impact Matrix: Readiness vs Societal Potential', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(2, 9); ax.set_ylim(5.5, 11)
    ax.grid(True, alpha=0.3)
    # Legend for clusters
    unique_labels = sorted(set(labels))
    for lbl in unique_labels:
        name = cluster_results['cluster_names'].get(lbl, f'Cluster {lbl}')
        ax.scatter([], [], c=COLORS[lbl], s=100, label=name, alpha=0.7, edgecolors='white')
    ax.legend(loc='lower right', fontsize=9)
    return _save(fig, output_dir, '13_impact_matrix')


def chart_00_vc_shift(datasets, output_dir):
    fig, ax = plt.subplots(figsize=(12, 6))
    d = datasets['vc_shift_data']
    ax.stackplot(d['year'], d['software_only_pct'], d['hard_tech_pct'], d['hybrid_pct'],
                 labels=['Software-Only', 'Hard Tech / Deep Tech', 'Hybrid'],
                 colors=[COLORS[0], COLORS[1], COLORS[8]], alpha=0.8)
    ax.set_xlabel('Year'); ax.set_ylabel('Share of VC Investment (%)')
    ax.set_title('The Great Pivot: VC Investment Shift from Software to Hard Tech', fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='center right'); ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 100)
    return _save(fig, output_dir, '00_vc_shift')


def chart_14_convergence(convergence_matrix, output_dir):
    fig, ax = plt.subplots(figsize=(12, 10))
    short_names = [t[:12] for t in convergence_matrix.index]
    sns.heatmap(convergence_matrix.values, xticklabels=short_names, yticklabels=short_names,
                cmap='viridis', annot=True, fmt='.2f', ax=ax, linewidths=0.5,
                cbar_kws={'label': 'Convergence Score'}, annot_kws={'size': 7})
    ax.set_title('Technology Convergence Matrix (Neural Network Predicted)', fontsize=14, fontweight='bold', pad=15)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.yticks(fontsize=8)
    return _save(fig, output_dir, '14_convergence_matrix')


def generate_all_charts(datasets, cluster_results, convergence_results, output_dir):
    """Generate all charts and return paths."""
    os.makedirs(output_dir, exist_ok=True)
    paths = {}
    paths['vc_shift'] = chart_00_vc_shift(datasets, output_dir)
    paths['fusion'] = chart_01_fusion(datasets, output_dir)
    paths['batteries'] = chart_02_batteries(datasets, output_dir)
    paths['dac'] = chart_03_dac(datasets, output_dir)
    paths['gene_editing'] = chart_04_gene_editing(datasets, output_dir)
    paths['synbio'] = chart_05_synbio(datasets, output_dir)
    paths['regen'] = chart_06_regen(datasets, output_dir)
    paths['nanotech'] = chart_07_nanotech(datasets, output_dir)
    paths['materials'] = chart_08_materials(datasets, output_dir)
    paths['quantum'] = chart_09_quantum(datasets, output_dir)
    paths['bci'] = chart_10_bci(datasets, output_dir)
    paths['space'] = chart_11_space(datasets, output_dir)
    paths['depin'] = chart_12_depin(datasets, output_dir)
    paths['impact_matrix'] = chart_13_impact_matrix(datasets['impact_matrix'], cluster_results, output_dir)
    paths['convergence'] = chart_14_convergence(convergence_results['convergence_matrix'], output_dir)
    print(f"Generated {len(paths)} charts in {output_dir}")
    return paths
