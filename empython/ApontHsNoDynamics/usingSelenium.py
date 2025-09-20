# from selenium import webdriver
# driver = webdriver.Firefox(executable_path='C:\Program Files\SeleniumMozila\geckodriver.exe')
# driver.get("http://www.python.org")
import password as pw
import variables
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Configurações opcionais do Firefox
options = webdriver.FirefoxOptions()
firefox_profile_path = r'C:\Users\krisf\AppData\Local\Mozilla\Firefox\Profiles\72xxqwy5.default-release'  # Caminho do meu perfil
options.set_preference('profile', firefox_profile_path)

# Inicializa o Firefox
service = webdriver.FirefoxService(executable_path=r'C:\Program Files\SeleniumMozila\geckodriver.exe')
driver = webdriver.Firefox(service=service, options=options)
# options.add_argument("--start-maximized")  # inicia maximizado (não funciona no Windows)
driver.maximize_window() # maximiza de verdade

# Acessa a página desejada
driver.get('https://linxprd.crm2.dynamics.com/main.aspx?pagetype=entitylist&etn=msdyn_workorder&viewid=63e0ccf4-8db5-e711-80f9-e0071b664ec1&viewType=1039&forceUCI=1&appid=0f6e740a-7a48-4536-872f-268ac257e0c7')
time.sleep(5)  # espera a página carregar

#-------------------------------------- Funções --------------------------------------

# Função para Localiza elementos
def localizar_elemento(driver, element_id: str, element_xpath: str):
    """
    Tenta localizar um elemento primeiro pelo ID, depois pelo XPath.
    Faz 3 tentativas com intervalos crescentes.
    Caso não encontre, pergunta ao usuário se deseja sair ou continuar.
    """
    
    # Tentativas por ID
    tentativas_id = [0, 2, 3]  # espera antes da tentativa
    for espera in tentativas_id:
        if espera > 0:
            time.sleep(espera)
        try:
            elemento = driver.find_element("id", element_id)
            print(f"[OK] Elemento encontrado pelo ID: {element_id}")
            return elemento
        except Exception as e:
            print(f"[X] Tentativa com ID falhou (espera {espera}s): ",e)

    # Tentativas por XPATH
    tentativas_xpath = [0, 2, 3]
    for espera in tentativas_xpath:
        if espera > 0:
            time.sleep(espera)
        try:
            elemento = driver.find_element("xpath", element_xpath)
            print(f"[OK] Elemento encontrado pelo XPATH: {element_xpath}")
            return elemento
        except Exception as e:
            print(f"[X] Tentativa com XPATH falhou (espera {espera}s) :", e)

    # Se não encontrou
    while True:
        escolha = input("Elemento não encontrado. Digite 1 para sair ou 2 para continuar: ")
        if escolha == "1":
            print("Saindo do programa...")
            exit(0)
        elif escolha == "2":
            print("Prosseguindo sem o elemento...")
            return None
        else:
            print("Opção inválida, tente novamente.")

# Função para logar
def logando():
    #preenchendo username
    userName = localizar_elemento(driver, variables.fieldUsername_ID, variables.fieldUsername_XPATH)
    if userName:
        userName.send_keys(pw.userK)
        time.sleep(2)
        # userName.submit() #está enviado com campo vazio

    #pressionando botão next
    nextButton = localizar_elemento(driver, variables.buttonNext_ID, variables.buttonNext_XPATH)
    if nextButton:
        nextButton.click()

    #preenchendo password
    time.sleep(2)  
    password = localizar_elemento(driver, variables.fieldPassword_ID, variables.fieldPassword_XPATH)
    if password:
        password.send_keys(pw.passK)
        password.submit()   

    #pressionando botão Sign in
    time.sleep(2)
    nextButton = localizar_elemento(driver, variables.buttonNext_ID, variables.buttonNext_XPATH)
    if nextButton:
        nextButton.click()
    time.sleep(25)

    #marcar não mostrar novamente e clicar em Yes
    checkboxDontShowAgain = localizar_elemento(driver, variables.checkboxDontShowAgain_ID, variables.checkboxDontShowAgain_XPATH)
    if checkboxDontShowAgain:
        checkboxDontShowAgain.click()
        time.sleep(2)
        nextButton.click()


#-------------------------------------- Pós login --------------------------------------
time.sleep(10)  # espera a página carregar
# Clica em "Reservas de Recursos"
buttonReservaDeRecurso = localizar_elemento(driver, variables.buttonReservaDeRecurso_ID, variables.buttonReservaDeRecurso_XPATH)
if buttonReservaDeRecurso:
    buttonReservaDeRecurso.click()
    time.sleep(5)  # espera a página carregar