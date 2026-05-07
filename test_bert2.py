import os
import sys
import django

# Setup Django environment
sys.path.append(r'd:\Rerun_Project\text_classifier\text_classifier')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'text_classifier.settings')
django.setup()

from classifier.ml_models.bert_bgca import BERT_BGCA_Classifier

texts = [
    "The basketball team won their 10th consecutive game, setting a new league record.",
    "足球世界杯决赛吸引了全球数十亿观众观看。",
    "भारतीय क्रिकेट टीम ने विश्व कप के फाइनल में शानदार जीत हासिल की。"
]

model = BERT_BGCA_Classifier()

print("\n--- BERT classify_batch ---")
res_batch = model.classify_batch(texts)
for t, r in zip(texts, res_batch):
    print(f"R: {r['category']} - {r['confidence']:.2f}")

print("\n--- BERT classify (single) ---")
for t in texts:
    r = model.classify(t, threshold=0.5)
    print(f"R: {r['category']} - {r['confidence']:.2f} ({r.get('method', '')})")

