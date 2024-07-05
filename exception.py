nome = input("Digite seu nome: ")

continuar = True
while (continuar == True):
    try:
        ano_nascimento = int(input("Digite seu ano de nascimento (Entre 1922 e 2021): "))
        if(ano_nascimento >= 1922 and ano_nascimento <= 2021):
            idade = 2022 - ano_nascimento
            print(f"\n{nome} completou ou completará {idade} em 2022\n")
            continuar = False
        else:
            print("Ano de nascimento inválido, por favor digite um ano entre 1922 e 2021")
    except:
        print('Valor do ano de nascimento precisa ser um número válido')