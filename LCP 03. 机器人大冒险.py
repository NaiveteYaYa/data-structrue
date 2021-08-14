# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 23:35
# @Author  : WuxieYaYa

"""
力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，
机器人就会无限循环这条指令的步骤进行移动。指令有两种：

U: 向y轴正方向移动一格
R: 向x轴正方向移动一格。
不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。

给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。

 

示例 1：

输入：command = "URR", obstacles = [], x = 3, y = 2
输出：true
解释：U(0, 1) -> R(1, 1) -> R(2, 1) -> U(2, 2) -> R(3, 2)。
示例 2：

输入：command = "URR", obstacles = [[2, 2]], x = 3, y = 2
输出：false
解释：机器人在到达终点前会碰到(2, 2)的障碍物。
示例 3：

输入：command = "URR", obstacles = [[4, 2]], x = 3, y = 2
输出：true
解释：到达终点后，再碰到障碍物也不影响返回结果。
 

限制：

2 <= command的长度 <= 1000
command由U，R构成，且至少有一个U，至少有一个R
0 <= x <= 1e9, 0 <= y <= 1e9
0 <= obstacles的长度 <= 1000
obstacles[i]不为原点或者终点

链接：https://leetcode-cn.com/problems/programmable-robot
"""





def robot(command, obstacles, x, y):
    """此法超时：
    循环判断超时。
    """
    # xx, yy = 0, 0
    # for i in command:
    #     if i == "U":
    #         yy += 1
    #     else:
    #         xx += 1
    # m = min(x // xx+1, y // yy+1)
    # s = set()
    # for ob in obstacles:
    #     s.add(tuple(ob))
    # # position = [0,0]
    # z, j = 0, 0
    #
    # for i in m * command:
    #     if i == 'U':
    #         j += 1
    #     else:
    #         z += 1
    #     if (z, j) in s or z > x or j > y:
    #         return False
    #
    #     if z == x and j == y:
    #         return True

    # return False
    """法2, 仅判断obstacle"""
    def reach(x1, y1, xx, yy, command):
        multi = (x1 + y1) // (len(command))
        step = (x1 + y1) % (len(command))
        start = [multi * xx, multi * yy]
        if step != 0:
            for s in command[:step]:
                if s == "U":
                    start[1] += 1
                else:
                    start[0] += 1
        if x1 == start[0] and y1 == start[1]:
            return True
        else:
            return False

    xx, yy = 0, 0
    for i in command:
        if i == "U":
            yy += 1
        else:
            xx += 1
    newO = []
    for o in obstracts:
        if o[0] > x or o[1] > y:
            continue
        else:
            newO.append(o)
    if reach(x, y, xx, yy, command):
        for o in newO:
            if reach(o[0], o[1], xx, yy, command):
                return False
        return True
    else:
        return False




if __name__ == '__main__':
    command = "URRURRR"
    obstracts = [[7, 7], [0, 5], [2, 7], [8, 6], [8, 7], [6, 5], [4, 4], [0, 3], [3, 6]]
    x = 20
    y = 8
    print(robot(command, obstracts, x, y))
