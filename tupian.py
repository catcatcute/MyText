import base64
import os,pyautogui


def pic2py(picture_names, py_name):
    write_data = []
    for picture_name in picture_names:
        filename = picture_name.replace('.', '_')
        with open("%s" % picture_name, 'rb') as r:
            b64str = base64.b64encode(r.read())
        # 注意这边 b64str 一定要加上.decode()
        write_data.append('%s = "%s"\n' % (filename, b64str.decode()))

    with open(f'{py_name}.py', 'w+') as f:
        for data in write_data:
            f.write(data)
# 需要转码的图片：
#os.chdir("g:\\pkg\\Images")#路径转为图像所在路径


pics = ['./png/jieshou.png','./png/aaaaa.png','./png/exit.png','./png/fuzhi.png','./png/jihuo.png','./png/jiqima.png','./png/pojie.png','./png/queding.png','./png/queding2.png','./png/wendang.png']#将你的图片都输入进去
# 将pics里面的图片写到 image.py 中
pic2py(pics, 'images')
print("转码完成...")
# rect1=pyautogui.locateCenterOnScreen('./aaaaa.png')
# os.remove('./aaaaa.png')
# pyautogui.click(rect1)