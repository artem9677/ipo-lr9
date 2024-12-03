from .isCorrectRect import isCorrectRect, RectCorrectError

def intersectionAreaRect(rectangles):
    area = 0  

    try:
        isCorrectRect(rectangles)
    except RectCorrectError as e:
        print(e)
        return 0  

    n = len(rectangles)   
    is_intersection = False 

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = rectangles[i][0]
            x2, y2 = rectangles[i][1]

            x3, y3 = rectangles[j][0]
            x4, y4 = rectangles[j][1]

            left = max(x1, x3)
            top = min(y2, y4)
            right = min(x2, x4)
            bottom = max(y1, y3)

            width = right - left
            height = top - bottom

            if width > 0 and height > 0:
                area += width * height  
                is_intersection = True  

    if not is_intersection:
        return 0

    return area 