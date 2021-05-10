# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import tifffile
import matplotlib.pyplot as plt

path_input_array= r"D:\PythonCode\Lab_pythonCode\logscale.tif"

with tifffile.TiffFile(path_input_array) as imfile:
        input_array =imfile.asarray()
# Change linear image to log image
# log_int = 10*np.log10(input_array);

numberX = range(0,512);
# print(numberX)
# a = range(0,402);
plt.imshow(input_array[40], 'gray')
plt.colorbar()
plt.show()

in_p = np.array(input_array[40][100,:]);  # 简写
in_pn = np.array(input_array[40][100,:]);  # 简写
# get the depth-intensity image
plt.plot(numberX,input_array[40][100,:]);
plt.xlabel("X");
plt.ylabel("Intensity")
plt.show()

new_p = in_p[-1:]+in_p[:-1]; # 移动了一格的新数组

# 平移100个
tem = in_pn[-100:];
in_p[-100:] = in_p[0:100];
in_p[0:100] = tem
plt.plot(numberX,in_p);
plt.xlabel("X");
plt.ylabel("Intensity")
plt.show()
# print(new_p)
# np.multiply(ax,axx) ;  //矩阵中对应元素相乘并得到一个新数组
# print(new_p * in_p);
