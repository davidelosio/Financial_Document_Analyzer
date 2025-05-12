import matplotlib.pyplot as plt


def analyze_energy_costs(classified_expenses, service_costs, production_costs):
    """Calculate energy costs and their ratios to service and production costs."""
    energy_total = sum(value for category, value in classified_expenses if category == "Energy")
    return {
        'Energy_Costs': energy_total,
        'Energy_to_Service_Ratio': (energy_total / service_costs) * 100 if service_costs > 0 else 0,
        'Energy_to_Production_Ratio': (energy_total / production_costs) * 100 if production_costs > 0 else 0
    }


def plot_sector_analysis(df):
    """Visualize average energy cost ratios by sector."""
    # Extract ratios
    df['Energy_to_Service_Ratio'] = df['Analysis'].apply(lambda x: x['Energy_to_Service_Ratio'])
    df['Energy_to_Production_Ratio'] = df['Analysis'].apply(lambda x: x['Energy_to_Production_Ratio'])

    # Group by sector and calculate mean ratios
    sector_analysis = df.groupby('Sector_Code').agg({
        'Energy_to_Service_Ratio': 'mean',
        'Energy_to_Production_Ratio': 'mean'
    }).reset_index()

    # Plot
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].bar(sector_analysis['Sector_Code'], sector_analysis['Energy_to_Service_Ratio'], color='skyblue')
    ax[0].set_title('Avg Energy Costs as % of Service Costs by Sector')
    ax[0].set_xlabel('Sector')
    ax[0].set_ylabel('Percentage (%)')

    ax[1].bar(sector_analysis['Sector_Code'], sector_analysis['Energy_to_Production_Ratio'], color='lightgreen')
    ax[1].set_title('Avg Energy Costs as % of Production Costs by Sector')
    ax[1].set_xlabel('Sector')
    ax[1].set_ylabel('Percentage (%)')

    plt.tight_layout()
    plt.savefig('../outputs/sector_energy_analysis.png')
    plt.show()