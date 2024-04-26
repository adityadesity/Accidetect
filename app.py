from flask import Flask,render_template,url_for,request,flash,redirect
from src import utils
from src.pipeline.predict_pipeline import PredictionPipeline
from src.exception import CustomException
import os
import sys
from src.logger import logging
app = Flask(__name__)
app.config['SECRET_KEY'] = 'accidetect'

# Clear the results folder on first load
utils.clear_directory('static/results')
logging.info("Cleared result directory")
# Initiate prediction pipeline that includes model loading
preds_obj = PredictionPipeline()
from_email = 'teams.accidetect@gmail.com'
password = '*'
subject = "Accidents and timestamps"
folder_path = 'static/results'
num_uses = 0
# Routes
@app.route('/')
def home():
    utils.clear_directory('static/results')
    utils.clear_directory('static/Compressed_Results')
    return render_template('index.html')
# Testing route
@app.route('/result',methods = ['GET','POST'])
def result():
    if request.method == 'POST':
        video = request.form.get('video')
        email = request.form.get('email')
        print(email)
        if utils.allowed_file(video):
            result=preds_obj.predict(video_path=f'static/uploads/{video}')
            print(result)
            try:
                utils.compress_and_email(folder_path, email, from_email, password, subject)
                logging.info(f"Email sent to {email}")
                
                logging.info(f'No. of uses in this session : {num_uses}')
            except Exception as e:
                flash('Provide a valid email id!','error')
                logging.info("Invalid email id")
                raise CustomException(e,sys)
            return render_template('result.html',result = result)
        else:
            flash('Supported Format - ''mp4'', ''avi'', ''mkv'', ''mov'', ''wmv'', ''flv'', ''webm'' ', 'error')
    return redirect('/')

@app.route('/about')    
def about():
    return render_template('about.html')
@app.route('/team')
def team():
    return render_template('team.html')
# Test Route
@app.route('/test')
def test():
    preds_obj.predict('static/uploads/Demo.mp4')
    return "Test Success"



if __name__ == "__main__":
    app.run(port=5000, debug=True)
    utils.clear_directory('static/results')
    utils.clear_directory('static/Compressed_Results')