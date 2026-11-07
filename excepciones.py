# -*- coding: utf-8 -*-
"""
Excepciones personalizadas - Sistema de Gestión FJ
Curso: Programación 213023 - Fase 4
"""

class ErrorSistema(Exception):
    """Clase base para todos los errores del sistema"""
    pass

class DatoInvalidoError(ErrorSistema):
    """Se lanza cuando un dato no cumple el formato o valor requerido"""
    pass

class ReservaInvalidaError(ErrorSistema):
    """Se lanza cuando una reserva no se puede crear o procesar"""
    pass

class ServicioNoDisponibleError(ErrorSistema):
    """Se lanza cuando el servicio no está disponible"""
    pass

class EstadoInvalidoError(ErrorSistema):
    """Se lanza cuando un cambio de estado no está permitido"""
    pass
