import cv2

def draw_text(frame, text, position, color=(0,255,0), scale=1.0, thickness=2):
    cv2.putText(
        frame,
        text,
        position,
        cv2.FONT_HERSHEY_SIMPLEX,
        scale,
        color,
        thickness
    )
