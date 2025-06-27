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
        <div class="glass-animated light-wireframe d-flex flex-column align-items-center justify-content-center position-relative">
          <!-- Fondo SVG animado: red de puntos y líneas + ondas de luz -->
          <svg class="bg-tech-svg" viewBox="0 0 400 220" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Líneas animadas -->
            <g class="lines-group">
              <polyline points="20,40 100,60 200,30 300,80 380,40" class="tech-line" />
              <polyline points="30,180 120,120 200,200 280,140 370,180" class="tech-line delay1" />
              <polyline points="60,60 180,100 320,60" class="tech-line delay2" />
              <polyline points="80,200 200,160 320,200" class="tech-line delay3" />
            </g>
            <!-- Puntos animados -->
            <g class="points-group">
              <circle cx="100" cy="60" r="3" class="tech-dot" />
              <circle cx="200" cy="30" r="3" class="tech-dot delay1" />
              <circle cx="300" cy="80" r="3" class="tech-dot delay2" />
              <circle cx="120" cy="120" r="3" class="tech-dot delay3" />
              <circle cx="200" cy="200" r="3" class="tech-dot delay4" />
              <circle cx="280" cy="140" r="3" class="tech-dot delay5" />
            </g>
            <!-- Ondas animadas -->
            <g class="waves-group">
              <path class="tech-wave" d="M0 110 Q100 90 200 110 T400 110" />
              <path class="tech-wave delay1" d="M0 130 Q100 150 200 130 T400 130" />
            </g>
          </svg>
          <!-- Icono SVG animado con pulso -->
          <svg class="pulse-icon" width="90" height="90" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="12" cy="12" r="10" fill="#fff" fill-opacity="0.7"/>
            <path d="M8 13l2-2 2 2 4-4" stroke="#4f8cff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="12" cy="12" r="6" fill="#4f8cff" fill-opacity="0.15"/>
          </svg>
          <span class="glass-text mt-3 wireframe-text">¡Bienvenido{{ nombreUsuario ? ' ' + nombreUsuario : '' }}!
            <span class="wireframe-reflection"></span>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Particles from '@tsparticles/vue3';
import { loadFull } from 'tsparticles';

const nombreUsuario = ref('');

onMounted(() => {
  const userData = localStorage.getItem('user');
  if (userData) {
    try {
      const user = JSON.parse(userData);
      // Intenta obtener el primer nombre de fullName, first_name o username
      let nombre = '';
      if (user.fullName) {
        nombre = user.fullName.split(' ')[0];
      } else if (user.first_name) {
        nombre = user.first_name;
      } else if (user.username) {
        nombre = user.username;
      }
      nombreUsuario.value = nombre;
    } catch (e) {
      nombreUsuario.value = '';
    }
  }
});

const particlesInit = async (engine) => {
  await loadFull(engine);
};

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

