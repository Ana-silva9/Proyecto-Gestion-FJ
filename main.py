# -*- coding: utf-8 -*-
"""
Programa principal: 10+ operaciones de prueba
Demuestra estabilidad y manejo de errores
Curso: Programación 213023 — Fase 4
"""

from gestor_logs import GestorLogs
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from excepciones import DatoInvalidoError, ReservaInvalidaError, EstadoInvalidoError

log = GestorLogs()

def main():
    print("=" * 55)
    print("   SISTEMA INTEGRAL DE GESTIÓN — Software FJ")
    print("   Curso: Programación 213023 — Fase 4")
    print("=" * 55)
    log.info("==== INICIO DE EJECUCIÓN DEL SISTEMA ====")

    clientes = []
    servicios = []
    reservas = []

    # 1. Registrar cliente válido
    print("\n--- Operación 1: Registrar cliente válido ---")
    try:
        c1 = Cliente("CLI001", "María López", "maria@unad.edu.co", "3101234567")
        clientes.append(c1)
        print(f"✅ {c1}")
    except DatoInvalidoError as e:
        print(f"❌ Error: {e}")

    # 2. Registrar cliente inválido
    print("\n--- Operación 2: Registrar cliente inválido ---")
    try:
        c2 = Cliente("CL", "Usuario Inválido", "correo_sin_arroba", "123")
        clientes.append(c2)
    except DatoInvalidoError as e:
        print(f"❌ Rechazado correctamente: {e}")

    # 3. Crear servicio válido
    print("\n--- Operación 3: Crear servicio válido ---")
    try:
        s1 = ReservaSala("SAL001", "Sala Conferencias A", "Capacidad 30 personas", 50000)
        servicios.append(s1)
        print(f"✅ {s1.describir()}")
    except DatoInvalidoError as e:
        print(f"❌ Error: {e}")

    # 4. Servicio con precio negativo
    print("\n--- Operación 4: Servicio con precio negativo ---")
    try:
        s2 = AlquilerEquipo("EQ-001", "Laptop", "Equipo portátil", -10000)
        servicios.append(s2)
    except DatoInvalidoError as e:
        print(f"❌ Rechazado correctamente: {e}")

    # 5. Reserva exitosa
    print("\n--- Operación 5: Crear y confirmar reserva ---")
    try:
        r1 = Reserva(c1, s1, 3)
        reservas.append(r1)
        r1.confirmar()
        print(f"✅ Reserva confirmada. Costo: ${r1.obtener_costo_total():,.2f}")
    except (ReservaInvalidaError, EstadoInvalidoError) as e:
        print(f"❌ Error: {e}")

    # 6. Duración inválida
    print("\n--- Operación 6: Duración inválida ---")
    try:
        r2 = Reserva(c1, s1, 0)
        r2.confirmar()
    except ReservaInvalidaError as e:
        print(f"❌ Rechazado correctamente: {e}")

    # 7. Cancelar reserva
    print("\n--- Operación 7: Cancelar reserva ---")
    try:
        s3 = AsesoriaEspecializada("ASES-001", "Consultoría en Seguridad", "Auditoría de sistemas", 120000)
        r3 = Reserva(c1, s3, 2)
        r3.cancelar("Cambio de agenda")
        print(f"✅ Reserva cancelada. Estado: {r3.estado}")
    except EstadoInvalidoError as e:
        print(f"❌ Error: {e}")

    # 8. Costo con descuento
    print("\n--- Operación 8: Costo con descuento 10% ---")
    try:
        costo_desc = r1.obtener_costo_total(descuento=0.10)
        print(f"✅ Costo con descuento: ${costo_desc:,.2f}")
    except Exception as e:
        print(f"❌ Error: {e}")

    # 9. Confirmar reserva ya confirmada
    print("\n--- Operación 9: Confirmar reserva ya confirmada ---")
    try:
        r1.confirmar()
    except EstadoInvalidoError as e:
        print(f"❌ Rechazado correctamente: {e}")

    # 10. Encadenamiento completo
    print("\n--- Operación 10: Registro encadenado ---")
    try:
        c_nuevo = Cliente("CLI002", "Juan Pérez", "juan@correo.com", "3209876543")
        s_nuevo = AlquilerEquipo("EQ-002", "Proyector 4K", "Alta definición", 25000)
        r_nuevo = Reserva(c_nuevo, s_nuevo, 4)
        r_nuevo.confirmar()
        print(f"✅ Encadenamiento exitoso")
        print(f"   Cliente: {c_nuevo.nombre}")
        print(f"   Servicio: {s_nuevo.nombre}")
        print(f"   Costo final: ${r_nuevo.obtener_costo_total(descuento=0.05):,.2f}")
    except DatoInvalidoError as e:
        print(f"❌ Encadenamiento fallido: {e}")

    log.info("==== FIN DE EJECUCIÓN ====")
    print("\n✅ Sistema finalizado. Revisa el archivo de registros.")

if __name__ == "__main__":
    main()
