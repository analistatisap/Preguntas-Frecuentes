<template>
  <div class="pagina-tips-manuales">
    <h1 class="titulo-pagina">Manuales SAP</h1>
    <!-- Descripción para la sección de Manuales -->
    <p class="descripcion-pagina">
      En este espacio encontrarás material de apoyo, el cual podrás usar de soporte durante el
      desarrollo de tu gestión a través de los diferentes sistemas de Información que la compañía
      ha dispuesto para ti.
    </p>
    <div class="grid-manuales">
      <div v-for="(manual, index) in manuales" :key="index" class="cuadro-manual">
        <h3>{{ manual.titulo }}</h3>
        <div class="icono-manual">
          <a v-if="manual.archivo" :href="getManualUrl(manual.archivo)" target="_blank" class="manual-icon-link">
            <img :src="getManualIcon(manual.titulo)" :alt="manual.titulo">
            <span>Descargar</span>
          </a>
          <a v-else-if="isUrl(manual.descripcion)" :href="manual.descripcion" target="_blank" class="manual-icon-link">
            <img :src="getManualIcon(manual.titulo)" :alt="manual.titulo">
            <span>Ver Link</span>
          </a>
          <div v-else>
            <img :src="getManualIcon(manual.titulo)" :alt="manual.titulo">
          </div>
        </div>
        <p v-if="manual.descripcion && !isUrl(manual.descripcion)" class="manual-desc" v-html="manual.descripcion"></p>
      </div>
    </div>

    <hr class="section-divider">

    <h1 class="titulo-pagina">Tips</h1>
    <!-- Descripción para la sección de Tips -->
    <p class="descripcion-pagina">
      Aquí encontrarás tips visuales y consejos rápidos para optimizar tu trabajo diario.
    </p>
    <div class="grid-manuales"> 
      <div v-for="(tip, index) in tips" :key="index" class="cuadro-tip">
        <h3 v-if="tip.titulo">{{ tip.titulo }}</h3>
        <div class="imagen-tip">
          <img v-if="tip.imagen" :src="getTipUrl(tip.imagen)" :alt="tip.titulo || 'Tip Image'">
          <a v-else-if="tip.archivo" :href="getTipUrl(tip.archivo)" target="_blank">Descargar archivo</a>
        </div>
        <p v-if="tip.descripcion" class="tip-desc">{{ tip.descripcion }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TipsYManuales',
  data() {
    return {
      manuales: [],
      tips: [],
      backendUrl: 'http://172.16.29.5:8000', 
    };
  },
  methods: {
    getManualUrl(path) {
      // Si el path ya es una URL absoluta, la retorna tal cual
      if (/^https?:\/\//.test(path)) return path;
      return `${this.backendUrl}${path}`;
    },
    getTipUrl(path) {
      if (!path) return '';
      if (/^https?:\/\//.test(path)) return path;
      return `${this.backendUrl}${path}`;
    },
    isUrl(text) {
      return /^https?:\/\//.test(text);
    },
    getManualIcon(titulo) {
      const t = titulo.toLowerCase();
      if (t.includes('pdf')) return '/imgtipsymanuales/libro.png';
      if (t.includes('sap')) return '/imgtipsymanuales/engranaje.png';
      if (t.includes('guía') || t.includes('guia')) return '/imgtipsymanuales/libro.png';
      if (t.includes('política') || t.includes('politica')) return '/imgtipsymanuales/candado.png';
      if (t.includes('factura')) return '/imgtipsymanuales/facturas.png';
      if (t.includes('cliente')) return '/imgtipsymanuales/clientes.png';
      if (t.includes('pedido')) return '/imgtipsymanuales/pedidos.png';
      if (t.includes('entrega')) return '/imgtipsymanuales/entregas.png';
      if (t.includes('movilidad')) return '/imgtipsymanuales/movilidad.png';
      if (t.includes('caja')) return '/imgtipsymanuales/caja-general.png';
      // ...agrega más casos según tus imágenes...
      return '/imgtipsymanuales/libro.png'; // genérico
    },
    getPortalIcon(titulo, descripcion) {
      const t = (titulo + ' ' + (descripcion || '')).toLowerCase();
      if (t.includes('web')) return '/imgtipsymanuales/nube.png';
      if (t.includes('seguro') || t.includes('privado')) return '/imgtipsymanuales/candado.png';
      if (t.includes('clientes')) return '/imgtipsymanuales/clientes.png';
      if (t.includes('exportación') || t.includes('exportacion')) return '/imgtipsymanuales/oferta-exportacion.png';
      if (t.includes('portal')) return '/imgtipsymanuales/portal-clientes-cd.png';
      // ...agrega más casos según tus imágenes...
      return '/imgtipsymanuales/nube.png'; // genérico
    },
    async fetchManuales() {
      try {
        const token = localStorage.getItem('access');
        const res = await fetch(`${this.backendUrl}/api/recursos/manuales/`, {
          headers: {
            ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
            'Content-Type': 'application/json'
          }
        });
        if (!res.ok) throw new Error('Error al obtener manuales');
        this.manuales = await res.json();
      } catch (e) {
        this.manuales = [];
      }
    },
    async fetchTips() {
      try {
        const token = localStorage.getItem('access');
        const res = await fetch(`${this.backendUrl}/api/recursos/tips/`, {
          headers: {
            ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
            'Content-Type': 'application/json'
          }
        });
        if (!res.ok) throw new Error('Error al obtener tips');
        this.tips = await res.json();
      } catch (e) {
        this.tips = [];
      }
    },
  },
  mounted() {
    this.fetchManuales();
    this.fetchTips();
  },
};
</script>

<style scoped>
.pagina-tips-manuales {
  padding: 2rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
}

.titulo-pagina {
  text-align: center;
  color: #007bff;
  margin-bottom: 1rem;
}

.descripcion-pagina {
  text-align: center;
  color: #555;
  margin-bottom: 2rem;
}

.grid-manuales {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.cuadro-manual {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  text-align: center;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Añadir transición para box-shadow */
  cursor: pointer; /* Añadir cursor pointer para indicar que es clickeable */
}

.cuadro-manual:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); /* Efecto de sombra al pasar el mouse */
}

.icono-manual {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  margin-bottom: 1rem;
}

/* Estilo para el enlace dentro del icono */
.icono-manual .manual-icon-link {
    display: flex; /* Permite centrar la imagen dentro del enlace */
    justify-content: center;
    align-items: center;
    width: 100%; /* Asegura que el enlace ocupe el área del icono */
    height: 100%; /* Asegura que el enlace ocupe el área del icono */
    text-decoration: none; /* Quitar el subrayado del enlace */
     transition: transform 0.3s ease-in-out; /* Transición para el efecto de escala del icono */
}

/* Efecto al pasar el mouse sobre el enlace/icono */
.icono-manual .manual-icon-link:hover img {
    transform: scale(1.1); /* Hacer la imagen del icono un poco más grande al pasar el mouse */
}


.icono-manual img {
  max-width: 80%;
  max-height: 80%;
  display: block; /* Asegura que la imagen se muestre correctamente */
  object-fit: contain; /* Asegura que la imagen se ajuste sin distorsionarse */
  transition: transform 0.3s ease-in-out; /* Añadir transición también a la imagen */
}

.cuadro-manual h3 {
  color: #333;
  margin-top: 0;
  font-size: 1.2rem;
  margin-bottom: 1rem; /* Añadir margen debajo del título */
}

/* Estilos para la nueva sección de Tips */

/* Separador entre secciones */
.section-divider {
  margin: 3rem 0; /* Espacio arriba y abajo */
  border: 0;
  border-top: 1px solid #eee; /* Línea divisoria sutil */
}

/* Estilos para los cuadros de tips (similares a los manuales) */
.cuadro-tip {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  text-align: center;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  cursor: pointer; /* Indicar que es clickeable/interactivo */
}

.cuadro-tip:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

/* Contenedor de la imagen del tip */
.imagen-tip {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 150px; /* Altura ajustada para imágenes de tips */
  margin-bottom: 1rem;
}

.imagen-tip img {
  max-width: 100%;
  max-height: 100%;
  display: block;
  object-fit: contain;
  transition: transform 0.3s cubic-bezier(.4,0,.2,1), box-shadow 0.3s cubic-bezier(.4,0,.2,1), border 0.3s cubic-bezier(.4,0,.2,1);
}

/* Efecto de escala en la imagen del tip al pasar el mouse sobre el cuadro */
.cuadro-tip:hover .imagen-tip img {
  transform: scale(1.25);
  box-shadow: 0 8px 24px rgba(41,128,217,0.18), 0 1.5px 6px rgba(44,62,80,0.10);
  border: 2.5px solid #2980d9;
  z-index: 2;
}

.manual-desc {
  color: #666;
  font-size: 0.95rem;
  margin-top: 0.5rem;
}
.tip-desc {
  color: #666;
  font-size: 0.95rem;
  margin-top: 0.5rem;
}
</style>