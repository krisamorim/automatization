from os import path

brownserPath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

ImglinkProjetoSenior = path.abspath(__file__).replace('variables.py',r'imgs\projSeniorLinkStatus2.png')

ImgbuttonOpenExcelonSharePoint = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'buttonOpenExcelonSharePoint')

buttonOpenExcelOnAppOnSharePoint = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'buttonOpenExcelOnAppOnSharePoint')

ImgbuttonSimdoAlerta = path.abspath(ImglinkProjetoSenior).replace('projSeniorLinkStatus2',r'buttonSimdoAlerta')

linkSeniorXLSX = 'https://miliumcombr.sharepoint.com/sites/Onda02-FolhadePagamento/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120008E83637B03E57B41B59039D7E1EFD29C&id=%2Fsites%2FOnda02%2DFolhadePagamento%2FShared%20Documents%2FGeneral%2F1%2E%20Status%20Report&viewid=a88c3865%2D0f79%2D4032%2D9c5d%2D67483c322cde.com'

menuOpen = ['xpath','/html/body/div[4]/div/div/div/div/div/div/ul/li[1]/button/div/span']
menuOpenInAppl = ['xpath','/html/body/div[5]/div/div/div/div/div/div/ul/li[2]/button/div/span']