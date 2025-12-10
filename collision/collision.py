def isCorrectRect(coords):
  bottom_left, top_right = coords
  x1, y1 = bottom_left
  x2, y2 = top_right
  
  return x1 < x2 and y1 < y2

print(isCorrectRect([(-3.4, 1), (9.2, 10)]))  # True
print(isCorrectRect([(-7, 9), (3, 6)]))       # False