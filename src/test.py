import zipfile
import smtplib
from email.message import EmailMessage
import os
'''
    File to test piece of codes
'''
def compress_and_email(folder_path, to_email, from_email, password, subject):
    # Compress the folder
    with zipfile.ZipFile('static/Compressed_Results/compressed_folder.zip', 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

    # Email the compressed file
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content('Please find the compressed folder attached.')

    with open('compressed_folder.zip', 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='zip', filename='compressed_folder.zip')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_email, password)
        smtp.send_message(msg)

# Example usage:
folder_path = 'static/assets'
to_email = 'adityadesity11@gmail.com'
from_email = 'aditidagadkhair3011@gmail.com'
password = 'esahbdetgodyhzoz'
subject = 'Compressed Folder'

compress_and_email(folder_path, to_email, from_email, password, subject)
