import { createRouter, createWebHistory } from 'vue-router';
import Inicio from '@/components/Inicio.vue';
import NuestroEquipo from '@/components/NuestroEquipo.vue';
import Portales from '@/components/Portales.vue';
import AboutView from '../views/AboutView.vue';
import PreguntasFrecuentes from '@/components/PreguntasFrecuentes.vue';
import Contacto from '@/components/Contacto.vue';
import TipsYManuales from '@/components/TipsYManuales.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'inicio',
      component: Inicio
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
    {
      path: '/nuestro-equipo',
      name: 'nuestro-equipo',
      component: NuestroEquipo,
    },
    {
      path: '/portales',
      name: 'portales',
      component: Portales,
    },

    {
      path: '/preguntas-frecuentes',
      name: 'Preguntas-frecuentes', // Asegúrate de que el 'name' coincida si lo usas en <router-link>
      component: PreguntasFrecuentes,
    },
    {
      path: '/contacto',
      name: 'contacto',
      component: Contacto,
    },
    {
      path: '/tips-y-manuales',
      name: 'tips-y-manuales',
      component: TipsYManuales,
    }
  ],
});

export default router;