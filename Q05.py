porta = input("Digite a porta: ")

if porta == "80":
    print("Porta HTTP aberta!")
elif porta == "443":
    print("Porta HTTPS aberta!")
elif porta == "21":
    print("Porta FTP aberta!")
elif porta == "22":
    print("Porta SSH aberta!")
else:
    print("Porta fechada!")