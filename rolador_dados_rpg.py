from random import randint


def rola_dado(dado):
    escolha = dado
    while len(escolha) > 1:
        print('O dado digitado é uma casa, tente novamente.')
        escolha = str(input('Digite a opção escolhida: '))
    while escolha not in '1 2 3 4 5 6':
        print('Você escolheu a opção', escolha)
        print('Opção inválida, tente novamente.')
        escolha = str(input('Digite a opção escolhida: '))

    if escolha == '1':
        sort = randint(1, 20)
        print(f'Você rolou {sort}')
        jogar_novamente()

    elif escolha == '2':
        sort = randint(1, 12)
        print(f'Você rolou {sort}')
        jogar_novamente()

    elif escolha == '3':
        sort = randint(1, 10)
        print(f'Você rolou {sort}')
        jogar_novamente()

    elif escolha == '4':
        sort = randint(1, 8)
        print(f'Você rolou {sort}')
        jogar_novamente()

    elif escolha == '5':
        sort = randint(1, 6)
        print(f'Você rolou {sort}')
        jogar_novamente()

    elif escolha == '6':
        sort = randint(1, 4)
        print(f'Você rolou {sort}')
        jogar_novamente()


def jogar_novamente():
    op = str(input('Deseja jogar outro dado? (S) Sim (N) Não: ')).strip().upper()
    while op not in 'N S':
        print('Opção inválida!')
        op = str(input('Deseja jogar outro dado? (S) Sim (N) Não: ')).strip().upper()
    if op == 'S':
        print('Escolha a opção abaixo para rolar o dado.')
        print('1 -> (d20) 2 -> (d12) 3 -> (d10) 4 -> (d8) 5 -> (d6) 6 -> (d4)')

        dado = str(input('Digite a opção escolhida: ')).strip()
        rola_dado(dado)

print('=' * 40)
print('         ROLADOR DE DADOS RPG')
print('=' * 40)

print('Escolha a opção abaixo para rolar o dado.')
print('1 -> (d20) 2 -> (d12) 3 -> (d10) 4 -> (d8) 5 -> (d6) 6 -> (d4)')

dado = str(input('Digite a opção escolhida: ')).strip()
rola_dado(dado)
