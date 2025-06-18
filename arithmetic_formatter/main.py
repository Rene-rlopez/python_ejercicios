

def add_operation(problem_list, num1, num2, operator):
    problem_list.append({'num1': num1, 'num2': num2, 'operator': operator})

def print_problems(problem_list, show_answer):

    if show_answer == False:
        for problem in problem_list:
            length = max(len(problem['num1']), len(problem['num2'])) + 2
            print(f"{problem['num1']:>{length}}")
            print(f"{problem['operator']}{problem['num2']:>{length - 1}}")
            print(f"-" * length)
            print()
    else:
        for problem in problem_list:
            length = max(len(problem['num1']), len(problem['num2'])) + 2
            print(f"{problem['num1']:>{length}}")
            print(f"{problem['operator']}{problem['num2']:>{length - 1}}")
            print(f"-" * length)
            # se realiza el calculo de requerido segun sea la operacion
            number1 = int(problem['num1'])
            number2 = int(problem['num2'])
            if problem['operator'] == '+':
                total = number1 + number2
                print(f'{total:>{length}}\n')
            elif problem['operator'] == '-':
                total = number1 - number2
                print(f'{total:>{length}}\n')

def rules(problem_list, show_answer):
    if len(problem_list) > 5:
        print('Error: Too many problems.')
        return
    for problem in problem_list:
        if problem['operator'] == '*' or problem['operator'] == '/':
            print("Error: Operator must be '+' or '-'.")
            return
        elif not problem['num1'].isdigit() or not problem['num2'].isdigit():
            print('Error: Numbers must only contain digits.')
            return
        elif len(problem['num1']) > 4 or len(problem['num2']) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return
    print_problems(problem_list, show_answer)

def is_operator(char):
    operators = {'+', '-', '*', '/'}
    return char in operators

def assign_elements(problems, problem_list):
    #Separamos los elementos de la operacion en diferentes variables para agregarlos dentro de un diccionario
    current_number = ''
    for digit in problems:
        if digit.isdigit():
            current_number += digit
        elif is_operator(digit):
            num1 = current_number
            current_number = ''
            operator = digit
        elif digit.isspace():
            continue
    if current_number != '':
        num2 = current_number
    add_operation(problem_list, num1, num2, operator)
    return problem_list


def arithmetic_arranger(problems, show_answers=True):
    problem_list = []
    for problem in problems:
        assign_elements(problem, problem_list)
    return rules(problem_list, show_answers)

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "3801 - 2"])}')