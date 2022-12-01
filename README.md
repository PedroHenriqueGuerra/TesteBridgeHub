# TesteBridgeHub

## 👤Desenvolvedor

| Nome                                              | GitHub                                           
| ------------------------------------------------- | --------------------------------------------------------|      
| Pedro Henrique                                    | [Pedro Henrique](https://github.com/PedroHenriqueGuerra)  

## Sobre o projeto
Backend - Desenvolver uma Api para realizar o CRUD de um usuário.

Frontend - Desenvolver um site/plataforma para o usuário conseguir realizar investimentos.

## Tecnologias

## Backend:
-Python

-SQLite

-Flask

##Frontend:

-ReactJS

## Instruções para utilização do projeto.

## BACKEND: 

Após a inicialização dos códigos do backend, você precisarar utilizar o prgrama Insomnia.

## Endpoints:

## Adicionar Usuário:

- http://127.0.0.1:5000/bridge/add_user

- Json = {
            "nome":"",
            "email":"",
            "telefone":""
	      }

## Consultar todos os usuários cadastrados:

- http://127.0.0.1:5000/bridge/users

## Consultar dados de um usuário a partir do seu id:

- id = id do usuário disponivel no banco de dados

- http://127.0.0.1:5000/bridge/users/id

## Editar dados do usuário:

- id = id do usuário disponivel no banco de dados

- http://127.0.0.1:5000/bridge/edit_user/id

- Json = {
            "nome":"",
            "email":"",
            "telefone":""
	      }

## Deletar usuário:

- id = id do usuário disponivel no banco de dados

- http://127.0.0.1:5000/bridgehub/delete_user/id



## FRONTEND
Depois de realizar o download do projeto, abra o cmd no arquivo do projeto e digite o comando "npm start".

Em seguida é só utilizar a  plataforma.

