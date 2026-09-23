# Algoritmo basico: validar si un afiliado puede agendar una cita
def validar_afiliado(documento, estado_afiliacion, cuotas_pendientes):
    if not documento.isdigit():
        return "Documento invalido"
    if estado_afiliacion != "ACTIVO":
        return "Afiliado inactivo, no puede agendar cita"
    if cuotas_pendientes > 0:
        return "Tiene cuotas pendientes, debe ponerse al dia"
    return "Afiliado valido, puede agendar cita"

print(validar_afiliado("1107050123", "ACTIVO", 0))
print(validar_afiliado("1107050123", "SUSPENDIDO", 0))
print(validar_afiliado("ABC123", "ACTIVO", 0))
