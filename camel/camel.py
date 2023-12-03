def main():
    camelCase = input("camelCase: ")
    string = add_underscore(camelCase)
    print(string)

def add_underscore(s):
    result = []
    for char in s:
        if char.isupper():
            result.append('_')
        result.append(char.lower())
    return ''.join(result)  

main()
