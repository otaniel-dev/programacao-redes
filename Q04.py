ip_list = []

while True:
    ip = input("Digite um IP: ")

    if ip.lower() == "fim":
        break
    ip_list.append(ip)

arquivo = open("ip.txt","w")
for ip in ip_list:
    print(ip)
    arquivo.write(f"{ip}\n")

arquivo.close()