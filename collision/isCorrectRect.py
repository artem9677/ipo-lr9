class RectCorrectError(Exception):
    pass

def isCorrectRect(rectangles):
    for i in rectangles:
        if i[0][0] >= i[1][0] or i[0][1] >= i[1][1]:
            raise RectCorrectError('Один из прямоугольников некорректный')

    return True