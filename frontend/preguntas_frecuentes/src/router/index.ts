import { createRouter, createWebHistory } from 'vue-router';
import Inicio from '@/components/Inicio.vue';
import NuestroEquipo from '@/components/NuestroEquipo.vue';
import Portales from '@/components/Portales.vue';
import AboutView from '../views/AboutView.vue';
import PreguntasFrecuentes from '@/components/PreguntasFrecuentes.vue';
import Contacto from '@/components/Contacto.vue';
import TipsYManuales from '@/components/TipsYManuales.vue';
import Login from '@/components/Login.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    
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
      name: 'preguntas-frecuentes',
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

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('user'); // Verifica si hay un usuario autenticado

  if (to.name === 'login' && isAuthenticated) {
    // Si el usuario está autenticado e intenta ir al login, lo redirigimos al inicio
    next({ name: 'inicio' });
  } else if (to.name !== 'login' && !isAuthenticated) {
    // Si el usuario NO está autenticado y no va al login, lo redirigimos al login
    next({ name: 'login' });
  } else {
    // En cualquier otro caso, permitimos la navegación
    next();
  }
});

export default router;