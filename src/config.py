from dataclasses import dataclass

@dataclass
class CounterConfig:
    model_path: str = "yolov8m.pt"
    conf: float = 0.30
    iou: float = 0.50
    tracker: str = "bytetrack.yaml"

    # door line settings
    x_line: int = 1465
    buffer: int = 35
    inside_is_right: bool = True

    # drawing
    show_line: bool = False
    show_boxes: bool = True
    show_ids: bool = True
    show_counts: bool = True
