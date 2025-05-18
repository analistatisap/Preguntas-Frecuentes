<template>
  <div class="pagina-corporativa">
    <header class="cabecera-corporativa" :class="{ 'header-loaded': headerLoaded }">
      <div class="logo-container">
        <div class="logo-corporativo">
          <router-link to="/">
            <img src="/robot.png" alt="Logo de tu empresa">
          </router-link>
        </div>
        <div class="home-menu-container">
          <div class="dropdown-corporativo" @mouseleave="closeMenu">
            <a href="#" class="home-icon dropbtn-corporativo" @click.prevent="toggleMenu">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle;">
                <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8h5z" />
              </svg>
            </a>
            <transition name="dropdown">
              <ul v-if="menuVisible" class="dropdown-content-corporativo">
                <li>
                  <router-link to="/nuestro-equipo">
                    <span class="menu-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
                      </svg>
                    </span>
                    NUESTRO EQUIPO
                  </router-link>
                </li>
                <li>
                  <router-link to="/portales">
                    <span class="menu-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
                      </svg>
                    </span>
                    PORTALES
                  </router-link>
                </li>
                <li>
                  <a href="https://gestionclavesap.grupodecor.com/" target="_blank">
                    <span class="menu-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12.65 10C11.83 7.67 9.61 6 7 6c-3.31 0-6 2.69-6 6s2.69 6 6 6c2.61 0 4.83-1.67 5.65-4H17v4h4v-4h2v-4H12.65zM7 14c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z"/>
                      </svg>
                    </span>
                    Gestor de Claves
                  </a>
                </li>
                <li>
                  <a href="https://entregabodega.grupodecor.com/" target="_blank">
                    <span class="menu-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/>
                      </svg>
                    </span>
                    Citas en Bodega
                  </a>
                </li>
                <li>
                  <a href="https://decorcrmprd.decorceramica.com:41212/sap(bD1lcyZjPTMwMCZkPW1pbg==)/bc/bsp/sap/crm_ui_start/default.htm?sap-client=300&sap-language=ES" target="_blank">
                    <span class="menu-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-8 2.75c1.24 0 2.25 1.01 2.25 2.25s-1.01 2.25-2.25 2.25S9.75 10.24 9.75 9 10.76 6.75 12 6.75zM17 17H7v-1.5c0-1.67 3.33-2.5 5-2.5s5 .83 5 2.5V17z"/>
                      </svg>
                    </span>
                    CRM
                  </a>
                </li>
                <li>
                  <router-link to="/preguntas-frecuentes">
                    <span class="menu-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M11.07 12.85c.77-1.39 2.25-2.21 3.11-3.44.91-1.29.4-3.7-2.18-3.7-1.69 0-2.52 1.28-2.87 2.34L6.54 6.96C7.25 4.83 9.18 3 11.99 3c2.35 0 3.96 1.07 4.78 2.41.7 1.15 1.11 3.3.03 4.9-1.2 1.77-2.35 2.31-2.97 3.45-.25.46-.35.76-.35 2.24h-2.89c-.01-.78-.13-2.05.48-3.15zM14 20c0 1.1-.9 2-2 2s-2-.9-2-2 .9-2 2-2 2 .9 2 2z"/>
                      </svg>
                    </span>
                    Preguntas frecuentes
                  </router-link>
                </li>
                <li>
                  <router-link to="/tips-y-manuales">
                    <span class="menu-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6C7.8 12.16 7 10.63 7 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z"/>
                      </svg>
                    </span>
                    Tips y Manuales
                  </router-link>
                </li>
                <li>
                  <router-link to="/contacto">
                    <span class="menu-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                      </svg>
                    </span>
                    Contacto
                  </router-link>
                </li>
              </ul>
            </transition>
          </div>
        </div>
      </div>
      <nav class="menu-corporativo">
        <ul>
          <li class="menu-item-corporativo"><router-link to="/preguntas-frecuentes" class="menu-item-link">Preguntas frecuentes</router-link></li>
          <li class="menu-item-corporativo"><router-link to="/tips-y-manuales" class="menu-item-link">Tips y Manuales</router-link></li>
          <li class="menu-item-corporativo"><router-link to="/contacto" class="menu-item-link">Contacto</router-link></li>
        </ul>
      </nav>
    </header>

    <router-view></router-view>

    <section class="seccion-secundaria-corporativa">
      <div class="info-corporativa">
        <h3>¿Necesitas ayuda?</h3>
        <p>Nuestro equipo de soporte está listo para asistirte.</p>
        <p class="correo-soporte-corporativa">soportemas@itaas.net.co</p>
      </div>
      <div class="video-inferior-blanco">
        <div class="video-container-corporativa">
          <video autoplay muted loop playsinline>
            <source src="/Video.mp4" type="video/mp4" />
            Tu navegador no soporta el elemento de video.
          </video>
        </div>
      </div>
    </section>

    <rasa-chatbot-widget server-url="http://localhost:5005" rest-enabled="true" widget-title="Titan"></rasa-chatbot-widget>
    <link rel="stylesheet" href="https://unpkg.com/@rasahq/chat-widget-ui/dist/rasa-chatwidget/rasa-chatwidget.css" />
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      menuVisible: false,
      headerLoaded: false, // Nueva propiedad para controlar la animación de la cabecera
    };
  },
  methods: {
    toggleMenu() {
      this.menuVisible = !this.menuVisible;
    },
    closeMenu() {
      setTimeout(() => {
        this.menuVisible = false;
      }, 100);
    }
  },
  mounted() {
    // Una vez que el componente está montado en el DOM, activamos la animación
    this.headerLoaded = true;
  }
};
</script>

