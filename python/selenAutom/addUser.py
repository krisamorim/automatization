import functions as fct
import credentias as crd
import excelData
from excelFunctions import pause

########## VARIABLES ##########
userField = '//*[@id="f_login"]'
passField = '//*[@id="f_senha"]'
selectEstabXPATH = '/html/body/span/span/span[2]/ul/li[3]'
selectEstabBtnID = 'btn'
menuSystemXPATH = '//*[@id="sidebar"]/ul/li[6]/a'
menuUserStoreXPATH = '//*[@id="sidebar"]/ul/li[6]/ul/li[3]/a'
menuUserStoreTXT = 'Usuários LJ'
usersToAddPortal = excelData.dados()
okUserAlreadyExistsXPATH = '/html/body/div[4]/div/div/div[3]/button[2]'

########## LISTS ##########
loginData = ['xpath',userField, crd.user, passField, crd.password] #[id, idUserValue, idPassValue, user, userPass]
estabData = ['xpath',selectEstabXPATH,'id', selectEstabBtnID] #[id, idUserValue, idPassValue, user, userPass]
# userStorePage = ['xpath', menuSystemXPATH, 'xpath', menuUserStoreXPATH]
userStorePage = ['xpath', menuSystemXPATH, 'link text', menuUserStoreTXT]

########## RUN ##########
fct.gotToUrl('https://portal.milium.com.br/index.aspx')
fct.loginPage(loginData)
fct.setEstabelecimento(estabData)
fct.goToUserStorePage(userStorePage)


for user in usersToAddPortal:
    store = user['loja']
    name = user['Name']
    cpf = user['CPF']

    fct.selectAndClik('xpath', '//*[@id="page"]/div[2]/div[1]/div[1]/button')#clicando no botão de +

    print(f'adding user {name}')
    fct.selectAndType('id', 'f_cpf' ,cpf)
    fct.selectAndClik('id', 'f_nome')#clicar no proximo campo(nome) só para o sistema checar se user ja existe

    pause('1-Continuar e 2-Sair\n>> ')
    #verificar se surgiu popup informando que user ja existe
    # alreadyExistAttempt1 = True if fct.selectAndClik('xpath', okUserAlreadyExistsXPATH) == 'ok' else False
    # alreadyExistAttempt2 = True if fct.selectAndClik('link text', 'OK') == 'ok' else False
    
    # if (alreadyExistAttempt1 == True) or (alreadyExistAttempt2 == True):
    #     fct.sleep(5)
    #     fct.addUserAlreadyExist()
    # else:   
    #     fct.addUserNotAlreadyExist(name)

fct.sleep(90)

