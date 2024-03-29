import os, datetime, random, socket

# Função para limpar a tela do terminal
def limpar_tela():
    os.system('clear')

def linha():
    print('-' * 80)

def print_limitado(texto, limite):
    partes = [texto[i:i+limite] for i in range(0, len(texto), limite)]
    for parte in partes:
        print(parte)

def print_centralizado(palavra):
    largura_terminal = os.get_terminal_size().columns
    print(palavra.center(largura_terminal))

def data_hora():
    # Obtém a data e hora atual
    agora = datetime.datetime.now()
    # Formata a data e hora para imprimir
    data_completa = agora.strftime("%A, %d de %B de %Y - %H:%M:%S")
    # Imprime a data e hora completa
    print("  DATA E HORA: ", data_completa)

def mostra_host_ip():
    # Obtém o hostname do sistema
    hostname = socket.gethostname()
    # Obtém o endereço IP do sistema
    endereco_ip = socket.gethostbyname(hostname)
    numero = contar_linhas_arquivo("quiz.dat")
    print("  HOSTNAME:", hostname + ' | ' + "IP: ", endereco_ip + " | ")
    #' | Banco: ' + str(numero) + ' questões'


def aguarde():
    input('  Pressione ENTER para prosseguir...')

def contato():
    limpar_tela()
    mostrar_time()

def como_funciona():
    limpar_tela()
    hello()
    abrir_arquivo("comofunciona.txt")
    aguarde()

def chama_chat():
    limpar_tela()
    hello()
    abrir_arquivo("chatola.txt")
    aguarde()

def contar_linhas_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            num_linhas = sum(1 for linha in arquivo)
        return num_linhas
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {e}"
    
def totalizar_pontos(nome_arquivo):
    # Dicionário para armazenar os pontos de cada usuário
    pontos_por_usuario = {}

    # Abrir o arquivo texto
    with open(nome_arquivo, 'r') as arquivo:
        # Ler cada linha do arquivo
        for linha in arquivo:
            # Dividir a linha em nome e pontos
            nome, pontos_str = linha.strip().split(';')
            pontos = int(pontos_str)

            # Adicionar os pontos ao total do usuário
            if nome in pontos_por_usuario:
                pontos_por_usuario[nome] += pontos
            else:
                pontos_por_usuario[nome] = pontos

    # Ordenar o dicionário por valor (pontos) em ordem decrescente
    pontos_por_usuario_ordenados = dict(sorted(pontos_por_usuario.items(), key=lambda item: item[1], reverse=True))

    # Retornar o dicionário com os totais de pontos ordenados
    return pontos_por_usuario_ordenados

def hello():
    print('')
    #os.system('figlet ....SIMULA CETAM')
    os.system("cat head")  
    #print('')
    print('                    CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
    print('')
    print('             😊' + ' ALEGRIA 1.0 - SIMULADOR DE QUESTÕES SOBRE TECNOLOGIA')  
    print('                       by: prof. Marcelo Fournier & time')
    print("")
    linha()
    data_hora()
    mostra_host_ip()
    
# Função para carregar as questões do arquivo
def carregar_questoes(nome_arquivo):
    questoes = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                questao, resposta = linha.strip().split('; ')
                questoes.append((questao, resposta))
    except FileNotFoundError:
        print("Arquivo de questões não encontrado.")
    return questoes

def selecionar_questoes(arquivo, quantidade):
    # Lista para armazenar as questões selecionadas
    questoes_selecionadas = []

    # Abre o arquivo e lê todas as linhas
    contador = 0
    with open(arquivo, 'r') as f:
        contador = contador +1
        linhas = f.readlines()
        
    # Embaralha as linhas para seleção aleatória
    random.shuffle(linhas)

    # Itera sobre as linhas para selecionar as questões
    for linha in linhas:
        # Divide a linha em pergunta e resposta
        pergunta, resposta = linha.strip().split('; ')
        print(pergunta, resposta)
        # Verifica se a resposta é 'V' (verdadeira) ou 'F' (falsa)
        if resposta == 'V':
            questoes_selecionadas.append((pergunta, "V"))
        elif resposta == 'F':
            questoes_selecionadas.append((pergunta, "F"))

        # Se já foram selecionadas a quantidade desejada de questões, sai do loop
        if len(questoes_selecionadas) == quantidade:
            break

    return questoes_selecionadas


def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        return conteudo
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except IOError as e:
        print(f"Ocorreu um erro de entrada/saída ao abrir o arquivo '{nome_arquivo}':", e)
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o arquivo '{nome_arquivo}':", e)
        return None

def mostrar_time():
    abrir_arquivo("time.txt")

def registrar_pontuacao(nickname, pontuacao, nome_arquivo):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f"{nickname};{pontuacao}\n")

