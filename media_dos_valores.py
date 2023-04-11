def calc_media(lista_num):

    soma = sum(lista_num)
    media = soma / len(lista_num)

    return media

num = [100, 200, 300, 400, 500]
media = calc_media(num)

print(f"A média dos números acima {num} é: {media}")