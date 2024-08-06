class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Box:
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth

    def contains(self, point):
        return (self.x <= point.x < self.x + self.width and
                self.y <= point.y < self.y + self.height and
                self.z <= point.z < self.z + self.depth)

    def intersects(self, range):
        return not (range.x > self.x + self.width or
                    range.x + range.width < self.x or
                    range.y > self.y + self.height or
                    range.y + range.height < self.y or
                    range.z > self.z + self.depth or
                    range.z + range.depth < self.z)

class Octree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def subdivide(self):
        x, y, z, w, h, d = self.boundary.x, self.boundary.y, self.boundary.z, self.boundary.width, self.boundary.height, self.boundary.depth
        nwf = Box(x, y, z, w / 2, h / 2, d / 2)
        nef = Box(x + w / 2, y, z, w / 2, h / 2, d / 2)
        swf = Box(x, y + h / 2, z, w / 2, h / 2, d / 2)
        sef = Box(x + w / 2, y + h / 2, z, w / 2, h / 2, d / 2)
        nwb = Box(x, y, z + d / 2, w / 2, h / 2, d / 2)
        neb = Box(x + w / 2, y, z + d / 2, w / 2, h / 2, d / 2)
        swb = Box(x, y + h / 2, z + d / 2, w / 2, h / 2, d / 2)
        seb = Box(x + w / 2, y + h / 2, z + d / 2, w / 2, h / 2, d / 2)

        self.northwest_front = Octree(nwf, self.capacity)
        self.northeast_front = Octree(nef, self.capacity)
        self.southwest_front = Octree(swf, self.capacity)
        self.southeast_front = Octree(sef, self.capacity)
        self.northwest_back = Octree(nwb, self.capacity)
        self.northeast_back = Octree(neb, self.capacity)
        self.southwest_back = Octree(swb, self.capacity)
        self.southeast_back = Octree(seb, self.capacity)
        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.northwest_front.insert(point):
                return True
            elif self.northeast_front.insert(point):
                return True
            elif self.southwest_front.insert(point):
                return True
            elif self.southeast_front.insert(point):
                return True
            elif self.northwest_back.insert(point):
                return True
            elif self.northeast_back.insert(point):
                return True
            elif self.southwest_back.insert(point):
                return True
            elif self.southeast_back.insert(point):
                return True

    def query(self, range, found):
        if not self.boundary.intersects(range):
            return

        for p in self.points:
            if range.contains(p):
                found.append(p)

        if self.divided:
            self.northwest_front.query(range, found)
            self.northeast_front.query(range, found)
            self.southwest_front.query(range, found)
            self.southeast_front.query(range, found)
            self.northwest_back.query(range, found)
            self.northeast_back.query(range, found)
            self.southwest_back.query(range, found)
            self.southeast_back.query(range, found)

# Usage
boundary = Box(0, 0, 0, 100, 100, 100)
ot = Octree(boundary, 4)
points = [Point3D(10, 10, 10), Point3D(50, 50, 50), Point3D(60, 60, 60), Point3D(90, 90, 90)]
for point in points:
    ot.insert(point)

range_query = Box(0, 0, 0, 60, 60, 60)
found_points = []
ot.query(range_query, found_points)
print("Points found in range:")
for p in found_points:
    print(f"({p.x}, {p.y}, {p.z})")
