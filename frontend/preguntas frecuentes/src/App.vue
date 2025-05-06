<template>
  <div class="pagina">
    <nav class="navbar">
      <div class="logo">
        <ul class="menu">
          <li class="menu-container">
            <ul v-if="menuVisible" class="dropdown-menu">
              <li class="home-button-li">
                <a href="#" @click="toggleMenu" class="home-button">🏠</a>
              </li>
              <li><a href="#">GESTOR DE CLAVES</a></li>
              <li><a href="#">MOVILIDAD</a></li>
              <li><a href="#">CRM</a></li>
              <li><a href="#">CITAS EN BODEGA</a></li>
              <li><a href="#">PROGRAMA DE LEALTAD</a></li>
              <li><router-link to="/nuestro-equipo">NUESTRO EQUIPO</router-link></li>
            </ul>
            <div v-if="!menuVisible" class="menu-toggle">
              <a href="#" @click="toggleMenu" class="home-button">🏠</a>
            </div>
          </li>
          <li><a href="#">Preguntas frecuentes</a></li>
          <li><a href="#">Tips y Manuales</a></li>
          <li><a href="#">Portales</a></li>
          <li><a href="#">Contacto</a></li>
        </ul>
      </div>
    </nav>
    <hr class="linea-separadora" />
    <router-view></router-view>
    <div class="contenido">
      <h1>Preguntas Frecuentes</h1>
    </div>

    <div class="video-container">
      <video autoplay muted loop playsinline>
        <source src="/Video.mp4" type="video/mp4" />
        Tu navegador no soporta el elemento de video.
      </video>
    </div>

    <div class="contenido_principal">
      <h3>
        Compártanos su requerimiento y <br />
        le daremos la solución.
      </h3>
    </div>

    <div class="correosoporte">
      <p>soportemas@itaas.net.co</p>
    </div>

    <button class="boton_ir" onclick="location.href='mailto:soportemas@itaas.net.co';">IR</button>
  </div>

  <rasa-chatbot-widget server-url="http://localhost:5005" rest-enabled="true" widget-title="Titan"></rasa-chatbot-widget>

  <link rel="stylesheet" href="https://unpkg.com/@rasahq/chat-widget-ui/dist/rasa-chatwidget/rasa-chatwidget.css" />
</template>

<script>
export default {
  name: "Inicio",
  data() {
    return {
      menuVisible: false, // Estado para controlar la visibilidad del menú desplegable
    };
  },
  methods: {
    toggleMenu() {
      this.menuVisible = !this.menuVisible; // Alterna la visibilidad del menú
    },
  },
};
</script>

<style scoped>
/* Estilos generales */
.pagina {
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  font-family: "Arial, sans-serif"; /* Fuente corporativa estándar */
  font-size: 16px;
  line-height: 1.6; /* Ligeramente más espaciado para mejor legibilidad */
  color: #333; /* Texto principal en gris oscuro */
  background-color: #f9f9f9; /* Fondo gris claro y sutil */
}

/* Estilos del menú */
.navbar {
  width: 100%;
  background-color: #ffffff; /* Fondo blanco limpio */
  padding: 1rem 2rem; /* Añadir más padding horizontal */
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); /* Sombra sutil */
  position: relative;
  z-index: 100;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #2c3e50; /* Color del logo en un tono corporativo */
}

.menu {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.menu li {
  margin: 0 1.5rem; /* Aumentar un poco el margen */
}

.menu a {
  text-decoration: none;
  color: #555; /* Texto del menú en un gris más suave */
  font-weight: 400;
  transition: color 0.2s ease-in-out;
}

.menu a:hover {
  color: #007bff; /* Color de hover en un azul corporativo */
}

/* Estilos del menú desplegable */
.menu-container {
  position: relative;
}

.dropdown-menu {
  list-style: none;
  padding: 0;
  margin: 0;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #ffffff; /* Fondo blanco para el dropdown */
  border: 1px solid #ddd; /* Borde sutil */
  border-top: none;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15); /* Sombra suave */
  z-index: 1000;
  display: none;
  width: 220px; /* Ancho ligeramente mayor */
  text-align: left;
}

.menu-container:hover .dropdown-menu {
  display: block;
}

.dropdown-menu li {
  padding: 0.8rem 1.2rem; /* Ajustar el padding */
}

.dropdown-menu a {
  display: block;
  width: 100%;
  clear: both;
  font-weight: 400;
  line-height: 1.5;
  color: #555; /* Color del texto del dropdown */
  text-align: left;
  white-space: nowrap;
  background-color: transparent;
  border: 0;
  transition: background-color 0.15s ease-in-out, color 0.15s ease-in-out;
}

.dropdown-menu a:hover {
  background-color: #f0f0f0; /* Fondo gris claro al pasar el ratón */
  color: #007bff; /* Color del texto al pasar el ratón */
}

.home-button {
  display: inline-block;
  padding: 0.5rem;
  font-size: 1.2rem;
  text-decoration: none;
  color: #555;
  transition: color 0.2s ease-in-out;
}

.home-button:hover {
  color: #007bff;
}

/* Estilos de la línea separadora */
.linea-separadora {
  width: 100%;
  height: 1px; /* Línea más delgada */
  background-color: #e0e0e0; /* Gris claro para la línea */
  margin: 1rem 0; /* Reducir el margen */
  border: none;
}

/* Otros estilos */
.contenido {
  padding: 2rem; /* Reducir un poco el padding */
  text-align: center;
}

.contenido h1 {
  font-size: 2rem; /* Reducir un poco el tamaño del título */
  color: #333;
}

.video-container {
  width: 100%;
  margin-bottom: 2rem; /* Reducir el margen inferior */
}

.video-container video {
  width: 100%;
  max-height: 400px; /* Reducir la altura máxima del video */
  object-fit: cover;
  border-radius: 5px; /* Reducir el radio del borde del video */
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); /* Sombra más sutil */
}

.contenido_principal {
  padding: 1.5rem; /* Reducir el padding */
  text-align: center;
}

.contenido_principal h3 {
  font-size: 1.3rem; /* Reducir el tamaño del subtítulo */
  color: #555;
}

.correosoporte {
  padding: 1.5rem; /* Reducir el padding */
  text-align: center;
  color: #777;
  font-size: 0.9rem; /* Reducir el tamaño del texto del correo */
}

.boton_ir {
  display: inline-block;
  padding: 0.8rem 1.5rem; /* Reducir el padding del botón */
  font-size: 1rem; /* Reducir el tamaño de la fuente del botón */
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  color: #fff;
  background-color: #007bff; /* Azul corporativo para el botón */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.boton_ir:hover {
  background-color: #0056b3; /* Tono más oscuro de azul al pasar el ratón */
}
</style>