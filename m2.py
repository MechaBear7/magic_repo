import random
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry import Polygon, MultiPolygon

from matplotlib.patches import Polygon as MplPolygon
from alphashape import alphashape


data_points = [
    ((100, 599), 1),
    ((552, 596), 35),
    ((430, 596), 35),
    ((294, 580), 36),
    ((50, 567), 36),
    ((160, 558), 36),
    ((366, 537), 22),
    ((482, 522), 22),
    ((579, 514), 36),
    ((276, 487), 22),
    ((186, 475), 22),
    ((423, 472), 22),
    ((599, 446), 1),
    ((117, 462), 22),
    ((33, 469), 36),
    ((599, 415), 0),
    ((356, 436), 22),
    ((263, 426), 22),
    ((524, 419), 36),
    ((105, 402), 22),
    ((536, 380), 1),
    ((191, 386), 22),
    ((453, 383), 22),
    ((253, 375), 22),
    ((598, 367), 35),
    ((30, 365), 36),
    ((358, 348), 22),
    ((209, 327), 22),
    ((87, 319), 22),
    ((143, 304), 22),
    ((484, 313), 36),
    ((296, 293), 22),
    ((137, 256), 0),
    ((224, 273), 22),
    ((573, 285), 36),
    ((397, 266), 22),
    ((585, 245), 1),
    ((162, 254), 22),
    ((33, 266), 36),
    ((461, 239), 22),
    ((98, 233), 22),
    ((328, 222), 22),
    ((194, 205), 22),
    ((377, 179), 22),
    ((530, 189), 36),
    ((248, 171), 22),
    ((10, 181), 36),
    ((502, 141), 1),
    ((306, 155), 22),
    ((137, 148), 22),
    ((71, 149), 22),
    ((190, 141), 22),
    ((451, 154), 36),
    ((577, 124), 36),
    ((370, 108), 22),
    ((261, 101), 22),
    ((15, 93), 36),
    ((202, 71), 22),
    ((114, 81), 36),
    ((433, 73), 36),
    ((315, 60), 22),
    ((512, 68), 36),
    ((575, 25), 34),
    ((464, 0), 34),
    ((371, 18), 36),
    ((267, 13), 36),
    ((166, 4), 36),
    ((55, 11), 36),
]


# 删除半径小于5的点
data_points = [data_point for data_point in data_points if data_point[1] > 5]

small_radius_points = [data_point for data_point in data_points if data_point[1] < 30]
big_radius_points = [data_point for data_point in data_points if data_point[1] >= 30]

big_radius_polygons = [Polygon(Point(point[0]).buffer(point[1])) for point in big_radius_points]


# 将小圆点转换为shapely.geometry.Point对象
def get_points(points):
    return [Polygon(Point(point[0]).buffer(point[1])) for point in points]


# 迭代次数
N = 200

# 主循环：迭代 N 次
for _ in range(N):
    if len(small_radius_points) < 4:
        break  # 如果小半径点少于3个，无法形成三角形，结束迭代

    # 随机选取三个小半径点
    selected_points = random.sample(small_radius_points, 4)
    triangle = Polygon([point[0] for point in selected_points])

    # 判断三角形是否与大半径圆相交
    if any(triangle.buffer(30).intersects(big_circle) for big_circle in big_radius_polygons):
        continue  # 如果相交，跳过该轮迭代

    # 检查三角形是否完全覆盖了某些小半径圆
    covered_points = [point for point in small_radius_points if triangle.contains(Point(point[0]).buffer(point[1]))]

    # 从小半径点集合中删除被覆盖的点
    if covered_points:
        for point in covered_points:
            small_radius_points.remove(point)


small_radius_polygons = get_points(small_radius_points)

big_radius_polygons = get_points(big_radius_points)


def plot_origin(small_points, big_points):
    fig, ax = plt.subplots()

    for poly in small_points:
        mpl_poly = MplPolygon(np.array(poly.exterior.coords), edgecolor="blue", facecolor="cyan", alpha=0.5)
        ax.add_patch(mpl_poly)
        ax.plot(*poly.centroid.xy, "bo")  # 在多边形中心绘制蓝色点

    for poly in big_points:
        mpl_poly = MplPolygon(np.array(poly.exterior.coords), edgecolor="red", facecolor="orange", alpha=0.5)
        ax.add_patch(mpl_poly)
        ax.plot(*poly.centroid.xy, "bo")  # 在多边形中心绘制蓝色点

    ax.autoscale()
    ax.set_aspect("equal")
    plt.show()


plot_origin(small_radius_polygons, big_radius_polygons)
