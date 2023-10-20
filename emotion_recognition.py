import cv2
import json
from deepface import DeepFace

def detect_emotions(video_path):
    cap = cv2.VideoCapture(video_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count = 0

    emotion_scores = {'neutral': 0, 'happy': 0, 'surprise': 0, 'angry': 0, 'disgust': 0, 'fear': 0, 'sad': 0 }

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 5 == 0:
            result = DeepFace.analyze(frame, actions=['emotion'], 
                                    enforce_detection=False,  
                                    detector_backend='ssd'
                                    )
            emotion_scores[result["dominant_emotion"]] += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

    emotion_results = {}

    for emotion, count in emotion_scores.items():
        score = (count / (total_frames // 5)) * 10

        formatted_score = "{:.2f}".format(score)
        emotion_results[emotion] = formatted_score

    emotion_json = json.dumps(emotion_results)

    return emotion_json

if __name__ == "__main__":
    video_path = 0 #'C:/Users/never/Desktop/web-site-development/backend/database/videos/recorded_video.webm'
    emotion_scores = detect_emotions(video_path)
    print(emotion_scores)
