from os import system

def limpar_tela():
    system("clear")

# Função Criar Evento, recebendo a referencia do dicionario evento
def criar_evento(evento):
    limpar_tela()
    print("Criar Evento")
    # Recebe o nome do evento a ser criado
    nome_evento = input("Informe o nome do evento: ")

    # Verifica se o nome do evento já consta no dicionario evento
    if nome_evento in evento:
        print(f"O Evento {nome_evento} já consta cadastrado.")
    else:
        # Caso negativo, coleta as outras informações e salva em variaveis locais
        data_evento = input("Data do Evento: (DD.MM.AAAA): ")
        descricao_evento = input("Breve Descrição do Evento: ")
        num_max_participantes = int(input("Número Máximo de Participantes: "))
        status_evento = input("Informe o status do evento (ABERTO / ADIADO / CANCELADO): ")
        
        # Iniciando com a mesma quantidade para vagas e numero maximo de participantes
        vagas_disponiveis = num_max_participantes
        
        # Gravando no dicionario evento, usando como chave, o nome do evento
        # As outras informacoes - valor do dicionario, juntadas através de uma lista.
        evento[nome_evento] = [data_evento, descricao_evento, num_max_participantes, vagas_disponiveis, status_evento]
    limpar_tela()

# Funcao atualizar evento, recebendo a referencia do dicionario evento como parametro
def atualizar_evento(evento):
    limpar_tela()
    print("Atualizar Evento")

    # Coleta o nome do evento a ser localizado
    nome_evento = input("Informe o nome do evento a ser atualizado: ")

    # Verifica se o nome informado, consta no dicionario evento
    if nome_evento in evento:
        print(f"O Evento {nome_evento} foi localizado.")
        print("1 - Atualizar Data do Evento")
        print("2 - Atualizar Descrição do Evento")
        print("3 - Atualizar Número Máximo de Participantes")
        print("4 - Atualizar Vagas Disponíveis")
        print("5 - Atualizar Status do Evento")
        
        # Variavel usada para receber a opcao listada acima
        opcao_atualizacao = int(input("Informe uma das opções acima: "))

        if opcao_atualizacao == 1:
            # Coleta a nova data e salva na variavel local data_evento
            data_evento = input("Informe a nova data do evento: (DD.MM.AAAA): ")

            # Associa a primeira posicao da lista (que é o valor do dicionario) o conteudo da variavel data_evento
            evento[nome_evento][0] = data_evento
            limpar_tela()
        elif opcao_atualizacao == 2:
            # Coleta a nova descricao do evento e grava na variavel local descricao_evento
            descricao_evento = input("Informe a nova descrição do evento: ")

            # Envia o conteudo de descricao_evento a segunda posicao da lista (que é o valor do dicionario evento)
            evento[nome_evento][1] = descricao_evento
            limpar_tela()
        elif opcao_atualizacao == 3:
            # Coleta o novo numero maximo de participantes
            num_max_participantes = int(input("Informe o número máximo de participantes: "))

            # Verifica se o que foi informado, é menor do que está informado nas vagas disponiveis
            if num_max_participantes < evento[nome_evento][3]:
                print("Número máximo de participantes não pode ser menor do que o numero de vagas disponíveis.")
                print(f"Número de vagas disponiveis: {evento[nome_evento][2]}")

                # Após exibir as mensagens acima, solicita novamente o numero maximo de participantes
                num_max_participantes = int(input("Informe o número máximo de participantes: "))

                # Grava o conteudo na terceira posicao da lista (que forma o valor do dicionario evento)
                evento[nome_evento][2] = num_max_participantes
                limpar_tela()
            else:
                # Se o numero maximo de participantes nao for menor do que o que foi informado nas vagas,
                # atualiza o valor na lista, no indice correspondente a esta informação, e chama a funcao limpar_tela
                evento[nome_evento][2] = num_max_participantes
                limpar_tela()
        elif opcao_atualizacao == 4:
            # Coleta o novo numero de vagas disponiveis
            vagas_disponiveis = int(input("Informe o número de vagas disponíveis: "))

            # Verifica se o numero de vagas disponiveis é maior do que está salvo na terceira posicao da lista
            # que é o numero maximo de participantes
            if vagas_disponiveis > evento[nome_evento][2]:
                print("Número de vagas disponíveis não pode ser maior do que o número máximo de participantes.")
                print(f"Número máximo de participantes: {evento[nome_evento][3]}.")

                # Caso positivo, exibe as mensagens acima e solicita novamente o numero de vagas disponiveis para o evento
                vagas_disponiveis = int(input("Informe o número de vagas disponíveis: "))

                # Atualiza na lista o indice correspondente as vagas disponiveis
                evento[nome_evento][2] = vagas_disponiveis
                limpar_tela()
            else:
                # Atualiza na lista o indice correspondente as vagas disponiveis
                evento[nome_evento][3] = vagas_disponiveis  
                limpar_tela()
        elif opcao_atualizacao == 5:
            # coleta o novo status do evento - para cancelar um evento, primeiro precisa passar aqui
            # para alterar para cancelado
            status_evento = input("Informe o status do evento(ABERTO / ADIADO / CANCELADO): ")

            # Envia o valor coletado para a posicao da lista respectiva a esta informacao
            evento[nome_evento][4] = status_evento
        
        # Entra neste bloco, caso tenha informado uma opcao nao prevista nas decisoes acima
        else:
            print("Opção Inválida. Tente Novamente.\n")
    
    # Entra neste bloco, caso não consiga localizar o evento informado.
    else:
        print(f"Evento {nome_evento} não foi localizado.\n")
    
