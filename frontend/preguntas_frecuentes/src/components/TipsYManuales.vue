<template>
  <div class="pagina-tips-manuales">
    <h1 class="titulo-pagina">Manuales SAP</h1>
    <!-- Descripción para la sección de Manuales -->
    <p class="descripcion-pagina">
      En este espacio encontrarás material de apoyo, el cual podrás usar de soporte durante el
      desarrollo de tu gestión a través de los diferentes sistemas de Información que la compañía
      ha dispuesto para ti.
    </p>

    <!-- Barra de búsqueda para manuales -->
    <div class="search-container">
      <input 
        v-model="searchManuales" 
        type="text" 
        placeholder="Buscar manuales..." 
        class="search-input"
        @input="filtrarManuales"
      >
      <div class="search-icon">🔍</div>
    </div>

    <!-- Indicador de carga para manuales -->
    <div v-if="loadingManuales" class="loading-container">
      <div class="loading-spinner"></div>
      <p>Cargando manuales...</p>
    </div>

    <!-- Estado vacío para manuales -->
    <div v-else-if="manualesFiltrados.length === 0 && !loadingManuales" class="empty-state">
      <div class="empty-icon">📚</div>
      <p>{{ searchManuales ? 'No se encontraron manuales que coincidan con tu búsqueda' : 'No hay manuales disponibles' }}</p>
    </div>

    <!-- Grid de manuales -->
    <div v-else class="grid-manuales">
      <div v-for="(manual, index) in manualesFiltrados" :key="index" class="cuadro-manual">
        <h3>{{ manual.titulo }}</h3>
        <div class="icono-manual">
          <a v-if="manual.archivo" :href="getManualUrl(manual.archivo)" target="_blank" class="manual-icon-link">
            <img :src="getManualIcon(manual.titulo)" :alt="manual.titulo">
          </a>
          <a v-else-if="isUrl(manual.descripcion)" :href="manual.descripcion" target="_blank" class="manual-icon-link">
            <img :src="getManualIcon(manual.titulo)" :alt="manual.titulo">
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

    <!-- Barra de búsqueda para tips -->
    <div class="search-container">
      <input 
        v-model="searchTips" 
        type="text" 
        placeholder="Buscar tips..." 
        class="search-input"
        @input="filtrarTips"
      >
      <div class="search-icon">🔍</div>
    </div>

    <!-- Indicador de carga para tips -->
    <div v-if="loadingTips" class="loading-container">
      <div class="loading-spinner"></div>
      <p>Cargando tips...</p>
    </div>

    <!-- Estado vacío para tips -->
    <div v-else-if="tipsFiltrados.length === 0 && !loadingTips" class="empty-state">
      <div class="empty-icon">💡</div>
      <p>{{ searchTips ? 'No se encontraron tips que coincidan con tu búsqueda' : 'No hay tips disponibles' }}</p>
    </div>

    <!-- Grid de tips -->
    <div v-else class="grid-tips">
      <div v-for="(tip, index) in tipsFiltrados" :key="index" class="cuadro-tip" @click="abrirModalTip(tip)">
        <h3 v-if="tip.titulo">{{ tip.titulo }}</h3>
        <div class="imagen-tip">
          <template v-if="tip.video_url">
            <iframe v-if="isUrl(tip.video_url) && (tip.video_url.includes('youtube') || tip.video_url.includes('vimeo'))"
                    :src="getEmbedUrl(tip.video_url)" frameborder="0" allowfullscreen class="tip-video"></iframe>
            <video v-else :src="getTipUrl(tip.video_url)" controls class="tip-video"></video>
          </template>
          <video v-else-if="tip.video" :src="getTipUrl(tip.video)" controls class="tip-video"></video>
          <img v-else-if="tip.imagen" :src="getTipUrl(tip.imagen)" :alt="tip.titulo || 'Tip Image'">
          <a v-else-if="tip.archivo" :href="getTipUrl(tip.archivo)" target="_blank">Descargar archivo</a>
        </div>
        <p v-if="tip.descripcion" class="tip-desc">{{ tip.descripcion }}</p>
      </div>
    </div>

    <!-- Modal de tip -->
    <transition name="modal-fade">
      <div v-if="modalTip" class="modal-tip-overlay" @click.self="cerrarModalTip">
        <div class="modal-tip-card">
          <button class="modal-tip-close" @click="cerrarModalTip">&times;</button>
          <h2 v-if="modalTip.titulo">{{ modalTip.titulo }}</h2>
          <template v-if="modalTip.video_url">
            <iframe v-if="isUrl(modalTip.video_url) && (modalTip.video_url.includes('youtube') || modalTip.video_url.includes('vimeo'))"
                    :src="getEmbedUrl(modalTip.video_url)" frameborder="0" allowfullscreen class="tip-video-modal"></iframe>
            <video v-else :src="getTipUrl(modalTip.video_url)" controls class="tip-video-modal"></video>
          </template>
          <video v-else-if="modalTip.video" :src="getTipUrl(modalTip.video)" controls class="tip-video-modal"></video>
          <img v-else-if="modalTip.imagen" :src="getTipUrl(modalTip.imagen)" :alt="modalTip.titulo || 'Tip Image'">
          <p v-if="modalTip.descripcion" class="tip-desc-expandida">{{ modalTip.descripcion }}</p>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'TipsYManuales',
  data() {
    return {
      manuales: [],
      tips: [],
      manualesFiltrados: [],
      tipsFiltrados: [],
      searchManuales: '',
      searchTips: '',
      loadingManuales: false,
      loadingTips: false,
      backendUrl: '/api', 
      modalTip: null,
      // Cache de datos
      cache: {
        manuales: null,
        tips: null,
        lastFetch: null,
        cacheDuration: 5 * 60 * 1000 // 5 minutos
      }
    };
  },
  methods: {
    getManualUrl(path) {
      // Si el path ya es una URL absoluta, la retorna tal cual
      if (/^https?:\/\//.test(path)) return path;
      return `${this.backendUrl}${path}`;
    },
    getTipUrl(path) {
      console.log('getTipUrl:', path);
      if (!path) return '';
      // Siempre fuerza la URL correcta para cualquier caso de media
      if (path.includes('/media/')) {
        // Extrae el path a partir de /media/
        const mediaPath = path.substring(path.indexOf('/media/'));
        return `https://preguntame.grupodecor.com:5046${mediaPath}`;
      }
      return path;
    },
    isUrl(text) {
      return /^https?:\/\//.test(text);
    },
    getManualIcon(titulo) {
      const t = titulo.toLowerCase();
      if (t.includes('oferta')) return '/imgtipsymanuales/ofertas.png';
      if (t.includes('atp')) return '/imgtipsymanuales/atp.png';
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
      if(t.includes('afluencia')) return '/imgtipsymanuales/afluencia.png';
      if(t.includes('citas en bodega')) return '/imgtipsymanuales/citasenbodega.png';
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
    // Verificar si el cache es válido
    isCacheValid() {
      return this.cache.lastFetch && 
             (Date.now() - this.cache.lastFetch) < this.cache.cacheDuration;
    },
    async fetchManuales() {
      // Verificar cache primero
      if (this.isCacheValid() && this.cache.manuales) {
        this.manuales = this.cache.manuales;
        this.manualesFiltrados = [...this.manuales];
        return;
      }

      this.loadingManuales = true;
      try {
        const res = await fetch(`${this.backendUrl}/recursos/manuales/`, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        if (!res.ok) throw new Error('Error al obtener manuales');
        this.manuales = await res.json();
        this.manualesFiltrados = [...this.manuales];
        
        // Guardar en cache
        this.cache.manuales = this.manuales;
        this.cache.lastFetch = Date.now();
      } catch (e) {
        this.manuales = [];
        this.manualesFiltrados = [];
        console.error('Error fetching manuales:', e);
      } finally {
        this.loadingManuales = false;
      }
    },
    async fetchTips() {
      // Verificar cache primero
      if (this.isCacheValid() && this.cache.tips) {
        this.tips = this.cache.tips;
        this.tipsFiltrados = [...this.tips];
        return;
      }

      this.loadingTips = true;
      try {
        const res = await fetch(`${this.backendUrl}/recursos/tips/`, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        if (!res.ok) throw new Error('Error al obtener tips');
        this.tips = await res.json();
        this.tipsFiltrados = [...this.tips];
        
        // Guardar en cache
        this.cache.tips = this.tips;
        this.cache.lastFetch = Date.now();
      } catch (e) {
        this.tips = [];
        this.tipsFiltrados = [];
        console.error('Error fetching tips:', e);
      } finally {
        this.loadingTips = false;
      }
    },
    // Búsqueda en tiempo real para manuales
    filtrarManuales() {
      if (!this.searchManuales.trim()) {
        this.manualesFiltrados = [...this.manuales];
        return;
      }
      
      const searchTerm = this.searchManuales.toLowerCase().trim();
      this.manualesFiltrados = this.manuales.filter(manual => 
        manual.titulo?.toLowerCase().includes(searchTerm) ||
        manual.descripcion?.toLowerCase().includes(searchTerm)
      );
    },
    // Búsqueda en tiempo real para tips
    filtrarTips() {
      if (!this.searchTips.trim()) {
        this.tipsFiltrados = [...this.tips];
        return;
      }
      
      const searchTerm = this.searchTips.toLowerCase().trim();
      this.tipsFiltrados = this.tips.filter(tip => 
        tip.titulo?.toLowerCase().includes(searchTerm) ||
        tip.descripcion?.toLowerCase().includes(searchTerm)
      );
    },
    abrirModalTip(tip) {
      this.modalTip = tip;
      document.body.style.overflow = 'hidden';
    },
    cerrarModalTip() {
      this.modalTip = null;
      document.body.style.overflow = '';
    },
    getEmbedUrl(url) {
      // Convierte enlaces de YouTube/Vimeo a formato embebido
      if (url.includes('youtube.com/watch?v=')) {
        return url.replace('watch?v=', 'embed/');
      }
      if (url.includes('youtu.be/')) {
        return url.replace('youtu.be/', 'youtube.com/embed/');
      }
      if (url.includes('vimeo.com/')) {
        return url.replace('vimeo.com/', 'player.vimeo.com/video/');
      }
      return url;
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

/* Estilos para la barra de búsqueda */
.search-container {
  position: relative;
  max-width: 400px;
  margin: 0 auto 2rem auto;
}

.search-input {
  width: 100%;
  padding: 12px 40px 12px 16px;
  border: 2px solid #e1e5e9;
  border-radius: 25px;
  font-size: 16px;
  transition: all 0.3s ease;
  background: #fff;
}

.search-input:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1);
}

.search-icon {
  position: absolute;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: #666;
  font-size: 18px;
  pointer-events: none;
}

/* Indicadores de carga */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  color: #666;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #f3f3f3;
  border-top: 3px solid #007bff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Estados vacíos */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  color: #666;
  text-align: center;
}

.empty-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  opacity: 0.5;
}

.empty-state p {
  font-size: 1.1rem;
  margin: 0;
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
.grid-tips {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}
.cuadro-tip {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1.2rem 1rem 1.5rem 1rem;
  text-align: center;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  cursor: pointer;
  overflow: visible;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 320px;
}
.cuadro-tip h3 {
  font-size: 1.15rem;
  color: #222;
  margin: 0 0 0.7rem 0;
  font-weight: 600;
  text-align: center;
  min-height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.imagen-tip {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 120px;
  width: 100%;
  margin-bottom: 0.7rem;
}
.imagen-tip img {
  max-width: 100%;
  max-height: 110px;
  object-fit: contain;
  border-radius: 6px;
  box-shadow: 0 1px 4px rgba(44,62,80,0.08);
}
.tip-desc {
  color: #666;
  font-size: 0.97rem;
  margin-top: 0.3rem;
  text-align: center;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  min-height: 3.5em;
  max-width: 95%;
  margin-left: auto;
  margin-right: auto;
}
.tip-card-expandida {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(1.2);
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(41,128,217,0.18), 0 1.5px 6px rgba(44,62,80,0.10);
  padding: 2rem 2rem 1.5rem 2rem;
  min-width: 320px;
  min-height: 320px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s cubic-bezier(.4,0,.2,1), box-shadow 0.3s cubic-bezier(.4,0,.2,1);
  z-index: 20;
}
.tip-card-expandida img {
  max-width: 90%;
  max-height: 220px;
  margin-bottom: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(44,62,80,0.10);
}
.tip-desc-expandida {
  color: #333;
  font-size: 1.1rem;
  margin-top: 0.5rem;
  text-align: center;
}
.expand-card-enter-active, .expand-card-leave-active {
  transition: opacity 0.2s, transform 0.2s;
}
.expand-card-enter, .expand-card-leave-to {
  opacity: 0;
  transform: scale(0.9);
}
.manual-desc {
  color: #666;
  font-size: 0.95rem;
  margin-top: 0.5rem;
}

/* MODAL TIP */
.modal-tip-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(44,62,80,0.45);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}
.modal-tip-card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(41,128,217,0.18), 0 1.5px 6px rgba(44,62,80,0.10);
  padding: 2.5rem 2.5rem 2rem 2.5rem;
  min-width: 340px;
  max-width: 95vw;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  overflow-y: auto;
}
.modal-tip-close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #666;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: background-color 0.2s;
}
.modal-tip-close:hover {
  background-color: #f0f0f0;
}
.modal-tip-card h2 {
  margin: 0 0 1.5rem 0;
  color: #333;
  text-align: center;
}
.modal-tip-card img,
.modal-tip-card video,
.modal-tip-card iframe {
  max-width: 100%;
  max-height: 400px;
  border-radius: 8px;
  margin-bottom: 1rem;
}
.tip-video-modal {
  width: 100%;
  max-width: 600px;
  height: 400px;
}
.modal-fade-enter-active, .modal-fade-leave-active {
  transition: opacity 0.3s;
}
.modal-fade-enter, .modal-fade-leave-to {
  opacity: 0;
}
.tip-video {
  width: 100%;
  height: 120px;
  border-radius: 6px;
}

/* Responsive design para móviles */
@media (max-width: 768px) {
  .pagina-tips-manuales {
    padding: 1rem;
  }
  
  .search-container {
    max-width: 100%;
  }
  
  .grid-manuales,
  .grid-tips {
    grid-template-columns: 1fr;
  }
  
  .modal-tip-card {
    margin: 1rem;
    padding: 1.5rem;
  }
}
</style> 