# Kavach 🛡️
### AI-Powered Scam Awareness Assistant

Kavach is a scam-awareness assistant designed to help people recognise suspicious messages, understand potential scam indicators, and make safer decisions online.

It combines rule-based scam detection with AI-generated explanations to make security advice easier to understand. The assistant supports text-based conversations in English, Hindi, and Hinglish, with an experimental voice-input feature for speaking messages directly.

## ✨ Features

- **Scam keyword detection:** Identifies suspicious phrases involving OTPs, banking, account verification, and urgent requests.
- **Fuzzy phrase matching:** Helps identify potential scam phrases even when their wording contains small spelling differences.
- **Suspicious URL checks:** Flags indicators such as IP-address links, shortened URLs, the `@` URL trick, and Punycode domains.
- **Risk scoring:** Calculates a score from 0 to 100 based on detected indicators and assigns a LOW, MEDIUM, or HIGH risk level.
- **AI-powered explanations:** Uses the Groq API to explain potential risks and suggest practical safety steps.
- **Conversation memory:** Retains recent messages to support follow-up questions during a session.
- **Voice input:** Converts spoken English into text using speech recognition.
- **Scam awareness guide:** Uses a local knowledge file to provide relevant safety guidance.

## 🧰 Tech Stack

- **Python** – application logic and detection rules
- **Groq API** – AI-powered scam analysis
- **SpeechRecognition** – speech-to-text input
- **pytest** – automated testing
- **Regular expressions and URL parsing** – suspicious link checks

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/jaden-mas1010/kavach-voice-agent.git
cd kavach-voice-agent
```

### 2. Install the dependencies

Make sure Python is installed, then run:

```bash
py -m pip install groq "SpeechRecognition[audio]" pytest
```

If your system uses `python` instead of `py`, replace `py` with `python` in the commands.

### 3. Configure your Groq API key

Create an API key through the official Groq developer console.

In PowerShell, set the key for your current terminal session:

```powershell
$env:GROQ_API_KEY = "your_api_key_here"
```

Replace the placeholder with your own key. Never commit API keys, passwords, or other secrets to GitHub.

### 4. Run Kavach

```powershell
py app.py
```

You can type a message, enter `/voice` to provide speech input, or type `exit` to end the conversation.

### 5. Run the tests

```powershell
py -m pytest -q
```

## 🧪 How It Works

1. **Input:** The user types a suspicious message or provides speech input.
2. **Detection:** Kavach checks the message for known scam phrases, similar wording, and suspicious URL characteristics.
3. **Risk assessment:** Detected indicators contribute to a weighted risk score.
4. **AI analysis:** The message is sent to the AI assistant for a plain-language explanation and practical safety advice.
5. **User guidance:** Kavach displays the detected indicators, risk level, recommendation, and AI analysis.

## 🔍 Example

**Sample message:**

> Your bank account is blocked. Verify your account immediately using this link.

Kavach may flag the account-verification wording and assess the message alongside any other detected indicators.

The AI assistant can then explain why the request deserves caution and recommend verifying the issue through the bank's official app or website.

## 🔐 Responsible Use

Kavach is an educational prototype, not a replacement for professional security tools or an official fraud investigation.

- A high risk score does not prove that a message is fraudulent.
- A low score does not guarantee that a message is safe.
- URL characteristics are indicators, not definitive proof of malicious activity.
- AI-generated explanations may be inaccurate and should be checked against trusted sources.
- Voice recognition and AI analysis may require an internet connection.

Always verify financial requests through official channels. Never share your OTP, UPI PIN, password, or recovery codes with someone who contacts you unexpectedly.

## 🚀 Future Improvements

- Bilingual and Hinglish voice recognition
- A dedicated web-based chat interface
- Text-to-speech responses
- Expanded automated tests and evaluation against real-world scam examples
- Improved detection accuracy and risk-score calibration

## 👨‍💻 Author

**Jaden Mascarenhas**

MSc Information & Network Security | Cybersecurity | Python | AI Security

GitHub: [@jaden-mas1010](https://github.com/jaden-mas1010)

---

*Built as a hands-on project exploring how AI and explainable detection rules can help make online safety more accessible.*
