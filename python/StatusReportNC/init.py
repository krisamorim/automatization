import functions as fc
import funcOption as fo

downFolder = "C:\\Users\\krisn\\Downloads"
reportFolder = "%desktopkris%\\NC\\Report"
createFile = 'Você já criou a pasta de hoje?\n1 para Sim\n0 para Não\n>> '

fo.checkOperaOpen()
fc.gotTourlWithOperaOpen('https://netcredbrasil.atlassian.net/issues/?filter=10021')
fc.moveFile()


fo.YesNoOption(createFile)
fc.downloadListOpenSprint()
fc.moveFile(downFolder,reportFolder)


fc.altTab(1)
fc.sleep(100)

# fc.getMousePosition(3)


# while True:
#     fc.cls()
#     someOption = fo.someOption()
#     if fo.someOption == 1:
#         print('digitou 1')
