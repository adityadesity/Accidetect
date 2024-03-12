import os
# static\images\results
ALLOWED_EXTENSIONS = set(['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'])

def clear_directory(directory):
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
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# if __name__ == "__main__":
#     clear_directory('static/results')   #success