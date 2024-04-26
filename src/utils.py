import os
import zipfile
import smtplib
from email.message import EmailMessage
import os
# static\images\results
ALLOWED_EXTENSIONS = set(['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm'])

def clear_directory(directory):
    '''
        Function to clear the current working directory.
    '''
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                clear_directory(file_path)
                os.rmdir(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


def allowed_file(filename):
    '''
        Function to check whether provided file is a video or not.
    '''
    # print('.' in filename)
    # print(filename.rsplit('.', 1)[1])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def compress_and_email(folder_path, to_email, from_email, password, subject):
    '''
        Function to compress the results and mail 
    '''
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
    msg.set_content('Team Accidetect welcomes you! Extracted Accident frames and timestamps from the given video footage. Please find the compressed folder attached.')

    with open('static/Compressed_Results/compressed_folder.zip', 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='zip', filename='compressed_folder.zip')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_email, password)
        smtp.send_message(msg)


if __name__ == "__main__":
    print(allowed_file('Demo1.mp4'))