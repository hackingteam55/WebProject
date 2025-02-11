var_string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."

print(f'String-ul initial este: {var_string}')

new_string = var_string[4:14]

print(new_string)

new_var = var_string.replace("Inquisitor", "Conquistador")

print(f'Prima formatare: {new_var}')

new_string_2 = var_string[25:31]

print(new_string_2)

new_var_2 = new_var.replace("Varric", "King")

print(f'A doua formatare: {new_var_2}')

new_string_3 = var_string[42:49]

print(new_string_3)

new_var_3 = new_var_2.replace("Skyhold", "Palace")

print(f'String-ul final este: {new_var_3}')
