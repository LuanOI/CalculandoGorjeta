def calculo(ValorTotalConta,porcentagemGorjeta):
    Gorjeta = ValorTotalConta * (porcentagemGorjeta/100)
    total_com_Gorjeta = ValorTotalConta + Gorjeta
    return total_com_Gorjeta

ValorConta = float(input('Digite o valor da conta: '))
Porcentagem = float(input('Digite a porcentagem da gorjeta: '))

CalculoFinal = calculo(ValorConta,Porcentagem)

print(f'O total a pagr, incluindo a gorjeta, é: R${CalculoFinal:}')




