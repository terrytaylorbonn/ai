#https://colab.research.google.com/github/googlesamples/mediapipe/blob/main/examples/gesture_recognizer/python/gesture_recognizer.ipynb#scrollTo=ihsUxUpouk0F

# prompt: webcam video recognize images

import cv2
import mediapipe as mp
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Initialize the hand detection model.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

model_path = '/home/tt15/Downloads/gesture_recognizer.task'



print("===========================================")


# #terry added
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)
# gesture = vision.GestureRecognizer.create_from_options()
#    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)


# Initialize the gesture recognition model.
# mp_gesture = mp.solutions.gesture_recognizer
# gesture = mp_gesture.GestureRecognizer(
#     static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

# Initialize the video capture object.
cam = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


while True:
  # Read each frame from the webcam.
  ret, frame = cam.read()

  # Convert the frame to RGB for gesture recognition.
  frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  # Process the frame with the hands model.
  # results = recognizer.recognize(frame_rgb)
  results = recognizer.process(frame_rgb)

  # Draw hand landmarks on the frame.
  if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
      mp_drawing.draw_landmarks(
          frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())

#   # # Process the frame with the gesture recognition model.
#   # results = gesture.process(frame_rgb)

#   # Draw gesture recognition results on the frame.
#   if results.gestures:
#     for gesture_id in results.gestures:
#       if gesture_id == 0:
#         cv2.putText(frame, 'Thumbs up', (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#       elif gesture_id == 1:
#         cv2.putText(frame, 'Thumbs down', (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#       elif gesture_id == 2:
#         cv2.putText(frame, 'Peace', (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#       elif gesture_id == 3:
#         cv2.putText(frame, 'High five', (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#       elif gesture_id == 4:
#         cv2.putText(frame, 'Stop', (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#       elif gesture_id == 5:
#         cv2.putText(frame, 'Fist', (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#       elif gesture_id == 6:
#         cv2.putText(frame, 'Wave', (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

  # Display the resulting frame.
  cv2.imshow('Gesture Recognition', frame)

  # Check if the user wants to quit.
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Release the webcam and close all windows.
cam.release()
cv2.destroyAllWindows()