<template>
  <div class="nuestro-equipo-page">
    <h2>Nuestro Equipo</h2>
    <p>Conoce a las personas que hacen posible nuestro trabajo.</p>
    <div class="equipo-jerarquia">

      <div class="miembro-nivel-1">
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="https://via.placeholder.com/150/CCCCCC?Text=Lider1" alt="Angee Reyes B">
          </div>
          <h3>Angee Reyes B</h3>
          <p class="rol">Gerente - Líder de Tecnología</p>
        </div>
      </div>

      <div class="miembros-nivel-2">
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="https://via.placeholder.com/120/AAAAAA?Text=Lider2" alt="Oscar Marino Garcia">
          </div>
          <h3>Oscar Marino Garcia</h3>
          <p class="rol">Líder Funcional - MM y BO</p>
        </div>
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="https://via.placeholder.com/120/BBBBBB?Text=Lider3" alt="Karen Eliana Caicedo B.">
          </div>
          <h3>Karen Eliana Caicedo B.</h3>
          <p class="rol">Líder de Desarrollo SAP y Aplicativos</p>
        </div>
      </div>

      <div class="miembros-nivel-3-coordinadores">
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="https://via.placeholder.com/100/CCEEFF?Text=Coord1" alt="Xiomara Estrada Salazar">
          </div>
          <h3>Xiomara Estrada Salazar</h3>
          <p class="rol">Coordinadora SAP FI-CO</p>
        </div>
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="https://via.placeholder.com/100/AACCFFAA?Text=Coord2" alt="Andrés Felipe Viveros Alban">
          </div>
          <h3>Andrés Felipe Viveros Alban</h3>
          <p class="rol">Coordinador SAP Desarrollo-DM</p>
        </div>
      </div>

      <div class="miembros-nivel-4-analistas">
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="https://via.placeholder.com/100/DDEEFF?Text=Analist1" alt="Juan Manuel Valencia">
          </div>
          <h3>Juan Manuel Valencia</h3>
          <p class="rol">Analista de Tecnología SAP</p>
        </div>
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="https://via.placeholder.com/100/FFEECC?Text=Analist2" alt="Jhonatan Alexander Grajales Medina">
          </div>
          <h3>Jhonatan Alexander Grajales Medina</h3>
          <p class="rol">Analista de Tecnología SAP</p>
        </div>
      </div>

      <div class="miembros-nivel-5-asistentes">
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="https://via.placeholder.com/100/FFDDDD?Text=Asist1" alt="Mariana Correa Ulloa">
          </div>
          <h3>Mariana Correa Ulloa</h3>
          <p class="rol">Asistente de Tecnología SAP</p>
        </div>
        <div class="tarjeta-miembro">
          <div class="imagen-container">
            <img src="https://via.placeholder.com/100/EEFFEE?Text=Asist2" alt="Luz Veronica Trejos Romero">
          </div>
          <h3>Luz Veronica Trejos Romero</h3>
          <p class="rol">Asistente de Tecnología SAP</p>
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
  text-align: center;
  background-color: #f9f9f9; /* Added a background for consistency */
}

h2 {
  color: #333;
  margin-bottom: 1rem;
}

p {
  color: #555;
  margin-bottom: 2rem;
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
.miembros-nivel-5-asistentes {
  display: flex;
  justify-content: center;
  gap: 1.5rem; /* Espacio horizontal entre los miembros dentro de un nivel */
  width: 100%; /* Permitir que los niveles ocupen todo el ancho para centrado */
  flex-wrap: wrap; /* Permitir que las tarjetas se envuelvan en pantallas pequeñas */
}

/* Añadir espaciado vertical específico entre niveles */
.miembros-nivel-2 {
  margin-top: 2rem; /* Espacio debajo del Nivel 1 */
}
.miembros-nivel-3-coordinadores {
    margin-top: 2rem; /* Espacio debajo del Nivel 2 */
}
 .miembros-nivel-4-analistas {
    margin-top: 2rem; /* Espacio debajo de Coordinadores */
}
  .miembros-nivel-5-asistentes {
    margin-top: 2rem; /* Espacio debajo de Analistas */
}


.tarjeta-miembro {
  background-color: #fff; /* Fondo blanco para las tarjetas */
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  text-align: center;
  width: 220px; /* Ancho ajustado para mejor espaciado */
  display: flex; /* Usar flexbox para controlar el layout interno */
  flex-direction: column;
  align-items: center;
 }

 .imagen-container {
  width: 100px; /* Tamaño fijo para consistencia del contenedor de imagen */
  height: 100px; /* Tamaño fijo para consistencia del contenedor de imagen */
  margin-bottom: 0.5rem;
  overflow: hidden; /* Ocultar partes de la imagen fuera del círculo */
  border-radius: 50%; /* Hacerlo circular */
  display: flex; /* Centrar la imagen dentro del contenedor */
  justify-content: center;
  align-items: center;
  border: 3px solid #007bff; /* Añadir un borde para separación visual */
  flex-shrink: 0; /* Evitar que se encoja */
 }

 .imagen-container img {
  display: block;
  width: 100%; /* La imagen llena el contenedor */
  height: 100%; /* La imagen llena el contenedor */
  object-fit: cover; /* Cubrir el área sin distorsionar la relación de aspecto */
 }

 h3 {
  color: #333;
  font-size: 1.1rem; /* Tamaño de fuente ajustado */
  margin-bottom: 0.2rem;
  word-break: break-word; /* Romper nombres largos */
 }

 .rol {
  color: #555; /* Color más oscuro para los roles */
  font-size: 0.9rem;
  font-weight: 600; /* Texto del rol ligeramente más audaz */
  word-break: break-word; /* Romper roles largos */
 }

 /* Estilos responsivos */
 @media (max-width: 768px) {
  .miembro-nivel-1,
  .miembros-nivel-2,
  .miembros-nivel-3-coordinadores,
  .miembros-nivel-4-analistas,
  .miembros-nivel-5-asistentes {
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