class Point2D():

    # ЧАСТЬ 1--------
    def __init__(self, x, y):
        self.coord = [x, y]

    def __str__(self):
        return f'Point: ({self.coord[0]}, {self.coord[1]})'

    def __del__(self):
        del self.coord

    def __getitem__(self, key):
        return self.coord[key]

    def __len__(self):
        return int((self.coord[0]**2 + self.coord[1]**2)**0.5)

    def distance(self):
        return (self.coord[0]**2 + self.coord[1]**2)**0.5
    # ЧАСТЬ 1---------------

    # ЧАСТЬ 2---------------
    def __eq__(self, other): # =
        return (self.coord[0] == other.coord[0])&(self.coord[1] == other.coord[1])

    def __lt__(self, other): # <
        return (self.distance() < other.distance())

    def __add__(self, other): # +
        if isinstance(other, Point2D):
            return Point2D(self.coord[0] + other.coord[0], self.coord[1] + other.coord[1])
        if isinstance(other, int):
            return Point2D(self.coord[0] + other, self.coord[1] + other)

    def __float__(self): # Point2D -> float
        return self.distance()
    # ЧАСТЬ 2---------------

    # ЧАСТЬ 3---------------
    def __getstate__(self):
        return self.coord

    def __setstate__(self, state):
        self.coord = state
    # ЧАСТЬ 3---------------

    # ЧАСТЬ 4---------------
    # статический метод
    @staticmethod
    def stat_method_ex(x, y):
        if (x**2+y**2)**0.5 > 1:
            return 1
        return 0

    # метод класса
    @classmethod
    def class_method_ex(cls):
        point_list = []
        for j in range(10):
            point_list.append(cls(j, j+1))
        return point_list
    # ЧАСТЬ 4---------------

if __name__ =='__main__':
    list_ = Point2D.class_method_ex()
    print(list_)

    for i in range(10):
        print(list_[i])

    print(Point2D.stat_method_ex(1, 2))

    point1 = Point2D(1, 1)
    print(point1)

    str1 = 'volvo'
    list_test = [1, 2, 3, 4]
    print(len(str1), len(list_test), len(point1))
    print(point1.distance())

    for item in str1:
        print(item)

    for item in list_test:
        print(item)

    print(2 in point1, 1 in point1)

    for coord in point1:
        print(coord)