"""3️⃣ Desafio adicional: A empresa BOLOS DE POTE  precisa investir em novos recursos para melhorar seus produto e precisa de R$ 20.000,00 para realizar as melhorias necessárias, o proprietário foi a um banco para fazer um empréstimo e precisa saber se vale a pena fazer esse empréstimo, para tanto precisa de um sistema que faça o cálculo de quanto vai pagar de juros e se atende as necessidades da empresa, não pode pagar mais de 10% do valor do empréstimo, dados abaixo:

Valor do empréstimo: R$ 20.000,00

Taxa de juros do banco: Juros Compostos de 1,25% ao mês

Quantidade de meses que deseja parcelar

Empréstimo está aprovado se o valor do juros for menor ou igual a 10% do valor do emprestimo"""

valor_emprestimo = 20000.00
taxa_juros_mensal = 0.0125
quantidade_meses = int(input('Digite a quantidade de meses para parcelar o empréstimo: '))
valor_total_juros = valor_emprestimo * ((1 + taxa_juros_mensal) ** quantidade_meses - 1)
valor_total_a_pagar = valor_emprestimo + valor_total_juros
if valor_total_juros <= valor_emprestimo * 0.10:
    print(f'O empréstimo está aprovado. Valor total a pagar: R$ {valor_total_a_pagar:.2f} (Juros: R$ {valor_total_juros:.2f})')
else:
    print(f'O empréstimo não está aprovado. Valor total a pagar: R$ {valor_total_a_pagar:.2f} (Juros: R$ {valor_total_juros:.2f})')