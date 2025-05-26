<template>
  <div class="nuestro-equipo-page">
    <h2>Nuestro Equipo</h2>
    <p>Conoce a las personas que hacen posible nuestro trabajo.</p>
    <div class="equipo-jerarquia">

      <div class="miembro-nivel-1">
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="/fotosNE/GerenteAngeeReyes.png" alt="Angee Reyes B">
          </div>
          <h3>Angee Reyes B</h3>
          <p class="rol">Gerente - Líder de Tecnología</p>
        </div>
      </div>

      <div class="miembros-nivel-2">
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="/fotosNE/OscarMarino.avif" alt="Oscar Marino Garcia">
          </div>
          <h3>Oscar Marino Garcia</h3>
          <p class="rol">Líder Funcional - MM y BO</p>
        </div>
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="/fotosNE/KarenElianaCaicedo.avif" alt="Karen Eliana Caicedo B.">
          </div>
          <h3>Karen Eliana Caicedo B.</h3>
          <p class="rol">Líder de Desarrollo SAP y Aplicativos</p>
        </div>
      </div>

      <div class="miembros-nivel-3-coordinadores">
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="/fotosNE/XiomaraEstrada.avif" alt="Xiomara Estrada Salazar">
          </div>
          <h3>Xiomara Estrada Salazar</h3>
          <p class="rol">Coordinadora SAP FI-CO</p>
        </div>
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="/fotosNE/AndresViveros.avif" alt="Andrés Felipe Viveros Alban">
          </div>
          <h3>Andrés Felipe Viveros Alban</h3>
          <p class="rol">Coordinador SAP Desarrollo-DM</p>
        </div>
      </div>

      <div class="miembros-nivel-4-analistas">
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="/fotosNE/JuanManuelValencia.avif" alt="Juan Manuel Valencia">
          </div>
          <h3>Juan Manuel Valencia</h3>
          <p class="rol">Analista de Tecnología SAP</p>
        </div>
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="/fotosNE/JhonatanGrajales.jpg" alt="Jhonatan Alexander Grajales Medina">
          </div>
          <h3>Jhonatan Alexander Grajales Medina</h3>
          <p class="rol">Analista de Tecnología SAP</p>
        </div>
      </div>

      <div class="miembros-nivel-5-asistentes">
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="/fotosNE/MarianaCorrea.avif" alt="Mariana Correa Ulloa">
          </div>
          <h3>Mariana Correa Ulloa</h3>
          <p class="rol">Asistente de Tecnología SAP</p>
        </div>
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="/fotosNE/VeronicaTrejos.jpg" alt="Luz Veronica Trejos Romero">
          </div>
          <h3>Luz Veronica Trejos Romero</h3>
          <p class="rol">Asistente de Tecnología SAP</p>
        </div>
      </div>

      <!-- Nueva Sección: Área de Infraestructura -->
      <div class="equipo-seccion">
        <h4>Área de Infraestructura</h4>
        <div class="miembros-infraestructura">
          <div class="tarjeta-miembro">
            <div class="imagen-container">
              <img src="/fotosNE/RubenDario.avif" alt="Ruben Dario Tobon Cardona">
            </div>
            <h3>Ruben Dario Tobon Cardona</h3>
            <p class="rol">Infraestructura</p>
          </div>
          <div class="tarjeta-miembro">
            <div class="imagen-container">
              <img src="/fotosNE/ValentinaCastaño.avif" alt="Valentina Echeverry Castaño">
            </div>
            <h3>Valentina Echeverry Castaño</h3>
            <p class="rol">Infraestructura</p>
          </div>
          <div class="tarjeta-miembro">
            <div class="imagen-container">
              <img src="/fotosNE/caicedo.png" alt="Nombre Colaborador Infra 3">
            </div>
            <h3>Alejandro Cano Caicedo</h3>
            <p class="rol">Aprendiz de infraestructura</p>
          </div>
        </div>
      </div>

      <!-- Nueva Sección: Soporte Técnico -->
      <div class="equipo-seccion">
        <h4>Soporte Técnico</h4>
        <div class="miembros-soporte-tecnico">
          <div class="tarjeta-miembro">
            <div class="imagen-container">
              <img src="/fotosNE/JulianAlbertoPiña.avif" alt="Nombre Colaborador Soporte 1">
            </div>
            <h3>Julian Piña Garcia</h3>
            <p class="rol">Cordinador de soporte tecnico</p>
          </div>
          <div class="tarjeta-miembro">
            <div class="imagen-container">
              <img src="/fotosNE/robinson.png" alt="Julian Alberto Piña Garcia">
            </div>
            <h3>Robinson David Becoche</h3>
            <p class="rol">Soporte tecnico</p>
          </div>
          <div class="tarjeta-miembro">
            <div class="imagen-container">
              <img src="/fotosNE/Diego.png" alt="Robinson David Becoche">
            </div>
            <h3>Diego Alejandro Rico Angulo</h3>
            <p class="rol">Practicante de tecnologia</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'NuestroEquipo',
};
</script>

<style scoped>
.nuestro-equipo-page {
  padding: 2rem;
  padding-bottom: 4rem; /* Más espacio al final */
  text-align: center;
  background-color: #f4f7f6; /* Un fondo ligeramente más suave y moderno */
}

