<template>
  <div id="app">
    <div v-if="menuAbierto" class="menu-overlay" @click="closeMenu"></div>
    <header class="cabecera-corporativa" v-if="!isLoginPage">
      <div class="logo-corporativo">
        <img :src="logoUrl" alt="Logo Corporativo" />
      </div>
      <nav class="navegacion-principal" v-if="user">
        <button class="menu-toggle" @click="toggleMenu" aria-label="Toggle menu" v-if="false">
          <span class="hamburger-line"></span>
          <span class="hamburger-line"></span>
          <span class="hamburger-line"></span>
        </button>
        <ul class="menu-principal">
          <li class="menu-item"><a href="#" class="menu-link" @click.prevent="navigateTo('inicio')">Inicio</a></li>
          <li class="menu-item"><a href="#" class="menu-link" @click.prevent="navigateTo('tips-y-manuales')">Recursos</a></li>
          <li class="menu-item"><a href="#" class="menu-link" @click.prevent="navigateTo('contacto')">Contacto</a></li>
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
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      menuAbierto: false,
      logoUrl: '/logo_grupo.jpg',
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
          console.error("Error al parsear datos de usuario", e);
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
    navigateTo(routeName) {
      this.closeMenu();
      this.$router.push({ name: routeName });
    },
  },
  watch: {
    '$route': {
      handler() {
        this.loadUser();
      },
      immediate: true
    }
  },
  mounted() {
    this.loadUser();
  },
};
</script>

<style scoped>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  font-family: 'Segoe UI', sans-serif;
}

main {
  flex: 1;
  padding-top: 80px;
}

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
  transition: color 0.3s;
}

.menu-link:hover {
  color: #1abc9c;
}

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
}

.logout-button:hover {
  background-color: #c0392b;
}
</style>