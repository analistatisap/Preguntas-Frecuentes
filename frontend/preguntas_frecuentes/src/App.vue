<template>
  <div id="app">
    <!-- Overlay para cerrar el menú en móviles -->
    <div v-if="menuAbierto" class="menu-overlay" @click="closeMenu"></div>
    <header class="cabecera-corporativa" v-if="!isLoginPage">
      <div class="logo-corporativo">
        <img :src="logoUrl" alt="Logo Corporativo" />
      </div>
      <nav class="navegacion-principal" v-if="user">
        <button class="menu-toggle" @click="toggleMenu" aria-label="Toggle menu">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" width="24px" height="24px"><path d="M0 0h24v24H0z" fill="none"/><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
        </button>
        <ul :class="['menu-principal', { 'menu-visible': menuAbierto }]">
          <!-- Botón de cerrar solo visible en móviles -->
          <li class="close-btn" v-if="menuAbierto" @click="closeMenu">&times;</li>
          <li class="menu-item">
            <router-link to="/" class="menu-link">Inicio</router-link>
          </li>
          <li class="menu-item dropdown">
            <a href="#" class="menu-link" @click.prevent>Nosotros</a>
            <ul class="submenu">
              <li><router-link to="/nuestro-equipo" class="submenu-link">Nuestro Equipo</router-link></li>
            </ul>
          </li>
          <li class="menu-item dropdown">
            <a href="#" class="menu-link" @click.prevent>Recursos</a>
            <ul class="submenu">
              <li><router-link to="/tips-y-manuales" class="submenu-link">Tips y Manuales</router-link></li>
              <li><router-link to="/preguntas-frecuentes" class="submenu-link">Preguntas Frecuentes</router-link></li>
            </ul>
          </li>
          <li class="menu-item">
            <router-link to="/portales" class="menu-link">Portales</router-link>
          </li>
          <li class="menu-item">
            <router-link to="/contacto" class="menu-link">Contacto</router-link>
          </li>
        </ul>
      </nav>
      <div class="user-actions" v-if="user">
        <span class="user-name">Hola, {{ user.fullName || user.username }}</span>
        <button @click="logout" class="logout-button">Cerrar Sesión</button>
      </div>
    </header>
    <main>
      <router-view />
    </main>
    <ModalNotificacion
      :visible="modalInactividadVisible"
      titulo="Sesión finalizada"
      mensaje="Se finalizó su sesión por inactividad. Por favor, vuelva a iniciar sesión para continuar."
      @aceptar="cerrarModalInactividad"
    />
    <footer class="pie-pagina-corporativo" v-if="!isLoginPage">
      <p>&copy; 2025 GRUPO DECOR. Todos los derechos reservados.</p>
      <img src="http://atlasqa.grupodecor.com:4587/pruebas_proyectos/Vista_Reset_User/cinta_grupo_decor.png" alt="Cinta Grupo Decor" style="margin-top: 1rem; max-width: 400px; width: 100%; display: block; margin-left: auto; margin-right: auto;" />
    </footer>
  </div>
</template>

<script>
import logoUrl from '@/assets/logo.svg';
import ModalNotificacion from './components/ModalNotificacion.vue';

let inactivityTimeoutId = null;
const INACTIVITY_LIMIT = 15 * 60 * 1000; // 15 minutos

export default {
  name: 'App',
  components: { ModalNotificacion },
  data() {
    return {
      menuAbierto: false,
      logoUrl: '/logo_grupo.jpg',
      user: null,
      modalInactividadVisible: false,
    };
  },
  computed: {
    isLoginPage() {
      return this.$route.name === 'login';
    },
  },
  methods: {
    toggleMenu() {
      this.menuAbierto = !this.menuAbierto;
    },
    closeMenu() {
      this.menuAbierto = false;
    },
    loadUser() {
      const userData = localStorage.getItem('user');
      if (userData) {
        try {
          this.user = JSON.parse(userData);
        } catch (e) {
          console.error("Error al parsear datos de usuario desde localStorage", e);
          this.user = null;
          localStorage.removeItem('user'); // Limpiar dato corrupto
        }
      } else {
        this.user = null;
      }
    },
    logout(motivo) {
      localStorage.removeItem('user');
      this.user = null;
      if (motivo === 'inactividad') {
        this.modalInactividadVisible = true;
      } else {
        this.$router.push('/login');
      }
    },
    cerrarModalInactividad() {
      this.modalInactividadVisible = false;
      this.$router.push('/login');
    },
    resetInactivityTimer() {
      if (inactivityTimeoutId) clearTimeout(inactivityTimeoutId);
      if (!this.user) return;
      inactivityTimeoutId = setTimeout(() => {
        this.logout('inactividad');
      }, INACTIVITY_LIMIT);
    },
    setupInactivityListeners() {
      ['mousemove', 'keydown', 'mousedown', 'scroll', 'touchstart'].forEach(event => {
        window.addEventListener(event, this.resetInactivityTimer);
      });
      this.resetInactivityTimer();
    },
    removeInactivityListeners() {
      ['mousemove', 'keydown', 'mousedown', 'scroll', 'touchstart'].forEach(event => {
        window.removeEventListener(event, this.resetInactivityTimer);
      });
      if (inactivityTimeoutId) clearTimeout(inactivityTimeoutId);
    },
  },
  watch: {
    '$route'() {
      this.loadUser();
      this.closeMenu();
    },
    user(newVal) {
      if (newVal) {
        this.setupInactivityListeners();
      } else {
        this.removeInactivityListeners();
      }
    }
  },
  created() {
    this.loadUser();
    if (this.user) {
      this.setupInactivityListeners();
    }
  },
  beforeUnmount() {
    this.removeInactivityListeners();
  },
};
</script>

