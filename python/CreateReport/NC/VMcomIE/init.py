# import pyautogui
import variables as vari
import creden as cred
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# pyautogui.click('./imgs/IE-aberto.png')

# Caminho para o WebDriver do Microsoft Edge
webdriver_path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\129.0.2792.65\\msedgedriver.exe'

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

# Capturar o título da aba atual
page_title = driver.title
print("Título da aba atual:", page_title)


# Função para localizar e clicar no elemento com base no XPath
def localizarEclickar(xpath):
    try:
        # Tenta encontrar o elemento usando o XPath
        element = driver.find_element(By.XPATH, xpath)

        #Printa o emelemnto no cosole
        print(element)

        # Se encontrado, clica no elemento
        element.click()
        print("Elemento encontrado e clicado com sucesso.")

    except NoSuchElementException:
        # Caso o elemento não seja encontrado, exibe uma mensagem de erro
        print("Elemento não encontrado.")


localizarEclickar(vari.buttonAceptCookies)


sleep(100)

# Fechar o navegador após a captura
# driver.quit()