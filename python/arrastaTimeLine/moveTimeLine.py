import funcMoveTimeLineOnExcel as func
import variablesMoveTimeLine as var


func.cls()
func.altTab()
# func.setZoom('60')
if func.locateOnScreenFunc(var.imgList, 4, 2) == False:
    print('Bar not found')
    exit()
else:
    func.moveBar(1)
# func.sleep(.6)
# for i in range(1,x):
#     pyau.press('right')
#     # sleep(.1)
# # setZoom('50')
# func.sleep(1)
# func.altTab(.6)