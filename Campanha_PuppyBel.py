print('Campanha de Vacinação - PuppyBel!')

pets_vacinados = 0
continuar = 's'

while continuar == 's':
    especie = input('Qual a espécie do seu pet? ').lower().strip()
    if especie in ["cachorro", "cao", "canis", "gato", "felino"]:
        nome = input(f'Qual o nome do seu {especie}? ').title().strip()
        pets_vacinados += 1
        print(f'Espécie: {especie}, Nome: {nome}, Número: {pets_vacinados}')

        for i in range(1, 4):
            print(f'Vacina <{i}> - OK.')

        print(f'{nome} foi vacinado(a) com sucesso!')
    else:
        print(f"Desculpe, a campanha de vacinação não atende {especie}.")

    opcao = input("Há mais animais na fila para vacinar? (s/n) ").lower().strip()
    if opcao == "s":
        continuar = opcao
    else:
      continuar = 'n'

print(f'A campanha foi finalizada.\nTotal de animais vacinados: {pets_vacinados}')