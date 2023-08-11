import time
import cv2
import numpy as np
from multiprocessing import shared_memory, Queue

# 读取图像
image = cv2.imread('image.jpg')
if image is None:
    print("无法加载图像文件。")
    exit()
# np.copyto(np_array, image)
# 创建一个新的共享内存块
shm = shared_memory.SharedMemory(create=True, size=image.nbytes, name="image")
print(image.dtype)
# 将numpy数组指定为共享内存数组
np_array = np.ndarray(image.shape, dtype=image.dtype, buffer=shm.buf)
# 图像数据放入共享内存（numpy）
np_array[:] = image[:]
# 输出共享内存的名称，以便进程2可以访问它
print(shm.name)
time.sleep(50)
