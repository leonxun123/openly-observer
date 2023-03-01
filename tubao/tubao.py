import matplotlib.pyplot as pyp
import matplotlib.widgets as wid
import random

class the_key:
    def __init__(self,left_point, right_point, all_points, border_points):
        self.area_max = 0
        self.point_max = ()
        self.left_point=left_point
        self.right_point=right_point
        self.all_points = all_points
        self.border_points=border_points

    def upper_half(self):
        for item in self.all_points:
            if item != self.left_point or item != self.right_point:
                new_area = area(self.left_point, self.right_point, item)
                if new_area > self.area_max:
                    self.point_max = item
                    self.area_max = new_area

        if self.area_max != 0:
            self.border_points.append(self.point_max)
            left_up = the_key(self.left_point, self.point_max, self.all_points, self.border_points)
            left_up.upper_half()
            right_down = the_key(self.point_max, self.right_point, self.all_points, self.border_points)
            right_down.upper_half()

    def lower_half(self):
        for item in self.all_points:
            if item != self.left_point or item != self.right_point:
                new_area = area(self.left_point, self.right_point, item)
                if new_area < self.area_max:
                    self.point_max = item
                    self.area_max = new_area

        if self.area_max != 0:
            border_points.append(self.point_max)
            left_down= the_key(self.left_point, self.point_max, self.all_points, border_points)
            left_down.lower_half()
            right_down = the_key(self.point_max, self.right_point, self.all_points, border_points)
            right_down.lower_half()


    def paint(self,event):
        self.border_points.sort()
        left_x, left_y = self.border_points[0]
        right_x, right_y = self.border_points[-1]
        list_border_up = []
        for item in self.border_points:
            x, y = item
            if y > max(left_y, right_y):
                list_border_up.append(item)
            if min(left_y, right_y) < y < max(left_y, right_y):
                if area(self.border_points[0], self.border_points[-1], item) > 0:
                    list_border_up.append(item)
        list_border_down = [item for item in self.border_points if item not in list_border_up]
        all_border = list_border_up + list_border_down[::-1]
        all_border.append(all_border[0])
        for i in range(len(all_border) - 1):
            x1, y1 = all_border[i]
            x2, y2 = all_border[i + 1]
            ax.plot([x1, x2], [y1, y2],color='black')

def get_points():
   n = int(input("the number of random points"))
   while len(points) < n:
       x = random.randint(0, 200)
       y = random.randint(0, 200)
       if [x, y] not in points:
           points.append([x, y])
   return points

def area(min, max, point):
    x1, y1 = min
    x2, y2 = max
    x3, y3 = point
    return x1 * y2 + x3 * y1 + x2 * y3 - x3 * y2 - x2 * y1 - x1 * y3

def paint(all_of_points):
    point_x = []
    point_y = []
    for item in all_of_points:
        x,y = item
        point_x.append(x)
        point_y.append(y)
    ax.scatter(point_x, point_y)

points = []


if __name__ == "__main__":
    fig, ax = pyp.subplots()
    pyp.subplots_adjust(bottom=0.2)

    points=get_points()
    points.sort()
    print("all of points is ")
    print(points)
    left_p, right_p = points[0], points[-1]
    border_points = []
    paint(points)
    the_points=the_key(left_p, right_p, points, border_points)
    the_points.upper_half()
    the_points.lower_half()
    border_points.append(left_p)
    border_points.append(right_p)
    print("the border points is ")
    print(border_points)
    last = pyp.axes([0.59, 0.05, 0.1, 0.075])
    key = wid.Button(last, 'key')
    key.on_clicked(the_points.paint)
    pyp.show()


