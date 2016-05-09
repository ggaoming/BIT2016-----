# -*- coding:utf-8 -*-
#  Dependence : python2.7
#  run.py
#  calculate
#  Created by Gao Liming on 16/5/7.
#
import random


def generate_data(n=5):
    """
    生成测试数据 生成 n个点之间的相互距离
    :param n:测试数据维度 n*n距离矩阵
    :return: 返回生成的距离矩阵 a
             a[i][j] 为 点i到j的距离
    """
    if n > 0:
        a = []
        for i in range(n):
            a.append([])
            for j in range(n):
                a[i].append(0)
        for i in range(n):
            for j in range(i+1, n):
                a[i][j] = random.randint(1, 100)
                a[j][i] = a[i][j]

        print '****** Data Set ******'
        for i in range(n):
            print a[i]
        return a
    else:
        a = []
        f = open('text_input.txt')
        info = f.readlines()
        index = 0
        for line in info:
            temp = line.split(',')
            a.append([])
            for value in temp:
                a[index].append(int(value))
            index += 1
        f.close()
        print '****** Data Set ******'
        for i in range(index):
            print a[i]
        return a
        pass


def calculate(n=5):
    """
    计算
    :param n:处理数据维度 n*n距离矩阵
    :return:
    """
    data = generate_data(n)  # 生成随机距离
    n = len(data)

    value_map = []  # 记录距离
    process = []  # 记录合并操作  ()顺序为合并顺序

    for i in range(n):  # value_map process 初始化
        value_map.append([])
        process.append([])
        for j in range(n):
            value_map[i].append(0)
            process[i].append('*')

    for step in range(1, n):  # 从两点间隔为1开始计算
        for start in range(0, n-step):  # 计算不同间距的最优值
            if step == 1:  # 距离为1时直接赋值
                value_map[start][start+step] = data[start][start+step]
                process[start][start+step] = (start, start+step)
            else:
                min_val = -1  # 最短分割点获得的值
                min_process = None  # 最短分割点的操作
                # 递推方程 start
                for i in range(1, step):  # 距离大于1时选取最短的分割点
                    value = value_map[start][start+i]+value_map[start+i][start+step]\
                     + data[start][start+step]
                    if i > 1:
                         value += value + data[start][start+i]
                    if step - i > 1:
                        value += value + data[start+i][start+step]
                    if min_val == -1 or min_val > value:
                        min_val = value
                        min_process = (process[start][start+i], process[start+i][start+step])
                # 递推方程 end
                value_map[start][start+step] = min_val
                process[start][start+step] = min_process

    max_len = 0

    for i in range(n):
        for j in range(n):
            str_temp = str(process[i][j])+str(value_map[i][j])+':'
            str_len = len(str_temp)
            if max_len < str_len:
                max_len = str_len
    print '****** Process ******'
    for i in range(n):
        for j in range(n):
            str_temp = str(process[i][j])+':'+str(value_map[i][j])
            str_len = len(str_temp)
            process[i][j] = ' '*(max_len-str_len) + str_temp
        print process[i]

    print 'min value:', value_map[0][-1]
    print 'process', process[0][-1]
def get_random_data():
    """
    随机生成
    """
    random.seed(0)  # 固定随机种子, 使每次运算结果相同
    for i in range(5):
        print 'Num', i
        calculate(random.randint(3, 10))
        print '\n'

def text_input():
    """
    文件输入
    """
    calculate(-1)

if __name__ == '__main__':
    text_input()
