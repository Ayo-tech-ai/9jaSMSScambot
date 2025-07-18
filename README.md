# 🇳🇬 Naija Scam SMS Detector Bot

The **Naija Scam SMS Detector** is an AI-powered Telegram bot designed to help users in Nigeria quickly assess whether a suspicious SMS or message might be part of a scam.

Built using **machine learning (Naive Bayes + TF-IDF)** and localized with **Nigerian scam message patterns**, the bot allows users to **submit messages directly in Telegram**, and receive a result that includes:

- 🚦 Scam Status (Safe, Suspicious, or Scam)
- 📊 Confidence Score (e.g., 89.39%)
- 🔍 Simple explanation (highlights words that triggered detection)
- 🙋 Feedback option (users can help improve accuracy)

## ⚠️ Disclaimer

This bot uses AI to **assist**, not replace, human judgment.  
- It may occasionally flag legit messages or miss complex scams.
- One message alone may not give full context — users should consider the **entire conversation history** before acting.
- Users are fully responsible for how they respond to or act on the message results.

> Use this tool as a **guide**, not as a final authority.

---

## ✅ Real-World Example

A message was received via Facebook Messenger promising a card giveaway:

> *"Drop your phone number for Card Giveaway  
> MTN... 2000  
> GLO... 3000  
> Airtel...1500  
> 9MOBILE...1500"*

When passed through the Naija Scam Bot, the result was:

> **🔴 Scam Detected!**  
> **Confidence: 89.39%**

This example demonstrates the bot’s ability to catch **social engineering tactics** common in Nigerian scam culture, such as fake giveaways, vague sender identity, and request for sensitive info.

---

## 🔗 Try the Bot

[🚀 Launch Naija Scam Bot](**Coming Soon!**)
---

## 🛠 Built With
- Python 🐍
- scikit-learn
- Telegram Bot API
- Streamlit (for web version)
- Render.com (for deployment)

---

## 📬 Feedback or Issues?

Found a false positive or want to contribute a message sample?  
Please open an issue or submit feedback through the Telegram bot.
