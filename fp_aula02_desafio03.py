#Author: Raphael Campos Squilaro

#3️⃣ Desafio adicional: A hamburgueria LANCHÃO TOP tem 4 motoboys que realizam as entregas aos clientes, cada motoboy recebe um valor padrão para fazer as entregas, quanto mais entregas, mais eles ganham, os valores pagos tem relação com a distância, a empresa paga R$ 1,00 por km para cada motoboy.

distancia_km = float(input('Digite a distância percorrida em km: '))
valor_pago = distancia_km * 1.00
print(f'O valor pago para o motoboy é: R$ {valor_pago:.2f} por {distancia_km:.2f} km percorridos.')
