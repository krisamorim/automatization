
import variables as vari
import funcStatus as fst

while True:
    pptOUexcel = int(input(' 0 to EXIT\n 1 to Excel+PPT\n 2 to PPT\n>> '))
    if pptOUexcel == 0:
        exit()

    fst.cls()
    optionProject = int(input('Which status do you want to update:\n 0 to EXIT\n 1 to Sr Project\n 2 to CV Project\n 3 to Budget Project\n 4 to Acquirement Project\n 5 to ADSL Project\n 6 to DRAAS Project\n 7 to Zimbra Projact\n 8 to 82 Project\n 9 to 65 Project\n10 to IP Phone Project\n>> '))
    if optionProject == 0:
        exit()
   
    if pptOUexcel == 2:
        fst.updateImageOnPPT(optionProject)
    else:
        #update file
        fst.altTab(1)
        fst.setZoom('60')
        
        if fst.locateOnScreenFunc(vari.ListLineBar, 4, 2) == False:
            print('Bar not found')
            fst.sleep(10)
            exit()
        else:
            fst.moveBarAndCopyChart(optionProject)
        
        fst.updateImageOnPPT(optionProject)