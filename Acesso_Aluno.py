from os import system

def limpar_tela():
    system("clear")

# Funcao inscrever_evento, recebendo as referencias dos dois dicionarios declarados
def inscrever_evento(evento, inscricao_evento):
    limpar_tela()
    print("Inscricão Em Evento")
    nome_aluno = input("Informe o nome do aluno: ")
    nome_curso = input("Informe o nome do curso: ")
    nome_evento = input("Informe o nome do evento para se inscrever: ")

    # Após coletar as informacoes acima, verifica se o evento existe no dicionario
    if nome_evento in evento:
        # Cria a variavel local para a informacao relativa as vagas disponiveis do evento informado acima
        vagas_disponiveis = evento[nome_evento][3]

        # Verifica se tem vagas disponiveis
        if vagas_disponiveis > 0:

            # Cria a lista nova_inscricao com as variaveis locais nome_aluno e nome_curso
            nova_inscricao = [nome_aluno, nome_curso]

            # Atualiza as vagas disponiveis apos esta nova inscricao
            evento[nome_evento][3] = evento[nome_evento][3]-1

            # Verifica se já tem inscricoes realizadas com o evento informado
            # É importante porque o nome do evento, é usado como chave do dicionario inscricao_evento
            # nao podendo ser repetida, se não, tem seu conteudo sobreescrito
            if nome_evento in inscricao_evento:
               
               # Caso já tenha uma inscricao no evento informado, cria-se uma nova lista com o conteudo de nova_inscricao
               inscricao_evento[nome_evento].append(nova_inscricao)

               # mensagem de confirmacao da inscrição
               print(f"Aluno {nome_aluno}. Sua inscriçao no evento {nome_evento} foi efetivada.\n")
            else:
                # caso negativo, cria-se a lista como valor do dicionario inscricao_evento, tendo o evento, como chave
                inscricao_evento[nome_evento] = [nova_inscricao]
                print(f"Aluno {nome_aluno}. Sua inscriçao no evento {nome_evento} foi efetivada.\n")
        
        # Entra neste bloco, caso nao tenha vagas disponiveis, ou seja, o campo retornando, 0.
        else:
            print(f"Evento {nome_evento} não tem vagas disponíveis.\n")
    
    # Vem para este bloco caso o evento informado nao seja localizado
    else:
        print(f"Evento {nome_evento} não foi localizado.\n")

# Funcao visualizar_evento
def aluno_visualizar_evento(evento):
    limpar_tela()
    print("Aluno - Visualizar Eventos Disponíveis")

    # percorre o dicionario evento, usando o metodo items, dentro do for
    for key, value in evento.items():

        # Associa a cada uma das posicoes da lista que compoe o valor do dicionario evento
        data_evento = value[0]
        descricao_evento = value[1]
        num_max_participantes = value[2]
        vagas_disponiveis = value[3]
        status_evento = value[4]

        # Saída das variaveis locais
        print(f"Evento: {key}.")
        print(f"Data do Evento: {data_evento}.")
        print(f"Descrição do Evento: {descricao_evento}.")
        print(f"Número de participantes: {num_max_participantes}")
        print(f"Vagas Disponíveis: {vagas_disponiveis}.")
        print(f"Status do Evento: {status_evento}.")
        print("\n")
