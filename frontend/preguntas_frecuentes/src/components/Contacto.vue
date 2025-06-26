<template>
  <div class="pagina-contacto">
    <section class="contacto-seccion">
      <div class="contacto-izquierda">
        <h2>ÁREA DE TECNOLOGÍA DE LA INFORMACIÓN</h2>
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
              required
              aria-labelledby="nombre-label"
              aria-describedby="nombre-error"
              :aria-invalid="!!errors.nombre"
            >
            <span v-if="errors.nombre" id="nombre-error" class="error-text" role="alert">{{ errors.nombre }}</span>
          </div>
          <div class="campo">
            <label for="apellido" id="apellido-label">APELLIDO</label>
            <input 
              type="text" 
              id="apellido" 
              placeholder="Tu apellido" 
              v-model="formData.apellido" 
              required
              aria-labelledby="apellido-label"
              aria-describedby="apellido-error"
              :aria-invalid="!!errors.apellido"
            >
            <span v-if="errors.apellido" id="apellido-error" class="error-text" role="alert">{{ errors.apellido }}</span>
          </div>
          <div class="campo">
            <label for="correo" id="correo-label">CORREO</label>
            <input 
              type="email" 
              id="correo" 
              placeholder="Tu correo electrónico" 
              v-model="formData.correo" 
              required
              aria-labelledby="correo-label"
              aria-describedby="correo-error"
              :aria-invalid="!!errors.correo"
            >
            <span v-if="errors.correo" id="correo-error" class="error-text" role="alert">{{ errors.correo }}</span>
          </div>
          <div class="campo mensaje-campo">
            <label for="mensaje" id="mensaje-label">MENSAJE</label>
            <textarea 
              id="mensaje" 
              placeholder="Escribe tu mensaje" 
              v-model="formData.mensaje" 
              required
              aria-labelledby="mensaje-label"
              aria-describedby="mensaje-error"
              :aria-invalid="!!errors.mensaje"
            ></textarea>
            <span v-if="errors.mensaje" id="mensaje-error" class="error-text" role="alert">{{ errors.mensaje }}</span>
          </div>
          <button 
            type="submit" 
            class="boton-enviar"
            :disabled="loading"
            :aria-busy="loading"
          >
            {{ loading ? 'Enviando...' : 'ENVIAR' }}
          </button>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
import { useToast } from 'vue-toastification';
import { fetchWithAuth } from '@/utils/authFetch';

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
      loading: false
    };
  },
  methods: {
    validateForm() {
      const errors = {};
      
      // Validar nombre
      if (!this.formData.nombre.trim()) {
        errors.nombre = 'El nombre es obligatorio';
      } else if (this.formData.nombre.trim().length < 2) {
        errors.nombre = 'El nombre debe tener al menos 2 caracteres';
      }
      
      // Validar apellido
      if (!this.formData.apellido.trim()) {
        errors.apellido = 'El apellido es obligatorio';
      } else if (this.formData.apellido.trim().length < 2) {
        errors.apellido = 'El apellido debe tener al menos 2 caracteres';
      }
      
      // Validar correo
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!this.formData.correo.trim()) {
        errors.correo = 'El correo electrónico es obligatorio';
      } else if (!emailRegex.test(this.formData.correo)) {
        errors.correo = 'El correo electrónico no tiene un formato válido';
      }
      
      // Validar mensaje
      if (!this.formData.mensaje.trim()) {
        errors.mensaje = 'El mensaje es obligatorio';
      } else if (this.formData.mensaje.trim().length < 10) {
        errors.mensaje = 'El mensaje debe tener al menos 10 caracteres';
      } else if (this.formData.mensaje.trim().length > 1000) {
        errors.mensaje = 'El mensaje no puede exceder 1000 caracteres';
      }
      
      return errors;
    },
    
    async handleSubmit() {
      const toast = useToast();
      
      // Validación mejorada
      this.errors = this.validateForm();
      if (Object.keys(this.errors).length > 0) {
        Object.values(this.errors).forEach(error => toast.error(error));
        return;
      }

      try {
        this.loading = true;
        // Envia los datos al backend
        const response = await fetchWithAuth(`${this.backendUrl}/api/contacto/enviar-correo/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            ...this.formData,
            destinatario: 'jagrajales@grupodecor.com'
          }),
        });

        if (response.ok) {
          toast.success('¡Mensaje enviado con éxito!');
          // Limpiar el formulario
          this.formData.nombre = '';
          this.formData.apellido = '';
          this.formData.correo = '';
          this.formData.mensaje = '';
        } else {
          const errorData = await response.json().catch(() => ({}));
          toast.error(errorData.error || 'Error al enviar el mensaje. Por favor, inténtalo de nuevo.');
        }
      } catch (error) {
        console.error('Error al enviar el formulario:', error);
        toast.error('Ocurrió un error de conexión. Por favor, inténtalo de nuevo más tarde.');
      } finally {
        this.loading = false;
      }
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
}

.campo input[type="text"],
.campo input[type="email"],
.campo textarea {
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  color: #333;
}

.campo textarea {
  resize: vertical;
  min-height: 80px;
}

.mensaje-campo {
  flex-grow: 1; /* Para que el mensaje ocupe más espacio vertical */
}

.boton-enviar {
  background-color: #2c3e50; /* Un color oscuro para el botón */
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
  align-self: flex-end; /* Alinear el botón a la derecha */
}

.boton-enviar:hover {
  background-color: #1a2530;
}

/* Estilos para mensajes de error */
.error-text {
  color: #dc3545;
  font-size: 0.8rem;
  margin-top: 0.25rem;
  display: block;
}

.campo input[aria-invalid="true"],
.campo textarea[aria-invalid="true"] {
  border-color: #dc3545;
  box-shadow: 0 0 0 0.2rem rgba(220, 53, 69, 0.25);
}

.campo input[aria-invalid="true"]:focus,
.campo textarea[aria-invalid="true"]:focus {
  border-color: #dc3545;
  box-shadow: 0 0 0 0.2rem rgba(220, 53, 69, 0.25);
}

/* Mejoras en el botón de envío */
.boton-enviar:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
  opacity: 0.6;
}

.boton-enviar:disabled:hover {
  background-color: #6c757d;
}

/* Mejoras en la accesibilidad */
.campo input:focus,
.campo textarea:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
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
}
</style>