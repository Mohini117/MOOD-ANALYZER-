# 🌤️ MoodAnalyzer - Flask ML App on GCP

MoodAnalyzer is a simple machine learning web application built with **Flask** that predicts a user's mood based on their social media usage patterns. The primary goal of this project was to **learn deployment workflows** using **Docker** and **Google Cloud Platform (GCP)**.

This project is open to the public — feel free to try it and drop your feedback in the comments or issues section!

---

## 🚀 Live Demo

🔗 [Click here to try MoodAnalyzer](https://moodanalyzer-461407.uc.r.appspot.com/)  


---

## 📌 Features

- Takes inputs like age, gender, Instagram usage data (likes, comments, etc.)
- Predicts mood: **Happy**, **Anxious**, **Neutral**, etc.
- Built with Flask and Scikit-learn
- Dockerized and deployed on **Google Cloud Platform**
- Lightweight and easy to use

---

## 🧠 Machine Learning Model

A simple **supervised classification model** trained on user behavior features:
- `Age`
- `Gender`
- `Platform` (Instagram)
- `Daily_Usage_Time (minutes)`
- `Posts_Per_Day`
- `Likes_Received_Per_Day`
- `Comments_Received_Per_Day`
- `Messages_Sent_Per_Day`

---

## 🛠️ Tech Stack

| Layer            | Tech Used               |
|------------------|--------------------------|
| Backend          | Python, Flask            |
| ML Model         | Scikit-learn             |
| Containerization | Docker                   |
| Deployment       | Google Cloud Platform (GCP) |

---

## ⚙️ Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/Mohini117/MOOD-ANALYZER-.git
cd MOOD-ANALYZER-
