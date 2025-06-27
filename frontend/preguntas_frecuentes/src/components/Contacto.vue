<template>
  <div class="pagina-contacto">
    <section class="contacto-seccion">
      <div class="contacto-izquierda">
        <h2>ÁREA DE TECNOLOGÍA DE LA INFORMACIÓN</h2>
        <img :src="imgArbolSrc" alt="Árbol" class="img-arbol-contacto" />
        <div style="background:#f3f3f3; border-radius:8px; padding:1rem 1.2rem; margin-bottom:1.2rem; color:#333; font-size:0.98rem; text-align:left; box-shadow:0 2px 8px rgba(44,62,80,0.06); border:1px solid #e0e0e0;">
          Los correos dirigidos a <b>soportemas@itaas.net.co</b> son exclusivamente para solicitudes relacionadas con:<br>
          <ul style="margin:0.5rem 0 0.5rem 1.2rem; padding:0; color:#222;">
            <li>Soporte técnico general</li>
            <li>Impresoras</li>
            <li>Licencias</li>
          </ul>
          Para temas relacionados con <b>SAP</b>, por favor incluyan además a <b>decorsap@grupodecor.com</b> en copia.<br>
          <span style="color:#1976d2; font-weight:500;">Esto nos permite canalizar correctamente cada tipo de gestión y brindar una atención más eficiente.</span>
        </div>
        <p>CORREO</p>
        <div class="correos">
          <div class="correo-item">
            <span>SOPORTEMAS@ITAAS.NET.CO</span>
            <a href="mailto:SOPORTEMAS@ITAAS.NET.CO" class="boton-ir">IR</a>
          </div>
          <div class="correo-item">
            <span>DECORSAP@GRUPODECOR.COM</span>
            <a href="mailto:DECORSAP@GRUPODECOR.COM" class="boton-ir">IR</a>
          </div>
          </div>
      </div>
      <div class="contacto-derecha">
        <h2>CONTACTO</h2>
        <form class="formulario-contacto" @submit.prevent="handleSubmit" role="form" aria-label="Formulario de contacto">
          <div class="campo">
            <label for="nombre" id="nombre-label">NOMBRE</label>
            <input 
              type="text" 
              id="nombre" 
              placeholder="Tu nombre" 
              v-model="formData.nombre" 
              @blur="validateField('nombre')"
              @input="clearError('nombre')"
              required
              aria-labelledby="nombre-label"
              aria-describedby="nombre-error"
              :aria-invalid="!!errors.nombre"
              :class="{ 'error-input': errors.nombre }"
            >
            <span v-if="errors.nombre" id="nombre-error" class="error-text" role="alert">
              <span class="error-icon">⚠️</span> {{ errors.nombre }}
            </span>
          </div>
          <div class="campo">
            <label for="apellido" id="apellido-label">APELLIDO</label>
            <input 
              type="text" 
              id="apellido" 
              placeholder="Tu apellido" 
              v-model="formData.apellido" 
              @blur="validateField('apellido')"
              @input="clearError('apellido')"
              required
              aria-labelledby="apellido-label"
              aria-describedby="apellido-error"
              :aria-invalid="!!errors.apellido"
              :class="{ 'error-input': errors.apellido }"
            >
            <span v-if="errors.apellido" id="apellido-error" class="error-text" role="alert">
              <span class="error-icon">⚠️</span> {{ errors.apellido }}
            </span>
          </div>
          <div class="campo">
            <label for="correo" id="correo-label">CORREO</label>
            <input 
              type="email" 
              id="correo" 
              placeholder="Tu correo electrónico" 
              v-model="formData.correo" 
              @blur="validateField('correo')"
              @input="clearError('correo')"
              required
              aria-labelledby="correo-label"
              aria-describedby="correo-error"
              :aria-invalid="!!errors.correo"
              :class="{ 'error-input': errors.correo }"
              readonly
            >
            <span v-if="errors.correo" id="correo-error" class="error-text" role="alert">
              <span class="error-icon">⚠️</span> {{ errors.correo }}
            </span>
          </div>
          <div class="campo mensaje-campo">
            <label for="mensaje" id="mensaje-label">MENSAJE</label>
            <textarea 
              id="mensaje" 
              placeholder="Escribe tu mensaje" 
              v-model="formData.mensaje" 
              @blur="validateField('mensaje')"
              @input="clearError('mensaje')"
              required
              aria-labelledby="mensaje-label"
              aria-describedby="mensaje-error"
              :aria-invalid="!!errors.mensaje"
              :class="{ 'error-input': errors.mensaje }"
            ></textarea>
            <div class="mensaje-counter">
              <span :class="{ 'counter-warning': formData.mensaje.length > 800 }">
                {{ formData.mensaje.length }}/1000
              </span>
            </div>
            <span v-if="errors.mensaje" id="mensaje-error" class="error-text" role="alert">
              <span class="error-icon">⚠️</span> {{ errors.mensaje }}
            </span>
          </div>
          <button 
            type="submit" 
            class="boton-enviar"
            :disabled="loading || !isFormValid"
            :aria-busy="loading"
          >
            <span v-if="loading" class="loading-spinner"></span>
            {{ loading ? 'Enviando...' : 'ENVIAR' }}
          </button>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
