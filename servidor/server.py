from socket import socket, AF_INET, SOCK_STREAM
import json 
import sys

porta = int(sys.argv[1])
lista_status = []
server = socket(AF_INET,SOCK_STREAM)
server.bind(('', porta)) #Ip host vazio pois ira funcionar nesta maquina, entao ele adiciona o proprio ip
server.listen(1)
while True:
	conteudo, endereco = server.accept()#recebendo conteudo do socket
	
	while True:
		mensagem = conteudo.recv(1024) 
		if mensagem == b'':
			break
		status_geral = json.loads(mensagem.decode('utf-8')) #decodificar
		lista_status.append(status_geral)
		lista_ordenada = reversed(lista_status)
		with open("www/index.html", "w") as html:
			for status in lista_ordenada:
				html.write(f'{status}')
				html.write("<br>")
				html.write("<br>")
		print("SALVO COM SUCESSO")
		
