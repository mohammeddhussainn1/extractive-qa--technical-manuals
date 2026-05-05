# 📚 Extractive Question Answering in Technical Manuals

## 🔍 Overview

This project presents an Extractive Question Answering system for technical manuals using Natural Language Processing.

The system receives a question and a technical manual text, then extracts the most relevant answer directly from the document.

## 🧠 Key Idea

Instead of generating new text, the system searches inside the given manual and returns the exact answer span or most relevant sentence.

## 🧩 System Architecture

Question + Technical Manual → Preprocessing → QA Model → Extracted Answer

## 📂 Project Structure

extractive-qa-technical-manuals/
├── data/
│   └── sample_manuals.txt
├── model/
│   └── qa_model.py
├── utils/
│   └── preprocessing.py
├── train.py
├── evaluate.py
├── requirements.txt
└── README.md

## ⚙️ How It Works

1. Load technical manual text
2. Clean and preprocess the text
3. Receive a user question
4. Search for the most relevant sentence
5. Return the extracted answer

## ▶️ Run the Project

python train.py
python evaluate.py

## 📊 Example Output

Question: What is a router?
Predicted Answer: a router is a networking device that forwards data packets between computer networks.

## 🛠️ Technologies Used

* Python
* Natural Language Processing (NLP)
* Rule-Based Extractive QA
* Text Preprocessing

## 🚀 Future Improvements

* Add BERT-based question answering
* Improve answer span extraction
* Add larger datasets
* Add evaluation metrics (F1 Score, Exact Match)

## 👨‍💻 Author

Mohammed Hussain Ali
