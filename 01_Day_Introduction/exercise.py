# check python version using sys
import sys
print("Python version: ", end="")
print(sys.version)

# =========================================================================

def euclidean_distance(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b

    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

point_a = (2, 3)
point_b = (10, 8)

print("%.2f" % euclidean_distance(point_a, point_b))
