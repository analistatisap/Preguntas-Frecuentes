<template>
  <div class="portales-page">
    <div v-for="(seccion, seccionIndex) in seccionesPortales" :key="'seccion-' + seccionIndex">
      <h2>{{ seccion.titulo }}</h2>
      <div class="portal-container">
        <div class="portal-card" v-for="(portal, portalIndex) in seccion.portales" :key="'portal-' + seccionIndex + '-' + portalIndex">
          <img :src="portal.imagen" :alt="portal.alt">
          <h3>{{ portal.titulo }}</h3>
          <p>{{ portal.descripcion && portal.descripcion.length > 60 ? portal.descripcion.slice(0, 60) + '...' : portal.descripcion }}</p>
          <button @click="descargarArchivo(portal.link)">INGRESAR</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Portales',
  data() {
    return {
      // Estructura de datos agrupada por secciones
      seccionesPortales: [
        {
          titulo: 'PORTAL DE APLICACIONES WEB',
          portales: [

            {
              imagen: '/imagen3.png', // Reemplaza con la ruta de tu imagen
              titulo: 'Citas en bodega',
              descripcion: 'Aquí podrás encontrar información del portal citas en bodega.',
              link: 'https://entregabodega.grupodecor.com/'
            },
             {
              imagen: '/imagen3.png', // Reemplaza con la ruta de tu imagen
              titulo: 'GDecorbot',
              descripcion: 'Aquí podrás accder al chatbot para realizar diferentes tramites como descargar desprendibles de pagos entre otros.',
              link: 'https://decorghnet.grupodecor.com:5450/chatbot_decor/'
            },
            // Puedes añadir más portales web aquí
          ]
        },
        {
          titulo: 'PORTALES SAP',
          portales: [
            // Añade aquí los datos de tus portales SAP

            {
              imagen: '/imagen3.png', // Reemplaza con la ruta de tu imagen
              titulo: 'Gestor claves',
              descripcion: 'Aquí podrás encontrar gestionar las claves del CRM y ERP logon.',
              link: 'https://gestionclavesap.grupodecor.com/'
            },
             {
              imagen: '/sap-gui.png', // Reemplaza con la ruta de la imagen para SAP GUI
              titulo: 'CRM',
              descripcion: 'Podras ingresar al CRM.',
              link: 'https://decorcrmprd.decorceramica.com:41212/sap(bD1lcyZjPTMwMCZkPW1pbg==)/bc/bsp/sap/crm_ui_start/default.htm?sap-client=300&sap-language=ES' // <-- Pega la URL (quizás un manual) para SAP GUI aquí
            },
             {
              imagen: '/sap-business-one.png', // Reemplaza con la ruta de la imagen para SAP Business One
              titulo: 'SAP BO',
              descripcion: 'Podras ingresar a Sap BO.',
              link: 'http://bo.decorceramica.com:8080/BOE/BI' // <-- Pega la URL para SAP Business One aquí
            },
            // Puedes añadir más portales SAP aquí
          ]
        },
        {
          titulo: 'WEBS CORPORATIVAS',
          portales: [
            // Añade aquí los datos de tus webs corporativas
            {
              imagen: '/web-corporativa-1.png', // Reemplaza con la ruta de la imagen para la Web Corporativa 1
              titulo: 'Decorcerámica',
              descripcion: 'Portal de clientes Decorceramica.',
              link: 'https://www.decorceramica.com/' // <-- Pega la URL para el Sitio Web Principal aquí
            },
             {
              imagen: '/intranet.png', // Reemplaza con la ruta de la imagen para la Intranet
              titulo: 'NovaCasa',
              descripcion: 'Acceso al portal de Novacasa.',
              link: 'https://www.novacasacenter.com/' // <-- Pega la URL para la Intranet aquí
            },
            // Puedes añadir más webs corporativas aquí
          ]
        }
      ]
    };
  },
  methods: {
    descargarArchivo(url) {
      // Esta función abre la URL en una nueva pestaña
      window.open(url, '_blank');
      console.log('Abriendo URL:', url);
    }
  }
};
</script>

<style scoped>
.portales-page {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f4f4f4; /* Un fondo similar al de la imagen */
}

h2 {
  color: #333;
  margin-top: 2rem; /* Añadir espacio arriba para el segundo título */
  margin-bottom: 1.5rem;
  text-align: center; /* Centrar el título */
  width: 100%; /* Asegurar que ocupe el ancho para centrar */
}

/* Aseguramos que el primer h2 no tenga margin-top si es el primero */
.portales-page > div:first-child h2 {
    margin-top: 0;
}


.portal-container {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 2rem; /* Espacio debajo de cada contenedor de portales */
  width: 100%; /* Asegurar que el contenedor use el ancho disponible */
}

.portal-card {
  background-color: #e0e0e0; /* Un color de tarjeta similar */
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  width: 300px; /* Ajusta el ancho según necesites */
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* Para empujar el botón hacia abajo si es necesario */
}

.portal-card img {
  width: 100%;
  height: auto;
  display: block;
}

.portal-card h3 {
  color: #333;
  padding: 1rem;
  margin-bottom: 0.5rem; /* Espacio reducido */
  text-align: center;
}

.portal-card p {
  color: #555;
  padding: 0 1rem; /* Ajuste de padding */
  margin-top: 0;
  text-align: center;
  flex-grow: 1; /* Permite que el párrafo ocupe espacio flexible */
}

.portal-card button {
  background-color: #28a745; /* Un color verde para indicar acción */
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  cursor: pointer;
  font-size: 1rem;
  border-radius: 0 0 8px 8px;
  transition: background-color 0.3s ease;
  width: 100%; /* Asegura que el botón ocupe todo el ancho inferior */
}

.portal-card button:hover {
  background-color: #1e7e34;
}
</style>