<template>
  <div class="preguntas-frecuentes-page">
    <section class="hero">
      <div class="hero-content">
        <h1>Preguntas Frecuentes</h1> <p>Encuentra respuestas rápidas a tus dudas y aprende cómo sacar el máximo provecho de esta herramienta.</p>
        <div class="search-bar">
          <input type="text" placeholder="Buscar preguntas y respuestas..." v-model="searchQuery">
          <button>Buscar</button>
        </div>
      </div>
      <div class="hero-image">
        <img src="/prf.png" alt="Descripción de la imagen de ayuda">
      </div>
    </section>

    <section class="faq-categories">
      <nav class="clasificacion-preguntas">
        <button
          @click="seleccionarCategoria(null)"
          :class="{ 'categoria-activa': categoriaSeleccionada === null && !searchQuery }"
        >
          Todas las Categorías
        </button>
        <button
          v-for="(categoria, index) in categorias"
          :key="index"
          @click="seleccionarCategoria(categoria)"
          :class="{ 'categoria-activa': categoriaSeleccionada === categoria && !searchQuery }"
        >
          {{ categoria.nombre }}
        </button>
      </nav>

      <div class="listado-preguntas"> <h2 v-if="searchQuery">Resultados de búsqueda para "{{ searchQuery }}"</h2>
        <h2 v-else-if="categoriaSeleccionada">{{ categoriaSeleccionada.nombre }}</h2>
        <h2 v-else>Todas las preguntas</h2>

        <ul class="faq-list" v-if="filteredPreguntas.length > 0">
          <li
            v-for="(pregunta, index) in filteredPreguntas"
            :key="'pregunta-' + index"
            :class="{ 'pregunta-activa': pregunta.respuestaVisible }" >
            <div v-if="categoriaSeleccionada === null || searchQuery" class="category-indicator">{{ pregunta.categoriaNombre }}</div>

            <div class="pregunta-container" @click="toggleRespuesta(pregunta)">
              <div class="question">{{ pregunta.pregunta }}</div>
              <button class="toggle-respuesta-btn">
                <svg :class="{ 'rotated': pregunta.respuestaVisible }" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 15l-4-4h8z"/></svg> </button>
            </div>
            <div class="answer" :class="{ 'is-visible': pregunta.respuestaVisible }" v-html="pregunta.respuesta"></div>
            </li>
        </ul>
        <p v-else>No se encontraron preguntas {{ searchQuery ? `para "${searchQuery}"` : 'en esta sección' }}.</p>
      </div>

      <p v-if="!searchQuery && categoriaSeleccionada === null && filteredPreguntas.length === 0">Selecciona una categoría para ver las preguntas o usa la barra de búsqueda.</p>

    </section>
  </div>
</template>

