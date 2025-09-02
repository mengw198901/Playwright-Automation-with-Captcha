#没有用过opencv的cv2导入报错的  可以安装
#pip install opencv-python

import cv2
def get_notch_location(hx, bg):
    '''
    根据文件进行识别
    :param hx: 滑块图片的文件路径
    :param bg: 背景图片的文件路径
    :return:
    '''
    bg_img = cv2.imread(hx,0)
    tp_img = cv2.imread(bg,0)  # 读取到两个图片，进行灰值化处理
    img = cv2.imread(bg)  # 读取图片画框直观可以看到，上边是灰度的所以重新打开一个原图
    res = cv2.matchTemplate(_tran_canny(bg_img), _tran_canny(tp_img), cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc[0]  # 横坐标
    # 展示圈出来的区域
    x, y = max_loc  # 获取x,y位置坐标
    w, h = bg_img.shape[::-1]  # 宽高
    #矩形画图
    cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
    #显示
    cv2.imshow('Show', name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #这个是滑块要移动的距离
    return top_left
