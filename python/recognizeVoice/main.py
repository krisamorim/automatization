import speech_recognition as sr
import pyttsx3
from subprocess import Popen
from time import sleep

def ouvir():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Diga alguma coisa...")
        print("Qual comando?")

        reconhecedor.adjust_for_ambient_noise(source)
        audio = reconhecedor.listen(source)

    try:
        texto = reconhecedor.recognize_google(audio, language='pt-BR')
        print("Você disse: " + texto)
        return texto
    except sr.UnknownValueError:
        print("Não entendi o que você disse")
        return ""
    except sr.RequestError as e:
        print("Erro ao requisitar resultados, {0}".format(e))
        return ""

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

if __name__ == "__main__":
    falar("Olá meu grande mestre, me chamo Ana Lúcia.")
    while True:
        entrada = ouvir().lower()
        if "parar" in entrada:
            falar("Até logo meu grande mestre!")
            break
        if "executar ping" in entrada:
            Popen(["ping", '8.8.8.8'], shell=True)
            sleep(6)
        # Adicione outras condições para lidar com diferentes comandos aqui
