import cv2
import os
import sys
from pathlib import Path

# Add parent directory to path so src module can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import CounterConfig
from src.counter import PeopleCounter


def run(video_name="peoplecount1.mp4"):
    cfg = CounterConfig()
    counter = PeopleCounter(cfg)

    input_path = os.path.join("data", video_name)
    output_path = os.path.join("outputs", "output.mp4")

    cap = cv2.VideoCapture(input_path)
    assert cap.isOpened(), f"Error reading video file: {input_path}"

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    os.makedirs("outputs", exist_ok=True)

    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (w, h),
    )

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = counter.process_frame(frame)
        writer.write(frame)

    writer.release()
    cap.release()

    print("================================")
    print(f"Entered: {counter.entered}")
    print(f"Exited: {counter.exited}")
    print(f"Output saved to: {output_path}")
    print("================================")


if __name__ == "__main__":
    run()
