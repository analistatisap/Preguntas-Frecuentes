<template>
  <div class="container my-5">
    <div class="row align-items-center justify-content-center">
      <!-- Columna de texto -->
      <div class="col-md-6 mb-4 mb-md-0">
        <div class="p-4 rounded-3 bg-white shadow-sm">
          <h2 class="mb-3">¿Sabías que…</h2>
          <p class="lead">
            A través de este portal podrás obtener material de utilidad para el óptimo desarrollo de tus procesos?
          </p>
        </div>
      </div>
      <!-- Columna de imagen -->
      <div class="col-md-6 text-center">
        <div class="animated-gradient rounded-3 d-flex flex-column align-items-center justify-content-center" style="height: 220px;">
          <!-- Icono Robot SVG -->
          <svg width="80" height="80" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="4" y="8" width="16" height="10" rx="4" fill="#fff" stroke="#333" stroke-width="2"/>
            <circle cx="8" cy="13" r="1.5" fill="#333"/>
            <circle cx="16" cy="13" r="1.5" fill="#333"/>
            <rect x="10" y="2" width="4" height="6" rx="2" fill="#333"/>
            <rect x="2" y="10" width="2" height="4" rx="1" fill="#333"/>
            <rect x="20" y="10" width="2" height="4" rx="1" fill="#333"/>
          </svg>
          <!-- Espacio -->
          <div style="height: 16px;"></div>
          <!-- Icono Celular SVG -->
          <svg width="50" height="80" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="6" y="2" width="12" height="20" rx="3" fill="#fff" stroke="#333" stroke-width="2"/>
            <rect x="10" y="18" width="4" height="2" rx="1" fill="#333"/>
            <rect x="9" y="4" width="6" height="10" rx="2" fill="#e0e0e0"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const entornos = [
  {
    titulo: 'Entorno SAP',
    descripcion: 'Gestión de cuentas para sistemas SAP ERP - LOGON, SAP CRM, SAP BO y otros sistemas SAP',
    icono: 'bi bi-database'
  },
  {
    titulo: 'Intiva – (Movilidad)',
    descripcion: 'Gestión Comercial para las Ventas, Inicio de Sesión y Restablecimiento de Clave',
    icono: 'bi bi-bag'
  },
  {
    titulo: 'Entorno Office-Red',
    descripcion: 'Restablecer la clave de su equipo afectando el Directorio Activo y servicios relacionados',
    icono: 'bi bi-diagram-3'
  }
]
</script>

<style scoped>
/* Estilos de la sección principal con los cuadros */
.seccion-principal-corporativa {
  display: flex;
  justify-content: center; /* Centramos el contenido principal */
  align-items: center;
  padding: 2rem;
  background-color: #f0f0f0; /* Un color de fondo para la sección principal */
}

.contenedor-principal {
  display: flex;
  max-width: 960px; /* Un ancho máximo para el contenido principal */
  width: 100%;
  align-items: center; /* Alineamos verticalmente los elementos */
  /* Permitir que los elementos se apilen en pantallas pequeñas */
  flex-wrap: wrap;
  justify-content: center; /* Centrar en pantallas pequeñas */
  gap: 2rem; /* Espacio entre el texto y los cuadros en pantallas pequeñas */
}

.texto-izquierda {
  flex: 1; /* El texto ocupa espacio disponible */
  padding-right: 20px; /* Espacio entre el texto y los cuadros */
  text-align: left;
  min-width: 300px; /* Asegura que el texto no se comprima demasiado */
}

.texto-izquierda p {
  font-size: 1.2rem;
  color: #333;
  line-height: 1.6;
  margin-bottom: 10px;
}

/* Contenedor del Grid de cuadros */
.cuadros-interactivos {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 2 columnas de igual tamaño */
  grid-template-rows: repeat(2, 1fr);    /* 2 filas de igual tamaño */
  gap: 0; /* ¡Importante! Elimina el espacio entre las celdas del grid */
  width: 420px; /* Aseguramos un tamaño fijo */
  height: 420px; /* Aseguramos un tamaño fijo */
  max-width: 420px; /* Aseguramos que los cuadros no se expandan demasiado */
  /* Centrar el grid si el contenedor flex es más grande */
  justify-content: center;
  align-content: center;
}

/* Estilos para cada cuadro individual (Actualizado) */
.cuadro {
  /* background-color: #fff; /* Se puede quitar si la imagen cubre todo */
  border-radius: 0; /* Quitamos el borde redondeado para que parezcan unidas */
  box-shadow: none; /* Quitamos la sombra inicial para que parezcan unidas */
  overflow: hidden; /* Asegura que la imagen no se salga al escalar */
  cursor: pointer;
  transition: transform 0.4s ease-in-out, box-shadow 0.4s ease-in-out; /* Transición para la transformación y sombra */
  margin: 0; /* Aseguramos que no haya márgenes externos */
  padding: 0; /* Aseguramos que no haya padding interno */
  /* Eliminado display: flex y centrado de items aquí, ya que la imagen llenará el espacio */
  position: relative; /* Necesario para z-index en hover */
}

.cuadro:hover {
  transform: scale(1.02) rotate(360deg); /* Efecto en el contenedor (el cuadro) */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* Añadimos la sombra al pasar el ratón */
  z-index: 1; /* Asegura que el cuadro al que pasamos el ratón esté por encima */
}

/* Estilos para la imagen dentro de cada cuadro (Actualizado para precisión) */
.cuadro img {
  display: block; /* Importante: ayuda a eliminar pequeños espacios debajo de la imagen */
  width: 100%; /* La imagen ocupa todo el ancho del cuadro */
  height: 100%; /* La imagen ocupa todo el alto del cuadro */
  /* Eliminamos max-width y max-height ya que width/height 100% es más directo */
  /* max-width: 100%; */
  /* max-height: 100%; */
  object-fit: fill; /* **FORZAMOS que la imagen llene exactamente el contenedor, incluso si distorsiona ligeramente** */
  transition: transform 0.3s ease-in-out; /* Efecto en la imagen (dentro del cuadro) */
}

.cuadro:hover img {
  transform: scale(1.08); /* Efecto en la imagen al pasar el ratón */
}

/* Media query para ajustar el layout en pantallas pequeñas si es necesario */
@media (max-width: 768px) {
  .contenedor-principal {
    flex-direction: column; /* Apila el texto y los cuadros */
    padding: 1rem;
  }

  .texto-izquierda {
    padding-right: 0;
    margin-bottom: 1.5rem; /* Espacio entre el texto y los cuadros apilados */
    text-align: center; /* Centra el texto en pantallas pequeñas */
  }

  .cuadros-interactivos {
    width: 100%; /* Permite que el grid ocupe todo el ancho disponible */
    height: auto; /* Ajusta la altura automáticamente */
    max-width: 300px; /* Limita el ancho máximo del grid en pantallas pequeñas */
    /* Aseguramos que las celdas del grid sigan una proporción 1:1 */
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr); /* O podrías usar 'auto' si quieres que la altura dependa del contenido */
  }
}

.animated-gradient {
  background: linear-gradient(270deg, #e0eafc, #cfdef3, #e0eafc, #cfdef3);
  background-size: 400% 400%;
  animation: gradientMove 6s ease-in-out infinite;
}
@keyframes gradientMove {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>