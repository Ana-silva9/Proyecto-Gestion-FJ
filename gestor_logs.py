# -*- coding: utf-8 -*-
"""
Gestor de registros de eventos y errores (Logs)
Curso: Programación 213023 - Fase 4
"""

import logging
from datetime import datetime

class GestorLogs:
    """Clase para registrar todas las acciones y errores en archivo"""
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
            cls._instancia._configurar()
        return cls._instancia

    def _configurar(self):
        nombre = f"registro_{datetime.now().strftime('%Y%m%d')}.log"
        logging.basicConfig(
            filename=nombre,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%d/%m/%Y %H:%M:%S",
            encoding="utf-8"
        )
        self.registro = logging.getLogger()

    def info(self, mensaje):
        """Registrar evento informativo"""
        self.registro.info(mensaje)

    def error(self, mensaje, excepcion=None):
        """Registrar error con detalles"""
        self.registro.error(mensaje, exc_info=excepcion)
