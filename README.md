# 🧍‍♂️ People Counter using YOLOv8

A computer vision project that counts how many people **enter** and **exit** a shop using **YOLOv8 object detection** and **ByteTrack multi-object tracking**.

The system analyzes video footage, tracks individuals across frames, and counts crossings through a virtual door line to determine entry and exit events.

---

## 🚀 Features

* ✅ YOLOv8 person detection
* ✅ ByteTrack multi-object tracking
* ✅ Entry / Exit counting using virtual line crossing
* ✅ Configurable parameters (door position, buffer zone, confidence)
* ✅ Invisible or visible counting line
* ✅ Annotated output video generation
* ✅ Modular and reusable architecture
* ✅ Clean GitHub-ready project structure

---

## 📂 Project Structure

```
people-counter-yolo/
│
├── data/                # Input videos (not included in repo)
├── outputs/             # Generated results
│
├── src/
│   ├── counter.py       # Core counting logic
│   ├── config.py        # Configuration parameters
│   └── utils.py         # Helper functions
│
├── scripts/
│   └── run_video.py     # Main execution script
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/people-counter-yolo.git
cd people-counter-yolo
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1️⃣ Place your video inside the **data/** folder:

```
data/peoplecount1.mp4
```

2️⃣ Run the script:

```bash
python scripts/run_video.py
```

3️⃣ Output will be saved to:

```
outputs/output.mp4
```

Console output example:

```
Entered: 4
Exited: 2
```

---

## ⚙️ Configuration

You can modify parameters inside:

```
src/config.py
```

Important settings:

| Parameter       | Description                             |
| --------------- | --------------------------------------- |
| x_line          | Position of the virtual door line       |
| buffer          | Dead zone to prevent flickering counts  |
| inside_is_right | Which side represents the shop interior |
| conf            | Detection confidence threshold          |
| show_line       | Show or hide the counting line          |

---

## 🧠 How It Works

1. YOLOv8 detects people in each frame.
2. ByteTrack assigns a unique ID to every person.
3. The system monitors movement across a virtual door line.
4. Crossing direction determines **enter** or **exit**.
5. Counts are accumulated and displayed on the video.

---

## 📸 Demo

You can add a GIF or screenshot here showing the system in action.

Example:

```
assets/demo.gif
```

---

## 📦 Requirements

* Python 3.9+
* OpenCV
* Ultralytics YOLOv8
* NumPy
* Shapely

Install with:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Notes

* Large videos and model weights are excluded from GitHub.
* Place your own videos inside the `data/` directory before running.
* GPU is recommended for faster inference but not required.

---

## 🔮 Future Improvements

* Real-time webcam support
* Streamlit dashboard UI
* Multi-camera counting
* Zone-based analytics
* Docker deployment
* Cloud inference support

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/YOUR_USERNAME

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ If You Found This Useful

Please consider giving the repository a star ⭐
