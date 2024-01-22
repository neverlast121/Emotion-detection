# Emotion-detection
Using DeepFace and OpenCV to detect  emotion 

# DeepFace Emotion

# Emotion Detection with OpenCV and DeepFace

This Python script utilizes OpenCV and DeepFace to perform real-time emotion detection through a webcam feed. The script continuously captures video frames from the webcam, analyzes the dominant emotion in each frame, and calculates an overall emotion score based on predefined emotion weights.

## Dependencies

- OpenCV: A computer vision library for real-time image and video processing.
- DeepFace: A deep learning-based facial analysis library for emotion detection.

## Code Overview

1. **Initialization:**
   - Import necessary libraries (`cv2`, `json`, `DeepFace`).
   - Set parameters, such as `frame_skip` for processing efficiency.
   - Open a webcam using OpenCV.

2. **Main Loop:**
   - Continuously capture frames from the webcam.
   - Analyze every `frame_skip`-th frame using DeepFace to obtain the dominant emotion.
   - Update the emotion scores based on predefined weights.

3. **Display Frames:**
   - Display the video frames in a window using OpenCV.
   - Press 'q' to stop the emotion detection loop.

4. **Calculate Overall Emotion Score:**
   - Define positive and negative emotion lists.
   - Sum the emotion scores for each category.
   - Calculate the overall emotion score as the difference between positive and negative emotions.

5. **Output:**
   - Display the overall emotion score in JSON format.
   - The JSON includes an 'emotion_score' key with the calculated value.

6. **Cleanup:**
   - Release the webcam when the script is terminated.

## Emotion Scoring
- Emotion scores are updated based on predefined weights for emotions like 'neutral,' 'happy,' 'surprise,' 'angry,' 'disgust,' 'fear,' and 'sad.'

## Positive and Negative Emotions
- Positive emotions: 'happy,' 'surprise,' 'neutral.'
- Negative emotions: 'angry,' 'disgust,' 'fear,' 'sad.'

## Overall Emotion Score Calculation
- The overall emotion score is calculated as the difference between the sum of positive emotion scores and the sum of negative emotion scores.

## Execution
- Execute the script, and it will continuously display webcam frames with real-time emotion scores until the 'q' key is pressed.

# Demo for detection
use the test_video.py file to check how this work with real time or on video it will visulse the detection emotion on every frame.

# Scoring emotion
some time many project need the score of emotion so you can use the score_emotion.py file, you can also change the scoreing to your required.

# project integration
you want integrate it to your existing project the use the emotion_recognition.py file.
