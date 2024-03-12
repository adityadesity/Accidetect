import sys
import os
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
# from tensorflow.keras.models import load_model
import cv2
from ultralytics import YOLO
class PredictionPipeline:
    def __init__(self):
        self.model = YOLO('artifacts/best.pt')
        logging.info("loaded the model")
        
    def predict(self,video_path):
        output = {}
        try:
            cap = cv2.VideoCapture(video_path)
            logging.info("Loaded the video")
            threshold = 0.5
            frame_count = 0
            i:int = 0
            while True:
                ret, frame = cap.read()

                # Check if the frame is read successfully
                if not ret:
                    break
                
                # Capture 1 frame per second
                if frame_count % int(cap.get(cv2.CAP_PROP_FPS)) == 0:
                    results = self.model(frame)[0]
                    logging.info(f"Checking for frame number {frame_count}.")
                    for result in results.boxes.data.tolist():
                        x1, y1, x2, y2, score, class_id = result
                        display_text = f"{results.names[int(class_id)].upper()}: {score:.2f}"
                        if score > threshold:
                            if class_id == 0 or class_id == 4 or class_id == 9:
                                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 0), 4)
                                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2, cv2.LINE_AA)
                                
                            else:
                                logging.info("Accident detected")
                                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 4)

                                cv2.putText(frame, display_text, (int(x1), int(y1 - 10)),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                                
                                timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
                                timestamp_seconds = timestamp / 1000  # Convert to seconds  
                                timestamp_seconds = round(timestamp_seconds,1)
                                output_path = f'./static/results/accident_frame_{i}.jpg'
                                logging.info(f"Logging the accident timestamp -> {timestamp_seconds} s")
                                output[f'accident_frame_{i}.jpg'] = timestamp_seconds
                                cv2.imwrite(output_path, frame)
                    i = i+1
                    
                frame_count += 1

            cap.release()
            cv2.destroyAllWindows()
            return output
        except Exception as e:
            raise CustomException(e,sys)
        

# if __name__ == "__main__":
#     prediction_obj = PredictionPipeline()
#     print(prediction_obj.predict('static/uploads/Demo.mp4'))
# success    