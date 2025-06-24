<template>
  <div class="login-container">
    <div class="login-box">
      <img src="/robot.png" alt="Logo" class="login-logo">
      <h2>Iniciar Sesión</h2>
      <p>Acceso al portal de Preguntas Frecuentes</p>
      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <label for="username">Usuario</label>
          <input type="text" id="username" v-model="username" required placeholder="Tu usuario de red">
        </div>
        <div class="input-group">
          <label for="password">Contraseña</label>
          <input type="password" id="password" v-model="password" required placeholder="Tu contraseña">
        </div>
        <div v-if="error" class="error-message">{{ error }}</div>
        <button type="submit" :disabled="loading">
          {{ loading ? 'Ingresando...' : 'Ingresar' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      error: null,
    };
  },
  methods: {
    async handleLogin() {
      this.loading = true;
      this.error = null;
      try {
        const response = await fetch('/api/auth/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        });

        if (response.ok) { // Status 200-299
          const data = await response.json();
          // Guardar la información del usuario en localStorage para mantener la sesión
          localStorage.setItem('user', JSON.stringify(data.user));
          // Redirigir a la página de inicio
          this.$router.push('/');
        } else { // Status 4xx, 5xx
          // Revisa si la respuesta es JSON antes de intentar parsearla
          const contentType = response.headers.get("content-type");
          if (contentType && contentType.includes("application/json")) {
              const errorData = await response.json();
              this.error = errorData.error || `Error: ${response.statusText}`;
          } else {
              // La respuesta no es JSON (probablemente una página de error HTML para el error 500)
              if (response.status === 500) {
                  this.error = 'Error interno del servidor. Por favor, contacte al administrador.';
              } else {
                  this.error = `Error inesperado del servidor (Código: ${response.status}).`;
              }
          }
        }
      } catch (err) {
        console.error('Error de red durante el login:', err);
        this.error = 'No se pudo conectar con el servidor. Revisa tu conexión de red.';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  background-color: #f0f2f5;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  z-index: 2000; /* Asegura que esté por encima de todo */
}

.login-box {
  background: white;
  padding: 2.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.login-logo {
  max-width: 80px;
  margin-bottom: 1rem;
  border-radius: 8px;
}

.input-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

.input-group input {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.error-message {
  color: #d93025;
  margin-bottom: 1rem;
}
</style>