def mostrar_ranking(nome_arquivo):
    # Abrir o arquivo e ler as pontuações
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Criar uma lista de tuplas (nickname, pontuação) a partir das linhas lidas
    resultados = []
    for linhaX in linhas:
        nickname, pontuacao = linhaX.strip().split(';')
        resultados.append((nickname, int(pontuacao)))

    # Ordenar os resultados com base na pontuação (em ordem decrescente)
    resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)

    # Mostrar os melhores resultados na tela
    limpar_tela()
    hello()
    linha()
    print("  MELHORES RESULTADOS:")
    linha()
    for i, (nickname, pontuacao) in enumerate(resultados_ordenados, start=1):
        print('  ' + f"{i}. {nickname}: {pontuacao}")

    linha()


def mostrar_xps(arquivo):
    resultados = totalizar_pontos(arquivo)
    limpar_tela()
    hello()
    linha()
    print('  XP POR USUÁRIO  | ARQUIVO: ' + arquivo )
    linha()
    for nome, pontos in resultados.items():
        print('  ' + f'{nome}: {pontos} pontos')


    print("")
    

def listar_arquivos_dat(extensao):
    # Lista de arquivos com extensão .dat
    arquivos_dat = [arquivo for arquivo in os.listdir() if arquivo.endswith(extensao)]
    #arquivos_dat.remove("ranking.dat")
    
    # Imprime os arquivos numerados
    for i, arquivo in enumerate(arquivos_dat, 1):
        print("  " + f"{i}. {' ==> ' + arquivo}")

    # Verifica se há arquivos .dat no diretório
    if not arquivos_dat:
        print("  Não há arquivos com a extensão " + extensao + " neste diretório.")
        return None

    # Menu de seleção
    while True:
        try:
            print("")
            linha()
            opcao = int(input("  Digite o número do arquivo que deseja selecionar: "))
            if opcao == 0:
                return None
            elif 0 < opcao <= len(arquivos_dat):
                return arquivos_dat[opcao - 1]
            else:
                print("  Opção inválida. Digite um número válido.")
        except ValueError:
            print("  Opção inválida. Digite um número.")


# Função para iniciar o quiz
def iniciar_quiz(questoes, arquivo_questoes, arquivo_ranking):
    limpar_tela()
    pontuacao = 0
    questao_numero = 0
    questoes_erradas = []
    questoes_puladas = []
    
    for questao, resposta in questoes:
        hello()
        linha()
        print('')
        #numero = questao_numero(arquivo_questoes)
        numero = contar_linhas_arquivo(arquivo_questoes)
        print('  Banco: ' + str(numero) + ' questões')
        print("")
        print('  ATENÇÃO: ')
        print('    Cada resposta CERTA  você GANHA 1 ponto')
        print('    Cada resposta ERRADA você PERDE 1 ponto')
        print('    Cada questão pulada você nem ganha nem perde ponto')
        print('')
        #texto = "  PERGUNTA ==> " + questao + " : " +  resposta
        questao_numero += 1
        texto = "  PERGUNTA " + str(questao_numero) +  " ==> " + questao

        print_limitado(texto, 88)
        print('')
        print('  RESPOSTA: ')
        print('  [V] verdadeiro | [F] Falso | [P] Pular | [S] Sair | ')
        #print('  RESPOSTA: ')

        resposta_usuario = input("  =======>: ").upper()        
        print('')

        if resposta_usuario == resposta:
                print("  Resposta correta!")
                pontuacao += 1

        elif resposta_usuario == "P":
                print("  Você pulou esta questão.")
                questoes_puladas.append(questao)
                aguarde()

        elif resposta_usuario == "S":
                print("  Você selecionou S para sair.")
                aguarde()
                limpar_tela()
                break

        else:
                print("  Resposta incorreta.")
                pontuacao -= 1
                questoes_erradas.append(questao)

        print('  RESUMO PARCIAL: ')
        linha()
        print("  Pontuação: {}/{}".format(pontuacao, len(questoes)))
        aguarde()
        limpar_tela()

    hello()
    linha()
    print('')
    print("  RESUMO TOTAL:")
    linha()
    print('  Você concluiu o simulado. Verifique abaixo um resumo do resultado obtido.')
    print('')

    if len(questoes_puladas) == 0:
        print('  Você não pulou nenhuma questão.')
        print('')
    else: 
        print('  Você pulou as seguintes questões:')
        for texto in questoes_puladas:
            print('  ' + texto)

        print('')

    if len(questoes_erradas) != 0: 
        print('  Você errou as seguintes questões:')
        for string in questoes_erradas:
            print('  ' + string)

        print('')

    else: 
        print('  Você não errou nenhuma questão!')

    print('')
    print("  Pontuação: {}/{}".format(pontuacao, len(questoes)))
    print('')
    linha()
    resposta = input("  Deseja registrar sua pontuação? (S/N): ")
    if resposta.lower() == 's':
        nickname = input("  Por favor, informe seu nickname: ")
        #pontuacao = int(input("  Agora, informe sua pontuação: "))
        registrar_pontuacao(nickname, pontuacao, arquivo_ranking)
        mostrar_ranking(arquivo_ranking)
        print("  Pontuação registrada com sucesso!")
    else:
        print("  Pontuação não registrada.")
    

