# Gmail Email Sender

A simple, interactive command-line tool for sending emails through Gmail.

## Requirements

- Python 3.8+
- Gmail account with 2-Step Verification enabled
- Gmail App Password

## Setup

1. Make sure you have Python installed on your system
2. Set up Gmail App Password
3. Save the Gmail App Password in a .env file, like this:
   ```
   echo "GMAIL_APP_PASSWORD='your_app_password'" > .env
   ```

## Usage

1. Run the script:
   ```
   python main.py
   ```

2. Follow the prompts to:
   - Enter your Gmail address
   - Enter recipient email address
   - Enter sender name/header (optional)
   - Enter email subject
   - Compose email body (press Enter twice to finish)
   - Review and confirm sending