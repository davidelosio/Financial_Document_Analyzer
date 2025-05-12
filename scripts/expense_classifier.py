from transformers import XLMRobertaTokenizer, AutoModelForSequenceClassification, pipeline

tokenizer = XLMRobertaTokenizer.from_pretrained("vicgalle/xlm-roberta-large-xnli-anli")

model = AutoModelForSequenceClassification.from_pretrained("vicgalle/xlm-roberta-large-xnli-anli")

classifier = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)

cost_classes = [
    'commissioni',
    'ammortamenti',
    'prestazione servizi',
    'energia elettrica',
    'compenso dipendenti',
    'assicurazioni',
    'imposte',
    'telecomunicazioni',
    'logistica',
    'carburanti e/o combustibili',
    'affitto e/o noleggio',
]

def classify_expense(expense_desc, candidate_labels=cost_classes):
    """Classify an expense description using zero-shot classification."""
    result = classifier(expense_desc, candidate_labels=candidate_labels)
    return result['labels'][0]

# expense = "Pagamento per energia elettrica"
# classification = classify_expense(expense)
# print(classification)  # Expected output: 'energia elettrica' or 'Uncategorized'