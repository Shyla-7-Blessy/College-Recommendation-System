# 🎓 AI-Powered College Recommendation System

An intelligent web application that recommends the most suitable colleges for students based on their academic profile. The system combines rule-based eligibility filtering, Machine Learning, and Large Language Models (LLMs) to provide personalized college recommendations along with AI-generated explanations.

---

## 📌 Project Overview

Choosing the right college can be challenging due to varying eligibility criteria, cutoffs, and student preferences. This project simplifies the process by analyzing a student's academic information, filtering eligible colleges using predefined rules, ranking them using a Machine Learning model, and generating human-friendly explanations using an LLM.

---

## ✨ Features

- ✅ Student profile-based college recommendations
- ✅ Rule-based eligibility filtering
- ✅ Machine Learning-based college ranking using Random Forest
- ✅ AI-generated explanations using LangChain + Groq LLaMA
- ✅ PostgreSQL database integration
- ✅ Responsive web interface using HTML, CSS & Bootstrap
- ✅ FastAPI REST backend
- ✅ Top 3 college recommendations with detailed reasoning

---

## 🏗️ System Workflow

```text
Student Input
      │
      ▼
FastAPI Backend
      │
      ▼
Rule-Based Eligibility Engine
      │
      ▼
Eligible Colleges
      │
      ▼
Random Forest Model
      │
      ▼
Top 3 Recommended Colleges
      │
      ▼
LangChain + Groq LLaMA
      │
      ▼
AI-Generated Explanation
      │
      ▼
Frontend Display
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Backend | FastAPI, Python |
| Database | PostgreSQL, SQLAlchemy |
| Machine Learning | Scikit-learn, Random Forest |
| AI | LangChain, Groq API (LLaMA 3.3) |
| Frontend | HTML, CSS, Bootstrap |
| Data Processing | Pandas, NumPy |
| Model Storage | Joblib |

---

## 📂 Project Structure

```
college-recommendation/
│
├── app/
├── dataset/
├── models/
├── recommendation/
├── static/
├── templates/
├── screenshots/
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/College-Recommendation-System.git
```

### 2. Navigate to the project

```bash
cd College-Recommendation-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file.

Example:

```env
DATABASE_URL=your_postgresql_database_url
GROQ_API_KEY=your_groq_api_key
```

### 7. Run the FastAPI application

```bash
uvicorn app.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

## 📊 Recommendation Process

1. Student enters academic details.
2. FastAPI receives and validates the request.
3. Rule Engine filters colleges based on eligibility.
4. Random Forest predicts the most suitable colleges.
5. Top 3 colleges are selected.
6. LangChain sends recommendation data to Groq LLaMA.
7. LLM generates personalized explanations.
8. Recommendations are displayed through the frontend.

---

## 📸 Screenshots

### 🏠 Home Page

*(Add screenshot here)*

---

### 📝 Student Input Form

*(Add screenshot here)*

---

### 🎯 College Recommendations

*(Add screenshot here)*

---

### 🤖 AI Explanation

*(Add screenshot here)*

---

## 🎯 Future Enhancements

- Student authentication and profile management
- Scholarship recommendation module
- College comparison dashboard
- Admission cutoff trend prediction
- Recommendation confidence score
- PDF report generation
- Cloud deployment (AWS/Azure)

---

## 📈 Project Highlights

- FastAPI-based backend architecture
- Machine Learning recommendation engine
- Rule-based eligibility validation
- AI-powered explanation generation
- PostgreSQL database integration
- Responsive web interface
- Modular and scalable design

---

## 👨‍💻 Author

**Shyla**

Artificial Intelligence & Data Science Graduate

---

## 📄 License

This project is licensed under the MIT License.


                    +----------------------+
                    |   Student Details    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   FastAPI Backend    |
                    +----------+-----------+
                               |
                               v
                  +---------------------------+
                  | Rule-Based Eligibility    |
                  +-----------+---------------+
                              |
                              v
                 +----------------------------+
                 | Eligible College List      |
                 +------------+---------------+
                              |
                              v
                 +----------------------------+
                 | Random Forest Model        |
                 +------------+---------------+
                              |
                              v
                 +----------------------------+
                 | Top 3 College Prediction   |
                 +------------+---------------+
                              |
                              v
                 +----------------------------+
                 | LangChain + Groq LLaMA     |
                 +------------+---------------+
                              |
                              v
                 +----------------------------+
                 | AI Explanation Generation  |
                 +------------+---------------+
                              |
                              v
                 +----------------------------+
                 | Frontend (HTML/CSS)        |
                 +----------------------------+
                 
