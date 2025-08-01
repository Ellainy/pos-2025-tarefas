import requests
from getpass import getpass
from tabulate import tabulate

api_url = "https://suap.ifrn.edu.br/api/"


user = input("Digite a matrícula do aluno: ")
password = getpass("Digite a senha: ")

aluno = {"username": user, "password": password}

response = requests.post(api_url + "v2/autenticacao/token/", json=aluno)
token = response.json()["access"]

headers = {
    "Authorization": f'Bearer {token}'
}

ano = input("Digite o ano do boletim que deseja vizualizar: ")
response = requests.get(f"https://suap.ifrn.edu.br/api/edu/meu-boletim/{ano}/1/", headers=headers)

if response.status_code != 200:
    print("Erro ao buscar o boletim.")
    print("Detalhes:", response.text)
    exit()

boletim = response.json()


tabela = []

for disciplina in boletim:
    nome = disciplina.get("disciplina", "—")
    nota_1 = disciplina.get("nota_etapa_1", {}).get("nota", "—")
    nota_2 = disciplina.get("nota_etapa_2", {}).get("nota", "—")
    nota_3 = disciplina.get("nota_etapa_3", {}).get("nota", "—")
    nota_4 = disciplina.get("nota_etapa_4", {}).get("nota", "—")
    media = disciplina.get("media_final_disciplina", "—")
    

    tabela.append([nome, nota_1, nota_2, nota_3, nota_4, media])

# Cabeçalho
cabecalho = ["Disciplina", "Nota 1", "Nota 2", "Nota 3", "Nota 4", "Média"]

print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))
