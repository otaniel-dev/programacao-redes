octetos = input("Digite seu IP: ").split(".");

if octetos[0] == "192" and octetos[1] == "168" and octetos[2] == "1":
    print("O endereco pertence a rede 192.168.1.0/24");
else:
    print("O endereco nao pertence a rede 192.168.1.0/24");