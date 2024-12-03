from collision.isCorrectRect import isCorrectRect , RectCorrectError
from collision.intersectionAreaRect import intersectionAreaRect
from collision.isCollisionRect import isCollisionRect
from collision.intersectionAreaMultiRect import intersectionAreaMultiRect


def main():
    while True:

        number = int(input("Выбор: 1 - intersectionAreaRect , 2 - isCorrectRect , 3 - isCollisionRect , 4 - intersectionAreaMultiRect , 5 - Выход\n"))

        if number == 1:
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rectangles = [(x1, y1), (x2, y2) ],[(x3, y3), (x4, y4)]
            print(intersectionAreaRect(rectangles))


        elif number == 2:
            rectangles=[]
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            rectangles.append([(x1, y1), (x2, y2)])
            try:
                print(isCorrectRect(rectangles))
            except RectCorrectError as e:
                print(e)

              

        elif number == 3:
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rectangles = [(x1, y1), (x2, y2)],[(x3, y3), (x4, y4)]
            print(isCollisionRect(rectangles))


        if number == 4:
            n = int(input("Количество прямоугольников: "))
            rectangles = []
            for i in range(n):
                print(f"Прямоугольник {i + 1}:")
                x1 = float(input('Введите x1: '))
                y1 = float(input('Введите y1: '))
                x2 = float(input('Введите x2: '))
                y2 = float(input('Введите y2: '))
                rectangles.append([(x1, y1), (x2, y2)])
            else:  
                try:
                    print(intersectionAreaMultiRect(rectangles))
                except RectCorrectError as e:
                    print(e)
                    return 0

        elif number == 5:
            print("Выход")
            break
        else:
            print(f"Вы ввели {number} . Чтобы продолжите введите число от 1 до 5")

main()