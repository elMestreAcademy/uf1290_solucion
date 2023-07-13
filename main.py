from datetime import datetime
from componente import Componente, Sistema

componentes  = [
    Componente("RAM", 1.0, datetime( 2019, 4, 12, 15, 36)),
    Componente("SSD", 3.14, datetime( 2023, 1, 3, 12, 48))
]

sist = Sistema("Principal")

for componente in componentes:
    sist.anyadir_componente(componente)

print(sist)
