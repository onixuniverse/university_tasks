# 9.16 Построить треугольник, описанный около окружности с радиусом R.
from PIL import Image, ImageDraw

if __name__ == "__main__":
    try:
        radius = float(input("Введите радиус окружности: "))

        image = Image.new('RGB', (600, 600))
        draw = ImageDraw.Draw(image)

        start_cords = 300

        ellipse_cords = [start_cords - radius, start_cords - radius, start_cords + radius, start_cords + radius]
        draw.ellipse(ellipse_cords, fill='red')  # L U R D

        triangle_cords = [(start_cords, start_cords - radius * 2.65), (start_cords - radius - radius // 2,
                                                                       start_cords + radius),
                          (start_cords + radius + radius // 2, start_cords + radius)]  # Y -X +X (X Y)
        draw.polygon(triangle_cords, outline="yellow")  # U L R

        image.save('triangle.png')
    except Exception as exc:
        print("Произошла ошибка:", exc)
