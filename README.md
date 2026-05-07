🧠 NLP Classification of Web Text Combined with Deep Learning

BERT-BGCA: A hybrid deep learning model for accurate web text classification
Achieves 95.21% accuracy on the THUCNews dataset using BERT + BiGRU + CNN + Attention mechanisms.


📌 Project Overview
This project presents BERT-BGCA, a novel deep learning architecture that combines:

🔵 BERT – Contextual word embeddings for rich language understanding
🟣 BiGRU – Bidirectional Gated Recurrent Unit to capture sequential context
🟠 CNN – Convolutional Neural Network to extract local text features
🟡 Attention Mechanism – Focuses on the most important parts of the input text

The model is deployed as a Django web application that allows users to classify web text into 10 categories in real time.

🖼️ Screenshots

(Add your project screenshots here — Home Page, Classify Text, Batch Classification, Upload File, Results)

Home Page
home page 1.jpeg

TextClassification

Single Text Classification(English,Chainese,Hindi)
single taxt english3.jpeg
singletext hindi 2.jpeg
singletextchainese 1.jpeg

Batch Text Classification(English,Chainese,Hindi)

batch text english3.jpeg
batch text chaines 2.jpeg
batch text hindi 4.jpeg

Upload File Text Classification

uploads file 5.jpeg
uploads file 6.jpeg
🎯 Supported Categories
The model classifies text into 10 categories:
#Category#Category1Finance6Education2Sports7Health3Entertainment8Fashion4Technology9Travel5Politics10Autos

🏗️ Model Architecture
Input Text
    ↓
BERT Embeddings (Contextual Representations)
    ↓
BiGRU Layer (Captures forward & backward context)
    ↓
CNN Layer (Extracts local n-gram features)
    ↓
Attention Mechanism (Weights important tokens)
    ↓
Fully Connected Layer
    ↓
Softmax Output → Predicted Category

📊 Performance Results
MetricScoreAccuracy95.21%DatasetTHUCNewsLanguageChinese Web TextCategories10

🌐 Web Application Features
✅ Pages / Modules
FeatureDescription🏠 HomeOverview of the model and its capabilities📝 Classify TextEnter any text and get instant category prediction📂 Batch ClassificationUpload multiple texts for bulk classification📤 Upload FileUpload a .txt or .csv file for classification

🛠️ Tech Stack
LayerTechnologyBackendDjango 4.2.0Deep LearningPyTorch 2.1.0, Transformers 4.36.0NLP ModelBERT (via HuggingFace Transformers)Data HandlingNumPy, Pandas, Scikit-learnDeploymentGunicorn + WhiteNoiseEnvironmentpython-dotenv

📦 Requirements
txtDjango==4.2.0
openai==1.12.0
transformers==4.36.0
torch==2.1.0
torchvision==0.16.0
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
python-dotenv==1.0.0
gunicorn==20.1.0
whitenoise==6.5.0
chardet
psutil

⚙️ Installation & Setup
Step 1 — Clone the Repository
bashgit clone https://github.com/your-username/bert-bgca-text-classifier.git
cd bert-bgca-text-classifier
Step 2 — Create a Virtual Environment
bashpython -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows
Step 3 — Install Dependencies
bashpip install -r requirements.txt
Step 4 — Set Up Environment Variables
Create a .env file in the root directory:
envSECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
Step 5 — Run Migrations
bashpython manage.py migrate
Step 6 — Start the Development Server
bashpython manage.py runserver
Open your browser and visit: http://127.0.0.1:8000/

📁 Project Structure
bert-bgca-text-classifier/
│
├── classifier/                  # Main Django app
│   ├── views.py                 # View logic for all pages
│   ├── urls.py                  # URL routing
│   ├── models.py                # Database models
│   └── templates/               # HTML templates
│       ├── home.html
│       ├── classify.html
│       ├── batch.html
│       └── upload.html
│
├── bert_bgca_model/             # Deep learning model files
│   ├── model.py                 # BERT-BGCA architecture
│   ├── train.py                 # Training script
│   └── predict.py               # Inference / prediction logic
│
├── static/                      # CSS, JS, Images
├── media/                       # Uploaded files
├── requirements.txt
├── manage.py
└── README.md

🔬 Dataset
THUCNews — A large-scale Chinese news text dataset collected from Sina News RSS feeds.

Total samples: ~740,000 news articles
Categories: 10 news topics
Used for: Training, Validation, and Testing the BERT-BGCA model


📖 How It Works

User inputs text via the web interface
BERT tokenizes the text into contextual embeddings
BiGRU processes the sequence in both forward and backward directions
CNN applies filters to extract local patterns
Attention layer highlights the most relevant tokens
Softmax classifier outputs the predicted category with confidence score


👩‍💻 Author
B Gayathri
B.Tech – Computer Science (Data Science)
Samskruti College of Engineering and Technology, Hyderabad


📜 License
This project is developed for academic purposes as part of the B.Tech final year project.

🌟 Acknowledgements

HuggingFace Transformers — for the BERT pre-trained model
THUCNews Dataset — for the benchmark dataset
Django Framework — for the web application backbone
PyTorch — for deep learning model training and inference
