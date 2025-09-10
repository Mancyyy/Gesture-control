# Gesture-control
Gesture-based computer control using Python, OpenCV, MediaPipe, and PyAutoGUI. Tracks hand landmarks via webcam to enable mouse movement, left/right clicks, and gesture-based control. Supports real-time interaction with intuitive finger gestures, providing a hands-free way to navigate and control the system


🖐️ Gesture Control Project
This project implements a gesture-based computer control system using Python, OpenCV, MediaPipe, and PyAutoGUI. By tracking hand landmarks in real-time through a webcam, it enables mouse movement, left/right clicks, and gesture-based interactions, providing a hands-free way to control your computer.

📌 Features
👆 Move Mouse Cursor – Control cursor by moving your index and middle fingers.

🖱️ Left Click – Triggered when the index finger is lowered while the middle finger is raised.

🖱️ Right Click – Triggered when the middle finger is lowered while the index finger is raised.

✋ Stop Mouse Movement – Raise your pinky finger to stop the cursor from moving.

🎥 Real-time Hand Tracking – Powered by MediaPipe Hand Landmarks for accurate gesture recognition.

🛠️ Tech Stack
Python 3.x

OpenCV – For image processing & webcam input

MediaPipe – For real-time hand tracking

PyAutoGUI – For simulating mouse actions

⚙️ Installation
Clone the repository:

git clone https://github.com/your-username/gesture-control-project.git
cd gesture-control-project
Install required dependencies:

pip install opencv-python mediapipe pyautogui
Run the project:

python gesture_control_project.py
🎮 How It Works
The webcam captures live video.

MediaPipe detects and tracks hand landmarks.

Gestures are interpreted based on finger positions:

Index Up + Middle Up → Move mouse

Index Down + Middle Up → Left Click

Middle Down + Index Up → Right Click

Pinky Up → Pause cursor movement

📊 Use Cases
Hands-free navigation for accessibility

Alternative input system for gaming and interactive applications

Prototype for gesture-based HCI (Human-Computer Interaction) research

🚀 Future Improvements
Add scrolling gestures (two-finger swipe)

Integrate multi-hand tracking

Support for custom gesture training

Add voice + gesture hybrid control
