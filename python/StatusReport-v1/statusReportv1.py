import credntials as cred
import variables as vari
import funcStatus as fst

while True:
    fst.cls()
    optionProject = int(input('Which status do you want to update:\n 0 to EXIT\n 1 to Sr Project\n 2 to CV Project\n 3 to Budget Project\n 4 to Acquirement Project\n 5 to ADSL Project\n 6 to DRAAS Project\n 7 to Zimbra Projact\n 8 to 82 Project\n 9 to 65 Project\n10 to IP Phone Project\n>> '))
    
    if optionProject == 0:
        exit()
   
    import funcBrownser as fbro
    fbro.brownser.get(fst.setProj(optionProject)['urlProject'])
    
    #Open status
    fbro.selectAndType('name', 'loginfmt', cred.userName)#type name
    fst.pyau.press('enter')
    fbro.selectAndType('name', 'passwd', cred.passWord)#type password
    fst.pyau.press('enter')
    fbro.selectAndClik('id', 'KmsiCheckboxField')#checkbox to remember
    fbro.selectAndClik('id', 'idSIButton9')#checkbox to remember
    fst.maxWindow()
    fst.sleep(5)
    fst.searchAndClickIMG(vari.ListImglinkProjetoSenior, 3, 2)
    fst.searchAndClickIMG(vari.listImgbuttonOpenExcelonSharePoint, 3, 2)
    fst.searchAndClickIMG(vari.listbuttonOpenExcelOnAppOnSharePoint, 3, 2)
    fst.searchAndClickIMG(vari.listImgbuttonConfirmOpenExcelApp, 3, 2)
    fst.searchAndClickIMG(vari.listImgbuttonSimdoAlerta, 3, 2) #click on Yes to open on excel app

    #Going to excel
    if fst.searchAndClickIMG(vari.liststatusBarExcel, 2, 2):#Check if excel is open on screen
        print('Elxcel open on screen')
    else:
        fst.searchAndClickIMG(vari.listexcelOntaskBar, 3, 2)#click in excel on taskbar
        fst.sleep(1)
    fst.searchAndClickIMG(vari.listbuttonEditExcel, 3, 2)#click in edit on excel
    fst.maxWindow()
    fst.sleep(1)

    #update file
    fst.setZoom('60')
    if fst.locateOnScreenFunc(vari.ListLineBar, 4, 2) == False:
        print('Bar not found')
        fst.sleep(10)
        exit()
    else:
        fst.moveBarAndCopyChart(optionProject)
    
    #going to PowerPoint
    fst.searchAndClickIMG(vari.listpowerPointOntaskBar, 3, 2)#click in powerPoint on taskbar
    fst.gotToSlide(optionProject)
    fst.updateImageOnPPT(optionProject)




    #past chart