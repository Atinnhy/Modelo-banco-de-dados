from src.models import Employee
from src import Session

def create():

    first_name = input("Primeiro nome: ").strip().capitalize()
    last_name = input("Ultimo nome: ").strip().capitalize()
    age = int(input("Idade: ").strip())
    gender = input("Género (Male, Female ou Other): ").upper().strip()
    salary = int(input("Salário: ").strip())
    position_id = int(input("ID do trabalho: ").strip())

    with Session() as session:

        new_employee = Employee(
            first_name = first_name,
            last_name = last_name,
            age = age,
            gender = gender,
            salary = salary,
            position_id = position_id
        )

        session.add(new_employee)
        session.commit()
    
def read(parametro):
    with Session() as session:
        employee = session.query(Employee).filter_by(id=parametro).first()

        print(f"Empregado ID: {employee.id};") 
        print(f"Nome: {employee.first_name}, {employee.last_name}.")
        print(f"Idade: {employee.age}; Género: {employee.gender.value}; Salário: {employee.salary}; ID de trabalho: {employee.position_id}.")
        input("Aperte 'Enter' para continuar")

def update(parametro):
    with Session() as session:
        employee = session.query(Employee).filter_by(id=parametro).first()

        print("PARA NÃO ALTERAR OS DADOS, APERTE 'ENTER'.")
        first_name = input(f"Altere o primeiro nome {employee.first_name}: ").capitalize().strip()
        last_name = input(f"Altere o ultimo nome {employee.last_name}: ").capitalize().strip()
        age = input(f"Altere a idade, {employee.age} anos: ").strip()
        gender = input(f"Altere o genero {employee.gender.value}: ").strip().upper()
        salary = input(f"Altere o salário R${employee.salary}: ")
        position_id = input(f"Altere o ID da profissão {employee.position_id} para: ")

        if len(first_name) != 0:
            employee.first_name = first_name

        if len(first_name) != 0:
            employee.last_name = last_name
            
        if len(age) != 0:
            employee.age = age
            
        if len(gender) != 0:
            employee.gender = gender
            
        if len(salary) != 0:
            employee.salary = salary

        if len(position_id) != 0:
            employee.position_id = position_id
        
        if employee:
            session.commit()

def delete(parametro):
    with Session() as session:
        delete_employee = session.query(Employee).filter_by(id=parametro).first()

        if delete_employee:
            session.delete(delete_employee)
            session.commit()
            print(f"O empregado {delete_employee.first_name} de ID: {parametro} foi deletado.")
            input("Aperte 'Enter' para continuar")