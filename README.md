# Apresentação 
Trabalho apresentado à disciplina de Laboratório de Redes do curso de Eng. Elétrica IFES Campus Guarapari, ministrada pelo Prof. Dr. Alexandre Pereira do Carmo.

# Alunos
- João Vitor Alves Barradas
- Peter Gleiser Garcez 

# Procedimentos

1) Caso você não tenha instalado o DockerHub, abra um terminal de comando e dê os comandos abaixo para instalá-lo: 
- sudo apt-get update
- sudo apt-get remove docker-engine docker.io
- sudo apt install docker.io

2) Crie uma pasta e coloque dentro dela o arquivo config.txt contido na pasta "monitor" deste repositório. Você pode alterar à vontade os valores dos IPs presentes neste arquivo. 

3) Abra um terminal de comando dentro desta pasta. Dê o comando abaixo para baixar a imagem do monitor a partir do DockerHub e rodá-la: 
- sudo docker run --rm -it --network=host -v "$PWD:/app/config" trabalhoredes/trabalho python3 monitor.py 127.0.0.1 8081

4) Abra outro terminal de comando dentro da mesma pasta. Dê o comando abaixo para baixar a imagem do servidor a partir do DockerHub e rodá-la:
- sudo docker run --rm -it -p 8081:8081 -v "$(pwd):/app/www" trabalhoredes/servidor python3 server.py 8081

5) Abra outro terminal de comando dentro da mesma pasta. Dê o comando abaixo para rodar o Apache e poder ver os resultados no navegador web: 
- sudo docker run --rm -it --name my-apache-app -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4 

6) Abra um navegador web e digite: <IP da sua máquina>:8081
