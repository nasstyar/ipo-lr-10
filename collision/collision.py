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


print(isCorrectRect([(-3.4, 1), (9.2, 10)]))  # True
print(isCorrectRect([(-7, 9), (3, 6)]))       # False

print(isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))  #вернет True
print(isCollisionRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))  #вернет False

try:
  print(isCollisionRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))  #вызовет ошибку
except RectCorrectError as e:
  print(f"Ошибка: {e}")