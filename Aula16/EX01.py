def coelho(pes, cabecas):
   coelhos = (pes - (2 * cabecas)) / 2

   return coelhos


def pato(pes,cabecas):
   patos = (-pes + (4 * cabecas)) / 2

   return patos


cabecas = 33
pes = 49

total_coelhos = coelho(pes, cabecas)
total_patos = pato(pes, cabecas)

print(f'Tem {int(pato(pes, cabecas))} patos')
print(f'Tem {int(coelho(pes, cabecas))} coelhos')
