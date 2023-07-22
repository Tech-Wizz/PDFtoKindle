import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_path):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Add body to the email
    message.attach(MIMEText(body, "plain"))

    # Attach the PDF file to the email
    with open(attachment_path, "rb") as file:
        part = MIMEApplication(file.read(), Name=os.path.basename(attachment_path))
    part["Content-Disposition"] = f'attachment; filename="{os.path.basename(attachment_path)}"'
    message.attach(part)

    # Log in to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

def main():
    sender_email = "fill@gmail.com"  # Replace with your Gmail email address
    sender_password = "fill"      # Replace with your Gmail password
    recipient_email = "fill@email.com"  # Replace with the recipient's email address
    subject = "Fill"
    body = "Fill"

    pdf_folder = "pdf"  # Folder where the PDF files are located
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, pdf_path)
            print(f"Sent '{filename}' to {recipient_email}")

if __name__ == "__main__":
    main()
