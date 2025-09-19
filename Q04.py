ip_list = []

while True:
    ip = input("Digite um IP: ")

    if ip.lower() == "fim":
        break
    ip_list.append(ip)