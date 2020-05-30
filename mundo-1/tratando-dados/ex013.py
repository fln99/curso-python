employee_salary = float(input('Seu salario = '))

w_increase_sal = employee_salary + (employee_salary * 0.15)

print('Seu salario era de R${} reais.'.format(employee_salary))
print('Voce recebeu um aumento de 15%! Seu novo salario', end=" >>> ")
print(w_increase_sal)