<style scoped>
/* Estilos generales */
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  font-family: 'Segoe UI', sans-serif;
}

main {
  flex: 1;
  padding-top: 80px; /* Espacio para la cabecera fija */
}

/* Cabecera */
.cabecera-corporativa {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  align-items: center;
  padding: 0 2rem;
  background-color: #2c3e50;
  color: white;
  height: 80px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  z-index: 1000;
}

.logo-corporativo img {
  height: 50px;
}

/* Navegación */
.navegacion-principal {
  margin-left: 2rem;
}

.menu-principal {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  margin: 0;
  padding: 0;
}

.menu-link {
  color: white;
  text-decoration: none;
  padding: 0.5rem 0;
  position: relative;
  transition: color 0.3s;
}

.menu-link:hover {
  color: #1abc9c;
}

/* Submenú */
.dropdown {
  position: relative;
}
.dropdown .submenu {
  display: none;
  position: absolute;
  left: 0;
  top: 100%;
  background-color: #34495e;
  list-style: none;
  padding: 0.5rem 0;
  margin-top: 0.5rem;
  border-radius: 16px; /* Más redondeado */
  box-shadow: 0 8px 32px 0 rgba(44, 62, 80, 0.18), 0 1.5px 6px 0 rgba(0,0,0,0.10);
  min-width: 170px;
  opacity: 0;
  transform: translateY(10px) scale(0.98);
  pointer-events: none;
  transition: opacity 0.25s cubic-bezier(.4,0,.2,1), transform 0.25s cubic-bezier(.4,0,.2,1);
  z-index: 1001;
}
.dropdown:hover .submenu,
.dropdown:focus-within .submenu {
  display: block;
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}
/* Triángulo indicador */
.dropdown .submenu::before {
  content: '';
  position: absolute;
  top: -10px;
  left: 24px;
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid #34495e;
  filter: drop-shadow(0 2px 2px rgba(44,62,80,0.10));
}
.submenu-link {
  color: white;
  padding: 0.7rem 1.2rem;
  display: block;
  text-decoration: none;
  border-radius: 10px;
  font-size: 1.08rem;
  transition: background 0.18s, color 0.18s, transform 0.18s;
}
.submenu-link:hover {
  background: #1abc9c;
  color: #fff;
  transform: scale(1.04);
  box-shadow: 0 2px 8px rgba(26,188,156,0.10);
}

/* Acciones de Usuario */
.user-actions {
  margin-left: auto; /* Empuja a la derecha */
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-name {
  font-weight: 500;
}

.logout-button {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 0.6rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s;
}

.logout-button:hover {
  background-color: #c0392b;
}

/* Pie de página */
.pie-pagina-corporativo {
  text-align: center;
  padding: 1.5rem;
  background-color: #2c3e50;
  color: #bdc3c7;
}

.redes-sociales a {
  color: white;
  margin: 0 0.5rem;
  text-decoration: none;
}

/* Responsividad del menú */
.menu-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
}

.menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.3);
  z-index: 1100;
}

.menu-principal {
  transition: right 0.3s;
}

@media (max-width: 600px) {
  .menu-principal {
    position: fixed;
    top: 0;
    right: -100vw;
    width: 70vw;
    max-width: 320px;
    height: 100vh;
    background: #2c3e50;
    flex-direction: column;
    align-items: flex-start;
    padding: 2rem 1.5rem 1.5rem 1.5rem;
    font-size: 1.1rem;
    z-index: 1200;
    box-shadow: 2px 0 8px rgba(0,0,0,0.15);
    overflow-y: auto;
    right: -100vw;
  }
  .menu-principal.menu-visible {
    right: 0;
  }
  .close-btn {
    display: block;
    font-size: 2.2rem;
    color: #fff;
    background: none;
    border: none;
    margin-bottom: 1.5rem;
    margin-left: auto;
    cursor: pointer;
    text-align: right;
  }
  .menu-item {
    margin-bottom: 1.2rem;
  }
  .menu-link, .submenu-link {
    font-size: 1.1rem;
    padding: 0.5rem 0;
  }
}
</style>