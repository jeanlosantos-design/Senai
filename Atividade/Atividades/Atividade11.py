dias = int(input())

anos = dias // 360
dias = dias % 360
meses = dias // 30
dias = dias % 30

print(anos, "anos,", meses, "meses,", dias, "dias")