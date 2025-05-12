from bs4 import BeautifulSoup

def extract_tables(html):
    """Extract expense descriptions and values from HTML tables."""
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table')
    expenses = []
    for table in tables:
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == 2:
                desc = cells[0].text.strip()
                try:
                    value = float(cells[1].text.strip())
                    expenses.append((desc, value))
                except ValueError:
                    continue
    return expenses


def extract_descriptions(html):
    """Extract expense descriptions from HTML tables for frequency analysis."""
    soup = BeautifulSoup(html, 'html.parser')
    descriptions = set()
    for table in soup.find_all('table'):
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) >= 2:
                desc = cells[0].text.strip()
                if desc:
                    descriptions.add(desc)
    return list(descriptions)