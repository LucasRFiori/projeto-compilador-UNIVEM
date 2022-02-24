arq = open("./src/txt.txt", mode="r", encoding="utf-8")
tokens=["if","showthis","else", "=", "==", "*", "/", "%", "!=", "int", "float", "string", "boolean", "else if", "{", "}",
"(",")", "[","]", "for", "while", ";"]

linhas = arq.readlines()
i = 0
for linha in linhas:
    i+=1
    for token in linha:
        if token in tokens:
            print(token)

    print("linha {} {}".format(i, linha))
    print("")
