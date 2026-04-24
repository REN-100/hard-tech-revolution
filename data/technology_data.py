"""
Curated datasets for the Hard Tech Revolution analysis.
Sources: IEA, PitchBook, Grand View Research, clinicaltrials.gov, Fusion Industry Association,
         Mordor Intelligence, Goldman Sachs, KuCoin Research, and others cited in-line.
"""

import pandas as pd
import numpy as np


# =============================================================================
# 1. NUCLEAR FUSION — Investment & Milestones
# Sources: Fusion Industry Association, IEA State of Energy Innovation 2026
# =============================================================================
fusion_investment = pd.DataFrame({
    'year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
    'cumulative_private_investment_B': [1.0, 1.2, 1.5, 1.9, 2.4, 3.2, 4.8, 6.2, 7.1, 7.9, 8.6, 9.5],
    'num_companies': [10, 12, 15, 20, 25, 30, 35, 43, 45, 47, 50, 53],
})

fusion_milestones = pd.DataFrame({
    'year': [2022, 2024, 2025, 2026, 2028, 2030, 2035],
    'milestone': [
        'NIF ignition (energy gain >1)',
        'Google Willow / Tokamak Energy record temps',
        'Multiple MW-scale pilot designs finalized',
        'IEA: "On the cusp of demonstration"',
        'First MW-scale pilot plant operational',
        'First fusion plant producing saleable energy (IEA target)',
        'Commercial grid-connected fusion (projected)',
    ],
    'readiness_level': [3, 4, 5, 5, 6, 7, 9],
})


# =============================================================================
# 2. NEXT-GEN BATTERIES — Energy Density Trajectory
# Sources: IEA, Electrive, Bonnenbatteries
# =============================================================================
battery_data = pd.DataFrame({
    'year': [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2025, 2026, 2028, 2030, 2035],
    'li_ion_Wh_kg': [140, 155, 170, 190, 210, 230, 245, 255, 260, 265, 275, 285, 300],
    'solid_state_Wh_kg': [np.nan, np.nan, np.nan, np.nan, 200, 280, 320, 380, 420, 450, 520, 600, 800],
    'li_ion_cost_per_kWh': [900, 650, 400, 280, 185, 140, 151, 139, 133, 128, 110, 95, 70],
})

battery_market = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2030],
    'market_size_B': [41, 49, 57, 72, 95, 125, 155, 310],
    'ev_share_pct': [68, 70, 72, 73, 74, 75, 76, 80],
})


# =============================================================================
# 3. DIRECT AIR CAPTURE (DAC)
# Sources: Climeworks, Fortune Business Insights, DOE, IEA
# =============================================================================
dac_data = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2028, 2030, 2035],
    'cost_per_ton_usd': [800, 700, 600, 500, 420, 380, 340, 280, 200, 120],
    'installed_capacity_kt_yr': [0.01, 0.02, 0.04, 0.1, 0.5, 2.0, 8.0, 50, 200, 2000],
    'market_size_B': [0.01, 0.02, 0.05, 0.15, 0.5, 1.2, 3.5, 15, 50, 400],
})


# =============================================================================
# 4. GENE EDITING (CRISPR)
# Sources: Innovative Genomics Institute, clinicaltrials.gov, CRISPR Therapeutics
# =============================================================================
gene_editing_data = pd.DataFrame({
    'year': [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
    'active_clinical_trials': [5, 12, 22, 35, 48, 65, 90, 120, 140, 155],
    'fda_approved_therapies': [0, 0, 0, 0, 0, 0, 1, 1, 1, 2],
    'therapeutic_areas': ['Cancer', 'Cancer', 'Cancer, Blood', 'Cancer, Blood',
                          'Cancer, Blood, Eye', 'Cancer, Blood, Eye, Liver',
                          'Cancer, Blood, Eye, Liver, Heart',
                          'Cancer, Blood, Eye, Liver, Heart, Lung',
                          'Cancer, Blood, Eye, Liver, Heart, Lung, Neuro',
                          'Cancer, Blood, Eye, Liver, Heart, Lung, Neuro, Cardio'],
    'market_size_B': [1.2, 1.8, 2.5, 3.3, 4.5, 5.8, 7.5, 9.8, 12.2, 15.0],
})


# =============================================================================
# 5. SYNTHETIC BIOLOGY
# Sources: Grand View Research, Coherent Market Insights, BioSpace
# =============================================================================
synbio_data = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2030, 2033],
    'market_size_B': [9.5, 11.8, 14.5, 18.2, 23.0, 28.5, 35.0, 42.0, 51.0, 72.0, 112.0],
    'cagr_pct': [20.1, 21.3, 22.0, 22.5, 23.0, 22.8, 22.5, 22.0, 21.5, 20.0, 18.0],
})

