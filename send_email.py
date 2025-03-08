import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time
import os

def send_email(subject, body, img_path = None):
    # Email configuration
    sender_email = "smart.edge.doorbell@gmail.com"  # Sender's email address
    receiver_email = "sourav280902@gmail.com"  # Receiver's email address
    password = "egkrbqrembvqyefn"  # Sender's email password

    # Create message container - MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    
    # Attach image if provided
    if img_path:
        with open(img_path, "rb") as attachment:
            image_mime = MIMEApplication(attachment.read(), _subtype="jpg")
        image_mime.add_header("Content-Disposition", "attachment", filename=os.path.basename(img_path))
        message.attach(image_mime)

    # Connect to SMTP server and send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Login to sender's email account
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send email
