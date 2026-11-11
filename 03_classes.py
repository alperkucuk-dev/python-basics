class BoundingBox:
    def __init__(self, x1, y1 ,x2, y2, label):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.label = label

        
    def width(self):
        return self.x2 - self.x1 

    def height(self):
        return self.y2 - self.y1
    
    def area(self):
        return self.width() * self.height()

    def center(self):
        x_center = (self.x1 + self.x2) / 2
        y_center = (self.y1 + self.y2) / 2
        return x_center,y_center

    def iou(self,other):

        left_x = max(self.x1,other.x1)
        down_y = max(self.y1,other.y1)
        up_y = min(self.y2,other.y2)
        right_x = min(self.x2,other.x2)

        intersection_field = max((right_x - left_x),0) * max(0,(up_y - down_y))
        union_field = self.area() + other.area() - intersection_field

        IoU = intersection_field / union_field
        return IoU



box = BoundingBox(10, 20, 110, 70, "car")
print(box.label, box.width(), box.height(), box.area(), box.center())

a = BoundingBox(0, 0, 100, 100, "car")
b = BoundingBox(50, 50, 150, 150, "car")
c = BoundingBox(200, 200, 300, 300, "car")
print(a.iou(b))   
print(a.iou(c))  
print(a.iou(a))