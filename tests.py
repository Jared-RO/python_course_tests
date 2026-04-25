from __future__ import (
    annotations,
)

# para permitir referencias a clases que aún no han sido definidas sin usar ""
from typing import TypedDict, TypeVar, Generic, List, NamedTuple
from dataclasses import dataclass


class Person(TypedDict):
    name: str
    age: int


class Posicion(NamedTuple):
    x: float
    y: float
    z: float


class Employee(TypedDict):
    name: str
    age: int
    position: Posicion  # usamos la clase definida Point
    partners: List[
        "Employee"
    ]  # ponomos entre comillas "Employee" para indicar que es una referencia a la clase Employee


# podemos definir la instancia de esta manera
employee1: Employee = {
    "name": "Alice",
    "age": 28,
    "position": Posicion(x=1.0, y=2.0, z=3.0),
    "partners": [],
}

# pero también podemos definirla de esta otra manera, usando la sintaxis de clase
employee2 = Employee(
    name="Bob", age=35, position=Posicion(x=4.0, y=5.0, z=6.0), partners=[employee1]
)

# otra manera de crear clases es usando dataclass,
# que es una forma más sencilla de crear clases que solo contienen datos,
# sin necesidad de escribir métodos como __init__ o __repr__.
# La sintaxis es muy simple, solo hay que decorar la clase con @dataclass
# y definir los atributos con sus tipos.


@dataclass
class EmployeeDataClass:
    name: str
    age: int
    position: Posicion
    partners: List[EmployeeDataClass]


EmployeeDataClass1 = EmployeeDataClass(
    name="Charlie", age=30, position=Posicion(x=1.0, y=2.0, z=3.0), partners=[]
)

print(EmployeeDataClass1)


############ como usar GENERiCS

T = TypeVar("T")  # creamos un tipo genérico T


# que significa Generic[T]?= es una clase base que indica que la clase student
# es genérica y puede usar el tipo T como un parámetro de tipo.
@dataclass
class Student(
    Generic[T]
):  # hacemos que la clase student sea genérica, usando el tipo T
    name: str
    age: int
    position: Posicion
    partners: List[
        T
    ]  # usamos el tipo genérico T para definir el tipo de la lista de partners


class Animal: ...  # definimos una clase animal sin atributos ni métodos, solo para usarla como tipo genérico


jirafa = Animal()
tigre = Animal()  # creamos dos instancias de animal, una para jirafa y otra para tigre

therian = Student[
    Animal
](  # creamos una instancia de student usando el tipo animal como argumento para el tipo genérico T
    name="David",
    age=22,
    position=Posicion(x=1.0, y=2.0, z=3.0),
    partners=[
        jirafa,
        tigre,
    ],  # la lista de partners es una lista de objetos de tipo animal
)
print(therian)


############ como usar GENERiCS varios tipos

T1 = TypeVar("T1")  # creamos un tipo genérico T
T2 = TypeVar("T2")  # creamos un tipo genérico T


# que significa Generic[T]?= es una clase base que indica que la clase student
# es genérica y puede usar el tipo T como un parámetro de tipo.
@dataclass
class stud(
    Generic[T1, T2]
):  # hacemos que la clase student sea genérica, usando el tipo T
    name: str
    age: int
    position: Posicion
    partnerst1: List[
        T1
    ]  # usamos el tipo genérico T para definir el tipo de la lista de partners
    partnerst2: List[
        T2
    ]  # usamos el tipo genérico T para definir el tipo de la lista de partners


# creamos dos animales diferentes para usar como tipos genéricos
Gato = Animal()
Perro = Animal()  # creamos dos instancias de animal, una para jirafa y otra para tigre

# creamos dos personas diferentes para usar como tipos genéricos
Miguel = Person(name="Miguel", age=30)
Juan = Person(name="Juan", age=25)

semitherian = stud[
    Animal, Person
](  # creamos una instancia de student usando el tipo animal como argumento para el
    #   tipo genérico T
    name="David",
    age=22,
    position=Posicion(x=1.0, y=2.0, z=3.0),
    partnerst1=[
        Gato,
        Perro,
    ],  # la lista de partners es una lista de objetos de tipo animal
    partnerst2=[
        Miguel,
        Juan,
    ],  # la lista de partners es una lista de objetos de tipo Person
)
print(semitherian)


############ como usar GENERiCS con un tipo genérico que puede ser diferentes clases
# T = TypeVar(
#     "T", Animal, "objeto"
# )  # creamos un tipo genérico T que puede ser de tipo animal o de tipo Person


# @dataclass
# class objeto(Generic[T]):  # hacemos que la clase student sea genérica, usando el tipo T
#     name: str
#     age: int
#     position: Posicion
#     partners: List[
#         T
#     ]  # usamos el tipo genérico T para definir el tipo de la lista de partners


# unknown: objeto[objeto] = objeto(
#     # creamos una instancia de student usando el tipo animal como argumento
#     # para el tipo genérico T
#     name="David",
#     age=22,
#     position=Posicion(x=1.0, y=2.0, z=3.0),
#     partners=[objeto],  # la lista de partners es una lista de objetos de tipo animal
# )
# print(unknown)