<script>
export default {
  name: 'PreguntasFrecuentes',
  data() {
    return {
      searchQuery: '',
      categorias: [
        {
          nombre: 'CAJA GENERAL',
          preguntas: [
            {
              pregunta: '¿Que debo de tener en cuenta para no realizar RC en días diferentes al actual?',
              //Respuesta con formato HTML e imágenes
              respuesta: `
                <p>Desde la caja general, ingresar a opciones tratamiento: </p>
                <p><img src="/respuestaspreguntasfrecuentes/librocaja.png" alt="Imagen de Caja General"></p>
                <p>Validar que tenga las siguientes dos opciones (Periodo Visualización Hoy y Fijar fecha contable y documento igual a fecha sistema) estén marcadas de la siguiente manera:</p>
                <p><img src="/respuestaspreguntasfrecuentes/caja2.png" alt="Imagen de Opciones Tratamiento Contable"></p>
                <p class="nota"><strong>NOTA:</strong> en caso de que no se encuentren seleccionadas por defecto, se deben marcar las casillas y seleccionar el icono grabar:</p>
                <p><img src="/respuestaspreguntasfrecuentes/respuesta3caja.png" alt="Imagen del botón Grabar"></p>
                <p>Tener en cuenta, que cada que ingresen a la caja general deben validar la fecha que corresponde a la del día que ingresan, si la caja les muestra otra fecha es porque no tienen la anterior configuración, pero esto también lo solucionan oprimiendo Desde la Caja el botón "Hoy".</p>
                <p><img src="/respuestaspreguntasfrecuentes/caja4.png" alt="Imagen del botón Grabar"></p>
              `, // Usa comillas invertidas (`) para respuestas multilinea con HTML
              respuestaVisible: false
            },
          ],
        },
        {
          nombre: 'CLIENTE',
          preguntas: [
             
             { pregunta: '¿Cómo podemos abordar y solucionar el problema que surge al intentar crear cliente?', 
             respuesta: 
             '<p>1- Se debe validar la campana de los errores en el sistema Movilidad y en CRM  se debe expandir aviso de error </p><p><img src="/respuestaspreguntasfrecuentes/clientes1.png" alt="Imagen del boton de visualizar errores"></p><p><img src="/respuestaspreguntasfrecuentes/clientes2.png" alt="Imagen del boton de visualizar errores"></p><p>2- Se debe validar que si tenga Datos o Wifi </p> <p><img src="/respuestaspreguntasfrecuentes/clientes3.png" alt="Imagen visualizar si hay wifi"></p>  <p>3- Confirmar el diligenciamiento completo de todos los datos requeridos.</p> <p><img src="/respuestaspreguntasfrecuentes/clientes1.png" alt="Imagen del boton de visualizar errores"></p>', respuestaVisible: false },
             
             { pregunta: '¿Qué sucede si el sistema indica que el NIT ya existe?', 
             respuesta: '<p>El sistema mostrará un aviso indicando que el número de identificación tributaria (NIT) proporcionado ya ha sido registrado o existe. En este caso, se recomienda buscar en la base de datos de clientes para verificar si el cliente ya ha sido creado.</p>', respuestaVisible: false }, // Ejemplo con lista
             
             { pregunta: '¿El sistema indica que el NIT o cedula no es valido?',
               respuesta: '<p> Se debe validar en la pagina de Rues, si el nit existe. RUES </p>', respuestaVisible: false 
             },

             { pregunta: '¿Que acciones se debe tomar si no se visualiza el id ERP o CRM?',
               respuesta: '<p>En caso de que el ID ERP o CRM no sea visible, se debe proporcionar la opción de editar. Además, es crucial validar que todos los campos obligatorios estén debidamente diligenciados antes de proceder. </p>', respuestaVisible: false
             },
             { pregunta: '¿Qué medidas se deben tomar en caso de un error al crear una oferta desde el cliente?',
                respuesta: ' <p> Es necesario validar que el Cliente tenga el Tipo ID correcto, es decir, CRM y ERP, antes de crear la oferta.</p> <p><img src="/respuestaspreguntasfrecuentes/clientes5.png" alt="Imagen de los ID"></p>', respuestaVisible: false
             },
             { pregunta: '¿Qué medidas se deben tomar en caso de un error al crear un pedido desde el cliente?',
              respuesta: '<p>  1 Se debe verificar que el cliente tenga asignado el Tipo de ID correcto, es decir, CRM y ERP. </p> <p>2. Se debe comprobar en el área de datos de venta que el cliente no esté bloqueado por el área de Cartera antes de proceder. </p> <p>3.Se debe validar que tenga el Tipo ID: CRM y ERP.</p> <p>4.Se debe validar en Datos área de venta que el cliente no este bloqueado por el área de Cartera </p>', respuestaVisible: false  
            },
            { pregunta : 'Cómo puedo visualizar la cartera de un cliente ',
              respuesta: '<p> La cartera del cliente es un llamado del reporte de cartera, por lo tanto si no tiene datos no se muestran.</p> <p> Visualizar el estado financiero demora debido a que debe mostrar recibos, notas y facturas, favor esperar que se ejecute. </p>'
            }
          ],
        },
        {
          nombre: 'ACTIVIDADES',
          preguntas: [
              { pregunta: '¿Qué medidas deben tomarse en caso de un error al crear una actividad?', 
              respuesta: '<p> 1. Es necesario validar la campaña de errores para asegurar que los usuarios reciban notificaciones claras en caso de cualquier error durante la creación de la actividad.</p <p> 2. Se debe verificar que el dispositivo tenga conexión a Datos o Wifi antes de proceder con la creación de la actividad.</p> <p> 3. Es importante validar que todos los campos requeridos estén debidamente diligenciados antes de completar la creación de la actividad. </p>', respuestaVisible: false },

              { pregunta: '¿Qué accion se debe tomar en caso de un error al adicionar una nota?',
                respuesta: '<p> Se requiere hacer clic en Asignar nota para completar la acción de adición de la nota correctamente.</p>', respuestaVisible: false
              },

              { pregunta: '¿Por qué el sistema no permite modificar la actividad?',
                respuesta: '<p> El sistema puede no permitir la modificación de la actividad por dos razones: si la actividad no se encuentra dentro del mismo mes o si la actividad no está asignada al asesor que intenta modificarla.  </p>', respuestaVisible: false
              }
          ],
        },

        {
          nombre: 'OFERTA',
          preguntas: [
              { pregunta: '¿No puedo crear la oferta?', respuesta: '<p> 1. Es necesario validar la campaña de errores para garantizar que se notifiquen adecuadamente los errores que puedan surgir durante el proceso de creación de la oferta.</p> <p>1. Seleccionar el cliente.</p><p>2. Se debe validar que haya disponibilidad de Datos o Wifi antes de intentar crear la oferta." </p><p>3. Es crucial verificar que todos los datos requeridos estén debidamente diligenciados antes de proceder con la creación de la oferta.</p> <p>4. Se debe validar si la ruta y la clase de expedición están configuradas correctamente antes de crear la oferta.</p> <p> 5. La disponibilidad de zcre debe estar confirmada antes de intentar crear la oferta. </p>', respuestaVisible: false }, // Ejemplo con TIP
              { pregunta: '¿Cómo modificar una oferta?', 
              respuesta: '<p>Pasos para modificar ofertas: Buscar la oferta existente, hacer los cambios necesarios en productos, precios o condiciones, guardar la modificación.</p>', respuestaVisible: false },
              
              { pregunta: '¿Porqué no puedo avanzar de la pantalla inicial de crear ofertas?', 
                respuesta: 'Es necesario validar que todos los datos requeridos estén debidamente diligenciados antes de poder avanzar de la pantalla inicial de crear oferta.', respuestaVisible: false
              },
              { pregunta: '¿No me confirma las cantidades?',
                respuesta: '<p> Si las cantidades no se confirman, podría ser debido a que el centro, almacén o lote se encuentran en negativo. Es importante verificar estas condiciones antes de confirmar las cantidades. </p>', respuestaVisible: false
              },
              { pregunta: 'No puedo colocar interlucutores',
                respuesta:  '<p> 1- La  oferta debe estar abierta </p>', respuestaVisible: false
              },
              { pregunta: 'No guarda la oferta',
                respuesta: '<p> Antes de proceder, se debe validar que todos los datos estén diligenciados correctamente.</p>', respuestaVisible: false
              },
              {
                pregunta: 'No puedo colocar los descuentos',
                respuesta: '<p> Validar  si las posiciones están abiertas</p>', respuestaVisible: false
              },
              {
                pregunta: 'Por qué no puedo avanzar a la oferta de reserva ',
                respuesta: '<p> 1. Es necesario validar si la oferta está abierta antes de proceder.</p> <p>2. Se deben validar las fechas de entrega tanto en la cabecera como en las posiciones de la oferta.</p> <p> 3. Se debe verificar la disponibilidad de la oferta antes de avanzar hacia la reserva. </p> ', respuestaVisible: false
              },
              {
               pregunta: '¿No puedo pasar a pedido?',
               respuesta: ' <p> 1-Validar   si la oferta esta abierta</p> <p> 2-Validar   las fechas de entrega por cabecera y posición</p> <p> 3-Validar   la disponibilidad de la oferta</p>', respuestaVisible: false 
              },
              {
                pregunta: '¿Porque no se permite agregar posiciones?',
                respuesta: '<p> 1. Se debe validar si se ha hecho clic en editar antes de intentar agregar posiciones.</p> <p> 2- Validar si la oferta esta abierta </p>', respuestaVisible: false
              },
              {
                pregunta: 'No puedo colocar anexos',
                respuesta: '<p> Se debe validar si se ha hecho clic en editar antes de subir el anexo, y además, confirmar que el anexo se esté subiendo en formato PDF </p>', respuestaVisible: false
              },
              {
                pregunta: '¿Qué procedimiento se debe seguir antes de generar el pdf?',
                respuesta: '<p> 1. Se debe esperar a que el documento se sincronice completamente antes de generar el PDF </p>', respuestaVisible: false
              }
          ],
        },
        {
          nombre: 'PEDIDOS',
          preguntas: [
              { pregunta: '¿No puedo crear el pedido?', 
              respuesta: '<p>1. Se debe   de validar la campana de los errores</p> <p> 2. Se debe de Validar que si tenga Datos o Wifi </p> <p> 3. Se debe de validar que estén todos los datos diligenciados</p> <p> 4. Se debe de validar si las ruta, clase de Expedición esta correctas </p> <p> 5. Si la disponibilidad de ZCRE  esta confirmando </p>', respuestaVisible: false 
              },
              { pregunta: 'No me carga para crear el pedido',
                respuesta: '1-Se debe de Validar que si tenga Datos o Wifi',
                respuestaVisible: false
              },
              { pregunta: '¿ Porqué no puedo avanzar de la pantalla inicial de crear pedidos?',
                respuesta: 'Antes de proceder, se debe validar que todos los datos estén diligenciados correctamente.',
                respuestaVisible: false
              },
              { pregunta: 'No me confirma las cantidades',
                respuesta:'Si no  confirma cantidades es por que el centro, almacén o lote están en  negativo',
                respuestaVisible: false
              },
              { pregunta: 'No puedo colocar las notas',
                respuesta: 'se debe   dar clic en asignar nota',
                respuestaVisible: false
              },
              { pregunta: 'No puedo colocar interlucutores',
                respuesta: 'El pedido debe estar abierto',
                respuestaVisible: false
              },
              { pregunta: 'No guarda el pedido',
                respuesta: 'Se debe   de validar que estén todos los datos diligenciados',
                respuestaVisible: false
              },
              { pregunta: 'No puedo colocar los descuentos',
                respuesta: 'Validar   si las posiciones están abiertas',
                respuestaVisible: false
              },
              { pregunta: 'No puedo pasar a pedido', 
                respuesta: 'Validar si la oferta esta abierta',
                respuestaVisible: false
              },
              { pregunta: 'No permite agregar posiciones',
                respuesta: 'Validar   si se dio clic en editar',
                respuestaVisible: false
              },
              { pregunta:  'No puedo colocar anexos',
                respuesta: '',
                respuestaVisible: false
              },
              { pregunta: 'No puedo pasar a pdf',
                respuesta: 'Se debe   de esperar que el documento sincronice para generar el PDF',
                respuestaVisible: false
              },
              { pregunta: 'No puedo colocar anexos',
                respuesta: 'Se debe  de validar si se dio editar para subir el anexo y que se este subiendo en PDF',
                respuestaVisible: false
              }
          ],
        },
        {
          nombre: 'ENTREGA',
          preguntas: [
              { pregunta: 'No guarda la entrega', 
              respuesta: '<p> Se debe   de validar si tienen pendiente autorizaciones el pedido de venta y que la   cantidad solicitada sea la misma cantidad pedida</p>', 
              respuestaVisible: false 
              },
              { pregunta: 'No puedo buscar la entrega',
                respuesta:'Se debe   de validar el numero de la entrega',
                respuestaVisible: false
              },
              { pregunta: 'Las entregas no estan en el cliente',
                respuesta: 'En el   cliente solo se visualizan las entregas pendientes',
                respuestaVisible: false
              }
          ],
        },
        {
          nombre: 'FACTURA',
          preguntas: [
              { pregunta: '¿No puedo buscar la factura factura?', 
               respuesta: '<p> Se debe   de validar si tienen pendiente autorizaciones el pedido de venta y que la   cantidad solicitada sea la misma cantidad pedida </p>',
               respuestaVisible: false 
              },
              { pregunta: 'No sale la factura del cliente',
                respuesta: ' <p> Se debe   de validar el numero de la factura </p>',
                respuestaVisible: false
              },
              { pregunta: 'No puedo visualizar la factura',
                respuesta: ' <p> En el   cliente solo se visualizan las factura pendientes </p> ',
                respuestaVisible: false
              }
          ],
        },
        {
          nombre: 'PQR',
          preguntas: [
              { pregunta: '¿No puedo buscar un PQR?', 
              respuesta: '<pSe puede   validar desde el cliente y solo salen los PQR abiertos.</p>', 
              respuestaVisible: false 
            },
            { pregunta: 'No salen los PQR en el cliente',
              respuesta: 'No salen los PQR en el cliente',
              respuestaVisible: false
            },
            { pregunta: 'No puedo crear un PQR',
             respuesta: '<p> Desde   movilidad no se puede crear PQR </p> ',
             respuestaVisible: false
            }
          ],
        },
        {
          nombre: 'WORKFLOWS',
          preguntas: [
              { pregunta: 'No puedo contestar los WF', 
               respuesta: '<p> Desde   movilidad no se puede dar respuesta a los WF.</p>',
               respuestaVisible: false 
              },
              { pregunta: 'No se donde visualizar los wf', 
              respuesta: '<p> Se   visualizan en la pagina de inicio o en las alertas.</p>', 
              respuestaVisible:  false 
              },
          ],
        },
        {
          nombre: 'PRODUCTOS',
          preguntas: [
              { pregunta: 'No sale el producto cuando lo busco', 
                respuesta: '<p> Validar el codigo del producto.</p>', 
               respuestaVisible: false
             },
             { pregunta: 'No sale el productio cuando lo busco',
               respuesta: ' <p> Validar  el código del producto </p>',
               respuestaVisible: false
             },
             { pregunta: 'No sale la foto del producto',
               respuesta: '<p> Cuando  no salen fotos es por que no se han cargado desde el área de   comunicaciones </p>',
                respuestaVisible: false
             },
             { pregunta: 'La disponibilidad no concuerda',
               respuesta: '<p> Se debe   de validar los negativos de centros, almacenes y lotes </p>',
               respuestaVisible: false
             },
             { pregunta: 'No muestra la disponibilidad por centro',
               respuesta: '<p> Se deben   de validar los negativos</p>',
               respuestaVisible: false
             },
             { pregunta: 'No sale la ficha tecnica', 
               respuesta: '<p> Si  no   sale la ficha técnica es por que desde el área de comunicaciones no se a cargado</p>',
               respuestaVisible: false
             },
             { pregunta: 'No puedo enviar la ficha tecnica',
               respuesta: '<p> Se debe   de dar clic en enviar una copia o comunicarse con soporte técnico</p>',
               respuestaVisible: false 
             }
          ],
        },
        {
          nombre: 'ORDENES DE COMPRA',
          preguntas: [
              { pregunta: '¿Cómo liberar una OC?', 
              respuesta: '<p> 1. Para la liberación de los pedidos se utiliza la transacción ME29N, se debe tener en cuenta que la estrategia de liberación esta asociada al monto del pedido - Política de compras.</p>  <p><img src="/respuestaspreguntasfrecuentes/oc.png" alt="Liberar pedido"></p> <p> Posteriormente hacemos clic sobre el icono que se observa en la imagen:</p> <p> <img src="/respuestaspreguntasfrecuentes/liberarpedido.png" alt="Liberar pedido"> </p> <p> Una vez el pedido de compras sea liberado se cambia el icono y se indica que fue liberado: </p> <p> <img src="/respuestaspreguntasfrecuentes/liberarpedido1.png" alt="Liberar pedido"> </p>  <p> Hacemos clic en grabar y el pedido de compra queda disponible para su posterior proceso.</p>  <p> <img src="/respuestaspreguntasfrecuentes/liberarpedido2.png" alt="Liberar pedido"> </p>', 
              respuestaVisible: false 
            },
          ],
        },
        {
          nombre: 'SOLPED',
          preguntas: [
              { pregunta: '¿Comó liberar una SOLPED?', respuesta: '<p> Para liberar una Solped de manera individual se utiliza la transacción ME54N e indicamos el numero de Solped que deseamos liberar:</p> <p> <img src="/respuestaspreguntasfrecuentes/liberarsolped.png" alt="Liberar solped"> </p>  <p> Posteriormente hacemos click sobre el icono que se observa en la imagen: </p> <p> <img src="/respuestaspreguntasfrecuentes/solpped.png" alt="Liberar solped"> </p>  <p> Una vez la solped es liberada se cambia el icono y se indica que fue liberada:</p>', respuestaVisible: false },
              { pregunta: '¿Porqué la SOLPED no genero liberación',
                respuesta: '<p> La novedad se pudo haber presentado por dos posibles causas: </p>  <p> Existen grupos de compras diferentes entre las posiciones: </p> <p>  </p> ',
                respuestaVisible: false

              }
             
          ],
        },
      ],
      categoriaSeleccionada: null, // null significa "Todas las categorías" inicialmente
    };
  },
  computed: {
    filteredPreguntas() {
      const query = this.searchQuery.toLowerCase().trim();

      let allQuestions = [];
      this.categorias.forEach(categoria => {
        const questionsWithCategory = categoria.preguntas.map(pregunta => ({
          ...pregunta,
          // Asegurarse de que respuestaVisible está presente y es reactivo
          respuestaVisible: pregunta.respuestaVisible,
          categoriaNombre: categoria.nombre // Añadir el nombre de la categoría al objeto pregunta
        }));
        allQuestions = allQuestions.concat(questionsWithCategory);
      });


      if (query) {
        // Buscar en todas las preguntas si hay un término de búsqueda
        return allQuestions.filter(pregunta =>
          pregunta.pregunta.toLowerCase().includes(query) || pregunta.respuesta.toLowerCase().includes(query) // La búsqueda ahora buscará en el HTML de la respuesta
        );
      } else if (this.categoriaSeleccionada !== null) {
         // Si no hay búsqueda y hay una categoría seleccionada, mostrar solo esa categoría
          return allQuestions.filter(pregunta => pregunta.categoriaNombre === this.categoriaSeleccionada.nombre);

      } else {
          // Si no hay búsqueda y no hay categoría seleccionada, mostrar todas las preguntas
          return allQuestions;
      }
    },
  },
 methods: {
    seleccionarCategoria(categoria) {
      this.categoriaSeleccionada = categoria;
      this.searchQuery = ''; // Limpiar la búsqueda al seleccionar una categoría
        // Ocultar todas las respuestas al cambiar de categoría
        this.categorias.forEach(cat => {
           cat.preguntas.forEach(p => {
              // Usar asignación directa en Vue 3
              p.respuestaVisible = false;
           });
        });
    },
      // Método para alternar la respuesta
      toggleRespuesta(preguntaToToggle) {
          // Encontrar la pregunta original en el array de datos
          let foundQuestion = null;
          for (const categoria of this.categorias) {
              foundQuestion = categoria.preguntas.find(p => p.pregunta === preguntaToToggle.pregunta && categoria.nombre === preguntaToToggle.categoriaNombre);
              if (foundQuestion) break;
          }

          if (foundQuestion) {
              // Cerrar todas las demás respuestas
              this.categorias.forEach(cat => {
                  cat.preguntas.forEach(p => {
                      if (p !== foundQuestion && p.respuestaVisible) {
                           // Usar asignación directa en Vue 3
                           p.respuestaVisible = false;
                       }
                   });
               });
              // Alternar la visibilidad de la pregunta encontrada usando asignación directa
              foundQuestion.respuestaVisible = !foundQuestion.respuestaVisible;
          } else {
               console.error("Could not find original question in data for toggling.");
          }
      }
  },
    watch: {
    // Observar cambios en searchQuery para ocultar respuestas al buscar
    searchQuery(newQuery, oldQuery) {
        if (newQuery) {
          // Ocultar todas las respuestas cuando se inicia una búsqueda
          this.categorias.forEach(categoria => {
              categoria.preguntas.forEach(pregunta => {
                   // Usar asignación directa en Vue 3
                   pregunta.respuestaVisible = false;
              });
             });
            // Deseleccionar la categoría al iniciar una búsqueda
            this.categoriaSeleccionada = null;
        }
    }
  },
  mounted() {
      // Asegurarse de que todas las preguntas tienen la propiedad respuestaVisible al cargar
      // Esto ya se maneja en data() al usar .map, que crea la propiedad inicialmente.
      // No necesitas hacer nada extra aquí a menos que la propiedad no se esté creando en data.
  }
};
</script>

