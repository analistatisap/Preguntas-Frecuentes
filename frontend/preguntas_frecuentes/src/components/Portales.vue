<template>
  <div class="portales-page">
    <div v-for="(seccion, seccionIndex) in seccionesPortales" :key="'seccion-' + seccionIndex">
      <h2>{{ seccion.titulo }}</h2>
      <div class="portal-container">
        <div class="portal-card" v-for="(portal, portalIndex) in seccion.portales" :key="'portal-' + seccionIndex + '-' + portalIndex">
          <div class="portal-icon-wrapper">
            <template v-if="portal.titulo.toLowerCase().includes('colaboradores')">
              <!-- Icono grupo/personas -->
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" class="portal-icon">
                <circle cx="24" cy="18" r="5" fill="#223046"/>
                <circle cx="14" cy="22" r="3" fill="#223046"/>
                <circle cx="34" cy="22" r="3" fill="#223046"/>
                <rect x="10" y="28" width="28" height="8" rx="4" fill="#223046"/>
              </svg>
            </template>
            <template v-else-if="portal.titulo.toLowerCase().includes('citas en bodega')">
              <!-- Icono camión elegante -->
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" class="portal-icon">
                <g>
                  <!-- Cabina del camión -->
                  <rect x="6" y="20" width="18" height="10" rx="3" fill="#223046"/>
                  <!-- Caja del camión -->
                  <rect x="24" y="16" width="14" height="14" rx="3" fill="#223046"/>
                  <!-- Ventana de la cabina -->
                  <rect x="10" y="22" width="6" height="5" rx="1.5" fill="#fff" opacity="0.7"/>
                  <!-- Ruedas -->
                  <circle cx="14" cy="34" r="3" fill="#223046"/>
                  <circle cx="32" cy="34" r="3" fill="#223046"/>
                  <!-- Detalle de sombra bajo el camión -->
                  <ellipse cx="24" cy="38" rx="12" ry="2" fill="#223046" opacity="0.10"/>
                </g>
              </svg>
            </template>
            <template v-else-if="portal.titulo.toLowerCase().includes('movilidad') || portal.titulo.toLowerCase().includes('intiva')">
              <!-- Icono candado -->
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" class="portal-icon">
                <rect x="14" y="22" width="20" height="14" rx="4" fill="#223046"/>
                <rect x="18" y="16" width="12" height="8" rx="6" fill="none" stroke="#223046" stroke-width="2"/>
                <circle cx="24" cy="30" r="2" fill="#fff"/>
              </svg>
            </template>
            <template v-else-if="portal.titulo.toLowerCase().includes('crm')">
              <!-- Icono persona/corbata -->
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" class="portal-icon">
                <circle cx="24" cy="16" r="6" fill="#223046"/>
                <rect x="16" y="26" width="16" height="10" rx="5" fill="#223046"/>
                <polygon points="24,22 22,32 26,32" fill="#fff"/>
              </svg>
            </template>
            <template v-else-if="portal.titulo.toLowerCase().includes('bo')">
              <!-- Icono gráfico circular -->
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" class="portal-icon">
                <circle cx="24" cy="24" r="12" fill="none" stroke="#223046" stroke-width="4"/>
                <path d="M24 24 L24 12 A12 12 0 0 1 36 24 Z" fill="#223046"/>
              </svg>
            </template>
            <template v-else-if="portal.titulo.toLowerCase().includes('gestor') || portal.titulo.toLowerCase().includes('cuentas')">
              <!-- Icono billetera/tarjeta -->
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" class="portal-icon">
                <rect x="10" y="18" width="28" height="16" rx="4" fill="#223046"/>
                <rect x="14" y="26" width="8" height="4" rx="2" fill="#fff" opacity="0.7"/>
              </svg>
            </template>
            <img v-else :src="portal.imagen" :alt="portal.alt" class="portal-icon" />
          </div>
          <h3>{{ portal.titulo }}</h3>
          <p>{{ portal.descripcion && portal.descripcion.length > 60 ? portal.descripcion.slice(0, 60) + '...' : portal.descripcion }}</p>
          <a :href="portal.link" target="_blank" class="portal-link">Acceder <span class="arrow">→</span></a>
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
              imagen: '/citabodega.png',
              titulo: 'Citas en bodega',
              descripcion: 'Aquí podrás encontrar información del portal citas en bodega.',
              link: 'https://entregabodega.grupodecor.com/'
            },
             {
              imagen: '/imagen3.png',
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

            {
              imagen: '/imagen3.png', 
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
  background-color: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(44, 62, 80, 0.10);
  overflow: hidden;
  width: 320px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem 1.2rem 1.2rem 1.2rem;
  margin-bottom: 1.5rem;
  position: relative;
  transition: box-shadow 0.2s;
}

.portal-card:hover {
  box-shadow: 0 8px 24px rgba(41,128,217,0.18), 0 1.5px 6px rgba(44,62,80,0.10);
}

.portal-icon-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-bottom: 1.2rem;
}

.portal-icon {
  width: 48px;
  height: 48px;
  object-fit: contain;
  filter: grayscale(100%) brightness(0.3) sepia(1) hue-rotate(-20deg) saturate(4);
}

.portal-card h3 {
  color: #223046;
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0 0 0.5rem 0;
  text-align: center;
}

.portal-card p {
  color: #555;
  font-size: 1rem;
  margin: 0 0 1.2rem 0;
  text-align: center;
  flex-grow: 1;
}

.portal-link {
  display: flex;
  align-items: center;
  color: #223046;
  font-weight: 500;
  text-decoration: none;
  font-size: 1.05rem;
  margin-top: auto;
  margin-left: 0;
  transition: color 0.2s;
}

.portal-link:hover {
  color: #2980d9;
}

.arrow {
  font-size: 1.2em;
  margin-left: 0.3em;
}
</style>