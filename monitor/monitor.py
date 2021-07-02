from icmplib import ping 
from nslookup import Nslookup
import requests
from socket import socket, AF_INET, SOCK_STREAM
import json
import time
from datetime import datetime
import sys

 
def leitura_arq():
	configtxt = open('config/config.txt','r')
	configtxtall= [line.split() for line in configtxt]
	
	return configtxtall


configtxtall = leitura_arq()

ipHost= ''
ipAp = ''
ipWeb = ''
ipDns = ''
httpAdress = ''
domain = ''

if len(sys.argv) !=3:
	print("Informe os dados corretamente: arquivo ipHost porta")	
	sys.exit()

ipServer = sys.argv[1]
porta = int(sys.argv[2])

for teste_elemento in configtxtall: 
	
	if teste_elemento[0] == 'ipHost':
		ipHost = teste_elemento[1]

	elif teste_elemento[0] == 'ipAp':
		ipAp = teste_elemento[1]

	elif teste_elemento[0] == 'ipWeb':
		ipWeb = teste_elemento[1]

	elif teste_elemento[0] == 'ipDns':
		ipDns = teste_elemento[1]

	elif teste_elemento[0] == 'httpAdress':
		httpAdress = teste_elemento[1]

	if teste_elemento[0] == 'domain':
		domain = teste_elemento[1]


while True:
	
	ping_ipHost = ping(ipHost, count=4)
	ping_ipHost_resultado = f"pingIPHOST OK {datetime.now()}" if ping_ipHost.packet_loss == 0 else f"pingIPHOST NOK {datetime.now()}"
	
	ping_ipAp = ping(ipAp, count=4)
	ping_ipAp_resultado = f"pingAP OK {datetime.now()}" if ping_ipAp.packet_loss == 0 else f"pingAP NOK {datetime.now()}"
	
	ping_ipWeb = ping(ipWeb, count=4)
	ping_ipWeb_resultado = f"pingWEB OK {datetime.now()}" if ping_ipWeb.packet_loss == 0 else f"pingWEB NOK {datetime.now()}"
	
	ping_ipDns = ping(ipDns, count=4)
	ping_ipDns_resultado = f"pingDNS OK {datetime.now()}" if ping_ipDns.packet_loss == 0 else f"pingDNS NOK {datetime.now()}"
	

	dns_query = Nslookup(dns_servers = [ipDns])
	ips_record = dns_query.dns_lookup(domain)
	dns_resultado = f"DNS OK {ips_record.response_full[0]} {datetime.now()}" if ips_record.response_full !=[] else f"DNS INDISPONÍVEL {datetime.now()}"
	
	
	request_httpAdress = requests.get(httpAdress)

	
	request_httpAdress_resultado = f"STATUS CODE {request_httpAdress.status_code} {datetime.now()}"
	
	
	listas_resultados_ping = [{"ip":ipHost, "status":ping_ipHost_resultado},
				{"ip":ipAp, "status":ping_ipAp_resultado},
				{"ip":ipWeb, "status":ping_ipWeb_resultado},
				{"ip":ipDns, "status":ping_ipDns_resultado}]
	
	dict_dns_resultado= {"ip":ipDns, "status":dns_resultado}
	dict_request_httpAdress_resultado= {"httpAdress":httpAdress, "status":request_httpAdress_resultado}
	
	status_geral = {"status ping":listas_resultados_ping,
			"status dns":dict_dns_resultado, 
			"status httpAdress":dict_request_httpAdress_resultado}

	print(status_geral)

	

	
	with socket(AF_INET, SOCK_STREAM) as enviar:
		try:
			enviar.connect((ipServer,porta))
			b = json.dumps(status_geral).encode('utf-8')
			enviar.sendall(b)
			print("CONTEUDO ENVIADO COM SUCESSSO")
		except ConnectionRefusedError:
			print("FALHA NO ENVIO")
	time.sleep(5)

