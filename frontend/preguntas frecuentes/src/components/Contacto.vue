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
        <form class="formulario-contacto" @submit.prevent="handleSubmit">
          <div class="campo">
            <label for="nombre">NOMBRE</label>
            <input type="text" id="nombre" placeholder="Tu nombre" v-model="formData.nombre" required>
          </div>
          <div class="campo">
            <label for="apellido">APELLIDO</label>
            <input type="text" id="apellido" placeholder="Tu apellido" v-model="formData.apellido" required>
          </div>
          <div class="campo">
            <label for="correo">CORREO</label>
            <input type="email" id="correo" placeholder="Tu correo electrónico" v-model="formData.correo" required>
          </div>
          <div class="campo mensaje-campo">
            <label for="mensaje">MENSAJE</label>
            <textarea id="mensaje" placeholder="Escribe tu mensaje" v-model="formData.mensaje" required></textarea>
          </div>
          <button type="submit" class="boton-enviar">ENVIAR</button>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'PaginaContacto',
  data() {
    return {
      formData: {
        nombre: '',
        apellido: '',
        correo: '',
        mensaje: ''
      }
    };
  },
  methods: {
    async handleSubmit() {
      // Validación básica (puedes añadir más si es necesario)
      if (!this.formData.nombre || !this.formData.apellido || !this.formData.correo || !this.formData.mensaje) {
        alert('Por favor, completa todos los campos.');
        return;
      }

      try {
        // IMPORTANTE: Reemplaza '/api/enviar-correo' con la URL real de tu endpoint en el backend.
        // Este endpoint es el que realmente enviará el correo.
        const response = await fetch('http://127.0.0.1:8000/api/contacto/enviar-correo/', { // URL del backend
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            ...this.formData,
            destinatario: 'jagrajales@grupodecor.com' // El correo al que se enviará
          }),
        });

        if (response.ok) {
          alert('¡Mensaje enviado con éxito!');
          // Limpiar el formulario
          this.formData.nombre = '';
          this.formData.apellido = '';
          this.formData.correo = '';
          this.formData.mensaje = '';
        } else {
          alert('Error al enviar el mensaje. Por favor, inténtalo de nuevo.');
        }
      } catch (error) {
        console.error('Error al enviar el formulario:', error);
        alert('Ocurrió un error de conexión. Por favor, inténtalo de nuevo más tarde.');
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

/* Responsive adjustments */
@media (max-width: 768px) {
  .contacto-seccion {
    flex-direction: column;
  }

  .contacto-izquierda,
  .contacto-derecha {
    flex: none; /* Remove flex grow on smaller screens */
    width: 100%; /* Make them take full width */
    padding: 1rem; /* Adjust padding */
  }
   .boton-enviar {
        align-self: stretch; /* Estirar el botón ENVIAR en pantallas pequeñas */
    }
     .correo-item {
        flex-direction: column; /* Apilar correo y botón en pantallas pequeñas */
        align-items: stretch; /* Estirar elementos */
        gap: 0.5rem; /* Espacio entre span y botón */
    }
    .correo-item span {
        text-align: center; /* Centrar texto del correo */
    }
}
</style>