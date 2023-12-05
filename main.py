from time import sleep

import src.crud_employee as crud_e
import src.crud_position as crud_p

while True:
    print("O que você deseja fazer?")
    sleep(1)
    opcoes = int(input("""
    1. Adicionar funcionário;
    2. Procurar funcionário;
    3. Atualizar funcionarios;
    4. Deletar funcionário;
    ------------------------------
    5. Adicionar cargo;
    6. Procurar cargo;
    7. Atualizar cargo;
    8. Deletar cargo;
    ------------------------------
    0. Encerrar o programa.
    """))
    
    # Funcionarios
    if opcoes == 1:
        crud_e.create()

    elif opcoes == 2:
        id = int(input("Insira o ID do funcionário desejado para encontralo: "))
        crud_e.read(id)

    elif opcoes == 3:
        id = int(input("Insira o ID do funcionário desejado para atualizar seus dados:"))
        crud_e.update(id)

    elif opcoes == 4:
        id = int(input("Insira o ID do funcionário desejado para exclui-lo: "))
        crud_e.delete(id)

    # Cargos
    if opcoes == 5:
        crud_p.create()
        
    elif opcoes == 6:
        id = int(input("Insira o ID do cargo desejado para encontralo: "))
        crud_p.read(id)

    elif opcoes == 7:
        id = int(input("Insira o ID do cargo desejado para atualizar seus dados: "))
        crud_p.update(id)
    
    elif opcoes == 8:
        id = int(input("Insira o ID do cargo desejado para exclui-lo: "))
        crud_p. delete(id)

    elif opcoes == 0:
        break