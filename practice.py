def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p
  
  
>>> center = find_center(box)
>>> print_point(centers)
(50, 100)

box.width = box.width + 50
box.height = box.height + 100

def grow_retangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight
    
>>> box.width, box.height
(150.0, 300.0)
