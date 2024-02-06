# prompt: video gesture recognition python 

import cv2
import mediapipe as mp
import numpy as np

# Load the MediaPipe Hands model.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Load the MediaPipe Gesture Recognition model.
mp_gesture = mp.solutions.gesture_recognizer
gesture = mp_gesture.GestureRecognizer(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize the video capture object.
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read the frame from the video capture object.
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to RGB for Mediapipe.
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe Hands.
    results = hands.process(frame_rgb)

    # Process the frame with Mediapipe Gesture Recognition.
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Convert the hand landmarks to pixel values.
            hand_landmarks_pixel = mp_hands.HandLandmark.convert_landmarks_to_pixel_coordinates(
                hand_landmarks, frame_rgb.shape)

            # Draw the hand landmarks on the frame.
            mp_drawing.draw_landmarks(
                frame, hand_landmarks_pixel, mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            # Convert the hand landmarks to normalized values.
            hand_landmarks_normalized = mp_hands.HandLandmark.convert_landmarks_to_normalized_coordinates(
                hand_landmarks, frame_rgb.shape)

            # Recognize the gesture.
            gesture_result = gesture.recognize(hand_landmarks_normalized)

            # Draw the gesture result on the frame.
            if gesture_result.gestures:
                gesture_name = gesture_result.gestures[0].name
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks_pixel, mp_gesture.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                cv2.putText(frame, gesture_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame.
    cv2.imshow('Gesture Recognition', frame)

    # Break the loop if the 'q' key is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object.
cap.release()

# Close all the windows.
cv2.destroyAllWindows()
