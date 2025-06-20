<template>
  <div class="login-page">
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Usuario</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Contraseña</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Iniciar Sesión</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await fetch('http://localhost:8000/api/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
          credentials: 'include', // Incluye cookies para sesiones
        });

        if (!response.ok) {
          throw new Error('Credenciales inválidas');
        }

        // Redirige al usuario después del login
        this.$router.push('/');
      } catch (error) {
        this.error = error.message;
      }
    },
  },
};
</script>

<style scoped>
.login-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f0f2f5; /* Fondo de página neutro y claro */
  padding: 1rem;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}

h2 {
  color: #333;
  margin-bottom: 2rem;
  font-size: 1.8rem;
  font-weight: 600;
}

form {
  background: #ffffff;
  padding: 2rem 2.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08); /* Sombra suave y moderna */
  width: 100%;
  max-width: 400px;
  box-sizing: border-box;
  text-align: left; /* Alinea el contenido del formulario a la izquierda */
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #495057; /* Color de texto de etiqueta más suave */
  font-size: 0.9rem;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 0.8rem 1rem;
  border: 1px solid #ced4da; /* Borde estándar */
  border-radius: 4px;
  box-sizing: border-box;
  font-size: 1rem;
  color: #495057;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

input[type="text"]:focus,
input[type="password"]:focus {
  border-color: #80bdff; /* Color de resaltado al enfocar (azul claro) */
  outline: 0;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25); /* Efecto de brillo al enfocar */
}

button[type="submit"] {
  width: 100%;
  padding: 0.8rem 1rem;
  background-color: #007bff; /* Color de acción principal (azul) */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  transition: background-color 0.2s ease-in-out;
  margin-top: 0.5rem; /* Espacio sobre el botón */
}

button[type="submit"]:hover {
  background-color: #0056b3; /* Tono más oscuro al pasar el cursor */
}

.error {
  background-color: #ffebee; /* Fondo rojo más claro para el error */
  color: #c62828;      /* Texto rojo más oscuro para el error */
  padding: 0.75rem 1.25rem;
  margin-top: 1.5rem;
  border: 1px solid #ef9a9a; /* Borde rojo más suave */
  border-radius: 4px;
  font-size: 0.9rem;
  text-align: center;
  width: 100%;
  max-width: 400px; /* Asegura que el mensaje de error tenga el mismo ancho que el formulario */
  box-sizing: border-box;
}
</style>