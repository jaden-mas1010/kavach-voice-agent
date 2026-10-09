# Kavach 🛡️
### AI-Powered Scam Awareness Assistant

Kavach is a Python scam-awareness assistant designed to help people recognise suspicious messages, understand potential scam indicators, and make safer decisions online.

It combines **rule-based detection**, **weighted risk scoring**, and **AI-generated explanations**. Kavach supports text conversations in English, Hindi, and Hinglish, experimental **English voice input**, and a basic **email-header inspection** feature for `.eml` files.

## ✨ Features

### Message analysis
- **Scam keyword detection:** Flags suspicious wording involving OTPs, banking, KYC, fake refunds, and urgency.
- **Fuzzy phrase matching:** Uses Python's `SequenceMatcher` to catch some misspelled scam phrases.
- **Suspicious URL indicators:** Checks for IP-address links, shortened URLs, the `@` URL trick, and Punycode domains.
- **Explainable risk scoring:** Adds predefined weights for detected indicators (capped at 100), then assigns LOW, MEDIUM, or HIGH risk.
- **AI-powered explanations:** Uses the Groq API and a local scam-awareness guide to provide practical, cautious advice.
- **Recent conversation history:** Retains a limited number of messages during the session.
- **Experimental voice input:** Uses speech recognition to turn spoken English into text for the existing analysis pipeline.

### Email-header inspection (new)
- Reads a locally saved **`.eml`** email using Python's `email` parser.
- Displays **From**, **Reply-To**, **Return-Path**, **Subject**, and **Received** routing headers.
- Displays any **DKIM-Signature** headers, without claiming they are valid.
- Extracts **reported SPF, DKIM, and DMARC statuses** from `Authentication-Results` headers.
- Flags a **From/Reply-To domain mismatch** and certain **reported authentication failures**.

> **Important:** The email feature inspects *header text*. It does **not** independently perform SPF checks, cryptographically verify DKIM signatures, validate DMARC alignment, or establish that `Authentication-Results` headers were inserted by a trusted receiving server. Header claims can be spoofed. A mismatch or authentication failure is a warning sign, not proof of fraud.

## 🧰 Tech Stack

- **Python** — application logic and security detection
- **Groq API** — generative-AI explanations (`openai/gpt-oss-20b` in the current code)
- **SpeechRecognition** — experimental voice-to-text using Google's recognition service
- **Python `email` package** — `.eml` parsing and header inspection
- **`re`, `difflib`, `urllib.parse`, `ipaddress`** — text and URL indicator checks
- **pytest** — automated tests for the message-detection functionality

## ⚙️ Getting Started

### 1. Clone the repository

```powershell
git clone https://github.com/jaden-mas1010/kavach-voice-agent.git
cd kavach-voice-agent
```

### 2. Install dependencies

Make sure Python is installed. On Windows, run:

```powershell
py -m pip install groq "SpeechRecognition[audio]" pytest
```

On other systems, replace `py` with `python` if appropriate. Microphone use may require audio-device permissions and a working audio backend.

### 3. Configure your Groq API key

Create an API key using the Groq developer console. For the current PowerShell session:

```powershell
$env:GROQ_API_KEY = "your_api_key_here"
```

Never commit a real API key, secret, or `.env` file.

### 4. Start Kavach

```powershell
py app.py
```

At the prompt, you can enter:

| Input | Purpose |
| --- | --- |
| `Hello, are we still meeting tomorrow?` | Demonstrate a normal message |
| `Urgent! Share your OTP immediately.` | Demonstrate a high-risk OTP/urgency example |
| `/voice` | Speak a message into your microphone (experimental English input) |
| `/email sample_email.eml` | Inspect a local example email's headers |
| `exit` | End the program |

Use `/email "C:\path\to\message.eml"` when the file is located elsewhere. Only inspect email files you are authorised to handle.

### 5. Run the existing automated tests

```powershell
py -m pytest -q
```

The included `test_kavach.py` covers several message-detection and URL-indicator cases. It does not, by itself, constitute a test of the new email-header analyser, live Groq responses, or microphone recognition.

## 🔎 How It Works

**Text or voice path**

1. Read typed text or transcribe English microphone input.
2. Check keyword matches, fuzzy phrases, urgency cues, and suspicious URL patterns.
3. Calculate a weighted heuristic risk score and assign a LOW/MEDIUM/HIGH level.
4. Ask the AI for a plain-language explanation using the scam-awareness guide.
5. Display findings, a recommendation, and the AI response.

**Email-header path**

1. Enter `/email sample_email.eml` to open a local email file.
2. `BytesParser` parses the raw email into a structured message object.
3. Kavach prints sender, reply, routing, and authentication-related headers.
4. It compares the From and Reply-To domains and extracts reported SPF/DKIM/DMARC results.
5. It prints warning indicators; **this command currently inspects headers rather than automatically analysing the email body through the AI pipeline**.

## 🧪 Examples

**Suspicious text:**

```text
Urgent! Share your OTP immediately.
```

This combines an OTP request and urgency. Kavach's rule-based scoring identifies these indicators and can assign a HIGH risk level.

**Email-header demo:**

```powershell
py app.py
# At the Kavach prompt:
/email sample_email.eml
```

The fictional `sample_email.eml` used in development has a differing From/Reply-To domain and reports `spf=fail`, `dkim=none`, and `dmarc=fail`. In the demo, the current rules display **three warnings**: one domain mismatch and two reported failures. These values are part of the **sample email's text**, not independently verified mail authentication results.

## 📁 Key Files

| File | Purpose |
| --- | --- |
| `app.py` | Main CLI, Groq integration, message analysis, voice input, and `/email` command |
| `scam_keyword.py` | Suspicious phrase list |
| `scam_guide.txt` | Local safety-advice reference for the AI |
| `email_headers.py` | Email-header parsing and heuristic warning checks |
| `sample_email.eml` | Fictional example email for demonstration |
| `test_kavach.py` | Automated tests for the core message-detection rules |

## 🔐 Responsible Use and Limitations

Kavach is an educational prototype, not a replacement for fraud investigation or production email-security tools.

- **High risk** does not prove fraud; **low risk** does not guarantee safety.
- IP-address links, shortened URLs, and domain mismatches can appear in legitimate messages.
- Reported `Authentication-Results` values can be untrustworthy, especially when received from an unknown or attacker-controlled source.
- The presence of a DKIM signature does not mean its cryptographic signature was verified.
- The email-header feature does not calculate a validated fraud probability.
- AI responses can be inaccurate; follow up through independently verified official channels.
- The voice-input feature currently uses `en-IN` speech recognition and needs a microphone and access to the recognition service.

Never share OTPs, UPI PINs, passwords, or recovery codes with unexpected contacts. Don't upload genuine personal emails, secrets, or sensitive headers to a public repository.

## 🚀 Future Improvements

- Independent DKIM cryptographic verification and trustworthy mail-authentication assessment
- Safer HTML email-body parsing and cross-checking body content against header indicators
- A dedicated web-based chat interface
- Better Hindi and Hinglish speech recognition and optional text-to-speech responses
- An expanded labelled scam dataset, false-positive/false-negative evaluation, and risk-score calibration
- More comprehensive automated tests, including email-header edge cases

## 👨‍💻 Author

**Jaden Mascarenhas**  
MSc Information & Network Security | Cybersecurity | Python | AI Security  
GitHub: [@jaden-mas1010](https://github.com/jaden-mas1010)

---

*Built as a hands-on project exploring how AI and explainable detection rules can help make online safety more accessible.*
