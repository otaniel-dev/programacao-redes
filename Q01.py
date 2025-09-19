conexao = int(input("Digite a velocidade de donwload em Mbps: "))

if conexao < 10:
    print("Conexão lenta!")
elif conexao >= 10 and conexao < 100:
    print("Conexão normal!")
elif conexao > 100:
    print("Conexão rápida")