from collections import defaultdict

def calculate_document_frequency(df, description_column='Descriptions'):
    """Calculate document frequency for each expense description across documents."""
    term_df = defaultdict(int)
    cost_stop_words = ['descrizione', 'totale', 'totali', 'descrizioni', '0', '1', '2', 'totale calcolato']  # Your stop words
    for doc_descriptions in df[description_column]:
        unique_terms = set(doc_descriptions)
        for term in unique_terms:
            if term not in cost_stop_words and term.strip():
                term_df[term] += 1
    total_documents = len(df)
    return dict(term_df), total_documents

def get_frequent_terms(term_df, total_documents, min_freq=0.1):
    """Filter terms that appear in at least min_freq of documents.

        Note that by changing freq. we can extract different high quality candidates.
        By default, we only extract the candidates that appear in at least 10% of all
        the note integrative we have. We could also use an absolute number like 30 as
        minimum document frequency for extraction, or bump the ratio to 50% using 0.5

    """
    if isinstance(min_freq, float):
        if not 0.0 < min_freq < 1.0:
            raise ValueError('If float, min_freq must be between 0.0 and 1.0')
        min_freq = round(total_documents * min_freq)
    frequent_terms = [term for term, freq in term_df.items() if freq >= min_freq]
    return frequent_terms