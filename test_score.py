from classifier.ml_models.bert_bgca import BERT_BGCA_Classifier
from classifier.ml_models.openai_classifier import OpenAIClassifier
import json

text = "New high-speed rail line connects major cities, reducing travel time by half."
text_lower = text.lower()

bert_clf = BERT_BGCA_Classifier(use_rule_based=True)
openai_clf = OpenAIClassifier()

print("\n--- BERT rule-based ---")
scores = {}
for category, keywords in bert_clf.CATEGORY_KEYWORDS.items():
    if category not in bert_clf.categories: continue
    
    score = 0
    matches = []
    for keyword in keywords:
        if keyword.lower() in text_lower:
            score += 1
            matches.append(keyword)
    if score > 0:
        scores[category] = {'score': score, 'matches': matches}
print(json.dumps(scores, indent=2, ensure_ascii=False))

print("\n--- OpenAI fallback ---")
scores2 = {}
# Simulate OpenAI fallback
for category, keywords in openai_clf._guess_category.__code__.co_consts: # It's hardcoded?
    pass # I'll just print from BERT since I copied the dict
