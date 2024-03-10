from os import path

brownserPath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

linkSeniorXLSX = 'https://miliumcombr.sharepoint.com/sites/Onda02-FolhadePagamento/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120008E83637B03E57B41B59039D7E1EFD29C&id=%2Fsites%2FOnda02%2DFolhadePagamento%2FShared%20Documents%2FGeneral%2F1%2E%20Status%20Report&viewid=a88c3865%2D0f79%2D4032%2D9c5d%2D67483c322cde.com'

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

