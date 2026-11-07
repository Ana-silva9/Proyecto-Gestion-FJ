# -*- coding: utf-8 -*-
"""
Clase abstracta EntidadBase y Clase Cliente
Curso: Programación 213023 - Fase 4
"""

from abc import ABC, abstractmethod
from gestor_logs import GestorLogs
from excepciones import DatoInvalidoError

log = GestorLogs()

class EntidadBase(ABC):
    """Clase abstracta: estructura común para todas las entidades"""
    @abstractmethod
    def __str__(self):
        pass

class Cliente(EntidadBase):
    """Clase que representa a un cliente con encapsulación"""
    def __init__(self, id_cliente, nombre, correo, telefono):
        # Validaciones estrictas
        if not id_cliente or len(id_cliente.strip()) < 3:
            raise DatoInvalidoError("ID inválido: mínimo 3 caracteres")
        if "@" not in correo or "." not in correo:
            raise DatoInvalidoError(f"Correo inválido: {correo}")
        if not telefono.isdigit() or len(telefono) < 7:
            raise DatoInvalidoError("Teléfono inválido: solo números, mínimo 7 dígitos")

        # Atributos privados (encapsulación)
        self.__id = id_cliente.strip()
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

        log.info(f"Cliente registrado: {self.__nombre} (ID: {self.__id})")

    @property
    def id(self): return self.__id
    @property
    def nombre(self): return self.__nombre
    @property
    def correo(self): return self.__correo
    @property
    def telefono(self): return self.__telefono

    def __str__(self):
        return f"Cliente: {self.nombre} | ID: {self.id} | Correo: {self.correo}"
