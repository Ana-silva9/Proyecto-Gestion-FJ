# -*- coding: utf-8 -*-
"""
Clase Reserva: integra cliente, servicio y manejo de estados
Curso: Programación 213023 - Fase 4
"""

from gestor_logs import GestorLogs
from excepciones import ReservaInvalidaError, EstadoInvalidoError

log = GestorLogs()

class Reserva:
    """Clase que gestiona una reserva con confirmación y cancelación"""
    ESTADOS_PERMITIDOS = {"PENDIENTE", "CONFIRMADA", "CANCELADA", "COMPLETADA"}

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.__estado = "PENDIENTE"
        log.info(f"Reserva creada: {cliente.nombre} → {servicio.nombre}")

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):
        """Confirmar reserva con manejo completo de excepciones"""
        try:
            if self.__estado != "PENDIENTE":
                raise EstadoInvalidoError(f"No se puede confirmar: estado {self.__estado}")
            if self.duracion <= 0:
                raise ReservaInvalidaError("Duración debe ser mayor a cero")
        except (EstadoInvalidoError, ReservaInvalidaError) as error:
            log.error(f"Fallo confirmación: {error}", error)
            raise
        else:
            self.__estado = "CONFIRMADA"
            log.info(f"✅ Reserva CONFIRMADA: {self.cliente.nombre}")
            return True
        finally:
            log.info("Proceso de confirmación finalizado")

    def cancelar(self, motivo="No especificado"):
        """Cancelar reserva con validación de estado"""
        try:
            if self.__estado in {"COMPLETADA", "CANCELADA"}:
                raise EstadoInvalidoError(f"No se puede cancelar: estado {self.__estado}")
            self.__estado = "CANCELADA"
            log.info(f"❌ Reserva CANCELADA: {self.cliente.nombre} | Motivo: {motivo}")
            return True
        except EstadoInvalidoError as error:
            log.error(f"Fallo cancelación: {error}", error)
            raise

    def obtener_costo_total(self, impuesto=0.19, descuento=0.0):
        """Calcular costo con valores opcionales"""
        return self.servicio.calcular_costo(self.duracion, impuesto, descuento)