h2 {
  color: #343a40; /* Color de texto oscuro estándar */
  margin-bottom: 1rem;
  font-size: 2.2rem; /* Un poco más grande */
  font-weight: 600;
}

.nuestro-equipo-page > p:first-of-type { /* Selector más específico para el párrafo introductorio */
  color: #495057; /* Color de texto secundario */
  margin-bottom: 2rem;
  font-size: 1.1rem;
  max-width: 700px; /* Limitar ancho para mejor legibilidad */
  margin-left: auto;
  margin-right: auto;
}

.equipo-jerarquia {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem; /* Espacio vertical entre los niveles jerárquicos */
}

/* Estilos para los contenedores de cada nivel */
.miembro-nivel-1,
.miembros-nivel-2,
.miembros-nivel-3-coordinadores,
.miembros-nivel-4-analistas,
.miembros-nivel-5-asistentes,
.miembros-infraestructura, /* Estilo para el contenedor de miembros de Infraestructura */
.miembros-soporte-tecnico { /* Estilo para el contenedor de miembros de Soporte Técnico */
  display: flex;
  justify-content: center; /* Centra las tarjetas horizontalmente */
  gap: 1.5rem; /* Espacio horizontal entre los miembros dentro de un nivel */
  width: 100%; /* Permitir que los niveles ocupen todo el ancho para centrado */
  flex-wrap: wrap; /* Permitir que las tarjetas se envuelvan en pantallas pequeñas */
  margin-bottom: 1.5rem; /* Espacio uniforme debajo de cada nivel */
}

.equipo-seccion { /* Contenedor para las nuevas secciones con título */
  width: 100%;
  margin-top: 2.5rem; /* Espacio encima de cada nueva sección */
}

.equipo-seccion h4 {
  color: #343a40;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  font-weight: 600;
}

/* Añadir espaciado vertical específico entre niveles */
.miembros-nivel-2 {
  margin-top: 1.5rem; /* Espacio debajo del Nivel 1 */
}
.miembros-nivel-3-coordinadores {
    margin-top: 1.5rem; /* Espacio debajo del Nivel 2 */
}
 .miembros-nivel-4-analistas {
    margin-top: 1.5rem; /* Espacio debajo de Coordinadores */
}
  .miembros-nivel-5-asistentes {
    margin-top: 1.5rem; /* Espacio debajo de Analistas */
}


.tarjeta-miembro {
  background-color: #fff; /* Fondo blanco para las tarjetas */
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* Sombra más sutil y moderna */
  padding: 1.5rem 1rem; /* Más padding vertical */
  text-align: center;
  width: 220px; /* Ancho ajustado para mejor espaciado */
  display: flex; /* Usar flexbox para controlar el layout interno */
  flex-direction: column;
  align-items: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Transición para hover */
 }

 .tarjeta-miembro:hover {
  transform: translateY(-6px); /* Efecto de elevación al pasar el mouse */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12); /* Sombra más pronunciada en hover */
}

 .imagen-container {
  width: 100px; /* Tamaño fijo para consistencia del contenedor de imagen */
  height: 100px; /* Tamaño fijo para consistencia del contenedor de imagen */
  margin-bottom: 1rem; /* Más espacio debajo de la imagen */
  overflow: hidden; /* Ocultar partes de la imagen fuera del círculo */
  border-radius: 50%; /* Hacerlo circular */
  display: flex; /* Centrar la imagen dentro del contenedor */
  justify-content: center;
  align-items: center;
  border: 3px solid #e9ecef; /* Borde más sutil y neutro, color Bootstrap para bordes */
  flex-shrink: 0; /* Evitar que se encoja */
 }

 .imagen-container img {
  display: block;
  width: 100%; /* La imagen llena el contenedor */
  height: 100%; /* La imagen llena el contenedor */
  object-fit: cover; /* Cubrir el área sin distorsionar la relación de aspecto */
 }

 h3 {
  color: #343a40; /* Color de texto oscuro estándar */
  font-size: 1.15rem; /* Tamaño de fuente ligeramente aumentado */
  margin-bottom: 0.35rem; /* Espacio ajustado */
  word-break: break-word; /* Romper nombres largos */
  font-weight: 600;
 }

 .rol {
  color: #007bff; /* Usar un color de acento primario para el rol */
  font-size: 0.9rem;
  font-weight: 500; /* Peso de fuente normal/medio */
  word-break: break-word; /* Romper roles largos */
  margin-bottom: 0; /* Resetear el margen inferior del párrafo para el rol */
 }

 /* Estilos responsivos */
 @media (max-width: 768px) {
  .miembro-nivel-1,
  .miembros-nivel-2,
  .miembros-nivel-3-coordinadores,
  .miembros-nivel-4-analistas,
  .miembros-nivel-5-asistentes,
  .miembros-infraestructura,
  .miembros-soporte-tecnico {
    flex-direction: column;
    align-items: center;
    gap: 1rem; /* Reducir el espacio en pantallas pequeñas */
  }
  .tarjeta-miembro {
    width: 80%; /* Hacer las tarjetas más anchas en pantallas pequeñas */
    max-width: 300px; /* Restricción de ancho máximo */
  }
   .imagen-container {
        width: 80px; /* Imágenes más pequeñas en móviles */
        height: 80px;
    }
 }
 </style>