import datetime

ip_list = []

while True:
    ip = input("Digite um IP: ")

    if ip.lower() == "fim":
        break
    ip_list.append(ip)

agora = datetime.datetime.now()
data_hora_formatada = agora.strftime("%d_%m_%Y %H-%M-%S")

arquivo = open(f"{data_hora_formatada}.txt","w")
for ip in ip_list:
    print(ip)
    arquivo.write(f"{ip}\n")

arquivo.close()