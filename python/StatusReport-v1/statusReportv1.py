import credntials as cred
import funcStatus as fst
import variables as vari

fst.selectAndType('name', 'loginfmt', cred.userName)#type name
fst.pyau.press('enter')
fst.selectAndType('name', 'passwd', cred.passWord)#type password
fst.pyau.press('enter')
fst.selectAndClik('id', 'KmsiCheckboxField')#checkbox to remember
fst.selectAndClik('id', 'idSIButton9')#checkbox to remember
fst.pyau.hotkey('alt','space')
fst.sleep(1)
fst.pyau.press('x')
fst.sleep(5)
fst.searchAndClickIMG(vari.ListImglinkProjetoSenior, 3, 2)
fst.searchAndClickIMG(vari.listImgbuttonOpenExcelonSharePoint, 3, 2)
fst.searchAndClickIMG(vari.listbuttonOpenExcelOnAppOnSharePoint, 3, 2)
fst.searchAndClickIMG(vari.listImgbuttonConfirmOpenExcelApp, 3, 2)
fst.searchAndClickIMG(vari.listImgbuttonSimdoAlerta, 3, 2)
fst.sleep(90)
# fst.searchAndClickIMG(vari.ImglinkProjetoSenior)#search and click on link of the status
# fst.searchAndClickIMG(vari.ImgbuttonOpenExcelonSharePoint)#click on excel button 
# fst.searchAndClickIMG(vari.buttonOpenExcelOnAppOnSharePoint)

# fst.selectAndClikRight('partial link text', '00-StatusFolhaDePonto')
# fst.selectAndClik('partial link text', '00-StatusFolhaDePonto')
# linkProjSenior = fst.pyau.locateCenterOnScreen(r'\imgs\projSeniorLinkStatus.png')
# fst.pyau.rightClick(linkProjSenior)
# fst.sleep(120)


# fst.brownser.find_element('link text', '00-StatusFolhaDePonto.xlsx').click(2)