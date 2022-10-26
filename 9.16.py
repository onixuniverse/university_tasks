# 9.16 Построить треугольник, описанный около окружности с радиусом R.
from PIL import Image, ImageDraw


def draw_ellipse(draw, coordinates):
    draw.ellipse(coordinates, fill='red')  # L U R D


def draw_polygon(draw, coordinates):
    draw.polygon(triangle_cords, outline="yellow")  # U L R


if __name__ == "__main__":
    try:
        radius = float(input("Введите радиус окружности: "))

        image = Image.new('RGB', (600, 600))
        draw = ImageDraw.Draw(image)

        start_cords = 300
        ellipse_cords = [start_cords - radius, start_cords - radius, start_cords + radius, start_cords + radius]
        triangle_cords = [(start_cords, start_cords - radius * 2.65),
                          (start_cords - radius - radius // 2, start_cords + radius),
                          (start_cords + radius + radius // 2, start_cords + radius)]  # Y -X +X (X Y)
        draw_ellipse(draw, ellipse_cords)
        draw_polygon(draw, triangle_cords)

        image.save('triangle.png')
    except Exception as exc:
        print("Произошла ошибка:", exc)
