import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
import os.path
import serial
import sys

remetente = ''
senha = ''
nome_remetente = ''
email = ''
email1 = ' '
temperature = []
humidity = []
x = 0


def media_temp():
    arq = open('med_temp.txt', 'r', encoding='utf8')

    temp = arq.readlines()
    arq.close()
    media = ''

    for linha in temp:
        media = linha

    mediaf = float(media)

    if mediaf > 25:
        email_temperatura()

    arquivo1 = 'med_temp.txt'
    os.remove(arquivo1)
    arquivo = 'temperature.txt'
    os.remove(arquivo)


def media_umid():
    arq = open('med_umid.txt', 'r', encoding='utf8')

    temp = arq.readlines()
    arq.close()
    media = ''

    for linha in temp:
        media = linha

    mediaf = float(media)

    if mediaf > 50:
        email_umidade()

    arquivo = 'med_umid.txt'
    os.remove(arquivo)
    arquivo1 = 'humidity.txt'
    os.remove(arquivo1)

def rastreamento():
    print("Iniciando rastreamento!")
    ser = serial.Serial("COM3", baudrate=9600, timeout=1)
    while 1:
        arduinodata = ser.readline().decode("ascii")
        if len(arduinodata) > 1:
            print(arduinodata.lstrip())
            if 't' in arduinodata:
                temperature.append(arduinodata.strip('t' + '\n'))
            elif 'h' in arduinodata:
                humidity.append(arduinodata.strip('h' + '\n'))
        if arduinodata == "pause":
            break

    arquivo = open("temperature.txt", "w")
    arquivo.writelines(temperature)

    arquivo = open("humidity.txt", "w")
    arquivo.writelines(humidity)

    print("Rastreamento finalizado!")


def email_umidade():
    global remetente, senha, nome_remetente

    destinatario = ''

    arq1 = open("usuario.txt", 'r', encoding='utf8')

    for linha in arq1:
        if 'email: ' in linha:
            destinatario = (linha.strip('email:'))

    arq = open('dados.txt', 'r', encoding='utf-8')

    for linha in arq:
        if "login: " in linha:
            remetente = (linha.strip("login:" + '\n'))

        if "senha: " in linha:
            senha = (linha.strip("senha:" + '\n'))

        if "nome: " in linha:
            nome_remetente = (linha.strip("nome:" + '\n'))

    destinatario = [destinatario]
    nomes_dests = ['']

    email_html = open('umidade_baixa.html')
    email_mensagem = email_html.read()

    for destinatario, nome_dest in zip(destinatario, nomes_dests):
        print("Enviando email de alerta de umidade...\n")

        msg = MIMEText(email_mensagem, 'html')
        msg['To'] = formataddr((nome_dest, destinatario))
        msg['From'] = formataddr((nome_remetente, remetente))
        msg['Subject'] = 'SISTEMA MONITORA - ALERTA DE ANORMALIDADE ENCONTRADA!'
        try:

            server = smtplib.SMTP('smtp.gmail.com', 587)

            context = ssl.create_default_context()
            server.starttls(context=context)

            server.login(remetente, senha)

            server.sendmail(remetente, destinatario, msg.as_string())
            print('Email de alerta de umidade enviado!\n')
            server.close()
        except Exception as e:
            print(f'Algo de errado aconteceu! {e}')


def email_temperatura():
    global remetente, senha, nome_remetente

    destinatario = ''

    arq1 = open("usuario.txt", 'r', encoding='utf8')

    for linha in arq1:
        if 'email: ' in linha:
            destinatario = (linha.strip('email:'))

    arq = open('dados.txt', 'r', encoding='utf-8')

    for linha in arq:
        if "login: " in linha:
            remetente = (linha.strip("login:" + '\n'))

        if "senha: " in linha:
            senha = (linha.strip("senha:" + '\n'))

        if "nome: " in linha:
            nome_remetente = (linha.strip("nome:" + '\n'))

    destinatario = [destinatario]
    nomes_dests = ['']

    email_html = open('temperatura_alta.html')
    email_mensagem = email_html.read()

    for destinatario, nome_dest in zip(destinatario, nomes_dests):
        print("Enviando email de alerta de temperatura...\n")

        msg = MIMEText(email_mensagem, 'html')
        msg['To'] = formataddr((nome_dest, destinatario))
        msg['From'] = formataddr((nome_remetente, remetente))
        msg['Subject'] = 'SISTEMA MONITORA - ALERTA DE ANORMALIDADE ENCONTRADA!'
        try:

            server = smtplib.SMTP('smtp.gmail.com', 587)

            context = ssl.create_default_context()
            server.starttls(context=context)

            server.login(remetente, senha)

            server.sendmail(remetente, destinatario, msg.as_string())
            print('Email de alerta de temperatura enviado!\n')
            server.close()
        except Exception as e:
            print(f'Algo de errado aconteceu! {e}')


def email_inicial():
    global remetente, senha, nome_remetente

    destinatario = ''

    arq1 = open("usuario.txt", 'r', encoding='utf8')

    for linha in arq1:
        if 'email: ' in linha:
            destinatario = (linha.strip('email:'))

    arq = open('dados.txt', 'r', encoding='utf-8')
    for linha in arq:
        if "login: " in linha:
            remetente = (linha.strip("login:" + '\n'))

        if "senha: " in linha:
            senha = (linha.strip("senha:" + '\n'))

        if "nome: " in linha:
            nome_remetente = (linha.strip("nome:" + '\n'))

    destinatario = [destinatario]
    nomes_dests = ['']

    email_html = open('boas_vindas.html')
    email_mensagem = email_html.read()

    for destinatario, nome_dest in zip(destinatario, nomes_dests):
        print("Enviando email de boas vindas...\n")

        msg = MIMEText(email_mensagem, 'html')
        msg['To'] = formataddr((nome_dest, destinatario))
        msg['From'] = formataddr((nome_remetente, remetente))
        msg['Subject'] = 'SISTEMA MONITORA - BOAS VINDAS!'
        try:

            server = smtplib.SMTP('smtp.gmail.com', 587)

            context = ssl.create_default_context()
            server.starttls(context=context)

            server.login(remetente, senha)

            server.sendmail(remetente, destinatario, msg.as_string())
            print('Email de boas vindas enviado!\n')
            server.close()
        except Exception as e:
            print(f'Algo de errado aconteceu! {e}')


if not os.path.exists('usuario.txt'):

    print("Bem vindo ao Sistema Monitora!")
    print('De início, pedimos que digite o seu e-mail para realizar o cadastro no sistema!\nEm seguida, '
          'um e-mail será enviado para sua caixa de entrada falando um pouco mais sobre o nosso sistema!')

    while email != email1:

        email = input("\nDigite o seu e-mail: ")
        email1 = input("\nConfirme o seu e-mail: ")

        if email == email1:
            print("\nCadastro realizado com sucesso!\n")
            abrir = open("usuario.txt", 'w', encoding='utf8')
            salvar_email = abrir.write('email: ' + email + '\n')
            abrir.close()
            email_inicial()
            sys.exit()
        else:
            print("\nOs e-mails não conferem! Por favor, digite novamente!")


if not os.path.exists('temperature.txt'):
    rastreamento()

if os.path.exists('med_temp.txt'):
    media_temp()

if os.path.exists('med_umid.txt'):
    media_umid()