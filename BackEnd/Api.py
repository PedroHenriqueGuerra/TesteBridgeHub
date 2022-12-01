import os

import api as api
from flask import request, app, Flask
from flask_restful import Resource, abort, Api

import BancoDeDados
import ValidarDados
app = Flask(__name__)
api = Api(app)

#Endpoint para adicionar o usuario
class Adicionar_Usuario(Resource):
    def post(self):
        nome = ValidarDados.validar_nome(request.json['nome'])
        email = ValidarDados.validar_email(request.json['email'])
        telefone = ValidarDados.valida_telefone(request.json['telefone'])

        if (nome == True) and (email== True ) and (telefone==True):
            BancoDeDados.add_usuario(request.json['nome'],request.json['email'], request.json['telefone'])

        else:
            abort(404, message='Os dados foram passados na formataçao errada, mande novamente')

        return {"message": "Usuario adicionado"}

#Endpoint para editar os dados do usuario
class Editar_Usuario(Resource):
    def post(self,id):
            nome = ValidarDados.validar_nome(request.json['nome'])
            email = ValidarDados.validar_email(request.json['email'])
            telefone = ValidarDados.valida_telefone(request.json['telefone'])

            if (nome == True) and (email == True) and (telefone == True):
                BancoDeDados.atulizar_usuario(request.json['nome'],id,1)
                BancoDeDados.atulizar_usuario(request.json['email'], id, 2)
                BancoDeDados.atulizar_usuario(request.json['telefone'], id, 3)

            else:
                abort(404, message='Os dados foram passados na formataçao errada, mande novamente')

            return {"message": "Usuario atualizado"}

#Endpoint para deletar o usuario
class Deletar_usuario(Resource):
    def delete(self,id):
        try:
            mensagem=BancoDeDados.deletar_usuario(id)
            return mensagem
        except:
            abort(404, message='Usuario não deletado, verifique se o id é existente')

#Endpoint para consultar todos os dados do banco de dados
class Consultar_todos_usuarios(Resource):
    def get(self):
        try:
            todos_usuarios = BancoDeDados.consultar_todos_usuarios()
            return todos_usuarios
        except:
            abort(404, message='Ocorreu um erro')

#Endpoint para consultar os dados de determinado usuario
class Consultar_usuario_especifico(Resource):
    def get(self,id):
        try:
            usuario = BancoDeDados.consultar_usuario_id(id)
            if usuario is None:
                return {"message": "Usuario não existente"}
            else:
                return usuario
        except:
            abort(404, message='Ocorreu um erro')


api.add_resource(Adicionar_Usuario, "/bridge/add_user")
api.add_resource(Editar_Usuario, "/bridge/edit_user/<int:id>")
api.add_resource(Deletar_usuario, "/bridge/delete_user/<int:id>")
api.add_resource(Consultar_todos_usuarios, "/bridge/users")
api.add_resource(Consultar_usuario_especifico, "/bridge/users/<int:id>")

create_db = not os.path.isfile('Bridge.db')
if create_db:
    BancoDeDados.criar_BD()
if __name__ == "__main__":
    app.run(debug=True)