.glass-animated {
  width: 100%;
  max-width: 320px;
  height: 220px;
  margin: 0 auto;
  border-radius: 24px;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
  background: linear-gradient(135deg, rgba(79,140,255,0.25) 0%, rgba(255,255,255,0.35) 100%);
  backdrop-filter: blur(12px) saturate(160%);
  -webkit-backdrop-filter: blur(12px) saturate(160%);
  border: 1.5px solid rgba(255,255,255,0.25);
  position: relative;
  overflow: hidden;
  animation: glassGradientMove 8s ease-in-out infinite;
}
@keyframes glassGradientMove {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.pulse-icon {
  animation: pulse 1.8s infinite cubic-bezier(0.66, 0, 0, 1);
}
@keyframes pulse {
  0% { transform: scale(1); filter: drop-shadow(0 0 0 #4f8cff44); }
  50% { transform: scale(1.08); filter: drop-shadow(0 0 16px #4f8cff88); }
  100% { transform: scale(1); filter: drop-shadow(0 0 0 #4f8cff44); }
}
.glass-text {
  color: #4f8cff;
  font-size: 1.3rem;
  font-weight: 600;
  letter-spacing: 1px;
  text-shadow: 0 2px 8px #fff8;
}
.bg-tecnologia {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 220px;
  height: 220px;
  max-width: 90%;
  max-height: 90%;
  transform: translate(-50%, -50%);
  opacity: 0.18;
  filter: blur(2px) brightness(1.1);
  pointer-events: none;
  z-index: 0;
  object-fit: contain;
}
.glass-animated > *:not(.particles-bg) {
  position: relative;
  z-index: 2;
}
.light-wireframe {
  background: linear-gradient(135deg, rgba(234,242,255,0.82) 60%, rgba(250,253,255,0.82) 100%);
  border: 1.5px solid #b3c6e6;
  box-shadow: 0 8px 32px 0 rgba(79, 140, 255, 0.13);
  position: relative;
  overflow: hidden;
}
.wireframe-bg {
  position: absolute;
  top: -10px; left: -10px;
  width: 120%;
  height: 120%;
  z-index: 0;
  pointer-events: none;
  animation: wireframeMove 12s linear infinite alternate;
}
@keyframes wireframeMove {
  0% { filter: blur(0.5px) brightness(1.1); opacity: 0.9; }
  50% { filter: blur(2px) brightness(1.2); opacity: 1; }
  100% { filter: blur(0.5px) brightness(1.1); opacity: 0.9; }
}
.wireframe-text {
  color: #1a237e;
  font-size: 2.1rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-shadow: 0 2px 16px #4f8cff44, 0 1px 0 #fff8;
  position: relative;
  z-index: 2;
  background: linear-gradient(90deg, #1a237e 60%, #4f8cff 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.wireframe-reflection {
  content: '';
  display: block;
  width: 100%;
  height: 0.7em;
  margin-top: -0.2em;
  background: linear-gradient(180deg, #fff6 0%, transparent 100%);
  opacity: 0.18;
  transform: scaleY(-1);
  filter: blur(2px);
}
.particles-bg {
  position: absolute !important;
  top: 0; left: 0; width: 100%; height: 100%;
  z-index: 1;
  pointer-events: none;
}
.bg-tech-svg {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
  opacity: 0.55;
}
.tech-line {
  stroke: #4f8cff;
  stroke-width: 2;
  fill: none;
  opacity: 0.5;
  stroke-dasharray: 400;
  stroke-dashoffset: 400;
  animation: lineDraw 2.5s forwards;
}
.tech-line.delay1 { animation-delay: 0.5s; }
.tech-line.delay2 { animation-delay: 1s; }
.tech-line.delay3 { animation-delay: 1.5s; }
@keyframes lineDraw {
  to { stroke-dashoffset: 0; }
}
.tech-dot {
  fill: #00eaff;
  filter: drop-shadow(0 0 6px #00eaff88);
  opacity: 0.7;
  transform: scale(0.7);
  animation: dotPulse 1.8s infinite alternate;
}
.tech-dot.delay1 { animation-delay: 0.3s; }
.tech-dot.delay2 { animation-delay: 0.6s; }
.tech-dot.delay3 { animation-delay: 0.9s; }
.tech-dot.delay4 { animation-delay: 1.2s; }
.tech-dot.delay5 { animation-delay: 1.5s; }
@keyframes dotPulse {
  to { opacity: 1; transform: scale(1.2); }
}
.tech-wave {
  stroke: #4f8cff;
  stroke-width: 2.5;
  fill: none;
  opacity: 0.18;
  filter: blur(1.5px);
  stroke-dasharray: 8 6;
  animation: waveMove 3.5s infinite alternate ease-in-out;
}
.tech-wave.delay1 { animation-delay: 1.2s; }
@keyframes waveMove {
  0% { transform: translateY(0); opacity: 0.18; }
  100% { transform: translateY(-10px) scaleX(1.04); opacity: 0.32; }
}
</style>