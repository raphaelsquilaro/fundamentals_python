#2️⃣ A loja VESTE BEM criou um sistema de fidelidade aos seus clientes, caso o cliente seja cadastrado na loja o mesmo tem 5% de descoto em qualquer compra independente da forma de pagamento, se o cliente não for cadastrado e pagar em dinheiro ou pix terá 3% de desconto, se for no crédito não tem desconto nenhum.

nome = input('Digite o nome do cliente: ')
cadastro = input('O cliente é cadastrado na loja? (s/n): ').lower()
forma_pagamento = input('Digite a forma de pagamento (dinheiro/pix/credito): ').lower()
preco = float(input('Digite o valor da compra: R$ '))
if cadastro == 's':
    print(f'O cliente {nome} tem direito a 5% de desconto por ser cadastrado na loja.')
    preco = preco - (preco * 0.05)
elif cadastro == 'n' and forma_pagamento in ['dinheiro', 'pix']:
    print(f'O cliente {nome} tem direito a 3% de desconto por pagar em {forma_pagamento}.')
    preco = preco - (preco * 0.03)
elif cadastro == 'n' and forma_pagamento == 'credito':
    print(f'O cliente {nome} não tem direito a desconto por pagar no crédito.')
else:
    print(f'O cliente {nome} tem uma situação indefinida com cadastro "{cadastro}" e forma de pagamento "{forma_pagamento}".')