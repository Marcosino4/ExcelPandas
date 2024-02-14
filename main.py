import pandas as pd
import json
from datetime import date
from openpyxl import Workbook

def load_employees_data(file_path):
    with open(file_path) as employeesJson:
        employees_data = json.load(employeesJson)
    return employees_data

def filter_employees(employees_data, project_name):
    valid_employees = []
    for employee in employees_data:
        if employee['proyect'] != project_name:
            valid_employees.append(employee)
    return valid_employees

def process_employees_salaries(employees):
    for employee in employees:
        rm_dot = employee['salary'][1:].replace(',', '').strip('$')
        salary_str = rm_dot.replace(',', '.')
        employee['salary'] = f"{float(salary_str) * 1.10:.2f}€"

def save_dataframe_to_excel(df, excel_name):
    with pd.ExcelWriter(excel_name, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

if __name__ == "__main__":
    employees_data = load_employees_data("employees.json")
    valid_employees = filter_employees(employees_data, "GRONK")
    process_employees_salaries(valid_employees)
    df = pd.DataFrame(valid_employees)
    hoy = date.today()
    fecha = f"{hoy.day}-{hoy.month}-{hoy.year}"
    excel_name = f"pagos-empleados-{fecha}.xlsx"
    save_dataframe_to_excel(df, excel_name)