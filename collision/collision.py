class RectCorrectError(Exception):
  pass

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

def intersectionAreaMultiRect(rectangles):

  for rect in rectangles:
    if not isCorrectRect(rect):
      raise RectCorrectError("Прямоугольник некорректный")
  
  if len(rectangles) == 0:
    return 0
  
  if len(rectangles) == 1:
    x1, y1 = rectangles[0][0]
    x2, y2 = rectangles[0][1]
    return (x2 - x1) * (y2 - y1)
  
  x_coords = set()
  y_coords = set()
  
  for rect in rectangles:
    x1, y1 = rect[0]
    x2, y2 = rect[1]
    x_coords.add(x1)
    x_coords.add(x2)
    y_coords.add(y1)
    y_coords.add(y2)
  
  x_coords = sorted(x_coords)
  y_coords = sorted(y_coords)
  
  total_area = 0
  
  for i in range(len(x_coords) - 1):
    for j in range(len(y_coords) - 1):
      x_left = x_coords[i]
      x_right = x_coords[i + 1]
      y_bottom = y_coords[j]
      y_top = y_coords[j + 1]
      
      inside_all = True
      for rect in rectangles:
        x1, y1 = rect[0]
        x2, y2 = rect[1]
        
        if not (x_left >= x1 and x_right <= x2 and y_bottom >= y1 and y_top <= y2):
          inside_all = False
          break
      
      if inside_all:
        cell_area = (x_right - x_left) * (y_top - y_bottom)
        total_area += cell_area
  
  return total_area