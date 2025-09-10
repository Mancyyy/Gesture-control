import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hand class.
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam.
cap = cv2.VideoCapture(0)

# Configure hand tracking
with mp_hands.Hands(
        max_num_hands=1,  # Track only one hand
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the image horizontally for a selfie-view display.
        image = cv2.flip(image, 1)

        # Convert the BGR image to RGB before processing.
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and detect hand.
        results = hands.process(image_rgb)

        # If hand is detected, proceed.
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                # Draw hand landmarks.
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract landmark positions (Tip and base of fingers).
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
                pinky_base = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]
                index_base = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
                middle_base = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]

                # Gesture: Left Click if index finger is lowered
                if index_tip.y > index_base.y and middle_tip.y < middle_base.y:
                    pyautogui.click()
                    print("Left Click Triggered")
                    continue  # Skip further movement and clicks if left click is triggered

                # Gesture: Right Click if middle finger is lowered
                if middle_tip.y > middle_base.y and index_tip.y < index_base.y:
                    pyautogui.rightClick()
                    print("Right Click Triggered")
                    continue  # Skip further movement and clicks if right click is triggered

                # Gesture: Stop mouse movement if the little (pinky) finger is raised
                if pinky_tip.y < pinky_base.y:
                    print("Mouse movement stopped because little finger is raised.")
                    continue  # Skip mouse movement if pinky is raised

                # Gesture: Move mouse when index and middle fingers are up
                if (index_tip.y < index_base.y and middle_tip.y < middle_base.y):
                    screen_width, screen_height = pyautogui.size()
                    mouse_x = int(index_tip.x * screen_width)
                    mouse_y = int(index_tip.y * screen_height)

                    pyautogui.moveTo(mouse_x, mouse_y)  # Move the mouse cursor
                    print(f"Moving mouse to: {mouse_x}, {mouse_y}")

        # Display the result.
        cv2.imshow('Hand Gesture Control', image)

        # Exit the loop if 'q' is pressed.
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# Release the webcam and close the window.
cap.release()
cv2.destroyAllWindows()
