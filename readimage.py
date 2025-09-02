#没有用过opencv的cv2导入报错的  可以安装
#pip install opencv-python
#first 
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

#Second
#有的检测移动速度的 如果匀速移动会被识别出来，来个简单点的 渐进
 def get_track(distance):  # distance为传入的总距离
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 1

    while current < distance:
        if current < mid:
            # 加速度为2
            a = 4
        else:
            # 加速度为-2
            a = -3
        v0 = v
        # 当前速度
        v = v0 + a * t
        # 移动距离
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track
#Third
#移动滑块
#首先咱们的找到要移动的东西吧
s = self.page.wait_for_selector('//div[@class="_3CvVPX _3gznAC _3BUN_s"]',strict=True)
#找到这个元素再当前页面的坐标（这个会返回一个字典里边四个数字）
box = s.bounding_box()
#移动鼠标到上边元素的中心（上边四个参数用途来了）
self.page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
#按下鼠标（这个不多说）
self.page.mouse.down()
#这里获取到x坐标中心点位置
x = box["x"] + box["width"] / 2
#这个把缺口获取到的长度放到轨迹加工一下得到一个轨迹
tracks = get_track(top_left)
for track in tracks:
  #循环鼠标按照轨迹移动
  #strps 是控制单次移动速度的比例是1/10 默认是1 相当于 传入的这个距离不管多远0.1秒钟移动完 越大越慢
  self.page.mouse.move(x + track, 0,steps=10)
  x += track
#移动结束鼠标抬起
self.page.mouse.up()
