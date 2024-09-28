# import pyautogui
import variables as vari
import creden as cred
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# Caminho para o WebDriver do Microsoft Edge
webdriver_path = vari.webdriver_path

# Configurando o navegador Microsoft Edge
edge_options = Options()
edge_options.add_argument("--start-maximized")  # Inicia a janela maximizada

# Iniciando o driver do Microsoft Edge
service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=edge_options)

# Fazer login no jira
driver.get(vari.jiraLoginPage)

# Aguarda um tempo para garantir que a página esteja totalmente carregada (se necessário)
sleep(6)

#Função para Capturar o título da aba atual
def cathTitleTab():
    '''
    Até o momento utilizado em:
    - Não utilizado
    '''
    page_title = driver.title
    print("Título da aba atual:", page_title)

# Função para localizar e clicar no elemento com base no XPath
def localizarEclickar(identification, opcao):
    '''
    1 para localizar por ID
    
    Qualquer outro numero para localizar por xpath
    '''
    try:
        # Tenta encontrar o elemento usando o XPath
        # elemento = driver.find_element(By.XPATH, xpath)
        elemento = driver.find_element(By.ID, identification) if opcao == 1 else driver.find_element(By.XPATH, identification)
        #Printa o emelemnto no cosole
        print(elemento)

        # Se encontrado, clica no elemento
        elemento.click()
        print("Elemento encontrado e clicado com sucesso.")

    except NoSuchElementException:
        # Caso o elemento não seja encontrado, exibe uma mensagem de erro
        print("Elemento não encontrado.")

def localizarEpreencher(identification, texto, opcao):
    '''
    1 para localizar por ID
    
    Qualquer outro numero para localizar por xpath
    '''

    try:
        # Tenta localizar o elemento usando o XPath fornecido
        # elemento = driver.find_element(By.XPATH, xpath)

        elemento = driver.find_element(By.ID, identification) if opcao == 1 else driver.find_element(By.XPATH, identification)


        # Se encontrado, insere o texto no campo input
        elemento.send_keys(texto)
        print(f"Texto '{texto}' inserido com sucesso.")
    except NoSuchElementException:
        # Se o elemento não for encontrado, imprime a mensagem no terminal
        print("Elemento não localizado")

localizarEpreencher(vari.inputUserName, cred.userName1, 2)#preencher userName
localizarEclickar(vari.buttonLogin, 2) #clicar no botão Login
sleep(1) #aguarda input de password aparecer
localizarEpreencher(vari.inputPassWord, cred.passName1, 2)
localizarEclickar(vari.buttonLoginID, 1) #clicar no botão Login
sleep(3) #aguardar
localizarEclickar(vari.buttonDismissAutnID, 1) #Negar ativar autent de 2 fat
sleep(3) #aguardar
driver.get(vari.urlProjNetcr)#ir p/ proj netc
sleep(4) #aguardar
localizarEclickar(vari.buttonAceptCookies, 2) #aceitar cookies
sleep(2) #aguardar
driver.get(vari.urlFiltros)#ir p/ filtros
sleep(2) #aguardar
localizarEclickar(vari.buttonExpandirExport, 2) #expandir exportar
sleep(2) #aguardar
localizarEclickar(vari.buttonExportCSV, 2) # exportar CSV filter fields
sleep(10)

# Fechar o navegador após a captura
# driver.quit()