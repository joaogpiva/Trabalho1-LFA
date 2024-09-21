# formato do labirinto (I = início, F = fim, * = obstáculo)
#  ----
# |*  F|
# |* * |
# |*   |
# |I * |
#  ----
# um estado pra cada posição => q03, q12, etc, mesmo esquema de matriz

# Configuração do autômato

estados = [
    'q00', 'q01', 'q02', 'q03',
    'q10', 'q11', 'q12', 'q13',
    'q20', 'q21', 'q22', 'q23',
    'q30', 'q31', 'q32', 'q33',
]

inicial = 'q30'

final = 'q03'

alfabeto = ['c', 'b', 'e', 'd'] # cima, baixo, esquerda, direita

transicoes = {
    ('q30', 'd'): 'q31',
    ('q31', 'e'): 'q30',
    ('q31', 'c'): 'q21',
    ('q21', 'b'): 'q31',
    ('q21', 'c'): 'q11',
    ('q21', 'd'): 'q22',
    ('q11', 'b'): 'q21',
    ('q11', 'c'): 'q01',
    ('q01', 'b'): 'q11',
    ('q01', 'd'): 'q02',
    ('q02', 'e'): 'q01',
    ('q02', 'd'): 'q03',
    ('q22', 'e'): 'q21',
    ('q22', 'd'): 'q23',
    ('q23', 'b'): 'q33',
    ('q23', 'c'): 'q13',
    ('q33', 'c'): 'q23',
    ('q13', 'b'): 'q23',
    ('q13', 'c'): 'q03',
}

# Execução

entrada = input("Digite a movimentação (d = direita, e = esquerda, c = cima, b = baixo): ")

estado_atual = inicial

for c in entrada:
    estado_atual = transicoes.get((estado_atual, c), estado_atual)

print(f'{entrada} foi aceita: {estado_atual == final}')