# Função principal
def main():
    while True:
        limpar_tela()
        linha()
        hello()
        linha()
        print("  MENU DE OPÇÕES:")
        linha()
        print("  1. COMO FUNCIONA")
        print("  2. RESPONDER SIMULADO")
        print("  3. IRC CHAT")
        print("  4. RANKING DE PONTOS")
        print("  5. RANKING DE XP")
        print("  6. TIME DO PROJETO")
        print("  0. SAIR")
        linha();       
        opcao = input("  SELECIONE A OPÇÃO DESEJADA ==> : ")

        if opcao == "1":
            como_funciona()
            input("  Pressione Enter para continuar...")
        elif opcao == "2":
            limpar_tela()
            hello()
            print("")
            linha()
            print("")
            print("  O SISTEMA PERMITE QUE VOCÊ TENHA VÁRIOS ARQUIVOS DE QUESTÕES")
            print("  CADA ARQUIVO DE QUESTÕES TEM SEU PRÓPRIO RANKING DE PONTOS")
            print("")
            print("  SELECIONE ABAIXO O ARQUIVO DE QUESTÕES DESEJADO")
            print("")
            arquivo_questoes = listar_arquivos_dat(".dat")
            #print("  Arquivo de questões: " + arquivo_questoes)
            arquivo_ranking = "ranking_" + arquivo_questoes + ".rkg"
            questoes = selecionar_questoes(arquivo_questoes, 30)
            #print("  Arquivo de ranking: " + arquivo_ranking)          
            iniciar_quiz(questoes, arquivo_questoes, arquivo_ranking)
            print("")
            linha()
            input("  Pressione Enter para continuar...")
        
        elif opcao == "3":
            chama_chat()
            input("  Pressione Enter para continuar...")
            os.system('irssi')
            aguarde()
        
        elif opcao == "4":
            limpar_tela()
            hello()
            linha()
            print("")
            print("  VISUALIZANDO O RANKING DE PONTOS")
            print("")
            arquivo_ranking = listar_arquivos_dat(".rkg")
            mostrar_ranking(arquivo_ranking)
            input("  Pressione Enter para continuar...")

        elif opcao == "5":
            limpar_tela()
            hello()
            linha()
            print("")
            print("VISUALIZANDO O RANKING DE PONTOS")
            print("")
            arquivo_ranking = listar_arquivos_dat(".rkg")
            mostrar_xps(arquivo_ranking)
            input("  Pressione Enter para continuar...")
        
        elif opcao == "6":
            limpar_tela()
            mostrar_time()
            input("  Pressione Enter para continuar...")

        elif opcao == "0":
            limpar_tela()
            print("  Saindo do programa...")
            hello()
            contato()
            break
        else:
            print("  Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

