def isCorrectRect(coords):
  
  bottom_left, top_right = coords
  x1, y1 = bottom_left
  x2, y2 = top_right
  
  return x1 < x2 and y1 < y2


def isCollisionRect(rect1, rect2):
 
  if not isCorrectRect(rect1):
    raise RectCorrectError("1й прямоугольник некорректный")
  
  if not isCorrectRect(rect2):
    raise RectCorrectError("2й прямоугольник некорректный")
  
  x1, y1 = rect1[0]  #нижний левый угол rect1
  x2, y2 = rect1[1]  #верхний правый угол rect1
  
  x3, y3 = rect2[0]  #нижний левый угол rect2
  x4, y4 = rect2[1]  #верхний правый угол rect2
  
  return x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3

def intersectionAreaRect(rect1, rect2):

  if not isCorrectRect(rect1):
    raise ValueError("1й прямоугольник некорректный")
  
  if not isCorrectRect(rect2):
    raise ValueError("2й прямоугольник некорректный")
  
  x1, y1 = rect1[0]  #левый нижний угол rect1
  x2, y2 = rect1[1]  #верхний правый угол rect1
  
  x3, y3 = rect2[0]  #левый нижний угол rect2
  x4, y4 = rect2[1]  #верхний правй угол rect2
  
  intersection_x1 = max(x1, x3) #левый край пересечения
  intersection_y1 = max(y1, y3) #нижний край пересечения
  intersection_x2 = min(x2, x4) #правый край пересечения
  intersection_y2 = min(y2, y4) #верхний край пересечения
  
  width = max(0, intersection_x2 - intersection_x1)
  height = max(0, intersection_y2 - intersection_y1)
  
  return width * height

print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))  # Вернет некоторое положительное число
print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))  # Вернет 0

try:
  print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))  # Вызовет ошибку
except ValueError as e:
  print(f"Ошибка: {e}")