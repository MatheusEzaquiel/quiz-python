# Quiz em Python

# Imports
import os
clear = lambda: os.system('cls')

import time

# Perguntas
pergunta = [
    
    [
        "Quanto é '1' + '1' ?",
        "3", 
        "11",
        "9",
        "2",
        "b"
    ],

    [
        "Qual das seguintes linguagens é considerada a linguagem mãe das linguagens de programação modernas?",
        "Python",
        "Flash",
        "Java",
        "C",
        "d"
    ],

    [
        "Qual destes bancos de dados segue o modelo relacional?",
        "MongoDB",
        "Amazon DynamoDB",
        "Hbase",
        "Postgre",
        "d"
    ],

    [
        "Qual linguagem é uma linguagem exclusiva do front-end?",
        "JavaScript",
        "SQL",
        "Flash",
        "Java",
        "c"
    ],

    [
        "Qual das alternativas é uma linguagem de programação?",
        "React.js",
        "Rust",
        "React.js",
        "Portugol",
        "b"
    ],

    [
        "Na linguagem Java, qual dessas opções não é uma palavra reservada?",
        "real",
        "class",
        "public",
        "int",
        "a"
    ]

]


# Função que executa o jogo
def comecarJogo():
    
    clear()
    time.sleep(2)

    pts = 0
    i = 0
        
    #INÍCIO DE JOGO
    print("=====================")
    print("     QUIZ MB")
    print("=====================")

    time.sleep(1)
    clear()

    for x in pergunta:
        
        print("Pergunta: ", x[0])
        print("a)", x[1])
        print("b)", x[2])
        print("c)", x[3])
        print("d)", x[4])

        res = input("Resposta: ")

        if res == pergunta[i][5]:

            print("[\u2713] Resposta correta! (+1 ponto)")
            pts += 1

        else:
            print("[\u0078] Resposta incorreta")

        i += 1

        #Delay na execução de 2 segundos
        time.sleep(1.5)
        clear()

    #FIM DE JOGO
    print("=====================")
    print("     FIM DE JOGO ")
    print("=====================")
    print("Total de pontos: ", pts)
    print("=====================")

   

# 1 - INICIAR JOGO
comecarJogo()

# 2 - REINICIAR JOGO
jogar = input("Reiniciar jogo? [s] ou [n]")

while jogar == 's':

    comecarJogo()

    jogar = input("Reiniciar jogo? [s] ou [n] ")

    if jogar == 'n':
        print("Obrigado por ter jogado!")