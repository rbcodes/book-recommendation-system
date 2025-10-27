# 📚 Book Recommendation System

## Overview  
This project is an **end-to-end Book Recommendation System** that suggests similar books based on user preferences.  
It integrates **machine learning**, **modern DevOps**, and **cloud deployment** to deliver a production-ready application.

The system uses the **K-Nearest Neighbors (KNN)** algorithm to recommend books and is deployed using **Docker**, **CI/CD**, and **AWS EC2**.

---

## 🔍 Features  

- **Book Recommendation Engine:**  
  Uses KNN to find and recommend books similar to the selected title.

- **Frontend (UI):**  
  Built with **Streamlit** for a clean and interactive user experience.

- **Backend (Logic):**  
  Python-based logic for data processing and recommendation generation.

- **Deployment Pipeline:**  
  Fully containerized with **Docker**, automated with **GitHub Actions**, and deployed on **AWS EC2**.

- **CI/CD Integration:**  
  Ensures seamless updates from code changes to production.

---

## 🧠 Tech Stack  

| Category | Technologies |
|-----------|---------------|
| Programming Language | Python |
| Framework/UI | Streamlit |
| Machine Learning | scikit-learn (KNeighbors) |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud Deployment | AWS EC2 |
| Data Handling | pandas, numpy |

---

## ⚙️ Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/rbcodes/book-recommendation-system.git
cd book-recommendation-system
```

### 2. Create Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate      # For macOS/Linux
venv\Scripts\activate         # For Windows
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Run the Application  
```bash
streamlit run app.py
```

---

## 🐳 Docker Setup  

### Build Docker Image  
```bash
docker build -t book-recommender .
```

### Run the Container  
```bash
docker run -p 8501:8501 book-recommender
```

Access the app at:  
[http://localhost:8501](http://localhost:8501)

---

## 🚀 Deployment  

This project is deployed on **AWS EC2** with automated builds using **GitHub Actions**.  
Each code push triggers a CI/CD pipeline to rebuild, test, and deploy the latest version seamlessly.

---

## 📂 Project Structure  

```
📁 Book Recommendation System
│
├── app.py                  # Streamlit app entry point
├── model.pkl               # Trained model file
├── books.pkl               # Dataset file
├── requirements.txt        # Dependencies
├── Dockerfile              # Container setup
├── .github/workflows/      # CI/CD workflow files
└── README.md               # Project documentation
```

---

## 📈 Future Improvements  
- Add user-based collaborative filtering  
- Include book ratings and user profiles  
- Enhance UI/UX for mobile responsiveness  
- Integrate a database for user history  

---

## 🙌 Acknowledgements  
- **Dataset:** [Books Dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset)  
- **Libraries:** Streamlit, scikit-learn, pandas, numpy  

---

## 📬 Contact  
**Author:** Rishabh Lashkari  
**LinkedIn:** [linkedin.com/in/rishabhlashkari](https://linkedin.com/in/rishabhlashkari)  
**GitHub:** [github.com/<your-username>](https://github.com/<your-username>)  
