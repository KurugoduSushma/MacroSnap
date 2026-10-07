# 🥗 MacroSnap

> **Snap it. Track it. Understand it.**

MacroSnap is an AI-powered nutrition assistant built with **Streamlit** and **Google Gemini**.

Users can upload a photo of their meal or describe what they are eating. MacroSnap analyzes the meal and provides an estimated calorie and macronutrient breakdown. Users can also send their nutrition summary to WhatsApp using **Twilio**.

---

## ✨ Features

- 📸 Upload a photo of your meal
- 🤖 AI-powered meal analysis using Google Gemini
- 🔥 Estimated calorie calculation
- 💪 Protein, carbohydrates, and fat estimation
- 💬 Ask nutrition-related questions
- 🧠 Conversation memory during the session
- 📊 Generate a nutrition summary
- 📱 Send nutrition summaries to WhatsApp
- 🔐 Secure API key management using Streamlit Secrets
- 🌐 Deployable using Streamlit Community Cloud

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application and UI |
| Google Gemini | AI meal and nutrition analysis |
| Google GenAI SDK | Gemini API integration |
| Twilio | WhatsApp messaging |
| Git | Version control |
| GitHub | Source code hosting |

---

## 📁 Project Structure


    MacroSnap/
    │
    ├── app.py
    ├── prompts.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    │
    └── .streamlit/
        └── secrets.toml
        
## ⚙️ Installation
1. Clone the repository

        git clone https://github.com/KurugoduSushma/MacroSnap.git
        cd MacroSnap

3. Create a virtual environment

        python -m venv venv

5. Activate the virtual environment

        Windows: venv\Scripts\activate

4. Install dependencies

        pip install -r requirements.txt

## 🔑 Configuration
Create the following file: .streamlit/secrets.toml

Add your credentials:

    GEMINI_API_KEY = "your-gemini-api-key"
    
    TWILIO_ACCOUNT_SID = "your-twilio-account-sid"
    TWILIO_AUTH_TOKEN = "your-twilio-auth-token"
    TWILIO_WHATSAPP_FROM = "whatsapp:+14155238886"
    TWILIO_CONTENT_SID = "your-content-template-sid"

## 🔐 Security

Never upload your real secrets.toml file to GitHub.
Make sure your .gitignore contains:

      venv/
      __pycache__/
      .streamlit/secrets.toml

## ▶️ Run Locally

Start the Streamlit application

    streamlit run app.py

The application will open automatically in your browser.
If it does not, open: http://localhost:8501


