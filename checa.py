import os

def verificar_arquivo_quiz(arquivo):
    try:
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            for num_linha, linha in enumerate(linhas, start=1):
                partes = linha.strip().split('; ')
                if len(partes) != 2 or partes[1].upper() not in {'V', 'F'}:
                #if len(partes) != 2 or partes[1] not in {'V', 'F'}:
                    print(f"Erro na linha {num_linha}: {linha.strip()}")
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")

# Exemplo de uso:

os.system("clear")
arquivo = 'quiz.dat'
verificar_arquivo_quiz(arquivo)