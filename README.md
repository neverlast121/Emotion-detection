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

# Project integration
If you want to Integrate it to your Project Use the given file emotion_recognition.py

# Emotion Detection from Video with OpenCV and DeepFace

This Python script utilizes OpenCV and DeepFace to perform emotion detection on a video file. The script reads frames from the video, analyzes the dominant emotion in each frame using DeepFace, and calculates emotion scores for different categories.

## Function: `detect_emotions`

### Input
- `video_path`: Path to the video file for emotion detection.

### Output
- Returns a JSON-formatted string containing emotion scores for 'neutral,' 'happy,' 'surprise,' 'angry,' 'disgust,' 'fear,' and 'sad.'

## Code Overview

1. **Initialization:**
   - Define the function `detect_emotions` that takes a `video_path` as input.

2. **Video Processing Loop:**
   - Open the video file using OpenCV.
   - Get the total number of frames in the video.
   - Initialize a dictionary to store emotion scores for different categories.

3. **Main Loop:**
   - Continuously read frames from the video.
   - Analyze every 5th frame using DeepFace to obtain the dominant emotion.
   - Update the emotion scores based on the dominant emotion in each frame.
   - Break the loop if the 'q' key is pressed.

4. **Emotion Score Calculation:**
   - Calculate emotion scores as a percentage of frames where each emotion is dominant.
   - Format the scores to two decimal places.

5. **Output:**
   - Return a JSON-formatted string containing emotion scores.

6. **Script Execution:**
   - If the script is executed directly, specify the `video_path` and call the `detect_emotions` function.
   - Print the resulting emotion scores.

## Execution
- Update the `video_path` variable with the path to the desired video file.
- Execute the script, and it will print JSON-formatted emotion scores based on the analysis of the video frames.


