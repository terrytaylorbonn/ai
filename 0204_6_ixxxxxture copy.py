# prompt: video gesture recognition python 

import cv2
import mediapipe as mp
import numpy as np

# Initialize the MediaPipe Hands object
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize the MediaPipe Gesture Recognition object
mp_gesture = mp.solutions.gesture_recognizer
gesture = mp_gesture.GestureRecognizer(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Load the video
video_path = 'path/to/video.mp4'
cam = cv2.VideoCapture(video_path)

while True:
    # Read each frame from the video
    ret, frame = cam.read()

    if not ret:
        print("Error reading frame")
        break

    # Convert the frame to RGB for Mediapipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe Hands
    results = hands.process(frame_rgb)

    # Check if any hands are detected
    if results.multi_hand_landmarks:
        # Convert the frame back to BGR for drawing
        frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

        # Draw hand landmarks on the frame
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        # Process the frame with Mediapipe Gesture Recognition
        results = gesture.process(frame_rgb)

        # Display the gesture recognition results
        if results.gestures:
            for gesture_id in results.gestures:
                if gesture_id == 0:
                    gesture_name = 'Fist'
                elif gesture_id == 1:
                    gesture_name = 'Palm'
                elif gesture_id == 2:
                    gesture_name = 'Thumbs Up'
                elif gesture_id == 3:
                    gesture_name = 'Thumbs Down'
                elif gesture_id == 4:
                    gesture_name = 'Peace'
                elif gesture_id == 5:
                    gesture_name = 'High Five'
                elif gesture_id == 6:
                    gesture_name = 'Stop'
                else:
                    gesture_name = 'Unknown'

                # Draw the gesture name on the frame
                cv2.putText(frame, gesture_name, (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Hand Gesture Recognition', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the windows
cam.release()
cv2.destroyAllWindows()
