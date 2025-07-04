# pip install opencv-python matplotlib pyzbar
import cv2
import matplotlib.pyplot as plt
from pyzbar.pyzbar import decode


def detect_and_decode_barcode(image_path):
    gray = cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)

    barcode_data = decode(gray)  # Обнаружение штрих-кода в изображении

    # цикл по всем обнаруженным штрих-кодам
    for barcode in barcode_data:
        barcode_data = barcode.data.decode("utf-8")  # извлечение данных штрих-кода
        barcode_type = barcode.type  # извлечение типа штрих-кода

        print(f"Штрих-код обнаружен: {barcode_data}")
        print(f"Тип штрих-кода: {barcode_type}")

        # рисует прямоугольник вокруг обнаруженного штрих-кода
        x, y, w, h = barcode.rect
        cv2.rectangle(image_path, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # добавляет текст с данными штрих-кода и типом на изображение
        cv2.putText(
            image_path,
            f"{barcode_data} ({barcode_type})",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2,
        )

    # конвертирует изображение из формата BGR в формат RGB
    # для отображения с помощью matplotlib
    image_rgb = cv2.cvtColor(image_path, cv2.COLOR_BGR2RGB)

    plt.imshow(image_rgb)  # Отображение изображения с обнаруженным штрих-кодом
    plt.axis("off")
    # plt.show()


image = cv2.imread("barcode.png")  # Чтение изображения
detect_and_decode_barcode(image)
