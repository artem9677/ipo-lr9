from .isCorrectRect import isCorrectRect
from .isCollisionRect import RectCorrectError

def intersectionAreaRect(list):
    try:
        isCorrectRect(list)
    except RectCorrectError as e:
        print(e)
        return 0
    n = len(list)
    intersection = False

    for i in range(n):
        for j in range(i+ 1,n):
            x1, y1 = list[i][0]
            x2, y2 = list[i][1]

            x3, y3 = list[j][0]
            x4, y4 = list[j][1]

            left = max(x1, x3)
            top = min(y2, y4)
            right = min(x2, x4)
            bottom = max(y1, y3)

            width = right - left
            height = top - bottom

            if width > 0 and height > 0:
                area = width * height  
                intersection = True 
    if not intersection: return 0

    return area 