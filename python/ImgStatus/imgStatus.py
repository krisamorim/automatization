import funcImgStatus as func

while True:
    downKey = func.option()
    func.altTab(.7)
    func.sleep(.5)
    func.updateImage(downKey)
    func.animacao()
    func.altTab(.2)
    func.cls()
    