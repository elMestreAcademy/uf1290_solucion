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

class Sistema:
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__componentes = []

    def anyadir_componente(self, componente: Componente) -> None:
        self.__componentes.append(componente)

    def obtener_componente(self) -> list:
        return self.__componentes

    def __str__(self) -> str:

        textlist = ""
        for componente in self.__componentes:
            textlist += f"\n  - {componente}"

        return f"{self.__nombre} {textlist}"
