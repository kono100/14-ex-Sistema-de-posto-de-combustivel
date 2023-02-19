

'''. Um motorista deseja colocar no seu tanque X reais de gasolina. Faça uma função que receba 
por parâmetros o preço do litro da gasolina e o valor do pagamento. Retorne quantos litros 
ele conseguiu colocar no tanque. '''



valor = float(input('Quantos reais de gasolina o senhor deseja colocar? '))
preco_gasolina = 5.25
litro_total = valor/preco_gasolina
print(f'Você conseguira encher um total de {litro_total:.2f} litros')
