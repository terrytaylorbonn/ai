# prompt: mediapipe gesture recognizer python video

import cv2
import mediapipe as mp

# Initialize the MediaPipe Hands object
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

model_path = '/home/tt15/Downloads/gesture_recognizer.task'




# Initialize the MediaPipe Gesture Recognizer object
mp_gesture = mp.solutions.gesture_recognizer
gesture = mp_gesture.GestureRecognizer(
    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

# Open a video file or webcam stream
#video_path = 'path/to/video.mp4'
# For webcam stream, use video_path = 0
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    # Read each frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to RGB for Mediapipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Hands and Gesture Recognizer
    results = hands.process(frame_rgb)
    results_gesture = gesture.process(frame_rgb)

    # Draw hand landmarks on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

    # Draw gesture recognition results on the frame
    if results_gesture.multi_hand_landmarks:
        for hand_landmarks, classification_results in zip(
                results_gesture.multi_hand_landmarks,
                results_gesture.classifications):
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_gesture.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            # Print the gesture classification results
            for classification in classification_results:
                print(f'Gesture: {classification.gesture_name}, Score: {classification.score}')

    # Display the resulting frame
    cv2.imshow('Gesture Recognition', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the windows
cap.release()
cv2.destroyAllWindows()
