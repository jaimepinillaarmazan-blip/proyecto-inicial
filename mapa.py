import folium

# 1. Crear el mapa centrado en la USM
mapa_riesgos = folium.Map(location=[-33.0348, -71.5965], zoom_start=16)

# 2. Agregar un reporte de infraestructura
folium.Marker(
    location=[-33.0355, -71.5950],
    popup="<b>¡Precaución!</b><br>Escaleras con peldaños sueltos.",
    tooltip="Clic para ver detalle",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(mapa_riesgos)

# 3. Agregar un reporte de seguridad
folium.Marker(
    location=[-33.0330, -71.5975],
    popup="<b>Actividad Sospechosa</b><br>Evitar a altas horas.",
    tooltip="Clic para ver detalle",
    icon=folium.Icon(color="darkred", icon="warning-sign")
).add_to(mapa_riesgos)

# 4. Exportar a un archivo web listo para usar
mapa_riesgos.save("mapa_alertas_usm.html")
print("El mapa se ha generado en el archivo 'mapa_alertas_usm.html'")