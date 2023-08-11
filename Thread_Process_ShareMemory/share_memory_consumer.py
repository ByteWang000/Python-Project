import cv2
import numpy as np
from multiprocessing import shared_memory,Queue

# 获取共享内存的名称
shm_name = "image"

# 连接到共享内存
shm = shared_memory.SharedMemory(name=shm_name)
print("连接到共享内存")

# 将共享内存数组转换为numpy数组(要指定内存文件大小！！！)
np_array = np.ndarray((900, 900, 3), dtype='uint8', buffer=shm.buf)
# 显示图像
cv2.imshow('Image', np_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 断开与共享内存的连接
shm.close()
