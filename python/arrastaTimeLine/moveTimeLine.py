import funcMoveTimeLineOnExcel as func
import variablesMoveTimeLine as var

func.cls()
func.altTab(.5)
func.setZoom('60')
if func.locateOnScreenFunc(var.imgList, 4, 2) == False:
    print('Bar not found')
    exit()
else:
    func.moveBarAndCopyChart(1)
func.sleep(.6)