# Função visualizar_evento recebendo a referencia do dicionario evento como parametro        
def coordenador_visualizar_evento(evento):
    limpar_tela()
    print("Coordenador - Visualizar Eventos Disponíveis")

    # Usando o metodo items, percorre a chave e o valor do dicionario recebido como parameto
    for key, value in evento.items():

        # Associa a cada uma das posicoes da lista que é o valor do dicionario, uma variavel local
        data_evento = value[0]
        descricao_evento = value[1]
        num_max_participantes = value[2]
        vagas_disponiveis = value[3]
        status_evento = value[4]

        # Saída das informações acessadas
        print(f"Evento: {key}.")
        print(f"Data do Evento: {data_evento}.")
        print(f"Descrição do Evento: {descricao_evento}.")
        print(f"Número Máximo de Participantes: {num_max_participantes}.")
        print(f"Vagas Disponíveis: {vagas_disponiveis}.")
        print(f"Status do Evento: {status_evento}.")
        print("\n")

# função visualizar_inscricao recebendo a referencia do dicionario inscricao_evento
def visualizar_inscricao(inscricao_evento):
    limpar_tela()
    print("Visualizar Inscrição")

    # Para visualizar as inscricoes, foi necessario aninhar estas duas repeticoes
    # A primeira, irá percorrer a chave principal, que é o evento informado na hora da inscrição
    for key, value in inscricao_evento.items():
        print(f"Evento: {key}.")

        # Esta repeticao interna, percorre a lista que recebeu duas informaçoes na inscricao
        # o aluno, e o curso
        for inscricoes in value:
            print(f"Aluno: {inscricoes[0]}.")
            print(f"Curso: {inscricoes[1]}.")
        print("\n")

# excluir_eventos, recebendo os dois dicionarios como parametro
def excluir_eventos(evento, inscricao_evento):
    limpar_tela()
    print("Excluir Eventos Cancelados")
    nome_evento = input("Informe o nome do evento a ser excluído: ")

    # Apos coletar o nome do evento a ser excluido, verifica se o mesmo existe no dicionario evento
    if nome_evento in evento:    
        # Verifica o status do evento a ser excluido
        if evento[nome_evento][4] == "cancelado" or evento[nome_evento][4] == "CANCELADO":
            print(f"Excluindo o evento {nome_evento}.\n")
            # Remove o evento informado, bem como as inscricoes relativas ao mesmo evento
            del evento[nome_evento]
            del inscricao_evento[nome_evento]
        
        # Entra neste bloco caso o status nao esteja como cancelado
        else:
            print(f"Status do Evento {nome_evento} não consta como CANCELADO.\n")
    
    # Vem para este bloco se nao localizar o evento
    else:
        print(f"Evento {nome_evento} não localizado.\n")   
    

