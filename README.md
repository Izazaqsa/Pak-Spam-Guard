#  Pak Spam Guard

Pak Spam Guard is a localized, intelligent machine learning system designed to detect and classify spam and fraudulent messages within the Pakistani communication ecosystem. 

Unlike standard text classification models that only look at traditional English spam, this project focuses specifically on the unique, multilingual, and mixed-script ways people communicate in Pakistan. It is trained to identify complex phishing tactics, fake government grants, and mobile wallet scams that exploit everyday mobile users.

---

##  What This Project Does 

When you receive an SMS or chat message, it can be written in English, Urdu script, or Roman Urdu (Urdu words written using English characters). This project takes that raw message, processes the text, converts it into numbers that a computer can read, and runs it through an optimized machine learning classifier. 

The system instantly flags the message as either:
* **Ham (Legitimate):** Safe, everyday text messages or operational updates.
* **Spam / Fraud:** Malicious messages designed to steal sensitive information, passwords, or money.

### Real-World Threats Detected
The model is trained on **9,300 annotated records** (`expanded_pakistan_spam_dataset_10k.csv`) featuring realistic local fraud distributions, including:
* **Bank Phishing:** Fake security alerts impersonating local banks (HBL, Meezan Bank, Allied Bank, UBL).
* **Mobile Wallet Scams:** Unauthorized account blocking or PIN verification traps targeting **EasyPaisa** and **JazzCash** users.
* **Government Program Frauds:** Fake prize distribution alerts mimicking official programs like **BISP** (Benazir Income Support Programme) and **Ehsaas Program**.
* **Easyload & Emergency Scams:** Fake messages asking for quick financial emergency top-ups.

---

##  The Tech Stack Behind It

* **Language:** Python
* **Data Manipulation:** Pandas & NumPy
* **Machine Learning (NLP):** Scikit-Learn (`CountVectorizer` for extracting text patterns and `BernoulliNB` for binary classification)
* **User Interface:** Streamlit (For building the web application interface)

---

##  How the Interactive Interface Works

The project includes an interactive web application where you don't need to look at code to test the model. You simply type or paste any message into a web browser text box, click a button, and the background model analyzes the phrasing patterns to deliver a real-time assessment.



---

##  How to Setup and Run This Project on Your Own

Follow these step-by-step instructions to get the interactive interface running locally on your computer:

### 1. Clone the Repository
Open your terminal (or Command Prompt) and run the following command to download this repository:
```bash
git clone [https://github.com/Izazaqsa/Pak-Spam-Guard.git](https://github.com/Izazaqsa/Pak-Spam-Guard.git)
cd Pak-Spam-Guard
