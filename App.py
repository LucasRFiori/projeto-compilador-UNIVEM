arq = open("./src/txt.txt", mode="r", encoding="utf-8")
linhas = arq.readlines()
i = 0
for linha in linhas:

    i+=1
    print("linha {} {}".format(i, linha))

