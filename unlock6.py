import shutil,os
import win32gui
import pyautogui
import time
import win32clipboard as w
import win32con
import sys
from images import *
import base64


nowPath=os.path.dirname(os.path.realpath(sys.argv[0]))
print(nowPath)
path1=nowPath+"\\StudioOne注册机.exe"  
path2=nowPath+"\\Studio One 2\\Studio One.exe"

def get_text():
  w.OpenClipboard()
  d = w.GetClipboardData(win32con.CF_TEXT)
  w.CloseClipboard()
  return d.decode('GBK')

def checkOpen(filePath):
  file=os.stat(filePath)
  fileOpen=(file.st_mode & os.O_RDWR) or (file.st_mode & os.O_WRONLY)
  return fileOpen


def getImage():
  with open('./jihuo.png','wb') as jihuo:
    jihuo.write(base64.b64decode(jihuo_png))
  with open('aaaaa.png','wb') as aaaaa:
    aaaaa.write(base64.b64decode(aaaaa_png))
  with open('./exit.png','wb') as exit:
    exit.write(base64.b64decode(exit_png))
  with open('./fuzhi.png','wb') as fuzhi:
    fuzhi.write(base64.b64decode(fuzhi_png))
  with open('./jiqima.png','wb') as jiqima:
    jiqima.write(base64.b64decode(jiqima_png))
  with open('./pojie.png','wb') as pojie:
    pojie.write(base64.b64decode(pojie_png))
  with open('./wendang.png','wb') as wendang:
    wendang.write(base64.b64decode(wendang_png))
  with open('./queding.png','wb') as queding:
    queding.write(base64.b64decode(queding_png))
  with open('./queding2.png','wb') as queding2:
    queding2.write(base64.b64decode(queding2_png))
# jieshou = base64.b64decode(jieshou_png)

# fuzhi = base64.b64decode(fuzhi_png)

name=os.getlogin()
if os.path.exists("C:\\Users\\"+name+"\\Documents\\aaa66yp"):
  shutil.rmtree("C:\\Users\\"+name+"\\Documents\\aaa66yp")
os.mkdir("C:\\Users\\"+name+"\\Documents\\aaa66yp")

getImage()

os.startfile(path2)
time.sleep(5)
if checkOpen(path2):
  # rect1=pyautogui.locateCenterOnScreen('./jieshou.png')
  # os.remove('./jieshou.png')
  # pyautogui.click(rect1)
  print("open success")

  window1=win32gui.FindWindow(None,"PreSonus 登录")
  rect=win32gui.GetWindowRect(window1)#左上右下,0123
  print(rect) 
  #1197 270
  
  time.sleep(1)

  x1=int(rect[2]*0.98)
  y1=int(rect[1]*1.01)
  pyautogui.click(x1,y1)
  time.sleep(2)
  window1=win32gui.FindWindow(None,"激活Studio One")
  rect=win32gui.GetWindowRect(window1)
  print(rect)
#1018 767
  
  rect1=pyautogui.locateCenterOnScreen('./jihuo.png')
  # pyautogui.screenshot('screen.png',region=rect)
  # im1=cv2.imread('screen.png')
  # im2=cv2.imread('jihuo.png')
  # result=cv2.matchTemplate(im1,im2,cv2.TM_CCOEFF_NORMED)
  # print(result)
  # threshold=0.8
  # rect1= np.where(result>=0.8)
  # print(rect1)
  os.remove('./jihuo.png')
  pyautogui.click(rect1)

  # x1=int(rect[0]*1.603)#1.438
  # y1=int(rect[1]*3.687)#2.341
  # print('离线激活',x1,y1)
  # pyautogui.click(x1,y1)
  time.sleep(1.5)
