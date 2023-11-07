def converte_hora_seg(h,m,s):
    segundos = h*3600
    segundos += m*60
    segundos += s
    return segundos


segundos = 0
m=100
s=100
h = int(input("digite a hora: "))
while m > 60:
    m = int(input("digite os minutos: "))
while s >60:
    s = int(input("digite os segundos: "))

print(converte_hora_seg(h,m,s))
