import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('@/components/Login.vue'),
    },
    
    {
      path: '/',
      name: 'inicio',
      component: () => import('@/components/Inicio.vue')
    },

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
    {
      path: '/portales',
      name: 'portales',
      component: () => import('@/components/Portales.vue'),
    },

    {
      path: '/preguntas-frecuentes',
      name: 'preguntas-frecuentes',
      component: () => import('@/components/PreguntasFrecuentes.vue'),
    },
    {
      path: '/contacto',
      name: 'contacto',
      component: () => import('@/components/Contacto.vue'),
    },
    {
      path: '/tips-y-manuales',
      name: 'tips-y-manuales',
      component: () => import('@/components/TipsYManuales.vue'),
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
    next();
  }
});

export default router;