synbio_segments = pd.DataFrame({
    'segment': ['Biopharmaceuticals', 'Industrial Enzymes', 'Biofuels & Chemicals',
                'Agriculture', 'Food & Nutrition', 'Research Tools'],
    'share_2026_pct': [32, 22, 18, 12, 9, 7],
    'growth_rate_pct': [24, 19, 26, 21, 28, 15],
})


# =============================================================================
# 6. REGENERATIVE BIOTECH
# Sources: Mordor Intelligence, Technavio, IMARC Group, Precedence Research
# =============================================================================
regen_data = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2028, 2030, 2035],
    'regen_medicine_B': [12.5, 16.0, 20.5, 25.8, 30.2, 37.0, 45.0, 68.0, 100.0, 210.0],
    'longevity_biotech_B': [8.5, 10.2, 12.8, 15.5, 18.2, 22.0, 26.5, 38.0, 55.0, 120.0],
    'organ_replacement_B': [5.5, 6.2, 7.0, 8.2, 9.5, 11.5, 14.0, 22.0, 35.0, 80.0],
})


# =============================================================================
# 7. NANOTECHNOLOGY
# Sources: Mordor Intelligence, NovaOne Advisor, AZoNano
# =============================================================================
nanotech_data = pd.DataFrame({
    'year': [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2028, 2030],
    'market_size_B': [48, 55, 62, 70, 78, 85, 93, 105, 118, 148, 190],
})

nanotech_sectors = pd.DataFrame({
    'sector': ['Healthcare/Pharma', 'Electronics/Semiconductors', 'Energy Storage',
               'Aerospace/Defense', 'Automotive', 'Environmental', 'Others'],
    'share_pct': [28, 25, 15, 12, 8, 7, 5],
    'value_2026_B': [33.0, 29.5, 17.7, 14.2, 9.4, 8.3, 5.9],
})


# =============================================================================
# 8. ADVANCED MATERIALS (Graphene + Metamaterials)
# Sources: GM Insights, IDTechEx, Precedence Research, Coherent Market Insights
# =============================================================================
graphene_data = pd.DataFrame({
    'year': [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2028, 2030],
    'market_size_B': [0.08, 0.12, 0.18, 0.28, 0.42, 0.65, 1.0, 1.5, 2.0, 3.8, 7.0],
    'production_tons': [80, 120, 200, 350, 600, 1000, 1800, 3200, 5500, 12000, 25000],
})

metamaterials_data = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2028, 2030],
    'market_size_B': [0.5, 0.65, 0.8, 1.0, 1.2, 1.4, 1.8, 3.0, 5.5],
})


# =============================================================================
# 9. QUANTUM COMPUTING
# Sources: IBM Research, Google Quantum AI, Forbes
# =============================================================================
quantum_data = pd.DataFrame({
    'year': [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2029],
    'physical_qubits_best': [53, 65, 127, 433, 1121, 1386, 1500, 2000, 4000, 100000],
    'logical_qubits': [0, 0, 0, 0, 1, 2, 5, 12, 30, 200],
    'market_size_B': [0.5, 0.7, 1.0, 1.5, 2.2, 3.5, 5.2, 7.5, 11.0, 28.0],
})

quantum_milestones = pd.DataFrame({
    'year': [2019, 2022, 2024, 2025, 2026, 2029],
    'milestone': [
        'Google quantum supremacy (Sycamore)',
        'IBM 433-qubit Osprey',
        'Google Willow: below-threshold error correction',
        'IBM Nighthawk (120 qubits, high connectivity)',
        'IBM targets "scientific quantum advantage"',
        'IBM Quantum Starling: 200 logical qubits target',
    ],
    'company': ['Google', 'IBM', 'Google', 'IBM', 'IBM', 'IBM'],
})


# =============================================================================
# 10. BRAIN-COMPUTER INTERFACES (BCI)
# Sources: SNS Insider, Neuralink, Economic Times
# =============================================================================
bci_data = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2028, 2030, 2035],
    'market_size_B': [1.2, 1.4, 1.7, 2.0, 2.4, 2.9, 3.5, 5.5, 9.0, 15.0],
    'clinical_trial_participants': [5, 8, 12, 18, 30, 50, 85, 250, 800, 5000],
    'typing_speed_wpm': [5, 8, 12, 18, 25, 32, 40, 60, 80, 120],
    'error_rate_pct': [25, 20, 16, 12, 8, 6, 4.5, 3.0, 2.0, 0.8],
})


# =============================================================================
# 11. SPACE INFRASTRUCTURE
# Sources: Precedence Research, Goldman Sachs, Morgan Stanley, SpaceX data
# =============================================================================
space_data = pd.DataFrame({
    'year': [2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2025, 2026, 2028, 2030],
    'launch_cost_per_kg': [54500, 45000, 35000, 25000, 12000, 5000, 2800, 2720, 2600, 2500, 2500, 2400, 1200, 100],
    'space_economy_B': [175, 200, 230, 265, 300, 330, 360, 385, 420, 480, 530, 570, 750, 1000],
    'annual_launches': [18, 20, 22, 24, 28, 35, 45, 60, 95, 140, 180, 220, 350, 500],
})


