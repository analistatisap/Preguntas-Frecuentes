import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import NuestroEquipo from '@/components/NuestroEquipo.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/nuestro-equipo',
      name: 'nuestro-equipo',
      component: () => import('@/components/NuestroEquipo.vue'),
    },
  ],
});

export default router;