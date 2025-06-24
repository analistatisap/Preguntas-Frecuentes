<template>
  <div id="app">
    <!-- El header y el nav solo se muestran si no estamos en la página de login -->
    <header class="cabecera-corporativa" v-if="!isLoginPage">
      <div class="logo-corporativo">
        <img src="/logo.png" alt="Logo Corporativo" />
      </div>

      <!-- La navegación principal solo se muestra si el usuario está autenticado -->
      <nav class="navegacion-principal" v-if="user">
        <button class="menu-toggle" @click="toggleMenu" aria-label="Toggle menu">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" width="24px" height="24px"><path d="M0 0h24v24H0z" fill="none"/><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
        </button>
        <ul :class="['menu-principal', { 'menu-visible': menuAbierto }]">
          <li class="menu-item">
            <router-link to="/" class="menu-link">Inicio</router-link>
          </li>
          <li class="menu-item dropdown">
            <a href="#" class="menu-link" @click.prevent>Nosotros</a>
            <ul class="submenu">
              <li><router-link to="/about" class="submenu-link">Acerca de</router-link></li>
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

      <!-- Acciones de usuario: Mostrar nombre y botón de logout -->
      <div class="user-actions" v-if="user">
        <span class="user-name">Hola, {{ user.fullName || user.username }}</span>
        <button @click="logout" class="logout-button">Cerrar Sesión</button>
      </div>
    </header>

    <main>
      <router-view />
    </main>

    <!-- El footer solo se muestra si no estamos en la página de login -->
    <footer class="pie-pagina-corporativo" v-if="!isLoginPage">
      <p>&copy; 2023 GRUPO DECOR. Todos los derechos reservados.</p>
      <div class="redes-sociales">
        <a href="https://www.facebook.com" target="_blank">Facebook</a>
        <a href="https://www.twitter.com" target="_blank">Twitter</a>
        <a href="https://www.linkedin.com" target="_blank">LinkedIn</a>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      menuAbierto: false,
      user: null,
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
    logout() {
      localStorage.removeItem('user');
      this.user = null;
      this.$router.push('/login');
    },
  },
  watch: {
    '$route'() {
      // Cada vez que la ruta cambia, verificamos el estado de autenticación
      // Esto asegura que el header se actualice correctamente después del login.
      this.loadUser();
      this.closeMenu(); // Opcional: cierra el menú al navegar
    },
  },
  created() {
    // Cargar el estado del usuario cuando la aplicación se inicia
    this.loadUser();
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
.dropdown .submenu {
  display: none;
  position: absolute;
  background-color: #34495e;
  list-style: none;
  padding: 0.5rem 0; /* Mantenemos el padding interno */
  margin-top: 0; /* Eliminamos el margen que crea el espacio problemático */
  border-radius: 4px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.dropdown:hover .submenu {
  display: block;
}

.submenu-link { /* Cambiamos el selector a la nueva clase, más específico y seguro */
  color: white;
  padding: 0.5rem 1rem;
  display: block;
  text-decoration: none;
  transition: background-color 0.3s;
}

.submenu-link:hover {
  background-color: #46627f;
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

@media (max-width: 992px) {
  .user-actions {
    /* Mover las acciones al menú hamburguesa */
    display: none; 
  }

  .menu-toggle {
    display: block;
    margin-left: auto; /* Empuja el botón a la derecha */
  }

  .navegacion-principal {
    margin-left: auto;
  }

  .menu-principal {
    display: none;
    flex-direction: column;
    position: absolute;
    top: 80px;
    right: 0;
    background-color: #2c3e50;
    width: 250px;
    padding: 1rem;
  }

  .menu-principal.menu-visible {
    display: flex;
  }

  .dropdown .submenu {
    position: static;
    display: block;
    background: none;
    box-shadow: none;
    padding-left: 1rem;
  }
}
</style>