#1075 616
  # x1=int(rect[0]*1.692)#1.504
  # y1=int(rect[1]*2.961)#1.979
  # print('复制',x1,y1)

  rect1=pyautogui.locateCenterOnScreen('./fuzhi.png')
  os.remove('./fuzhi.png')
  pyautogui.click(rect1)
  time.sleep(1.5)

  x1=int(rect[2]*0.98)
  y1=int(rect[1]*1.01)
  pyautogui.click(x1,y1)

user="66YP"
mashineStr=get_text()
print(mashineStr)
os.startfile(path1)
time.sleep(5)
if checkOpen(path1):
  print("open success")
  window1=win32gui.FindWindow(None,"StudioOne KeyGen v3.54.0")
  rect=win32gui.GetWindowRect(window1)#左上右下,0123
  print(rect)
  
#1104 614
  # x1=int(rect[0]*1.533)     #无效
  # y1=int(rect[1]*1.395)
  # print(x1,y1)
  # pyautogui.click(x1,y1)    
  # time.sleep(1)
  # pyautogui.hotkey('shift', 'home')
  # time.sleep(1)
  pyautogui.press('delete')
  time.sleep(1)
  pyautogui.typewrite(user)
  pyautogui.press('enter')
  time.sleep(1)

#1128 555  1142 615
  # x1=int(rect[0]*1.730)#1.533
  # y1=int(rect[1]*1.808)#1.504
  # print(x1,y1)
  # pyautogui.click(x1,y1)
  rect1=pyautogui.locateCenterOnScreen('./jiqima.png')
  os.remove('./jiqima.png')
  pyautogui.click(rect1)
  time.sleep(1)
  pyautogui.hotkey('ctrl', 'v')

  time.sleep(1)
  #os.mkdir()

#816 724 780 695
  # x1=int(rect[0]*1.133)
  # y1=int(rect[1]*2.044)#1.645
  # print(x1,y1)
  # pyautogui.click(x1,y1)
  rect1=pyautogui.locateCenterOnScreen('./pojie.png')
  os.remove('./pojie.png')
  pyautogui.click(rect1)
  time.sleep(1)
  
#839 465
 # pyautogui.click(839,465,2)
  rect1=pyautogui.locateCenterOnScreen('./wendang.png')
  os.remove('./wendang.png')
  pyautogui.click(rect1[0],rect1[1],2)
  time.sleep(1)
#873 388
  #pyautogui.click(873,388)
  rect1=pyautogui.locateCenterOnScreen('./aaaaa.png')
  os.remove('./aaaaa.png')
  pyautogui.click(rect1)
  time.sleep(1)
  #1001 745
  #pyautogui.click(1001,745)
  rect1=pyautogui.locateCenterOnScreen('./queding.png')
  os.remove('./queding.png')
  pyautogui.click(rect1)
  time.sleep(1)
#1141 696
  #pyautogui.click(1141,696)
  rect1=pyautogui.locateCenterOnScreen('./exit.png')
  os.remove('./exit.png')
  pyautogui.click(rect1)
  time.sleep(1)

#1051 618
  #pyautogui.click(1051,618)
  rect1=pyautogui.locateCenterOnScreen('./queding2.png')
  os.remove('./queding2.png')
  pyautogui.click(rect1)
  time.sleep(1)

source_file = "C:\\Users\\"+name+"\\Documents\\aaa66yp\\studioapp2.pro.license"
target_dir = 'C:\\ProgramData\\PreSonus\\Studio One 2'
# 移动文件
os.rename(source_file, os.path.join(target_dir, "user.license"))
shutil.rmtree("C:\\Users\\"+name+"\\Documents\\aaa66yp")
os.startfile(path2)
a = pyautogui.alert(text='执行完毕', title='Test')
print(a)

# hd = win32gui.GetDesktopWindow()
 
# # 获取所有子窗口
# hwndChildList = []
 
# win32gui.EnumChildWindows(hd, lambda hwnd, param: param.append(hwnd), hwndChildList)
 
# for hwnd in hwndChildList:
#     print("句柄：", hwnd, "标题：", win32gui.GetWindowText(hwnd))