import { useToast } from 'vue-toastification';

export default {
  name: 'PaginaContacto',
  data() {
    return {
      formData: {
        nombre: '',
        apellido: '',
        correo: '',
        mensaje: ''
      },
      backendUrl: 'http://172.16.29.5:8000',
      errors: {},
      loading: false,
      touched: {
        nombre: false,
        apellido: false,
        correo: false,
        mensaje: false
      }
    };
  },
  computed: {
    isFormValid() {
      return this.formData.nombre.trim() && 
             this.formData.apellido.trim() && 
             this.formData.correo.trim() && 
             this.formData.mensaje.trim() &&
             Object.keys(this.errors).length === 0;
    },
    imgArbolSrc() {
      return `${import.meta.env.BASE_URL}imgarbol.jpg`;
    }
  },
  methods: {
    validateField(fieldName) {
      this.touched[fieldName] = true;
      const value = this.formData[fieldName].trim();
      
      switch (fieldName) {
        case 'nombre':
          if (!value) {
            this.errors.nombre = 'El nombre es obligatorio';
          } else if (value.length < 2) {
            this.errors.nombre = 'El nombre debe tener al menos 2 caracteres';
          } else if (value.length > 50) {
            this.errors.nombre = 'El nombre no puede exceder 50 caracteres';
          } else if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(value)) {
            this.errors.nombre = 'El nombre solo puede contener letras y espacios';
          } else {
            delete this.errors.nombre;
          }
          break;
          
        case 'apellido':
          if (!value) {
            this.errors.apellido = 'El apellido es obligatorio';
          } else if (value.length < 2) {
            this.errors.apellido = 'El apellido debe tener al menos 2 caracteres';
          } else if (value.length > 50) {
            this.errors.apellido = 'El apellido no puede exceder 50 caracteres';
          } else if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(value)) {
            this.errors.apellido = 'El apellido solo puede contener letras y espacios';
          } else {
            delete this.errors.apellido;
          }
          break;
          
        case 'correo':
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!value) {
            this.errors.correo = 'El correo electrónico es obligatorio';
          } else if (!emailRegex.test(value)) {
            this.errors.correo = 'El correo electrónico no tiene un formato válido';
          } else if (value.length > 100) {
            this.errors.correo = 'El correo electrónico no puede exceder 100 caracteres';
          } else {
            delete this.errors.correo;
          }
          break;
          
        case 'mensaje':
          if (!value) {
            this.errors.mensaje = 'El mensaje es obligatorio';
          } else if (value.length < 10) {
            this.errors.mensaje = 'El mensaje debe tener al menos 10 caracteres';
          } else if (value.length > 1000) {
            this.errors.mensaje = 'El mensaje no puede exceder 1000 caracteres';
          } else {
            delete this.errors.mensaje;
          }
          break;
      }
    },
    
    clearError(fieldName) {
      if (this.errors[fieldName]) {
        delete this.errors[fieldName];
      }
    },
    
    validateForm() {
      ['nombre', 'apellido', 'correo', 'mensaje'].forEach(field => {
        this.validateField(field);
      });
      
      return Object.keys(this.errors).length === 0;
    },
    
    async handleSubmit() {
      const toast = useToast();
      
      // Validación completa del formulario
      if (!this.validateForm()) {
        // Mostrar el primer error encontrado
        const firstError = Object.values(this.errors)[0];
        toast.error(firstError);
        return;
      }

      try {
        this.loading = true;
        
        // Usar fetch normal en lugar de fetchWithAuth para evitar redirecciones
        const response = await fetch(`${this.backendUrl}/api/contacto/enviar-correo/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            ...this.formData,
            destinatario: 'jagrajales@grupodecor.com'
          }),
        });

        console.log('Respuesta del servidor:', response.status, response.statusText);

        if (response.ok) {
          const responseData = await response.json().catch(() => ({}));
          console.log('Datos de respuesta:', responseData);
          
          toast.success('¡Mensaje enviado con éxito! Te responderemos pronto.');
          
          // Pequeño delay para que el usuario vea la notificación antes de limpiar el formulario
          setTimeout(() => {
            this.resetForm();
          }, 1500);
        } else {
          const errorData = await response.json().catch(() => ({}));
          console.log('Error del servidor:', errorData);
          
          let errorMessage = 'Error al enviar el mensaje. Por favor, inténtalo de nuevo.';
          
          if (errorData.error) {
            errorMessage = errorData.error;
          } else if (errorData.message) {
            errorMessage = errorData.message;
          } else if (errorData.detail) {
            errorMessage = errorData.detail;
          } else if (response.status === 400) {
            errorMessage = 'Datos del formulario inválidos. Verifica la información ingresada.';
          } else if (response.status === 500) {
            errorMessage = 'Error interno del servidor. Por favor, inténtalo más tarde.';
          } else if (response.status === 403) {
            errorMessage = 'Acceso denegado. Verifica tus permisos.';
          }
          
          toast.error(errorMessage);
        }
      } catch (error) {
        console.error('Error al enviar el formulario:', error);
        
        let errorMessage = 'Ocurrió un error inesperado. Por favor, inténtalo de nuevo más tarde.';
        
        if (error.name === 'TypeError' && error.message.includes('fetch')) {
          errorMessage = 'Error de conexión. Verifica tu conexión a internet e inténtalo de nuevo.';
        } else if (error.name === 'AbortError') {
          errorMessage = 'La petición fue cancelada. Inténtalo de nuevo.';
        }
        
        toast.error(errorMessage);
      } finally {
        this.loading = false;
      }
    },
    
    resetForm() {
      this.formData = {
        nombre: '',
        apellido: '',
        correo: '',
        mensaje: ''
      };
      this.errors = {};
      this.touched = {
        nombre: false,
        apellido: false,
        correo: false,
        mensaje: false
      };
    }
  },
  mounted() {
    // Autocompletar el correo con el email del usuario autenticado
    const user = JSON.parse(localStorage.getItem('user'));
    if (user && user.email) {
      this.formData.correo = user.email;
      console.log('Correo autocompletado:', this.formData.correo);
      
    }
  },
};
</script>

<style scoped>
.pagina-contacto {
  padding: 2rem;
  background-color: #f9f9f9; /* Un fondo general */
}

.contacto-seccion {
  display: flex;
  gap: 2rem;
  max-width: 960px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #e0e0e0; /* Un fondo similar al de la imagen */
  border-radius: 8px;
}

.contacto-izquierda {
  flex: 1;
  padding: 1.5rem;
  background-color: #d0d0d0; /* Un fondo para el área izquierda */
  border-radius: 6px;
  text-align: center;
}

.contacto-izquierda h2 {
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 1rem;
}

.contacto-izquierda p {
  color: #555;
  margin-bottom: 0.5rem;
}

.correos {
  margin-top: 1rem;
}

.correo-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.8rem;
  padding: 0.5rem;
  background-color: #c0c0c0; /* Fondo para cada correo */
  border-radius: 4px;
}

.correo-item span {
  color: #333;
  font-size: 0.9rem;
}

/* Aseguramos que los estilos del botón se apliquen al enlace */
.boton-ir {
  background-color: #2c3e50; /* Un color oscuro para el botón */
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.8rem;
  transition: background-color 0.3s ease;
  text-decoration: none; /* Quitar el subrayado por defecto de los enlaces */
  display: inline-block; /* Asegurar que padding y border funcionen como en un botón */
  text-align: center; /* Centrar el texto si el padding lo requiere */
}

.boton-ir:hover {
  background-color: #1a2530;
}

.contacto-derecha {
  flex: 1;
  padding: 1.5rem;
  background-color: #c0c0c0; /* Un fondo para el área derecha */
  border-radius: 6px;
}

.contacto-derecha h2 {
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 1rem;
  text-align: center;
}

.formulario-contacto {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.campo {
  display: flex;
  flex-direction: column;
}

.campo label {
  font-size: 0.9rem;
  color: #555;
  margin-bottom: 0.3rem;
  font-weight: 600;
}

.campo input[type="text"],
.campo input[type="email"],
.campo textarea {
  padding: 0.8rem;
  border: 2px solid #e1e5e9;
  border-radius: 6px;
  font-size: 1rem;
  color: #333;
  transition: all 0.3s ease;
  background: #fff;
}

.campo input[type="text"]:focus,
.campo input[type="email"]:focus,
.campo textarea:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1);
}

.campo textarea {
  resize: vertical;
  min-height: 80px;
}

.mensaje-campo {
  flex-grow: 1; /* Para que el mensaje ocupe más espacio vertical */
}

.mensaje-counter {
  text-align: right;
  font-size: 0.8rem;
  color: #666;
  margin-top: 0.25rem;
}

.counter-warning {
  color: #ffc107;
  font-weight: 600;
}

.boton-enviar {
  background-color: #2c3e50; /* Un color oscuro para el botón */
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.3s ease;
  align-self: flex-end; /* Alinear el botón a la derecha */
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.boton-enviar:hover:not(:disabled) {
  background-color: #1a2530;
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
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

/* Mejoras en el botón de envío */
.boton-enviar:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
  opacity: 0.6;
  transform: none;
  box-shadow: none;
}

.boton-enviar:disabled:hover {
  background-color: #6c757d;
  transform: none;
  box-shadow: none;
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

/* Responsive adjustments */
@media (max-width: 768px) {
  .contacto-seccion {
    flex-direction: column;
  }

  .contacto-izquierda,
  .contacto-derecha {
    flex: none;
    width: 100%;
    padding: 1rem;
  }
  
  .boton-enviar {
    align-self: stretch;
  }
  
  .correo-item {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
  }
  
  .pagina-contacto {
    padding: 1rem;
  }
}

.img-arbol-contacto {
  display: block;
  margin: 1.5rem auto 1rem auto;
  max-width: 90px;
  width: 100%;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
</style>