<style>
/* Estilos generales de la aplicación */
body {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
}

/* Estilos del menú */
.pagina-corporativa {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
  background-color: #fff;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
}

.cabecera-corporativa {
  background-color: #fff;
  padding: 1rem 2rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 100;
}

/* Contenedor para el logo y el icono de casa */
.logo-container {
  display: flex;
  align-items: center;
  gap: 0.5rem; /* Espacio entre logo y el icono de casa */

  /* Estado inicial antes de la carga */
  opacity: 0;
  transform: translateY(-20px); /* Empieza 20px arriba */
}

.logo-corporativo {
  display: flex;
  align-items: center;
}

.logo-corporativo img {
  display: block;
  max-height: 50px;
  width: auto;
  border-radius: 8px;
  transition: opacity 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  box-shadow: 0 0 5px 3px rgba(0, 0, 0, 0.03);
}

.logo-corporativo img:hover {
  opacity: 0.9;
  box-shadow: 0 0 8px 5px rgba(0, 0, 0, 0.05);
}

/* Estilos para el contenedor del icono de casa y su menú */
.home-menu-container {
  position: relative;
}

.menu-corporativo ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  align-items: center;
}

.menu-item-corporativo {
  margin-left: 1.5rem;
}

.menu-item-link {
  text-decoration: none;
  color: #555;
  font-weight: 500;
  transition: color 0.3s ease;
  padding: 0.5rem 0;
  display: flex;
  align-items: center;
  font-size: 1rem;
}

.menu-item-link:hover {
  color: #007bff;
}

/* Estilos del menú desplegable en el icono de casa */
.dropdown-corporativo {
  position: relative;
}

.home-icon {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: #555;
  font-weight: 500;
  transition: color 0.3s ease;
  padding: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
}

.home-icon:hover {
  color: #007bff;
}

.dropdown-content-corporativo {
  position: absolute;
  top: 100%;
  left: 0;
  background-color: #fff;
  min-width: 220px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
  z-index: 1000;
  border-radius: 4px;
  padding: 0.5rem 0;
  list-style: none;
  margin: 0;
  transform-origin: top;
}

.dropdown-content-corporativo li a,
.dropdown-content-corporativo li router-link {
  color: #555;
  padding: 0.8rem 1rem;
  text-decoration: none;
  display: flex;
  align-items: center;
  transition: background-color 0.2s ease, color 0.3s ease;
  font-weight: 500;
  font-size: 1rem;
}

.dropdown-content-corporativo li a:hover,
.dropdown-content-corporativo li router-link:hover {
  background-color: #f0f0f0;
  color: #007bff;
}

.menu-icon {
  margin-right: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
}


/* --- ESTILOS DE TRANSICIÓN PARA EL MENÚ DESPLEGABLE (RESPUESTA ANTERIOR) --- */
.dropdown-enter-active, .dropdown-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.dropdown-enter-from, .dropdown-leave-to {
  opacity: 0;
  transform: scaleY(0.8);
}

.dropdown-enter-to, .dropdown-leave-from {
  opacity: 1;
  transform: scaleY(1);
}
/* --- FIN DE ESTILOS DE TRANSICIÓN --- */


/* --- NUEVOS ESTILOS PARA LA ANIMACIÓN DE ENTRADA DE LA CABECERA --- */

/* Estado inicial antes de la carga */
.menu-corporativo {
  opacity: 0;
  transform: translateY(-20px); /* Empieza 20px arriba */
}

/* Estado final (animado) cuando la clase 'header-loaded' está presente en la cabecera */
.cabecera-corporativa.header-loaded .logo-container {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out; /* Animación más larga */
}

.cabecera-corporativa.header-loaded .menu-corporativo {
  opacity: 1;
  transform: translateY(0);
  /* Animación con un pequeño retraso */
  transition: opacity 0.6s ease-out 0.2s, transform 0.6s ease-out 0.2s;
}

/* --- FIN DE NUEVOS ESTILOS --- */


/* Estilos de la sección secundaria y el chatbot */
.seccion-secundaria-corporativa {
  background-color: #e9ecef;
  padding: 3rem 2rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.info-corporativa h3 {
  font-size: 2rem;
  color: #343a40;
  margin-bottom: 1rem;
}

.info-corporativa p {
  color: #6c757d;
  margin-bottom: 0.8rem;
}

.info-corporativa .correo-soporte-corporativa {
  font-weight: bold;
  color: #007bff;
}

.video-inferior-blanco {
  width: 100%;
  max-width: 700px;
}

.video-container-corporativo {
  width: 100%;
  border-radius: 6px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.video-container-corporativa video {
  display: block;
  width: 100%;
  height: auto;
}
</style>