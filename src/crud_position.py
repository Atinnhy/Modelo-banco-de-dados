from src.models import Position
from src import Session

def create():
    
    position_name = input("Nome da posição: ").strip().capitalize()
    position_description = input("Descrição do cargo: ").strip().capitalize()
    position_workload = input("Carga horária: ").strip()

    with Session() as session:

        new_position = Position(
            position_name = position_name,
            position_description = position_description,
            position_workload = position_workload
        )

        session.add(new_position)
        session.commit()

def read(parametro):
    with Session() as session:
        position = session.query(Position).filter_by(position_id=parametro).first()

        print(f"ID do cargo: {position.position_id};")
        print(f"Nome do cargo: {position.position_name};")
        print(f"Descrição da posição: {position.position_description};")
        print(f"Carga horária: {position.position_workload}.")
        input("Aperte 'Enter' para continuar")

def update(parametro):
    with Session() as session:
        position = session.query(Position).filter_by(position_id=parametro).first()

        print("PARA NÃO ALTERAR OS DADOS, APERTE 'ENTER'.")
        position_name = input(f"Altere o nome do cargo {position.position_name}: ").capitalize().strip()
        position_description = input(f"Altere a descrição do cargo atualmente:'{position.position_description}'\nAltere para: ").strip()
        position_workload = input(f"Altere a carga horaria do trabalho, atualmente de {position.position_workload} para: ")

        if len(position_name) != 0:
            position.position_name = position_name
        
        if len(position_description) != 0:
            position.position_description == position_description
        
        if len(position_workload) != 0:
            position.position_workload = position_workload

        if position:
            session.commit()

def delete(parametro):
    with Session() as session:
        delete_position = session.query(Position).filter_by(position_id=parametro).first()

        if delete_position:
            session.delete(delete_position)
            session.commit()
            print(f"O cargo {delete_position.position_name} de ID: {parametro} foi deletado.")
            input("Aperte 'Enter' para continuar")