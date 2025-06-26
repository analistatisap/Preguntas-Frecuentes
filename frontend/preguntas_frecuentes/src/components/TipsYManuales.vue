<template>
  <div class="pagina-tips-manuales">
    <h1 class="titulo-pagina">Manuales SAP</h1>
    <!-- Descripción para la sección de Manuales -->
    <p class="descripcion-pagina">
      En este espacio encontrarás material de apoyo, el cual podrás usar de soporte durante el
      desarrollo de tu gestión a través de los diferentes sistemas de Información que la compañía
      ha dispuesto para ti.
    </p>
    <section class="manuales-seccion">
      <h2>Manuales</h2>
      <div class="grid-manuales">
        <div v-if="loading.manuales" class="loading-container">
          <div class="loading-spinner"></div>
          <p>Cargando manuales...</p>
        </div>
        <div v-else-if="manuales.length === 0" class="empty-state">
          <p>No hay manuales disponibles en este momento.</p>
        </div>
        <div v-else v-for="manual in manuales" :key="manual.id" class="cuadro-manual">
          <div class="icono-manual">
            <a :href="getManualUrl(manual.archivo)" target="_blank" class="manual-icon-link">
              <img :src="getManualIcon(manual.titulo)" :alt="manual.titulo" class="manual-icon">
            </a>
          </div>
          <h3>{{ manual.titulo }}</h3>
          <div v-html="manual.descripcion" class="descripcion-manual"></div>
        </div>
      </div>
    </section>

    <hr class="section-divider">

    <h1 class="titulo-pagina">Tips</h1>
    <!-- Descripción para la sección de Tips -->
    <p class="descripcion-pagina">
      Aquí encontrarás tips visuales y consejos rápidos para optimizar tu trabajo diario.
    </p>
    <section class="tips-seccion">
      <h2>Tips</h2>
      <div class="grid-tips">
        <div v-if="loading.tips" class="loading-container">
          <div class="loading-spinner"></div>
          <p>Cargando tips...</p>
        </div>
        <div v-else-if="tips.length === 0" class="empty-state">
          <p>No hay tips disponibles en este momento.</p>
        </div>
        <div v-else v-for="tip in tips" :key="tip.id" class="cuadro-tip" @click="abrirModalTip(tip)">
          <div class="tip-content">
            <h3>{{ tip.titulo }}</h3>
            <p>{{ tip.descripcion }}</p>
            <div v-if="tip.imagen" class="tip-image">
              <img :src="getTipUrl(tip.imagen)" :alt="tip.titulo">
            </div>
            <div v-else-if="tip.video" class="tip-video">
              <video :src="getTipUrl(tip.video)" controls></video>
            </div>
            <div v-else-if="tip.video_url" class="tip-video-url">
              <iframe :src="getEmbedUrl(tip.video_url)" frameborder="0" allowfullscreen></iframe>
            </div>
          </div>
        </div>
      </div>
    </section>
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
import { fetchWithAuth } from '@/utils/authFetch';
import { useToast } from 'vue-toastification';

export default {
  name: 'TipsYManuales',
  data() {
    return {
      manuales: [],
      tips: [],
      backendUrl: 'http://172.16.29.5:8000', 
      modalTip: null,
      loading: {
        manuales: false,
        tips: false
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
      if (!path) return '';
      if (/^https?:\/\//.test(path)) return path;
      return `${this.backendUrl}${path}`;
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
    async fetchManuales() {
      this.loading.manuales = true;
      const toast = useToast();
      
      try {
        const res = await fetchWithAuth(`${this.backendUrl}/api/recursos/manuales/`, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        if (!res.ok) throw new Error('Error al obtener manuales');
        this.manuales = await res.json();
      } catch (e) {
        console.error('Error al cargar manuales:', e);
        this.manuales = [];
        toast.error('No se pudieron cargar los manuales. Por favor, inténtalo más tarde.');
      } finally {
        this.loading.manuales = false;
      }
    },
    async fetchTips() {
      this.loading.tips = true;
      const toast = useToast();
      
      try {
        const res = await fetchWithAuth(`${this.backendUrl}/api/recursos/tips/`, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        if (!res.ok) throw new Error('Error al obtener tips');
        this.tips = await res.json();
      } catch (e) {
        console.error('Error al cargar tips:', e);
        this.tips = [];
        toast.error('No se pudieron cargar los tips. Por favor, inténtalo más tarde.');
      } finally {
        this.loading.tips = false;
      }
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
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.cuadro-manual:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
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
  margin: 1rem 0;
  color: #333;
  font-size: 1.2rem;
}

.descripcion-manual {
  flex-grow: 1;
  color: #666;
  font-size: 0.9rem;
  line-height: 1.4;
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
  padding: 1.5rem;
  cursor: pointer;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  height: 100%;
}
.cuadro-tip:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}
.tip-content h3 {
  margin: 0 0 1rem 0;
  color: #333;
  font-size: 1.1rem;
}
.tip-content p {
  color: #666;
  font-size: 0.9rem;
  line-height: 1.4;
  margin-bottom: 1rem;
  flex-grow: 1;
}
.tip-image img,
.tip-video video,
.tip-video-url iframe {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 4px;
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
.modal-tip-card img {
  max-width: 90%;
  max-height: 320px;
  margin-bottom: 1.2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(44,62,80,0.10);
}
.modal-tip-close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: transparent;
  border: none;
  font-size: 2.2rem;
  color: #007bff;
  cursor: pointer;
  z-index: 10;
  transition: color 0.2s;
}
.modal-tip-close:hover {
  color: #d32f2f;
}
.modal-fade-enter-active, .modal-fade-leave-active {
  transition: opacity 0.2s;
}
.modal-fade-enter, .modal-fade-leave-to {
  opacity: 0;
}
.tip-video {
  width: 100%;
  max-width: 180px;
  max-height: 110px;
  border-radius: 6px;
  box-shadow: 0 1px 4px rgba(44,62,80,0.08);
  margin-bottom: 0.7rem;
  background: #000;
}
.tip-video-modal {
  width: 100%;
  max-width: 480px;
  max-height: 320px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(44,62,80,0.10);
  margin-bottom: 1.2rem;
  background: #000;
}

/* Estilos para indicadores de carga */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  grid-column: 1 / -1;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #007bff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.empty-state {
  text-align: center;
  padding: 2rem;
  color: #666;
  grid-column: 1 / -1;
}

.empty-state p {
  font-size: 1.1rem;
  margin: 0;
}

/* Mejoras en las secciones */
.manuales-seccion,
.tips-seccion {
  margin-bottom: 3rem;
}

.manuales-seccion h2,
.tips-seccion h2 {
  color: #007bff;
  margin-bottom: 1.5rem;
  text-align: center;
  font-size: 1.8rem;
}

/* Mejoras en los cuadros */
.cuadro-manual {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  text-align: center;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.cuadro-manual:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.cuadro-manual h3 {
  margin: 1rem 0;
  color: #333;
  font-size: 1.2rem;
}

.cuadro-tip {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  cursor: pointer;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.cuadro-tip:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.tip-content h3 {
  margin: 0 0 1rem 0;
  color: #333;
  font-size: 1.1rem;
}

.tip-content p {
  color: #666;
  font-size: 0.9rem;
  line-height: 1.4;
  margin-bottom: 1rem;
  flex-grow: 1;
}

.tip-image img,
.tip-video video,
.tip-video-url iframe {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 4px;
}
</style>