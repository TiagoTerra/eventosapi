# EventosApi

Serviço responsável para criação e manutenção de eventos: essa aplicação foi construída para ser consumida pelo [projeto eventosweb](https://github.com/TiagoTerra/eventosweb/tree/master).

# Pré-requisitos

Baixe e instale o [Python](https://www.python.org/downloads/)

Instalar os pacotes que a aplicação precisa (esses pacotes estão no arquivo [Requiements.txt](https://github.com/TiagoTerra/eventosapi/blob/master/Aplicacao/requirements.txt).
Execute em um prompt a instrução abaixo:
pip install -r requirements.txt

A aplicação usa o [sqlite](https://www.sqlite.org/download.html) como banco de dados: após instalação executar os passos:

1. Crie um banco com o nome que vc desejar;
2. Execute em um prompt ocomando abaixo para criar as tabelas da base de ddos e a carga básica de dados para  aplicação funcionar:
sqlite3 encontro (para acessar a base)
.read script.sql


# Execução

# Autores
Tiago Terra
