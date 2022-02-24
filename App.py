file = open("./src/txt.txt", mode="r", encoding="utf-8")
tokens = ["if","showthis","else", "=", 
"==", "*", "/", "%", "!=", "int", "float", 
"string", "boolean", "else if", "{", "}",
"(",")", "[","]", "for", "while", ";", ">", "<"]
chartocompare = []
lines = file.readlines()
i = 0
for line in lines:
    i += 1
    for character in line:
        chartocompare.append(character)
        concatenation = "".join(chartocompare)
        if character == "\n":
            chartocompare.clear()
        if character in tokens:
            chartocompare.clear()
            print(character)
        if concatenation in tokens:
            chartocompare.clear()
            print(concatenation)
    # print("")
    # print("linha {} {}".format(i, line))
    # print("")
