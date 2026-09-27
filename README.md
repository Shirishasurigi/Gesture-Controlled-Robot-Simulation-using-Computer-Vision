\# 🤖 Gesture Controlled Robot Simulation



\## 📌 Project Overview



Gesture Controlled Robot Simulation is a real-time computer vision project that enables users to control a virtual robot using hand gestures. The system detects hand landmarks using MediaPipe, recognizes gestures, and controls a robot inside a simulated environment displayed through a web application.



The project combines computer vision, simulation, and web technologies to provide an interactive and user-friendly experience.



\---



\## 🎯 Objectives



\- Detect hand gestures using a webcam.

\- Recognize different hand gestures in real time.

\- Control a virtual robot using the recognized gestures.

\- Prevent robot collisions with walls and obstacles.

\- Display both live camera feed and robot simulation in a web interface.



\---



\## ✨ Features



\- 📷 Live webcam streaming

\- 🖐️ Real-time hand landmark detection using MediaPipe

\- 🤖 Gesture-based robot control

\- 🔄 Robot rotation and movement

\- 🚧 Collision detection with walls and obstacles

\- 🌐 Browser-based interface using Flask

\- ⚡ Live gesture status display



\---



\## 🛠️ Technologies Used



\- Python

\- Flask

\- OpenCV

\- MediaPipe

\- Pygame

\- HTML

\- CSS

\- JavaScript



\---



\## 📁 Project Structure



```

GestureRobotAI/

│

├── assets/

│   └── robot.png

│

├── src/

│   ├── camera/

│   ├── environment/

│   ├── gestures/

│   ├── robot/

│   ├── simulation/

│   └── main.py

│

├── web/

│   ├── static/

│   ├── templates/

│   ├── app.py

│   ├── camera\_stream.py

│   ├── simulator\_stream.py

│   └── requirements.txt

│

├── README.md

└── requirements.txt

```



\---



\## 🚀 Installation



\### 1. Clone or extract the project



```bash

git clone <repository-url>

```



or extract the ZIP file.



\---



\### 2. Create a virtual environment



```bash

python -m venv venv

```



Activate it:



\*\*Windows\*\*



```bash

venv\\Scripts\\activate

```



\---



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\---



\### 4. Run the application



```bash

cd web

python app.py

```



\---



\### 5. Open in your browser



```

http://127.0.0.1:5000

```



\---



\## 🖐️ Supported Gestures



| Gesture | Robot Action |

|---------|--------------|

| FORWARD | Move Forward |

| BACKWARD | Move Backward |

| LEFT | Rotate Left |

| RIGHT | Rotate Right |

| STOP | Stop Robot |



\---



\## 🔄 Workflow



1\. Capture live video from the webcam.

2\. Detect hand landmarks using MediaPipe.

3\. Recognize the hand gesture.

4\. Send the gesture to the robot simulator.

5\. Update robot movement.

6\. Display the live camera feed and simulator in the web interface.



\---



\## 📷 Screenshots



Add screenshots of:



\- Home Page

\- Live Camera Feed

\- Robot Simulator

\- Gesture Detection



\---



\## 🔮 Future Enhancements



\- Voice-controlled robot commands

\- Object pickup and drop functionality

\- Autonomous path planning

\- Database for gesture history

\- Mobile-responsive interface

\- Deployment on cloud platforms



\---



\## 👩‍💻 Developed By



\*\*Shirisha Surigi\*\*



B.Tech – Artificial Intelligence \& Machine Learning



\---



\## 📜 License



This project is developed for academic and internship purposes.

