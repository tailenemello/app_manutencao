from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import csv
import os
from datetime import datetime

def carregar_solicitacoes():
solicitacoes = []
if os.path.exists(ARQUIVO):
with open(
ARQUIVO, "r", newline="", encoding="utf-8"
) as arquivo:
leitor = csv.DictReader(arquivo)
solicitacoes.extend(leitor)
return solicitacoes

def salvar_solicitacoes(solicitacoes):
with open(
ARQUIVO, "w", newline="", encoding="utf-8"
) as arquivo:
escritor = csv.DictWriter(
arquivo, fieldnames=CAMPOS
)
escritor.writeheader()
escritor.writerows(solicitacoes)

def gerar_novo_id(solicitacoes):
ids = []
for solicitacao in solicitacoes:
try:
ids.append(
int(solicitacao["id"])
)
except (ValueError, KeyError):
pass
return str( max(ids, default=0) + 1 )
