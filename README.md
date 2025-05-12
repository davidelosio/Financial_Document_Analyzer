# Financial Document Analyzer

This project analyzes financial documents to extract and classify expenses, focusing on energy costs and their impact across sectors.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/financial-document-analyzer.git
   ```
   
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the demo notebook:

```bash
jupyter notebook notebooks/analysis_demo.ipynb
```

## Overview:

- Extracts tables from HTML using BeautifulSoup. 
- Classifies expenses with zero-shot NLP (Transformers). 
- Analyzes and visualizes energy cost trends.

## Project Structure
- data/: Sample financial data. 
- notebooks/: Jupyter notebook for demonstration. 
- scripts/: Core Python scripts for data loading, parsing, classification, and analysis. 
- outputs/: Generated visualizations.

