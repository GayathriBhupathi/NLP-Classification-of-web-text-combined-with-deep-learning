from classifier.ml_models.openai_classifier import OpenAIClassifier
model = OpenAIClassifier()
text_lower = "New high-speed rail line connects major cities, reducing travel time by half.".lower()

scores = {}
for category, keywords in model.keyword_map.items() if hasattr(model, 'keyword_map') else {}:
    pass # Wait, let me just run the _guess_category code

def test():
    scores = {}
    for category, keywords in model.categories: # No, I should paste the dict from openai
        pass
        
    keyword_map = OpenAIClassifier()._guess_category.__code__.co_consts # Not possible.
