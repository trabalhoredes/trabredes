# Apresentação 
Trabalho apresentado à disciplina de Laboratório de Redes do curso de Eng. Elétrica IFES Campus Guarapari, ministrada pelo Prof. Dr. Alexandre Pereira do Carmo.

# Alunos
  - João Vitor Alves Barradas
  - Peter Gleiser Garcez 

# Procedimentos

1) Caso você não tenha instalado o DockerHub, abra um terminal de comando e dê os comandos abaixo para instalá-lo (isso deve ser feito tanto na máquina monitor quanto na máquina host): 
    - sudo apt-get update
    - sudo apt-get remove docker-engine docker.io
    - sudo apt install docker.io

2) Crie uma pasta na máquina monitor e coloque dentro dela o arquivo config.txt contido na pasta "monitor" deste repositório. Você pode alterar à vontade os valores dos IPs presentes neste arquivo. 

3) Abra um terminal de comando dentro da pasta do passo 2 acima. Dê o comando abaixo para baixar e rodar o contêiner do programa monitor a partir do DockerHub (não esqueça de adicionar o IP da máquina host no campo assinalado <IP da máquina host>): 
    - sudo docker run --rm -it --network=host -v "$PWD:/app/config" trabalhoredes/trabalho python3 monitor.py <IP da máquina host> 8081

4) Na máquina host, crie uma pasta e abra um terminal de comando dentro desta. Dê o comando abaixo para baixar e rodar o contêiner servidor a partir do DockerHub:
    - sudo docker run --rm -it -p 8081:8081 -v "$(pwd):/app/www" trabalhoredes/servidor python3 server.py 8081

5) Após proceder o passo 4, um arquivo chamado "index.html" será criado automaticamente na pasta. Após se certificar de que este arquivo já consta na pasta, abra outro terminal de comando dentro da mesma pasta e dê o comando abaixo para rodar o contêiner do Apache e poder ver os resultados no navegador web: 
    - sudo docker run --rm -it --name my-apache-app -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4 

6) Abra um navegador web e digite: <IP da máquina host>:8080
