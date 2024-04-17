from typing import Optional, List
from model.entidades import Participante
from pydantic import BaseModel
from datetime import datetime

class SearchParticipanteSchema(BaseModel):
    eventoId: int = 1 

class ParticipanteSchema(BaseModel):
    """ Define um novo participante a ser inserido na base
    """
    nome: str = "Jonh Doe"
    email: str = "jondoe@email.com"
    cpf: str = "11122233344"
    inscricao: str = "00000001"
    centrosdeinteresse: List[int] = [1, 2, 3]
    idevento: int = 1

class ParticipanteViewSchema(BaseModel):
    """ Define o participante retornado
    """
    nome: str = "Jonh Doe"
    email: str = "jondoe@email.com"
    cpf: str = "11122233344"
    inscricao: str = "00000001"
    id: int = 1

class ListagemParticipantesSchema(BaseModel):
    """ Define como uma listagem de participantes será retornada.
    """
    participantes:List[ParticipanteViewSchema]

def mapeaentidade_paraschemaparticipantes(participantes: List[Participante]):
    """ Mapea uma lista de entidade Participante para lista de ParticipantesSchema

    Retorna uma lista de ParticipantesSchema
    """
    result = []
    for participante in participantes:
        result.append({
            "nome": participante.nome,
            "inscricao": participante.inscricao,
            "email": participante.email,
            "id": participante.id
        })

    return {"participantes": result}

def mapeaentidade_paraschemaparticipante(participante: List[Participante]):
    """ Mapea uma entidade Participante para ParticipanteSchema

    Retorna uma lista de ParticipantesSchema
    """
    return {
        "nome": participante.nome,
        "id" :participante.id
    }