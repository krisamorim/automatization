import pyautogui as pyau
import funcMoveTimeLineOnExcel as func
from os import path

# pathCode = os.path.join(os.getcwd(), r'Millium\arrastaTimeLine')
# os.chdir(pathCode)
img1 = path.abspath(__file__).replace('moveTimeLine.py', r'imgs\timeLineBar1.png')
img2 = path.abspath(__file__).replace('moveTimeLine.py', r'imgs\timeLineBar2.png')
img3 = path.abspath(__file__).replace('moveTimeLine.py', r'imgs\timeLineBar3.png')
imgList = [img3, img2, img1]
x = 28 #10 para um quadrado somente e 41 p/ 5
x *=4

func.cls()
func.altTab()
# print(len(img1))
func.locateOnScreenFunc(imgList, 3, 2)

# func.setZoom('70')
# func.runSearch(imgList)
# pyau.click()
# func.sleep(.6)
# for i in range(1,x):
#     pyau.press('right')
#     # sleep(.1)
# # setZoom('50')
# func.sleep(1)
# func.altTab(.6)