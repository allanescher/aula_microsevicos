# aula_microsevicos - Comandos para Ubuntu 

##Sempre atualizar o ubuntu
sudo apt-get update

##Instalar Git 
```sudo apt update```
```sudo apt install git```

##Abra o terminal e execute os seguintes comandos (cuide para responder S para as perguntas durante a instalação):

```sudo apt update```  
```sudo apt upgrade```  
```sudo apt install apt-transport-https ca-certificates curl software-properties-common```  
```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```  
```sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"```  
```sudo apt update```  
```sudo apt-cache policy docker-ce```  
```sudo apt install docker-ce```  
```sudo systemctl status docker```  
```sudo apt install docker```  
```sudo apt install docker-compose```  
  

##Logo em seguida, adicione as permissões para executar o docker, digitando no terminal:  
```sudo groupadd docker```  
```sudo usermod -aG docker $USER```  


##Reinicie o computador para aplicar as alterações, e em seguida execute o docker.  
```sudo systemctl enable docker```

##Instalando o Intellij 
```sudo snap install intellij-idea-community --classic```

##Comando Git para destivar SSL no push 
```git -c http.sslVerify=false push origin main```

##Comando Git para destivar SSL no clone 
```git -c http.sslVerify=false clone <http do projeto>```
