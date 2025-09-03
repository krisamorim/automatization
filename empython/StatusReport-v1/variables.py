from os import path

brownserPath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

#-------------- SR PORJECT ------------#
ImglinkProjetoSenior = path.abspath(__file__).replace('variables.py',r'imgs\projSeniorLinkStatus2.png')
ListImglinkProjetoSenior = [ImglinkProjetoSenior]
SRpositions = [420, 452, 484, 516, 540, 575, 600]
SRbeginningChart = 'C6'
SRmoveBar = 12
SRincreaseBar =  1.2
SRlastPointChart = [1292, 538]
SRslideTitle = 'PROJETO SENIOR '+'–'+' CRONOGRAMA'
SRdownImgOnPPT = 16

#-------------- CV PORJECT ------------#
ImglinkProjetoSenior = path.abspath(__file__).replace('variables.py',r'imgs\projSeniorLinkStatus2.png')
CVListImglinkProjetoSenior = [ImglinkProjetoSenior]
CVpositions = [420, 452, 484, 516, 540, 575, 600]
CVbeginningChart = 'C6'
CVmoveBar = 12
CVincreaseBar =  1.2
CVlastPointChart = [1292, 538]
CVslideTitle = 'PROJETO CONTRAVALE – CRONOGRAMA'
CVdownImgOnPPT = 16

#-------------- BUDGET PORJECT ------------#
ImglinkProjetoSenior = path.abspath(__file__).replace('variables.py',r'imgs\projSeniorLinkStatus2.png')
budGetListImglinkProjetoSenior = [ImglinkProjetoSenior]
budGetpositions = [405, 438]
budGetbeginningChart = 'B5'
budGetmoveBar = 26
budGetincreaseBar =  5.0
budGetlastPointChart = [1294, 553]
budGetslideTitle = 'PROJETO ORÇAMENTO – CRONOGRAMA'
budGetdownImgOnPPT = 16

#-------------- IMG e LIST OPEN ON EXCEL ------------#
ImgbuttonOpenExcelonSharePoint = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'buttonOpenExcelonSharePoint')
listImgbuttonOpenExcelonSharePoint = [ImgbuttonOpenExcelonSharePoint]
buttonOpenExcelOnAppOnSharePoint = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'buttonOpenExcelOnAppOnSharePoint')
listbuttonOpenExcelOnAppOnSharePoint = [buttonOpenExcelOnAppOnSharePoint]
ImgbuttonConfirmOpenExcelApp = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'buttonConfirmOpenExcelApp')
listImgbuttonConfirmOpenExcelApp = [ImgbuttonConfirmOpenExcelApp]
ImgbuttonSimdoAlerta = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'buttonSimdoAlerta')
listImgbuttonSimdoAlerta = [ImgbuttonSimdoAlerta]
ImgexcelOntaskBar = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'excelOntaskBar')
listexcelOntaskBar = [ImgexcelOntaskBar]
ImgbuttonEditExcel = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'buttonEditExcel')
listbuttonEditExcel = [ImgbuttonEditExcel]

#------------------------ To check excel is open ----------------#
ImgtatusBarExcel = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'statusBarExcel')
ImgfuncBarExcel = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'funcBarExcel')
liststatusBarExcel = [ImgtatusBarExcel,ImgfuncBarExcel]

#----------------- LineBar IMAGE LIST -----------------#
imgLineBar1 = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2', r'timeLineBar1')
imgLineBar2 = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2', r'timeLineBar2')
imgLineBar3 = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2', r'timeLineBar3')
ListLineBar = [imgLineBar1, imgLineBar2, imgLineBar3]

#----------------- POWERPOINT -----------------#
ImgpowerPointOntaskBar = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'powerPointOntaskBar')
listpowerPointOntaskBar = [ImgpowerPointOntaskBar]