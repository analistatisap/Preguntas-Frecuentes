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
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" width="32" height="32">
            <rect y="4" width="24" height="3" rx="1.5" fill="white"/>
            <rect y="10.5" width="24" height="3" rx="1.5" fill="white"/>
            <rect y="17" width="24" height="3" rx="1.5" fill="white"/>
          </svg>
        </button>
        <ul :class="['menu-principal', { 'menu-visible': menuAbierto }]">
          <!-- Botón de cerrar solo visible en móviles -->
          <li class="close-btn" v-if="menuAbierto" @click="closeMenu">&times;</li>
          <li class="menu-item">
            <a href="#" class="menu-link" @click.prevent="navigateTo('inicio')">Inicio</a>
          </li>
          <li class="menu-item dropdown">
            <a href="#" class="menu-link" @click.prevent>Nosotros</a>
            <ul class="submenu">
              <li><a href="#" class="submenu-link" @click.prevent="navigateTo('nuestro-equipo')">Nuestro Equipo</a></li>
            </ul>
          </li>
          <li class="menu-item dropdown">
            <a href="#" class="menu-link" @click.prevent>Recursos</a>
            <ul class="submenu">
              <li><a href="#" class="submenu-link" @click.prevent="navigateTo('tips-y-manuales')">Tips y Manuales</a></li>
              <li><a href="#" class="submenu-link" @click.prevent="navigateTo('preguntas-frecuentes')">Preguntas Frecuentes</a></li>
            </ul>
          </li>
          <li class="menu-item">
            <a href="#" class="menu-link" @click.prevent="navigateTo('portales')">Portales</a>
          </li>
          <li class="menu-item">
            <a href="#" class="menu-link" @click.prevent="navigateTo('contacto')">Contacto</a>
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
      <img src="/cinta_grupo_decor.png" alt="Cinta Grupo Decor" style="margin-top: 1rem; max-width: 400px; width: 100%; display: block; margin-left: auto; margin-right: auto;" />
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
        }
      }
    },
    logout() {
      localStorage.removeItem('user');
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      this.user = null;
      this.$router.push({ name: 'login' });
    },
    cerrarModalInactividad() {
      this.modalInactividadVisible = false;
      this.$router.push({ name: 'login' });
    },
    navigateTo(routeName) {
      this.closeMenu();
      this.$router.push({ name: routeName });
    },
  },
  watch: {
    '$route': {
      handler() {
        // Verificar usuario cuando cambia la ruta (incluyendo después del login)
        this.loadUser();
      },
      immediate: true
    }
  },
  mounted() {
    this.loadUser();

    // Timeout para cerrar sesión por inactividad
    const resetTimeout = () => {
      clearTimeout(inactivityTimeoutId);
      inactivityTimeoutId = setTimeout(() => {
        this.modalInactividadVisible = true;
      }, INACTIVITY_LIMIT);
    };

    window.addEventListener('mousemove', resetTimeout);
    window.addEventListener('keydown', resetTimeout);
    resetTimeout();
  },
  unmounted() {
    if (inactivityTimeoutId) {
      clearTimeout(inactivityTimeoutId);
    }
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
  top: 100%;
  left: 0;
  background-color: #34495e;
  list-style: none;
  padding: 0.5rem 0;
  margin: 0;
  min-width: 200px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  z-index: 1000;
}
.dropdown:hover .submenu {
  display: block;
}
.submenu-link {
  display: block;
  padding: 0.5rem 1rem;
  color: white;
  text-decoration: none;
  transition: background-color 0.3s;
}
.submenu-link:hover {
  background-color: #2c3e50;
  color: #1abc9c;
}

/* User actions */
.user-actions {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-name {
  font-weight: bold;
}

.logout-button {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.logout-button:hover {
  background-color: #c0392b;
}

/* Responsive */
@media (max-width: 768px) {
  .menu-toggle {
    display: block;
    background: none;
    border: none;
    cursor: pointer;
  }
  
  .menu-principal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 250px;
    height: 100vh;
    background-color: #2c3e50;
    flex-direction: column;
    padding: 2rem 1rem;
    z-index: 1001;
    transform: translateX(-100%);
    transition: transform 0.3s ease;
  }
  
  .menu-principal.menu-visible {
    display: flex;
    transform: translateX(0);
  }
  
  .close-btn {
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 2rem;
    cursor: pointer;
    color: white;
  }
}

@media (min-width: 769px) {
  .menu-toggle {
    display: none;
  }
}

/* Pie de página */
.pie-pagina-corporativo {
  background-color: #2c3e50;
  color: white;
  text-align: center;
  padding: 2rem;
  margin-top: auto;
}

.menu-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

@media (max-width: 768px) {
  .menu-overlay {
    display: block;
  }
}
</style>