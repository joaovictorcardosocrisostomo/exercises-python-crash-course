"""Meu projeto final. Agora que encerrei o ciclo básico de lógica de programação (capítulo 9 do livro que fala sobre classes e POO) eu me sinto apto a finalizar um programa básico. O programa já foi escrito sem utilizar do paradigma de orientação a objetos. Agora, usando uma lógica semelhante, eu irei refatorar o código e criar esse projeto seguindo o paradigma."""

"""para fins de estudo, eu vou fazer uma segunda versão com overengineering destrinchando cada comportamento em um método específico da classe (treinamento para separar bem funções em programas complexos). como eu pretendo fazer: o programa main vai chamar um objeto da classe 'Question' que recebe a dificuldade desejada, decide um número aleatório e chama a pergunta correspondente do banco de perguntas(levando em a dificuldade selecionada em consideração), além de exibir a pergunta e os itens na tela. o objeto também recebe a resposta correta e compara a resposta do usuário. os métodos serão get_question(seleciona, puxa e printa pergunta e itens), compare_answer(recebe a resposta do user, recebe a resposta correta, compara e notifica). a outra classe é a 'Menu' que vai ser responsável por iniciar o jogo, setar a dificuldade e enviar para a classe pergunta, informar como encerrar o programa a qualquer momento e perguntar se o usuário quer continuar. os métodos serão start(inicia o jogo e informa como encerrar), set_difficult(seleciona qual lista deve ser selecionada) e keep_going(pergunta se o usuário deseja prosseguir e informa quantas perguntas ainda tem). a última classe é a 'Score' que registra e exibe o número de pontos a cada nova pergunta e ao encerrar. métodos: increment_score(acrescenta a cada acerto), show_score(mostra o número de pontos a cada questão e quando encerrar)."""
from random import randint
import banco_questoes

class Menu():
    def __init__(self):
        self.difficulty = 'n'

    def set_difficulty(self):
        self.difficulty = input("Selecione a dificuldade: (f)ácil (n)ormal"
                          " (d)ifícil (a)leatória\n")
        
    def start(self):
        lista_perguntas = []
        pergunta_atual = []
        if self.difficulty == 'f':
            lista_perguntas = banco_questoes.perguntas_faceis
            pergunta_atual = lista_perguntas[randint(0,20)]
        elif self.difficulty == 'n':
            lista_perguntas = banco_questoes.perguntas_intermediarias
            pergunta_atual = lista_perguntas[randint(0,20)]
        elif self.difficulty == 'd':
            lista_perguntas = banco_questoes.perguntas_avancadas
            pergunta_atual = lista_perguntas[randint(0,20)]
        elif self.difficulty == 'a':
            lista_perguntas.extend(banco_questoes.perguntas_faceis)
            lista_perguntas.extend(banco_questoes.perguntas_intermediarias)
            lista_perguntas.extend(banco_questoes.perguntas_avancadas)
            pergunta_atual = lista_perguntas[randint(0,60)]
            
        
        current_question = Pergunta(pergunta_atual['pergunta'], pergunta_atual['resposta'],
                                   pergunta_atual['a'], pergunta_atual['b'],
                                   pergunta_atual['c'], pergunta_atual['d'])
        current_question.get_question()
        current_question.check_answer(input("Digite aqui: "))
        
class Pergunta():
    def __init__(self, pergunta, resposta, a, b, c, d):
        self.pergunta = pergunta
        self.resposta = resposta
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_question(self):
        print(f"{self.pergunta}\na) {self.a}\nb) {self.b}\nc) {self.c}\nd) {self.d}")
    
    def check_answer(self, user_answer):
        if user_answer == self.resposta:
            print("Resposta correta!")
        else:
            print("Resposta incorreta.")

game_quiz = Menu()
game_quiz.set_difficulty()
print()
while True:
    game_quiz.start()
    continuar = input("\nContinuar: (s)im (n)ão\n")
    if continuar == 's':
        continue
    elif continuar == 'n':
        print("Até logo!")
        break

            
