from os import path

brownserPath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

#-------------- IMG e LIST PROJETO SENIOR ------------#
ImglinkProjetoSenior = path.abspath(__file__).replace('variables.py',r'imgs\projSeniorLinkStatus2.png')
ListImglinkProjetoSenior = [ImglinkProjetoSenior]

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

