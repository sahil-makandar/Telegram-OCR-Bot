# Telegram OCR Bot - Extract text from Images

## About
This is a Telegram bot that allows users to send text or images containing text, and the bot will perform optical character recognition (OCR) on the images to extract the text. The bot is built using the Telegram Bot API and the EasyOCR library for OCR functionality.

## Installation

1. **Clone Repository**: 
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/your_username/telegram-ocr-bot.git
     ```

2. **Navigate to Repository**: 
   - Change directory to the cloned repository:
     ```bash
     cd telegram-ocr-bot
     ```

3. **Install Dependencies**: 
   - Install the required Python dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```

4. **Set Up Telegram Bot**: 
   - Create a new bot on Telegram and obtain the bot token.
   - Replace `"<telegram-bot-token>"` in the code with your actual bot token.

## Usage

1. **Start Bot**: 
   - Run the bot script to start the bot:
     ```bash
     python bot.py
     ```

2. **Interact with the Bot**: 
   - Start a conversation with the bot on Telegram.
   - Use the following commands to interact with the bot:
     - `/start`: Start the conversation with the bot.
     - `/help`: Display help message with available commands.
   - You can send text messages or images containing text to the bot.
   - The bot will perform OCR on images and reply with the extracted text.
