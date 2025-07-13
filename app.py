from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
import joblib
import numpy as np
import os

# === Load the saved model and vectorizer ===
bundle = joblib.load("naija_sms_detector_bundle.joblib")
model = bundle["model"]
vectorizer = bundle["vectorizer"]

# === /start command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intro_message = (
        "👋 *Welcome to the Naija SMS / WhatsApp Scam Detector Bot!*\n\n"
        "📩 *How to use:*\n"
        "Just *copy and paste* the suspicious message here — whether it's from SMS or WhatsApp.\n"
        "I'll instantly tell you if it looks like a *SCAM*, is *SUSPICIOUS*, or is *LEGIT*.\n\n"
        "⚠️ *Note:* This tool uses AI and may not be 100% accurate.\n"
        "Always use your own judgment before taking any action."
    )
    await update.message.reply_markdown(intro_message)

# === Analyze message and return response ===
def analyze_text(text):
    vector = vectorizer.transform([text])
    proba = model.predict_proba(vector)[0][1]  # Probability of SCAM
    confidence = round(proba * 100, 2)

    # === Classify based on confidence thresholds ===
    if confidence >= 85:
        emoji = "🔴"
        label = f"{emoji} *Scam Detected!*"
    elif 60 <= confidence < 85:
        emoji = "🔵"
        label = f"{emoji} *Suspicious Message* (Be Careful)"
    else:
        emoji = "🟢"
        label = f"{emoji} *Legit Message*"

    response = f"{label}\n*Confidence:* {confidence}%"
    return response

# === Handle incoming message ===
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    result = analyze_text(text)
    await update.message.reply_markdown(result)

# === Run the bot ===
if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("8049856412:AAEaHkM752bTS_FWknMFkXmTLLJAWdemzeM")).build()
    # /start intro
    app.add_handler(CommandHandler("start", start))

    # Handle normal messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