# =============================================================================
# 12. DePIN / DLT
# Sources: KuCoin Research, CoinCub, Binance Research
# =============================================================================
depin_data = pd.DataFrame({
    'year': [2021, 2022, 2023, 2024, 2025, 2026, 2028, 2030],
    'market_cap_B': [2.0, 3.5, 5.0, 6.5, 8.0, 10.0, 25.0, 65.0],
    'monthly_onchain_revenue_M': [2, 5, 15, 40, 80, 150, 400, 1200],
    'active_nodes_K': [50, 120, 280, 500, 800, 1200, 3000, 8000],
})

depin_segments = pd.DataFrame({
    'segment': ['GPU/Compute', 'Storage', 'Wireless/Connectivity',
                'Sensors/Data', 'Energy', 'CDN/Bandwidth'],
    'share_2026_pct': [35, 20, 18, 12, 10, 5],
    'key_protocol': ['Render/Aethir/Akash', 'Filecoin/Arweave', 'Helium',
                     'Hivemapper/DIMO', 'Arkreen', 'Theta'],
})


# =============================================================================
# VC INVESTMENT SHIFT (Software → Hard Tech)
# Sources: PitchBook, Dealroom, Forbes, Celesta VC
# =============================================================================
vc_shift_data = pd.DataFrame({
    'year': [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
    'software_only_pct': [78, 75, 72, 68, 62, 55, 48, 42, 38],
    'hard_tech_pct': [12, 14, 17, 20, 25, 30, 35, 38, 42],
    'hybrid_pct': [10, 11, 11, 12, 13, 15, 17, 20, 20],
    'total_vc_B': [130, 140, 165, 340, 240, 175, 195, 220, 250],
})


# =============================================================================
# IMPACT MATRIX — Readiness Level vs Societal Potential
# =============================================================================
impact_matrix = pd.DataFrame({
    'technology': [
        'Nuclear Fusion', 'Next-Gen Batteries', 'Direct Air Capture',
        'Gene Editing', 'Synthetic Biology', 'Regenerative Biotech',
        'Nanotechnology', 'Advanced Materials', 'Quantum Computing',
        'Brain-Computer Interfaces', 'Space Infrastructure', 'DePIN / DLT'
    ],
    'readiness_level': [4, 7, 5, 6, 7, 5, 6, 6, 4, 4, 7, 5],
    'societal_potential': [10, 9, 9, 9, 8, 8, 7, 7, 10, 8, 9, 7],
    'current_market_B': [9.5, 155, 3.5, 15, 35, 85, 118, 3.8, 7.5, 3.5, 570, 10],
    'projected_2035_B': [50, 500, 400, 80, 200, 410, 250, 15, 65, 15, 1500, 100],
    'primary_economic_driver': [
        'Unlimited clean energy', 'Electrification of everything',
        'Carbon removal at scale', 'Curative medicine',
        'Bio-based manufacturing', 'Organ/tissue replacement',
        'Precision engineering', 'Material performance leap',
        'Cryptographic/material discovery', 'Human augmentation',
        'Off-world economy', 'Decentralized infrastructure'
    ],
    'key_job_creation': [
        'Fusion engineers, plasma physicists',
        'Battery manufacturing, materials science',
        'Chemical/process engineers, geologists',
        'Genetic counselors, bioethicists',
        'Bioprocess engineers, fermentation techs',
        'Tissue engineers, regenerative surgeons',
        'Nanofabrication specialists',
        'Materials scientists, composite engineers',
        'Quantum software developers, QC engineers',
        'Neuroengineers, neural data scientists',
        'Orbital mechanics, space systems engineers',
        'Protocol engineers, node operators'
    ],
})


def get_all_datasets():
    """Return a dictionary of all datasets for easy access."""
    return {
        'fusion_investment': fusion_investment,
        'fusion_milestones': fusion_milestones,
        'battery_data': battery_data,
        'battery_market': battery_market,
        'dac_data': dac_data,
        'gene_editing_data': gene_editing_data,
        'synbio_data': synbio_data,
        'synbio_segments': synbio_segments,
        'regen_data': regen_data,
        'nanotech_data': nanotech_data,
        'nanotech_sectors': nanotech_sectors,
        'graphene_data': graphene_data,
        'metamaterials_data': metamaterials_data,
        'quantum_data': quantum_data,
        'quantum_milestones': quantum_milestones,
        'bci_data': bci_data,
        'space_data': space_data,
        'depin_data': depin_data,
        'depin_segments': depin_segments,
        'vc_shift_data': vc_shift_data,
        'impact_matrix': impact_matrix,
    }
