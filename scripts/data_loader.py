import pandas as pd
import random


EXPENSE_CATEGORIES = {
    "Energy": [
        "Electricity Costs", "Electric Utilities", "Gas Expenses", "Fuel Costs",
        "Energy Consumption", "Heating Expenses", "Power Supply"
    ],
    "Services": [
        "Consulting Fees", "Legal Services", "Accounting Services",
        "Marketing Expenses", "IT Support", "Maintenance Services"
    ],
    "Materials": [
        "Raw Materials", "Production Supplies", "Packaging Materials",
        "Construction Materials", "Inventory Purchases"
    ],
    "Other": [
        "Office Supplies", "Travel Expenses", "Insurance Costs",
        "Training Costs", "Miscellaneous Expenses"
    ]
}

SECTORS = ["Manufacturing", "Retail", "Construction", "Services"]


def generate_synthetic_html(num_rows=10):
    """Generate an HTML table with realistic expense descriptions and values."""
    html = "<table>"
    for _ in range(num_rows):
        # Randomly select a category and one of its descriptions
        category = random.choice(list(EXPENSE_CATEGORIES.keys()))
        desc = random.choice(EXPENSE_CATEGORIES[category])

        # Assign value based on category for realism
        if category == "Energy":
            value = random.randint(5000, 50000)  # Energy costs: €5,000–€50,000
        elif category == "Services":
            value = random.randint(2000, 30000)  # Services: €2,000–€30,000
        elif category == "Materials":
            value = random.randint(10000, 100000)  # Materials: €10,000–€100,000
        else:  # Other
            value = random.randint(500, 10000)  # Other: €500–€10,000

        html += f"<tr><td>{desc}</td><td>{value}</td></tr>"
    html += "</table>"
    return html


def generate_synthetic_data(num_companies=10, num_expenses=10):
    """Generate synthetic financial data for demonstration."""
    companies = [f"Company_{i}" for i in range(1, num_companies + 1)]
    sectors = [random.choice(SECTORS) for _ in range(num_companies)]

    # Generate total production and service costs (large companies)
    total_production_costs = [random.randint(500000, 5000000) for _ in range(num_companies)]
    service_costs = [random.randint(100000, 1000000) for _ in range(num_companies)]

    # Generate HTML tables for expenses
    html_data = [generate_synthetic_html(num_expenses) for _ in range(num_companies)]

    return pd.DataFrame({
        'Company_ID': companies,
        'Sector_Code': sectors,
        'HTML': html_data,
        'Total_Production_Costs': total_production_costs,
        'Service_Costs': service_costs
    })


def load_data(file_path=None):
    """Load financial data from a CSV file or generate synthetic data."""
    if file_path:
        return pd.read_csv(file_path)
    else:
        return generate_synthetic_data()