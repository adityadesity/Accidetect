# Accidetect

Accidetect is a Flask web application designed to automate the process of accident detection in surveillance footage and extract precise timestamps corresponding to the moment of occurrence. This project aims to facilitate insurance claims processing by eliminating the need for manual review of entire video footage, providing a more efficient and accurate solution.

## Features

- **Real-Time Accident Detection**: Utilizes deep learning techniques to classify images from surveillance cameras in real-time, accurately identifying accident occurrences.

- **Timestamp Extraction**: Automatically extracts timestamps of accident occurrences, providing precise temporal information crucial for insurance claims processing.

- **Flask Web Application**: User-friendly web interface allows users to upload surveillance footage and initiate real-time analysis with ease.

- **Efficient Claims Processing**: Accelerates insurance claims processing by automating accident detection and timestamp extraction, reducing manual effort and enhancing efficiency.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/adityadesity11/Accidetect.git
   ```

2. **Download requirements**
```bash
pip install -r requirements.txt
```
3. Save model.h5 to **artifacts/**

4. Run the command:
```bash
python app.py
```
Access the web application at http://localhost:5000 and follow the instructions to upload surveillance footage and extract accident timestamps.







![Sample result](static/sample_output.jpg)