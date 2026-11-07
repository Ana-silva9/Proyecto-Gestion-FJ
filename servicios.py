# -*- coding: utf-8 -*-
"""
Clase abstracta ServicioBase y 3 servicios derivados
Demuestra herencia y polimorfismo
Curso: Programación 213023 - Fase 4
"""

from abc import ABC, abstractmethod
from gestor_logs import GestorLogs
from excepciones import DatoInvalidoError

log = GestorLogs()

class ServicioBase(ABC):
    """Clase abstracta para todos los servicios"""
    def __init__(self, codigo, nombre, descripcion, precio_base):
        if precio_base < 0:
            raise DatoInvalidoError("El precio no puede ser negativo")
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):
        """Cálculo polimórfico de costo"""
        pass

    @abstractmethod
    def describir(self):
        """Devuelve información del servicio"""
        pass

class ReservaSala(ServicioBase):
    """Servicio: Reserva de salas"""
    def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):
        costo = self.precio_base * duracion
        costo += costo * impuesto
        costo -= costo * descuento
        return round(costo, 2)

    def describir(self):
        return f"🏠 {self.nombre} — {self.descripcion} | Precio/hora: ${self.precio_base:,}"

class AlquilerEquipo(ServicioBase):
    """Servicio: Alquiler de equipos"""
    def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):
        costo = self.precio_base * duracion * 0.95
        costo += costo * impuesto
        costo -= costo * descuento
        return round(costo, 2)

    def describir(self):
        return f"💻 {self.nombre} — {self.descripcion} | Precio/día: ${self.precio_base:,}"

class AsesoriaEspecializada(ServicioBase):
    """Servicio: Asesoría profesional"""
    def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):
        costo = self.precio_base * duracion
        if duracion > 3:
            costo *= 1.10
        costo += costo * impuesto
        costo -= costo * descuento
        return round(costo, 2)

    def describir(self):
        return f"🎓 {self.nombre} — {self.descripcion} | Precio/hora: ${self.precio_base:,}"
