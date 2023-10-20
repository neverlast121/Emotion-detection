import cv2
import json
from deepface import DeepFace

frame_skip = 5
cap = cv2.VideoCapture(0)

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_count = 0

# emotion scoring list
emotion_scores = {
    'neutral': 0.8, 
    'happy': 1, 
    'surprise': 0.7, 
    'angry': -1, 
    'disgust': -0.2, 
    'fear': -0.3, 
    'sad': -0.4 
    }

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % frame_skip == 0:
        result = DeepFace.analyze(frame, actions=['emotion'], 
                                enforce_detection=False,  
                                detector_backend='ssd')
        dominant_emotion = result[0]["dominant_emotion"]
        emotion_scores[dominant_emotion] += 1

    cv2.imshow("frame", frame) # open camera window
    if cv2.waitKey(1) & 0xFF == ord('q'): # press q to stop detection
        break
cap.release()

# Calculate the overall emotion score as the difference between positive and negative emotions
positive_emotions = ['happy', 'surprise', 'neutral'] # list of positive emotion
negative_emotions = ['angry', 'disgust', 'fear', 'sad'] # list of negative emotion

#sum all the emotion detected value in positive emotion list
positive_score = sum(emotion_scores[emotion] for emotion in positive_emotions) 
#sum all the emotion detected value in negative emotion list
negative_score = sum(emotion_scores[emotion] for emotion in negative_emotions) 
overall_score = (positive_score + negative_score)

emotion_results = {'emotion_score': overall_score}

# dump emotion to json format
emotion_json = json.dumps(emotion_results)

print(emotion_json)

