import Acesso_Aluno, Acesso_Coordenador
from os import system

# Declarando os dicionários a serem usados para receber os dados 
evento = {}
inscricao_evento = {}


def limpar_tela():
    system("clear")

# Função Menu Principal
def menu_principal():
    limpar_tela()
    # Varíavel local usada para controlar a estrutura da repetição abaixo.
    opcao_menu_principal = 0
    while opcao_menu_principal <= 3:
        print("UniFECAF - Gestão de Eventos")
        print("1 - Acesso Coordenação")
        print("2 - Acesso Alunos")
        print("3 - Sair do Sistema")
        opcao_menu_principal = int(input("Informar o perfil de acesso (1 / 2): "))
        # Após coletar a opcao dada pelo usuário, direciona para um menu específico, ou sai do laco e finaliza o programa
        if opcao_menu_principal == 1:
            # Chama o menu da coordenacao
            menu_coordenacao()     
        elif opcao_menu_principal == 2:
            # Chama o menu do aluno
            menu_aluno()
        elif opcao_menu_principal == 3:
            # Exibe mensagem de saída, interrompe o laço de repetição e finaliza o programa
            print("Finalizando sistema...")
            break
        else:
            print("Opção Inválida. Finalizando sistema... ")
            break
       
        

def menu_coordenacao():
    limpar_tela()
    # Repetição para exibir o menu da coordenação
    while True:
        print("Acesso Coordenador")
        print("1 - Criar Evento")
        print("2 - Atualizar Evento")
        print("3 - Visualizar Eventos Disponíveis")
        print("4 - Visualizar Inscricões Em Eventos")
        print("5 - Excluir Eventos")
        print("6 - Menu Principal")
        opcao_coordenador = int(input("Selecione uma das opções acima (1 a 6): "))

        # Após coletar a opcao dada pelo usuário, faz o direcionamento para cada funcao em específico
        # Dependendo da função a ser chamada, é enviada como parametro a referencia, de um, ou 
        # dos dois dicionarios declarados acima.
        if opcao_coordenador == 1:
            Acesso_Coordenador.criar_evento(evento)
        elif opcao_coordenador == 2:
            Acesso_Coordenador.atualizar_evento(evento)
        elif opcao_coordenador == 3: 
            Acesso_Coordenador.coordenador_visualizar_evento(evento)
        elif opcao_coordenador == 4:
            Acesso_Coordenador.visualizar_inscricao(inscricao_evento)
        elif opcao_coordenador == 5:
            Acesso_Coordenador.excluir_eventos(evento, inscricao_evento)
        elif opcao_coordenador == 6:
            limpar_tela()
            # Return, usado para voltar ao menu principal
            # Uso da recursão, acabou criando uma nova instancia do menu principal
            # o que prejudicava o pleno funcionamento do programa
            return
        
            
def menu_aluno():
    limpar_tela()
    # Repetição para exibir o menu do aluno
    while True:
        print("Acesso Aluno")
        print("1 - Inscrever-se Em Evento")
        print("2 - Visualizar Eventos Disponíveis")
        print("3 - Menu Principal")
        opcao_aluno = int(input("Selecione uma das opções acima (1 a 3): "))

        # Após coletar a opcao do usuario, chama a funcão em específico, enviando 
        # a referencia dos dicionarios declarados acima
        if opcao_aluno == 1:
            Acesso_Aluno.inscrever_evento(evento, inscricao_evento)
        elif opcao_aluno == 2:
            Acesso_Aluno.aluno_visualizar_evento(evento)
        elif opcao_aluno == 3:
            limpar_tela()
            return
        
# Chamada inicial                    
menu_principal()