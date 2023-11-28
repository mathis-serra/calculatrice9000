#L'exercise a était fait a la demande de l'énoncé, étant donné le fait qu'il faut priorisé les paranthèse et les multiplication et additions 
#cependant la consigne ne demande que deux nombre et une opération, donc aucunement besoin de priorisé les opérations,




historique = []

def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Error: Modulo by zero"
    else:
        return "Error: Invalid operator"
    
    historique.append(f"{num1} {operator} {num2} = {result}")
    
    return result
    
print(calcule(5, '/', 3))
print(calcule(5, '+', 3))
print(calcule(5, '-', 3))
print(calcule(5, '*', 3))
print(calcule(5, '%', 3))

print("Historique des calculs:")
for entry in historique:
    print(entry)