<style scoped>
.preguntas-frecuentes-page {
  padding: 2rem;
  background-color: #f9f9f9;
}

.hero {
  background-color: #3498db; /* Un color azul similar al de la imagen */
  color: white;
  padding: 3rem;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2rem;
  gap: 20px; /* Espacio entre contenido y imagen */
  flex-wrap: wrap; /* Permite que los elementos se envuelvan en pantallas pequeñas */
}

.hero-content {
  max-width: 50%;
  flex-grow: 1; /* Permite que crezca para ocupar espacio si es necesario */
  min-width: 300px; /* Ancho mínimo para evitar que se comprima demasiado */
}

.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.hero p {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.search-bar {
  display: flex;
  max-width: 400px;
  width: 100%; /* Asegura que ocupe el ancho del contenedor si es menor que max-width */
}

.search-bar input {
  flex-grow: 1;
  padding: 0.8rem;
  border: none;
  border-radius: 4px 0 0 4px;
  font-size: 1rem;
  color: #333;
}

.search-bar button {
  background-color: #2c3e50;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 0 4px 4px 0;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-bar button:hover {
  background-color: #1a2530;
}

.hero-image {
  max-width: 45%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0; /* Evita que la imagen se encoja demasiado */
  min-width: 200px; /* Ancho mínimo para la imagen */
}

.hero-image img {
  display: block;
  max-width: 100%;
  height: auto;
  border-radius: 8px; /* Bordes redondeados para la imagen */
}

.faq-categories {
  padding: 0 2rem;
}

.clasificacion-preguntas {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  overflow-x: auto;
  padding-bottom: 10px;
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.clasificacion-preguntas::-webkit-scrollbar {
    display: none;
}

.clasificacion-preguntas button {
  flex-shrink: 0;
  background: none;
  border: 1px solid #ccc;
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  cursor: pointer;
  color: #777;
  transition: color 0.3s ease-in-out, border-color 0.3s ease-in-out, background-color 0.3s ease;
  border-radius: 20px;
  white-space: nowrap;
  min-width: 120px; /* Ancho mínimo para los botones de categoría */
  text-align: center;
}

.clasificacion-preguntas button:hover,
.clasificacion-preguntas button.categoria-activa {
  color: white;
  background-color: #3498db;
  border-color: #3498db;
  font-weight: bold;
}


.listado-preguntas {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.listado-preguntas h2 {
  font-size: 1.8rem;
  color: #333;
  margin-bottom: 1rem;
  border-bottom: 2px solid #eee;
  padding-bottom: 0.5rem;
}

.faq-list {
  list-style: none;
  padding: 0;
}

.faq-list li {
  margin-bottom: 1rem;
  padding: 1rem; /* Añadido padding general a cada item */
  border-bottom: 1px solid #f0f0f0;
  transition: background-color 0.3s ease; /* Transición para hover */
  border-radius: 4px; /* Bordes redondeados para los items */
}

.faq-list li:last-child {
  border-bottom: none;
}

.faq-list li:hover {
    background-color: #f0f8ff; /* Fondo suave al pasar el ratón */
}

.faq-list li.pregunta-activa {
    background-color: #eaf4ff; /* Fondo diferente para la pregunta activa */
    border-left: 4px solid #3498db; /* Borde izquierdo para destacar */
    padding-left: calc(1rem - 4px); /* Ajuste de padding por el borde */
}


.pregunta-container {
  display: flex;
  justify-content: space-between;
  align-items: center; /* Centrar verticalmente pregunta y botón */
  cursor: pointer;
  gap: 10px;
}

.question {
  font-weight: bold;
  color: #555;
  flex-grow: 1;
}

/* Estilos para la animación de la respuesta (MODIFICADO para usar clase) */
.answer {
  color: #777;
  line-height: 1.5;
  margin-top: 0.5rem;
  padding-right: 50px; /* Ajusta si necesitas más espacio a la derecha */
  overflow: hidden; /* Oculta el contenido que excede max-height */
  /* Estado inicial colapsado */
  max-height: 0;
  opacity: 0;
  display: none; /* Oculto por defecto */
  /* Aseguramos que la transición esté definida */
  transition: max-height 0.5s ease-in-out, opacity 0.5s ease-in-out;
}

/* Estilo cuando la respuesta está visible (controlado por la clase .is-visible) */
.answer.is-visible {
    display: block; /* Hacer visible el contenedor */
    /* Usamos un max-height muy grande para asegurar que todo el contenido quepa */
    max-height: 9999px; /* Aumentado significativamente */
    opacity: 1; /* Opacidad completa */
    /* No necesitamos transición aquí */
}


/* Ajuste para asegurar que el padding no se corte en el estado colapsado */
.faq-list li .answer {
    padding-bottom: 0; /* Remueve el padding inferior cuando está colapsado */
}

.faq-list li.pregunta-activa .answer {
    padding-bottom: 1rem; /* Añade padding inferior cuando está expandido */
}

/* --- ESTILOS PARA EL CONTENIDO DENTRO DE LA RESPUESTA --- */
.answer p {
    margin-bottom: 1em; /* Espacio debajo de los párrafos */
    /* Asegúrate de que no haya margen superior en el primer párrafo si no lo deseas */
    margin-top: 0;
}

.answer p:last-child {
    margin-bottom: 0; /* No margen debajo del último párrafo */
}


.answer img {
    max-width: 100%; /* **La imagen no excederá el ancho del contenedor de respuesta** */
    height: auto; /* Mantiene la relación de aspecto */
    display: block; /* **La imagen como bloque** */
    margin: 1em auto; /* **Margen arriba y abajo y centrado horizontalmente** */
    border: 1px solid #ccc; /* **Borde sutil como en tu ejemplo** */
    padding: 5px; /* **Padding dentro del borde** */
    background-color: #fff; /* **Fondo blanco para la imagen** */
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1); /* **Sombra suave** */
    box-sizing: border-box; /* Asegura que padding y borde no aumenten el ancho */
    /* Estilos para efecto de expansión en hover */
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    cursor: zoom-in; /* Indica que la imagen se puede ampliar */
}

.answer .nota {
    background-color: #fff3cd; /* Fondo amarillo claro para notas */
    border-left: 4444px solid #ffc107; /* Borde izquierdo amarillo */ /* <-- Posible typo 4444px? */
    padding: 0.8rem 1rem; /* Padding interno */
    margin: 1em 0; /* Margen arriba y abajo */
    border-radius: 4px;
    color: #856404; /* Color de texto oscuro para contraste */
}

.answer .nota strong {
    color: #856404; /* Asegura que el "NOTA:" sea del mismo color */
}

.answer img:hover {
    transform: scale(2); /* Aumenta el tamaño de la imagen al 180% */
    box-shadow: 4px 4px 12px rgba(0,0,0,0.25); /* Sombra más pronunciada para destacar */
    /* z-index: 10; Opcional: si necesitas que la imagen se superponga a otros elementos */
}
.answer ul {
    margin-top: 1em;
    margin-bottom: 1em;
    padding-left: 1.5em; /* Indentación para la lista */
}

.answer li {
    margin-bottom: 0.5em; /* Espacio entre elementos de lista */
    /* Quitamos los estilos de borde y padding del li padre de .faq-list */
    border-bottom: none;
    padding: 0;
    background-color: transparent;
    border-left: none;
}
/* --- FIN DE NUEVOS ESTILOS --- */


.toggle-respuesta-btn {
  background: none;
  border: none;
  color: #3498db;
  cursor: pointer;
  padding: 0;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center; /* Centra el icono dentro del botón */
  width: 30px; /* Tamaño fijo para el botón */
  height: 30px; /* Tamaño fijo para el botón */
  transition: color 0.3s ease, transform 0.3s ease; /* Transición para color e ícono */
}

.toggle-respuesta-btn:hover {
  color: #1e6091;
}

.toggle-respuesta-btn svg {
    fill: currentColor; /* Usa el color del botón para el SVG */
    transition: transform 0.3s ease; /* Transición para la rotación */
}

.toggle-respuesta-btn svg.rotated {
    transform: rotate(180deg); /* Rota el icono 180 grados */
}


.category-indicator {
    font-size: 0.8rem;
    color: #888;
    margin-bottom: 0.8rem; /* Espacio ajustado */
    font-style: italic;
    text-align: right;
    width: 100%;
    padding-right: 40px; /* Ajuste para no superponer con el botón de toggle */
    box-sizing: border-box; /* Incluye padding en el ancho */
}

/* Media Queries para responsividad */
@media (max-width: 768px) {
    .hero {
        flex-direction: column; /* Apila contenido e imagen en pantallas pequeñas */
        text-align: center;
        padding: 2rem;
    }

    .hero-content {
        max-width: 100%; /* Ocupa todo el ancho */
        margin-bottom: 1.5rem;
    }

    .hero-image {
        max-width: 80%; /* Reduce el tamaño de la imagen */
    }

    .search-bar {
        max-width: 100%; /* Ocupa todo el ancho disponible */
    }

    .faq-categories {
        padding: 0 1rem; /* Reduce padding lateral */
    }

    .clasificacion-preguntas {
        flex-wrap: nowrap; /* Mantiene el scroll horizontal */
    }

    .listado-preguntas {
        padding: 1rem; /* Reduce padding del listado */
    }

    .listado-preguntas h2 {
        font-size: 1.5rem; /* Reduce tamaño del título */
    }

    .faq-list li {
        padding: 0.8rem; /* Reduce padding de los items */
    }

    .question {
        font-size: 0.95rem; /* Reduce tamaño de fuente de la pregunta */
    }

    .answer {
        padding-right: 20px; /* Ajuste de padding para la respuesta */
    }

    .category-indicator {
       padding-right: 30px; /* Ajuste de padding para el indicador */
    }
}
</style>