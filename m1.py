import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.geometry import Polygon, MultiPolygon

from matplotlib.patches import Polygon as MplPolygon


# 绘制出 origin
def plot_origin(origin, small_points, big_points):
    fig, ax = plt.subplots()

    if isinstance(origin, MultiPolygon):
        # 遍历 MultiPolygon 中的每个 Polygon
        for poly in origin.geoms:
            mpl_poly = MplPolygon(np.array(poly.exterior.coords), edgecolor="red", facecolor="orange", alpha=0.5)
            ax.add_patch(mpl_poly)
    else:
        # 如果 origin 是单独的 Polygon
        mpl_poly = MplPolygon(np.array(origin.exterior.coords), edgecolor="red", facecolor="orange", alpha=0.5)
        ax.add_patch(mpl_poly)

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


# 将小圆点转换为shapely.geometry.Point对象
def get_points(points):
    return [Polygon(Point(point[0]).buffer(point[1])) for point in points]


small_radius_polygons = get_points(small_radius_points)
big_radius_polygons = get_points(big_radius_points)

center = (MultiPolygon(small_radius_polygons).centroid.x, MultiPolygon(big_radius_polygons).centroid.y)
# 生成 N 个点的多边，边长为1
N = 64
expand_done = [False] * N
expand_time = [0] * N
origin_points = [(center[0] + np.cos(2 * np.pi / N * i), center[1] + np.sin(2 * np.pi / N * i)) for i in range(N)]
origin = Polygon(origin_points)

# 随机方向扩展直到包含所有小半径圆点
while not all(origin.contains(p) for p in small_radius_polygons):
    # 找到 expand_time 中的最小值，即最少扩展次数的点，判断是否已经扩展完成，如果完成则找到下一个点
    index = expand_time.index(min(expand_time))

    x, y = origin_points[index]

    # 计算该顶点的移动方向，向远离 center 的方向移动
    dxdy = [x - center[0], y - center[1]]
    dx, dy = dxdy / np.linalg.norm(dxdy)

    # 更新选定顶点的坐标
    new_vertex = (x + dx, y + dy)
    new_origin_points = origin_points.copy()
    new_origin_points[index] = new_vertex

    # 生成新的多边形
    new_origin = Polygon(new_origin_points)

    # 检查是否与大半径圆相交
    if any(new_origin.intersects(p) for p in big_radius_polygons):
        expand_done[index] = True
        expand_time[index] = 1000000
        if all(expand_done):
            print("All points have been expanded.")
        continue  # 如果相交，取消该次移动
    else:
        # 如果不相交，更新 origin 和顶点列表
        origin = new_origin
        origin_points = new_origin_points
        expand_time[index] += 1

plot_origin(origin, small_radius_polygons, big_radius_polygons)

# Min Distance
shink_done = [False] * N
while not all(shink_done):
    # 计算 origin 中每个点到 small_radius_polygons 的最小距离，找到最小距离最大的点
    min_distance = 0
    index = 0
    for i, point in enumerate(origin_points):
        distance = min(p.distance(Point(point)) for p in small_radius_polygons)
        if distance > min_distance:
            min_distance = distance
            index = i

    # 计算该顶点的移动方向，向 center 移动
    x, y = origin_points[index]
    dxdy = [center[0] - x, center[1] - y]
    dx, dy = dxdy / np.linalg.norm(dxdy)
    new_vertex = (x + dx, y + dy)

    # 计算新的点是否

    # 更新选定顶点的坐标
    new_origin_points = origin_points.copy()
    new_origin_points[index] = new_vertex

    origin = Polygon(new_origin_points)
    origin_points = new_origin_points

plot_origin(origin, small_radius_polygons, big_radius_polygons)
