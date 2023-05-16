input_name = input("Введіть імя ").title().strip(' 0123456789')
input_second_name = input("Введіть прізвище ").upper().strip(' 0123456789')
quantity = len(input_name)
hello = "Здарова"
end = '?'
template = f'{hello},  {input_name}  {input_second_name}  а ти знав, що твоє імя складється з {quantity} літер{end}'

print(template)
