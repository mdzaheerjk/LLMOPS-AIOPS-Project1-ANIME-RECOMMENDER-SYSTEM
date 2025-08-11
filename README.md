# 🤖 LLMOps & AIOps Project 1: Anime Recommender System

![LLMOps](https://img.shields.io/badge/LLMOPs-AIOps-blueviolet)
![Python](https://img.shields.io/badge/Python-3.12%2B-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deploy-blue)
![License](https://img.shields.io/badge/License-GPL--3.0-orange)

A next-generation, production-ready Anime Recommender System built with modern LLMOps and AIOps practices. This project leverages Large Language Models (LLMs), vector databases, and a scalable pipeline to provide smart, contextual anime recommendations. The solution features a modular pipeline, Dockerization, and Kubernetes manifest for cloud-native deployment.

> 📁 **Repository:** `LLMOPS-AIOPS-Project1-ANIME-RECOMMENDER-SYSTEM`

---

## 🚀 Project Highlights

- 🧠 **LLM-Augmented Recommendations:** Uses prompt engineering and vector search to deliver better, context-aware anime recommendations.
- 🔍 **Semantic Search:** Fast, scalable similarity search using ChromaDB vector database.
- 🏗️ **Modular Pipeline:** Easily extensible and maintainable with clear separation of concerns.
- 🐳 **Dockerized:** Build, test, and run anywhere.
- ☸️ **Kubernetes-Ready:** Includes deployment manifest for scalable, cloud-native serving.
- 🛠️ **Config-Driven:** Flexible setup via Python config files.
- 📦 **Production Focus:** Clean code, robust structure, and ready for enterprise and research adaptation.

---

## 🧠 Technical Stack

- **Python 3.12+**
- **ChromaDB** (vector database for embeddings)
- **Docker, Kubernetes**
- **Prompt Engineering** (customizable prompt templates)
- **Modern Python OOP & Pipeline Patterns**

---

## 🏗️ Project Structure

```bash
LLMOPS-AIOPS-Project1-ANIME-RECOMMENDER-SYSTEM/
├── app/
│   ├── __init__.py
│   └── app.py                 # Main API/app entry point
├── chroma_db/                 # Vector DB files (Chroma)
├── config/
│   ├── __init__.py
│   └── config.py
├── data/
│   ├── anime_updated.csv
│   └── anime_with_synopsis.csv
├── pipeline/
│   ├── __init__.py
│   ├── build_pipeline.py      # Pipeline creation and orchestration
│   └── pipeline.py            # Core pipeline logic
├── src/
│   ├── __init__.py
│   ├── data_loader.py         # Data reading utilities
│   ├── prompt_template.py     # LLM prompt templates
│   ├── recommender.py         # Recommendation logic
│   └── vector_store.py        # Vector DB utilities
├── utils/
│   └── (utility scripts)
├── Dockerfile
├── llmops-k8s.yaml            # Kubernetes deployment manifest
├── requirements.txt
├── setup.py
├── FULL_DOCUMENTATION.md      # Full technical and pipeline documentation
├── README.md
└── LICENSE
```

---

## ⚡ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/mdzaheerjk/LLMOPS-AIOPS-Project1-ANIME-RECOMMENDER-SYSTEM.git
cd LLMOPS-AIOPS-Project1-ANIME-RECOMMENDER-SYSTEM
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app/app.py
```
Or build and run with Docker:
```bash
docker build -t anime-recommender .
docker run -p 8000:8000 anime-recommender
```

### 5. Kubernetes Deployment
Apply the manifest to your cluster:
```bash
kubectl apply -f llmops-k8s.yaml
```

---

## 🧪 Example Usage

- **Smart Anime Recommendations:**  
  Get personalized anime suggestions based on user queries or preferences, leveraging LLM-driven prompt engineering and semantic similarity.

- **Scalable API or UI:**  
  Integrate as a backend for a website or chatbot.

---

## 📚 Documentation

See [FULL_DOCUMENTATION.md](FULL_DOCUMENTATION.md) for detailed pipeline, LLMOps/AIOps architecture, and configuration instructions.

---

## ✍️ Author

**Mohammed Zaheeruddin**  
🎓 First-Year B.Tech Student | AI/ML & GenAI Enthusiast  
🏫 Shetty Institute of Technology, Gulbarga  
📧 info.zaheerjk@gmail.com

---

## 📜 License

This project is licensed under the **GPL-3.0 License** – see the LICENSE file for details.

---

#### Key Features:
1. LLM-augmented, vector-based anime recommender system
2. Modular, extensible codebase with clear separation of concerns
3. Docker and Kubernetes ready for scalable production
4. Designed for research, education, and real-world applications
