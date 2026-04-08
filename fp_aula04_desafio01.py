"""1️⃣ A escola IANES fez uma reestruturação em seu sistema de aprovação de alunos, agora para ser aprovado o aluno precisa atender aos requisitos abaixo:

Aprovação vai depender de nota e presença:

Presença ≥75% - Aprovado
Presença<75% - Reprovado

Nota ≤5 - Aluno Reprovado;
Nota >5 e <7  - Aluno em recuperação
Nota ≥7 - Aluno Aprovado"""


nome = input('Digite o nome do aluno: ')
nota = float(input('Digite a nota do aluno: '))
presenca = float(input('Digite a porcentagem de presença do aluno: '))

if presenca >= 75 and nota >= 7:
    print(f'O aluno {nome} está aprovado com nota {nota:.2f} e presença de {presenca:.2f}%.')
elif presenca >= 75 and 5 < nota < 7:
    print(f'O aluno {nome} está em recuperação com nota {nota:.2f} e presença de {presenca:.2f}%.')
elif presenca >= 75 and nota <= 5:
    print(f'O aluno {nome} está reprovado com nota {nota:.2f} e presença de {presenca:.2f}%.')
elif presenca < 75:
    print(f'O aluno {nome} está reprovado por falta com presença de {presenca:.2f}%.')
else:
    print(f'O aluno {nome} tem uma situação indefinida com nota {nota:.2f} e presença de {presenca:.2f}%.')
