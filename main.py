import os
import smtplib
import getpass
import socket
import time
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(receiver: str,
              header: str,
              subject: str,
              body: str,
              sender: str,
              password: str) -> None:
    """
    Send an email using Gmail's SMTP server.
    Args:
        receiver (str): Email address of the recipient.
        header (str): Name of the sender.
        subject (str): Subject of the email.
        body (str): Body of the email.
        sender (str): Email address of the sender.
        password (str): App password for the sender's email.
    """
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = header if header else sender
    msg['To'] = receiver
    msg['Subject'] = subject

    # Attach body
    msg.attach(MIMEText(body, 'plain'))

    try:
        gmail_SMTP_server = "smtp.gmail.com"
        print(f"Connecting to {gmail_SMTP_server}...")

        with smtplib.SMTP(gmail_SMTP_server, 587, timeout=30) as smtp:

            print("Sending EHLO...")
            smtp.ehlo()

            print("Starting TLS encryption...")
            # Encrypt connection
            smtp.starttls()

            print("Sending second EHLO...")
            smtp.ehlo()

            print("Attempting login...")
            # Login
            smtp.login(sender, password)

            print("Sending email...")
            # Send email
            smtp.send_message(msg)
            print("Email sent successfully!")
    except socket.timeout:
        print("Error: Connection timed out. Check your internet connection.")
    except smtplib.SMTPServerDisconnected:
        print("Error: Server unexpectedly disconnected. Possible causes:")
        print("- Network issues")
        print("- Server temporarily unavailable")
        print("- Incorrect server settings")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email and password.")
        print("Note: For Gmail, you MUST use an app password, not your regular password.")
        print("Generate one at: https://myaccount.google.com/apppasswords")
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main() -> None:
    """
    Main function to send an email using Gmail's SMTP server.
    """
    print("=== Gmail Email Sender ===")

    # Get sender information
    sender = input("Enter your Gmail address: ")

    # Password
    load_dotenv()
    password = os.getenv("GMAIL_APP_PASSWORD")

    # Get email details
    receiver = input("Enter recipient email address: ")
    header = input("Enter header information: ")
    subject = input("Enter email subject: ")

    print("Enter email body (press Enter twice to finish):")
    body_lines = []
    while True:
        line = input()
        if not line and (not body_lines or not body_lines[-1]):
            break
        body_lines.append(line)
    body = "\n".join(body_lines)

    # Confirm sending
    print("\nReview your email:")
    print(f"From: {header if header else sender}")
    print(f"To: {receiver}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}")

    confirm = input("\nSend this email? (y/n): ")
    if confirm.lower() == 'y':
        send_mail(receiver, header, subject, body, sender, password)
    else:
        print("Email cancelled.")


if __name__ == "__main__":
    main()