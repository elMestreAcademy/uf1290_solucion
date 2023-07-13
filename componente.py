from datetime import datetime

class Componente:
    def __init__(self, nombre: str, version: float, fecha_creacion: datetime) -> None:
        self.__nombre = nombre
        self.__version = version
        self.__fecha_creacion = fecha_creacion

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        self.__nombre = value

    @property
    def version(self) -> float:
        return self.__version

    @version.setter
    def version(self, version: float):
        self.__version = version

    @property
    def fecha_creacion(self) -> datetime:
        return self.__fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, fecha_creacion: datetime):
        self.__fecha_creacion = fecha_creacion

    def __str__(self):
        return f"{self.nombre}({self.version}) - {self.fecha_creacion}"

if __name__ == "__main__":
    componentes  = [
        Componente("RAM", 1.0, datetime( 2019, 4, 12, 15, 36)),
        Componente("SSD", 3.14, datetime( 2023, 1, 3, 12, 48))
    ]

    for componente in componentes:
        print(componente)
