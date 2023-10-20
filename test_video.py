import cv2
from deepface import DeepFace
from collections import Counter
video = 'C:/Users/never/Desktop/activity-recognition/video_1.mp4'
cap = cv2.VideoCapture(video)


emotion_counter = Counter()

num_frames = 5

while True:
    for _ in range(num_frames):
        ret, frame = cap.read()

        result = DeepFace.analyze(frame, actions=['emotion'], 
                                  enforce_detection=False,  
                                  # detector_backend = 'retinaface',
                                  # detector_backend = 'mtcnn', 
                                  # detector_backend ='opencv',
                                  detector_backend = 'ssd'
                                )
        
        emotion_counter.update([result["dominant_emotion"]])
       
    most_common_emotion, _ = emotion_counter.most_common(1)[0]
    print(most_common_emotion)
   
    cv2.putText(frame, f'Emotion: {most_common_emotion}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Webcam Emotion Recognition', frame)

    emotion_counter.clear()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
