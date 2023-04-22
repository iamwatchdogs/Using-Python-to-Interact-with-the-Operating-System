#!/usr/bin/env python3
import os
import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    file_path = os.path.expanduser(csv_file_location)  # expand tilde to home directory path
    employee_file = csv.DictReader(open(file_path), dialect='empDialect')
    employee_list = []
    for data in employee_file:
      employee_list.append(data)
    return employee_list

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
      department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
      department_data[department_name] = department_list.count(department_name)
    return department_data

def write_report(dictionary, report_file):
    report_file_path = os.path.expanduser(report_file)
    with open(report_file_path, "w") as f:
      for k in sorted(dictionary):
        f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

employee_list = read_employees('~/data/employees.csv')
print(employee_list)

print()

dictionary = process_data(employee_list)
print(dictionary)

print()

write_report(dictionary, '~/test_report.txt')
