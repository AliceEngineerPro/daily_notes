# coding: utf8
"""
@File: t.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/15 16:28
"""

import cinrad
from cinrad.io import CinradReader
# from cinrad.io import StandardData
import os
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import cv2
import imageio
import warnings
# import datetime
# import time
# from math import radians, cos, sin, asin, sqrt, exp, isnan
# from numba import jit
# from xarray import DataArray, Dataset
# from pycwr.draw.RadarPlot import plot_xy
# from numba import jit
# import threading


def getRadarFile(filePath, dbz_Path, gray_file_Path):
    radius = 230  # 绘制图像的范围大小
    # radius = 460  # 绘制图像的范围大小
    file_dirs = os.listdir(filePath)
    for file_name in file_dirs:
        # f = StandardData(filePath + file_name) # FMT标准格式
        f = CinradReader(filePath + file_name) # 每个型号雷达各自的格式（非标准格式）
        rl = list(f.iter_tilt(radius, 'REF'))
        cr = cinrad.calc.quick_cr(rl)
        # 输出灰度图像
        _get_Gray_png(gray_file_Path, file_name, cr)

        # 输出GRB图像（该图像像素与灰度图像像素一致，方便进行对比）
        _get_dBzRGB_png(dbz_Path, file_name, cr)
        print(file_name + " 完成！")


# 获取灰度图像
def _get_Gray_png(filePath, file_name, cr):
    data = np.where(np.isnan(cr["CR"].values), 0, cr["CR"].values)  # 将小于0的值都命为0
    data = data * 255 / 75 # 此处75为最大回波值，该值根据样本集中实际最大值变更
    fig = plt.figure(figsize=[4.8, 4.8])
    ax = fig.add_subplot(111)
    ax.imshow(data[::-1, :], cmap=plt.cm.gray, vmin=0, vmax=255)
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.savefig(filePath + file_name + ".png", format='png', dpi=100)


# 获取原数据回波图（彩色）
def _get_dBzRGB_png(dbz_Path, file_name, cr):
    data = np.where(np.isnan(cr["CR"].values), 0, cr["CR"].values)
    data[data <= 0] = -999
    cr_colors = color_CR()
    cr_scale = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
    cmap = mpl.colors.ListedColormap(cr_colors)
    norm = mpl.colors.BoundaryNorm(cr_scale, len(cr_colors))
    fig = plt.figure(figsize=[4.8, 4.8])
    ax = fig.add_subplot(111)
    ax.imshow(data[::-1, :], cmap=cmap, norm=norm)
    plt.axis('off')
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.savefig(dbz_Path + file_name + ".png", format='png', dpi=100)


# 将灰度图转为回波图像（彩色）
def GraytodBz(gray_Path, save_GrayTodBz_Path):
    gray_files = os.listdir(gray_Path)
    for image in gray_files:
        img = cv2.imread(gray_Path + image)
        pred = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        data = pred * (75 / 255) # 此处75为最大回波值，该值根据样本集中实际最大值变更
        data[data <= 0] = -999
        cr_colors = color_CR()
        cr_scale = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
        cmap = mpl.colors.ListedColormap(cr_colors)
        norm = mpl.colors.BoundaryNorm(cr_scale, len(cr_colors))
        fig = plt.figure(figsize=[4.8, 4.8])
        ax = fig.add_subplot(111)
        ax.imshow(data, cmap=cmap, norm=norm)
        plt.axis('off')
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
        plt.margins(0, 0)
        plt.savefig(save_GrayTodBz_Path + image, format='png', dpi=100)

        print(image + " 完成！")


def color_CR():
    RGB_array = ['0,0,0', '0,0,246', '1, 160, 246', '0,236,236', '1,255,0', '0,200,0', '1,144,0', '255,255,0','231,192,0',
                 '255,144,0', '255,0,0', '214,0,0', '192,0,0', '255,0,240', '120,0,132', '173,144,240']
    CR_clolor = []
    for rgb in RGB_array:
        hex_color = RGB_to_Hex(rgb)
        CR_clolor.append(hex_color)

    return CR_clolor


def RGB_to_Hex(rgb):
    RGB = rgb.split(',')
    color = '#'
    for i in RGB:
        num = int(i)
        color += str(hex(num))[-2:].replace('x', '0').upper()
    return color


def _png_to_gif(pngPath, gifPath):
    pics = os.listdir(pngPath)
    duration = 0.5
    image_list = []
    for pic in pics:
        print(pic)
        image_list.append(pngPath + pic)
    gif_name = gifPath + '111.gif'
    create_gif(image_list, gif_name, duration)
    print(gif_name + "完成！")


def create_gif(image_list, gif_name, duration=0.35):
    frames = []
    for image_name in image_list:
        # frames.append(imageio.imread(image_name))
        frames.append(imageio.v2.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    # 为了对比外推预测图像与实况的差别，实况对比图像与外推预测图像的像素要一致，具体像素自己设置，

    # 雷达原数据路径
    file_Path = r"D:\develops\WorkSpace\analysis_radar\source\\"

    # 雷达图像保存路径(原数据RGB图像保存路径)
    dbz_Path = r"D:\develops\WorkSpace\analysis_radar\dbz\\"

    # 灰度图像数据路径(原数据灰度图像保存路径)
    gray_file_Path = r"D:\develops\WorkSpace\analysis_radar\gray\\"

    # 外推的灰度图像路径(外推的灰度图像输入路径)
    gray_Path = r"D:\develops\WorkSpace\analysis_radar\predict\\"

    # 外推灰度图像转为RGB色斑图像路径
    save_GrayTodBz_Path = r"D:\develops\WorkSpace\analysis_radar\predict_dbz\\"

    # gif保存路径
    gif_path = r"d:\develops\WorkSpace\analysis_radar\\"

    # 生成原数据的回波彩色图像和灰度图像
    getRadarFile(file_Path, dbz_Path, gray_file_Path)

    # 将灰度图像转为回波彩色图像
    GraytodBz(gray_Path, save_GrayTodBz_Path)

    # 将目录中的图像转为gif（dbz_Path为图片输入路径，gif_path为保存路径）
    _png_to_gif(dbz_Path, gif_path)



