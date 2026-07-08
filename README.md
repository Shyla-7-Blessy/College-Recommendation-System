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
http://127.0.0.1<img width="1920" height="855" alt="home_page" src="https://github.com/user-attachments/assets/d9b9d7e1-1fde-4ba3-aa0d-330395a9a985" />
<img width="1920" height="855" alt="home_page" src="https://github.com/user-attachments/assets/57cd93af-6908-4cae-9e13-9fe7ddf78122" />
:8000
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

### 🏠 Home Page & Student Input Form

*<img width="1920" height="855" alt="home_page" src="https://github.com/user-attachments/assets/6c35194b-3e46-43db-a588-6b233fb6c445" />
*

---


### 🎯 College Recommendations

*<img width="1920" height="839" alt="colleges_recommended" src="https://github.com/user-attachments/assets/9e6186df-7ded-4996-b0af-8e6839085abf" />
<img width="1920" height="848" alt="colleges_recommended3" src="https://github.com/user-attachments/assets/b2a7c57a-fb26-4be7-9cf4-71008967aee9" />
<img width="1920" height="844" alt="colleges_recommended2" src="https://github.com/user-attachments/assets/c36b9d43-44b7-4927-bbf8-30fe9afa9346" />
*

---

### 🤖 AI Explanation

*<img width="1920" height="844" alt="ai_explainaton" src="https://github.com/user-attachments/assets/89c4d534-0d45-4230-98e1-c77673b0078d" />
*

---


## 🎯 Future Enhancements

- Student authentication and profile management
- Scholarship recommendation module
- College comparison dashboard
- Admission cutoff trend prediction
- Recommendation confidence score
- Mobile application (Android & iOS) for seamless college recommendations
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
                 
