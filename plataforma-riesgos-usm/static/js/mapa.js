// 1. Inicializar el mapa centrado en la Casa Central de la USM (Latitud, Longitud)
var mapa = L.map('mapa-usm').setView([-33.0348, -71.5965], 16);

// 2. Cargar la capa visual del mapa (OpenStreetMap gratuito)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}).addTo(mapa);

// 3. Añadir un marcador de prueba en la entrada principal para verificar que funciona
var marcadorPrueba = L.marker([-33.0348, -71.5965]).addTo(mapa);
marcadorPrueba.bindPopup("<b>¡Mapa Funcionando!</b><br>Centro de la Casa Central USM.").openPopup();

// Nota: Más adelante aquí agregaremos la función fetch() 
// para pedirle a app.py los reportes de la base de datos.