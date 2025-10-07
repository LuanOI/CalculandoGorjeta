def usuario(CPF):
    
    if CPF.isdigit() and len(CPF) ==11:
        print(f'CPF Válido: {CPF}')
        return True
    else:
        print('CPF Inválido')    
        return False
DigiteCPF = (input('Digite seu CPF: '))

usuario(DigiteCPF)    

