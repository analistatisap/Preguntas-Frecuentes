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
import { useToast } from 'vue-toastification';
import { fetchWithAuth } from '@/utils/authFetch';

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
    validateForm() {
      const errors = [];
      
      if (!this.username.trim()) {
        errors.push('El usuario es obligatorio');
      }
      
      if (!this.password.trim()) {
        errors.push('La contraseña es obligatoria');
      }
      
      return errors;
    },
    
    async handleLogin() {
      this.loading = true;
      this.error = null;
      const toast = useToast();
      
      // Validación del formulario
      const errors = this.validateForm();
      if (errors.length > 0) {
        errors.forEach(error => toast.error(error));
        this.loading = false;
        return;
      }
      
      try {
        const response = await fetchWithAuth('http://172.16.29.5:8000/api/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.username.trim(),
            password: this.password,
          }),
        });

        if (response.ok) {
          const data = await response.json();
          // Guardar el token si viene en la respuesta
          if (data.access) localStorage.setItem('access', data.access);
          if (data.refresh) localStorage.setItem('refresh', data.refresh);
          // Guardar la información del usuario en localStorage para mantener la sesión
          localStorage.setItem('user', JSON.stringify(data.user));
          
          toast.success('¡Inicio de sesión exitoso!');
          // Redirigir a la página de inicio
          this.$router.push('/');
        } else {
          // Manejo específico de errores HTTP
          const contentType = response.headers.get("content-type");
          if (contentType && contentType.includes("application/json")) {
              const errorData = await response.json();
              this.error = errorData.error || errorData.detail || `Error: ${response.statusText}`;
              toast.error(this.error);
          } else {
              if (response.status === 500) {
                  this.error = 'Error interno del servidor. Por favor, contacte al administrador.';
              } else if (response.status === 401) {
                  this.error = 'Usuario o contraseña incorrectos.';
              } else if (response.status === 403) {
                  this.error = 'Acceso denegado. Contacte al administrador.';
              } else {
                  this.error = `Error del servidor (Código: ${response.status}).`;
              }
              toast.error(this.error);
          }
        }
      } catch (err) {
        console.error('Error de red durante el login:', err);
        this.error = 'No se pudo conectar con el servidor. Revisa tu conexión de red.';
        toast.error(this.error);
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
