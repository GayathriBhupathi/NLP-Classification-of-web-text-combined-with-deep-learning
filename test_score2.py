from classifier.ml_models.openai_classifier import OpenAIClassifier
model = OpenAIClassifier()
cat = model._guess_category("New high-speed rail line connects major cities, reducing travel time by half.")
print(cat)
