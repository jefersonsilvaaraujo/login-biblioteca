import sched, time, threading, sys, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def AcessarSite():
    while (True):
        
        #OPTIONS EXECUTA OS COMANDOS EM MODO HEADLESS
        #PARA DESABILITAR E PODER VER TODOS OS PROCESSOS BASTA UTILIZAR APENAS O COMANDO  - navegador= webdriver.Chrome() - ELIMINANDO AS LINHAS DE OPTIONS.
        #options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        #navegador= webdriver.Chrome(chrome_options=options)
        
    
        navegador= webdriver.Chrome()
        
        navegador.get("https://dliportal.zbra.com.br/Login.aspx?key=ESUP")
        time.sleep(8)
        return navegador
    

                        #Preencher o campo de login/senha
    
def Login(navegador):
    usuario = navegador.find_element(By.NAME, "userIdTextBox")   #Procurar o id ou então a classificação do login e da senha
    senha = navegador.find_element(By.NAME, "passwordTextBox")
    botao = navegador.find_element(By.CLASS_NAME, "cookies-policy-accept-button")
    botao.click()
    usuario.send_keys("1400206163")
    senha.send_keys("Aluno@esup")
    time.sleep(3)

                        #Localizar o botão de enviar e executar
    
def Entrar(navegador):
    #logar= navegador.find_element(By.NAME, "loginButton")
    logar= navegador.find_element(By.XPATH, "//*[@type='submit']").click()
    #logar.submit()
    #logar.click()
    
Navevagor= AcessarSite()
Login(Navevagor)
Entrar(Navevagor)
    
    



    












    
    



    








