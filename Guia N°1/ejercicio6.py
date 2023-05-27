hora = 0
minuto = 0
segundo = 0
while hora < 24:
    while minuto < 60:
        while segundo < 60:
            print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
            segundo += 1
        segundo = 0
        minuto += 1
    minuto = 0
    hora += 1
