<template>
  <div class="login-container">
    <div class="login-box">
      <img src="/robot.png" alt="Logo" class="login-logo">
      <h2>Iniciar Sesión</h2>
      <p>Acceso al portal de Preguntas Frecuentes</p>
      <form @submit.prevent="handleLogin" role="form" aria-label="Formulario de inicio de sesión">
        <div class="input-group">
          <label for="username" id="username-label">Usuario</label>
          <input 
            type="text" 
            id="username" 
            v-model="username" 
            @blur="validateField('username')"
            @input="clearError('username')"
            required 
            placeholder="Tu usuario de red"
            aria-labelledby="username-label"
            aria-describedby="username-error"
            :aria-invalid="!!errors.username"
            :class="{ 'error-input': errors.username }"
            autocomplete="username"
          >
          <span v-if="errors.username" id="username-error" class="error-text" role="alert">
            <span class="error-icon">⚠️</span> {{ errors.username }}
          </span>
        </div>
        <div class="input-group">
          <label for="password" id="password-label">Contraseña</label>
            <input 
              :type="showPassword ? 'text' : 'password'" 
              id="password" 
              v-model="password" 
              @blur="validateField('password')"
              @input="clearError('password')"
              required 
              placeholder="Tu contraseña"
              aria-labelledby="password-label"
              aria-describedby="password-error"
              :aria-invalid="!!errors.password"
              :class="{ 'error-input': errors.password }"
              autocomplete="current-password"
            style="padding-right:2.5rem;"
            >
            <button 
              type="button" 
              class="password-toggle"
              @click="togglePassword"
              :aria-label="showPassword ? 'Ocultar contraseña' : 'Mostrar contraseña'"
            style="position:absolute; right:20px; top:50%; transform:translateY(-50%);"
            >
              {{ showPassword ? '👁️' : '👁️‍🗨️' }}
            </button>
          <span v-if="errors.password" id="password-error" class="error-text" role="alert">
            <span class="error-icon">⚠️</span> {{ errors.password }}
          </span>
        </div>
        
        <!-- Indicador de fortaleza de contraseña -->
        <div v-if="password && !errors.password" class="password-strength">
          <div class="strength-bar">
            <div 
              class="strength-fill" 
              :class="passwordStrength.class"
              :style="{ width: passwordStrength.percentage + '%' }"
            ></div>
          </div>
          <span class="strength-text">{{ passwordStrength.text }}</span>
        </div>
        
        <div v-if="error" class="error-message">
          <span class="error-icon">❌</span> {{ error }}
        </div>
        
        <button 
          type="submit" 
          :disabled="loading || !isFormValid"
          :aria-busy="loading"
          class="login-button"
        >
          <span v-if="loading" class="loading-spinner"></span>
          {{ loading ? 'Ingresando...' : 'Ingresar' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { useToast } from 'vue-toastification';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      error: null,
      errors: {},
      showPassword: false,
      touched: {
        username: false,
        password: false
      }
    };
  },
  computed: {
    isFormValid() {
      return this.username.trim() && 
             this.password.trim() && 
             Object.keys(this.errors).length === 0;
    },
    passwordStrength() {
      if (!this.password) return { class: '', percentage: 0, text: '' };
      
      let score = 0;
      const checks = {
        length: this.password.length >= 8,
        lowercase: /[a-z]/.test(this.password),
        uppercase: /[A-Z]/.test(this.password),
        numbers: /\d/.test(this.password),
        special: /[!@#$%^&*(),.?":{}|<>]/.test(this.password)
      };
      
      score += checks.length ? 20 : 0;
      score += checks.lowercase ? 20 : 0;
      score += checks.uppercase ? 20 : 0;
      score += checks.numbers ? 20 : 0;
      score += checks.special ? 20 : 0;
      
      if (score <= 40) return { class: 'weak', percentage: score, text: 'Débil' };
      if (score <= 60) return { class: 'fair', percentage: score, text: 'Regular' };
      if (score <= 80) return { class: 'good', percentage: score, text: 'Buena' };
      return { class: 'strong', percentage: score, text: 'Fuerte' };
    }
  },
  methods: {
    validateField(fieldName) {
      this.touched[fieldName] = true;
      const value = this[fieldName].trim();
      
      switch (fieldName) {
        case 'username':
          if (!value) {
            this.errors.username = 'El usuario es obligatorio';
          } else if (value.length < 3) {
            this.errors.username = 'El usuario debe tener al menos 3 caracteres';
          } else if (value.length > 50) {
            this.errors.username = 'El usuario no puede exceder 50 caracteres';
          } else if (!/^[a-zA-Z0-9._-]+$/.test(value)) {
            this.errors.username = 'El usuario solo puede contener letras, números, puntos, guiones y guiones bajos';
          } else {
            delete this.errors.username;
          }
          break;
          
        case 'password':
          if (!value) {
            this.errors.password = 'La contraseña es obligatoria';
          } else if (value.length < 6) {
            this.errors.password = 'La contraseña debe tener al menos 6 caracteres';
          } else if (value.length > 128) {
            this.errors.password = 'La contraseña no puede exceder 128 caracteres';
          } else {
            delete this.errors.password;
          }
          break;
      }
    },
    
    clearError(fieldName) {
      if (this.errors[fieldName]) {
        delete this.errors[fieldName];
      }
      if (this.error) {
        this.error = null;
      }
    },
    
    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    
    validateForm() {
      ['username', 'password'].forEach(field => {
        this.validateField(field);
      });
      
      return Object.keys(this.errors).length === 0;
    },
    
    async handleLogin() {
      this.loading = true;
      this.error = null;
      const toast = useToast();
      // Validación del formulario
      if (!this.validateForm()) {
        const firstError = Object.values(this.errors)[0];
        toast.error(firstError);
        this.loading = false;
        return;
      }
      try {
        const response = await fetch('/api/login/', {
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
          if (data.access) {
            localStorage.setItem('access', data.access);
          }
          if (data.refresh) {
            localStorage.setItem('refresh', data.refresh);
          }
          if (data.user) {
            localStorage.setItem('user', JSON.stringify(data.user));
            // Emitir evento global para actualizar el estado del usuario en App.vue
            window.dispatchEvent(new CustomEvent('user-logged-in', {
              detail: { user: data.user }
            }));
          }
          toast.success('¡Inicio de sesión exitoso! Bienvenido.');
          this.$router.push('/');
        } else {
          let errorMessage = 'Usuario o contraseña incorrectos.';
          if (response.status === 403) {
            errorMessage = 'La cuenta está inactiva o bloqueada.';
          } else if (response.status === 401) {
            errorMessage = 'Credenciales inválidas.';
          } else if (response.status === 500) {
            errorMessage = 'Error interno del servidor. Por favor, contacte al administrador.';
          } else {
            const errorData = await response.json().catch(() => ({}));
            if (errorData.detail) errorMessage = errorData.detail;
          }
          this.error = errorMessage;
          toast.error(this.error);
        }
      } catch (err) {
        this.error = 'No se pudo conectar con el servidor. Verifique su conexión de red.';
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
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  z-index: 2000; /* Asegura que esté por encima de todo */
}

.login-box {
  background: white;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  text-align: center;
  animation: slideIn 0.5s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.login-logo {
  max-width: 80px;
  margin-bottom: 1rem;
  border-radius: 8px;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.login-box h2 {
  color: #333;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.login-box p {
  color: #666;
  margin-bottom: 2rem;
  font-size: 0.9rem;
}

.input-group {
  margin-bottom: 1.5rem;
  text-align: left;
  position: relative;
}

.input-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333;
  font-weight: 600;
  font-size: 0.9rem;
}

.input-group input {
  width: 100%;
  padding: 0.8rem;
  border: 2px solid #e1e5e9;
  border-radius: 6px;
  box-sizing: border-box;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: #fff;
}

.input-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

/* Contenedor de contraseña con botón de mostrar/ocultar */
.password-container {
  position: relative;
  display: flex;
  align-items: center;
}

.password-container input {
  width: 100%;
  padding: 0.8rem;
  padding-right: 2.5rem; /* Espacio para el ícono del ojo */
  border: 2px solid #e1e5e9;
  border-radius: 6px;
  box-sizing: border-box;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: #fff;
}

.password-container input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.password-toggle {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
  color: #666;
  padding: 0;
  border-radius: 4px;
  transition: all 0.3s ease;
  height: 2rem;
  width: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.password-toggle:hover {
  background-color: #f0f0f0;
  color: #333;
}

/* Indicador de fortaleza de contraseña */
.password-strength {
  margin-bottom: 1rem;
  text-align: left;
}

.strength-bar {
  width: 100%;
  height: 4px;
  background-color: #e1e5e9;
  border-radius: 2px;
  overflow: hidden;
  margin-bottom: 0.25rem;
}

.strength-fill {
  height: 100%;
  transition: all 0.3s ease;
}

.strength-fill.weak { background-color: #dc3545; }
.strength-fill.fair { background-color: #ffc107; }
.strength-fill.good { background-color: #17a2b8; }
.strength-fill.strong { background-color: #28a745; }

.strength-text {
  font-size: 0.8rem;
  color: #666;
}

/* Estilos para mensajes de error mejorados */
.error-text {
  color: #dc3545;
  font-size: 0.85rem;
  margin-top: 0.25rem;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-weight: 500;
}

.error-icon {
  font-size: 0.75rem;
}

.error-input {
  border-color: #dc3545 !important;
  box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.1) !important;
}

.error-input:focus {
  border-color: #dc3545 !important;
  box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.1) !important;
}

.error-message {
  color: #dc3545;
  margin-bottom: 1rem;
  padding: 0.75rem;
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  border-radius: 6px;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
}

.login-button {
  width: 100%;
  padding: 0.8rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.login-button:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.login-button:disabled {
  background: #6c757d;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
  opacity: 0.6;
}

/* Spinner de carga */
.loading-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid transparent;
  border-top: 2px solid currentColor;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Responsive design */
@media (max-width: 480px) {
  .login-box {
    margin: 1rem;
    padding: 2rem;
  }
  
  .login-box h2 {
    font-size: 1.5rem;
  }
  
  .input-group input {
    font-size: 16px; /* Evita zoom en iOS */
  }
}
</style>
