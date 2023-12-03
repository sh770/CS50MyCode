def main():
    
    math_user_input = input("Expression: ")
    
    x, y, z = math_user_input.split(" ")
    
    x = float(x)
    z = float(z)
    
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z
    else:
        result = "y nam oper"        
        
    print(result)
    

main()