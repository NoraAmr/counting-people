import cv2
from ultralytics import YOLO

class PeopleCounter:
    def __init__(self, config):
        self.cfg = config
        self.model = YOLO(self.cfg.model_path)
        self.entered = 0
        self.exited = 0
        self.track_state = {}  # id -> "left" or "right"

    def process_frame(self, frame):
        results = self.model.track(
            frame,
            persist=True,
            classes=[0],
            conf=self.cfg.conf,
            iou=self.cfg.iou,
            tracker=self.cfg.tracker,
        )
        boxes = results[0].boxes
        if boxes is None or boxes.id is None:
            return frame

        ids = boxes.id.int().cpu().tolist()
        xyxy = boxes.xyxy.cpu().numpy()

        for pid, (x1, y1, x2, y2) in zip(ids, xyxy):
            cx = (x1 + x2) / 2.0
            # bottom center is most stable:
            # cy = y2  # not needed for line crossing

            # dead-zone to avoid flicker
            if cx < self.cfg.x_line - self.cfg.buffer:
                side = "left"
            elif cx > self.cfg.x_line + self.cfg.buffer:
                side = "right"
            else:
                side = None

            if side is None:
                continue

            if pid not in self.track_state:
                self.track_state[pid] = side
                continue

            prev = self.track_state[pid]
            if prev != side:
                if self.cfg.inside_is_right:
                    if prev == "left" and side == "right":
                        self.entered += 1
                    elif prev == "right" and side == "left":
                        self.exited += 1
                else:
                    if prev == "right" and side == "left":
                        self.entered += 1
                    elif prev == "left" and side == "right":
                        self.exited += 1

                self.track_state[pid] = side

            # optional drawing
            if self.cfg.show_boxes:
                x1i, y1i, x2i, y2i = map(int, [x1, y1, x2, y2])
                cv2.rectangle(frame, (x1i, y1i), (x2i, y2i), (0, 255, 0), 2)
                if self.cfg.show_ids:
                    cv2.putText(frame, f"ID {pid}", (x1i, y1i - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        if self.cfg.show_line:
            cv2.line(frame, (self.cfg.x_line, 0), (self.cfg.x_line, frame.shape[0]), (0, 0, 255), 3)

        if self.cfg.show_counts:
            cv2.putText(frame, f"Entered: {self.entered}", (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
            cv2.putText(frame, f"Exited: {self.exited}", (30, 110),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)

        return frame
