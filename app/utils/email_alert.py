# app/utils/email_alert.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app

def send_alert_email(to_email, subject, change_summary, start_date, end_date):
    try:
        # Load credentials from Flask config
        smtp_server = current_app.config.get("MAIL_SERVER")
        smtp_port = current_app.config.get("MAIL_PORT")
        sender_email = current_app.config.get("MAIL_USERNAME")
        sender_password = current_app.config.get("MAIL_PASSWORD")

        # Compose email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to_email
        msg["Subject"] = subject

        body = f"""
        <h2>🛰️ AkashDrishti Change Detection Alert</h2>
        <p><strong>Change Summary:</strong> {change_summary}</p>
        <p><strong>Date Range:</strong> {start_date} to {end_date}</p>
        <p>This is an automated alert based on recent satellite data.</p>
        <br><p>Regards,<br><strong>AkashDrishti System</strong></p>
        """

        msg.attach(MIMEText(body, "html"))

        # Send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print(f"✅ Email sent to {to_email}")
        return True

    except Exception as e:
        print("❌ Failed to send email:", e)
        return False
