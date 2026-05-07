import os
import sys
import django

# Setup Django environment
sys.path.append(r'd:\Rerun_Project\text_classifier\text_classifier')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'text_classifier.settings')
django.setup()

from classifier.ml_models.bert_bgca import BERT_BGCA_Classifier

try:
    print("Loading model...")
    model_path = os.path.join(django.conf.settings.MODEL_CACHE_DIR, 'bert_bgca_model.pth')
    model = BERT_BGCA_Classifier.load_model(model_path)
    
    texts = [
        "加密货币市场经历大幅波动，比特币价格跌破关键支撑位。",
        "Interest rates are expected to rise next quarter as inflation concerns grow.",
        "शेयर बाज़ार में आज भारी गिरावट दर्ज की गई, जिससे निवेशकों को बड़ा नुकसान हुआ。"
    ]
    
    print("Testing predictions...")
    results = model.classify_batch(texts)
    for text, res in zip(texts, results):
        print(f"Text: {text}")
        print(f"Prediction: {res['category']} (Confidence: {res['confidence']}) [Method: {res['method']}]")
except Exception as e:
    import traceback
    traceback.print_exc()
