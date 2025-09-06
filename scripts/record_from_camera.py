"""
Скрипт на OpenCV, который:
- подключается к веб‑камере
- показывает превью в реальном времени
- пишет MP4 с нужным разрешением и FPS
- выходит по клавише Q

pip install opencv-python
"""
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple, Optional

import cv2


@dataclass(frozen=True)
class CaptureConfig:
    """Настройки захвата видео с веб‑камеры."""
    device_index: int = 0  # индекс камеры (0 — встроенная)
    width: int = 640  # ширина кадра
    height: int = 480  # высота кадра
    fps: int = 20  # кадров в секунду
    fourcc: str = "mp4v"  # кодек для MP4: mp4v, для AVI: XVID

def create_capture(config: CaptureConfig) -> cv2.VideoCapture:
    """Создаёт и настраивает объект VideoCapture."""
    cap = cv2.VideoCapture(config.device_index)
    if not cap.isOpened():
        raise RuntimeError(f"Не удалось открыть веб камеру {config.device_index}")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.height)
    cap.set(cv2.CAP_PROP_FPS, config.fps)
    return cap

def create_video_writer(output_path: Path, config: CaptureConfig) -> cv2.VideoWriter:
    """Создаёт объект записи видео (VideoWriter)."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*config.fourcc)
    writer = cv2.VideoWriter(
        str(output_path), fourcc, config.fps, (config.width, config.height)
    )

    if not writer.isOpened():
        raise RuntimeError(f"Не удалось создать файл для записи: {output_path}")
    return writer

def record_from_webcam(output_path: Path,
    cfg: CaptureConfig = CaptureConfig(),
    window_title: str = "Video",
) -> Tuple[bool, Optional[str]]:
    """
    Захватывает поток с веб‑камеры, показывает превью и пишет в файл.
    Возвращает (успех, сообщение_ошибки).
    Остановка по клавише 'q'.
    """
    try:
        cap = create_capture(cfg)
        writer = create_video_writer(output_path, cfg)
    except Exception as e:
        return False, str(e)

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                return False, "Не удалось прочитать кадр с камеры"

            writer.write(frame)
            cv2.imshow(window_title, frame)

            # выход по 'q'
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        return True, None
    finally:
        cap.release()
        writer.release()
        cv2.destroyAllWindows()

def main() -> None:
    cfg = CaptureConfig(
        device_index=0,
        width=640,
        height=480,
        fps=20,
        fourcc="mp4v",  # для .mp4; для .avi — XVID
    )
    ok, err = record_from_webcam(Path("records/video.mp4"), cfg)
    if ok:
        print("[+] Запись завершена успешно. Файл: records/video.mp4")
    else:
        print(f"[-] Ошибка записи: {err}")

if __name__ == "__main__":
    main()



























