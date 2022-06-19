def welcome():
    print('''
    Bem vindo a calculadora
    ''')
welcome()

def calculate():
    operation = input('''
+ para adição
- para subtração 
* para multiplicação
/ para divisão
** para potencia
% para porcentagem
Por favor, selecione a operação matemática que deseja concluir:
''')


    number_1 = int(input('Insira o seu primeiro numero: '))
    number_2 = int(input('Insira o seu segundo numero: '))

# adição
    if operation == '+':
        print('{} + {} ='.format(number_1, number_2))
        print(number_1 + number_2)

# subtração
    elif operation == '-':
        print('{} - {} ='.format(number_1, number_2))
        print(number_1 + number_2)

# Multiplicação
    elif operation == '*':
        print('{} * {} ='.format(number_1, number_2))
        print(number_1 + number_2)

# divisão
    elif operation == '/':
        print('{} / {} ='.format(number_1, number_2))
        print(number_1 + number_2)
# para porcentagem
    elif operation == '%':
        print('{} % {} ='.format(number_1, number_2))
        print(number_1 + number_2)

    else:
        print('voçe digitou uma operação errada, por favor reinicie o programa.')

    again()

def again():
    # recebe entrada do usuario:
    calc_again = input('''
    Deseja calcular novamente?
    Por favor digite Y para sim ou N, para não continuar.
    ''')

    # se o usuário digitar Y, execute a função calculate().
    if calc_again.upper() == 'Y':
        calculate()

    # se o usuário digitar N, execute essa função:
    elif calc_again.upper() == 'N':
        print('até mais')

    # se o usário digitar outra chave, execute a função novamente.
    else:
        again()


calculate()
