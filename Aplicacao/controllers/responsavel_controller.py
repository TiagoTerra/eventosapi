# from flask_openapi3 import OpenAPI, Info, Tag
# from flask import Blueprint, jsonify, request
# from schemas import ResponsavelSchema
# from model import Session
# import logging
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

# responsavel_bp = Blueprint('responsavel', __name__)
# responavel_tag = Tag(name="Responsável", description="Verbos referente a responsável")

# class ResponsavelController():
#     #paramos aqui:
#     # vamos tentar mais um dia apenas com controller, na verdade nao tempos tempo para isso
#     # vamos desistir da controller evamos dividir dentro do app.py por quanto de risco de projeto
#     # isso vai ficar pro final
#     @responsavel_bp.route('/responsavel', methods=['POST'], tags=[responavel_tag])
#     def add_responsavel(form: ResponsavelSchema):
#         """Adiciona um novo Responsavel à base de dados
#         Retorna uma representação dos responsavels e comentários associados.
#         """    
#         responsavel = Responsavel(
#             nome=form.nome,
#             cpf=form.cpf,
#             email=form.email,
#             matricula=form.matricula)
        
#         logging.debug(f"Adicionando responsavel de nome: '{responsavel.nome}'")
#         try:
#             # criando conexão com a base
#             session = Session()
#             # adicionando responsavel
#             session.add(responsavel)
#             # efetivando o comando de adição de novo item na tabela
#             session.commit()
#             logging.debug(f"Adicionado responsavel de nome: '{responsavel.nome}'")
#             return 200
#             # return apresenta_responsavel(responsavel), 200
#         except IntegrityError as e:
#             # como a duplicidade do nome é a provável razão do IntegrityError
#             logging.warning(e)
#             error_msg = "Responsavel de mesmo nome já salvo na base :/"
#             logging.warning(f"Erro ao adicionar responsavel '{responsavel.nome}', {error_msg}")
#             return {"mesage": error_msg}, 409
#         except Exception as e:
#             # caso um erro fora do previsto
#             error_msg = "Não foi possível salvar novo item :/"
#             logging.warning(f"Erro ao adicionar responsavel '{responsavel.nome}', {error_msg}")
#             return {"mesage": error_msg}, 400