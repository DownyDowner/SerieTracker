import { RouteLocationNormalized, RouteRecordRaw, createRouter, createWebHistory } from 'vue-router';
import { NavigationConst } from './routeConst';
import { useAuthenticationStore } from '../stores/authentication';
import LayoutConnected from '../layouts/LayoutConnected.vue';

const routes: Array<RouteRecordRaw> = [
    {
      path: NavigationConst.routeLogin,
      name: NavigationConst.nameLogin,
      component: () => import('../views/authentication/Login.vue'),
      beforeEnter: checkIsNotAuthenticated,
      meta: { title: NavigationConst.titleLogin },
    },
    {
      path: NavigationConst.routeSignUp,
      name: NavigationConst.nameSignUp,
      component: () => import('../views/authentication/SignUp.vue'),
      beforeEnter: checkIsNotAuthenticated,
      meta: { title: NavigationConst.titleSignup },
    },
    {
      path: NavigationConst.routeHome,
      component: LayoutConnected,
      beforeEnter: checkIsAuthenticated,
      children: [
        {
          path: '',
          name: NavigationConst.nameHome,
          component: () => import('../views/Home.vue'),
          meta: { title: NavigationConst.titleHome },
        },
      ],
    },
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
})

router.afterEach((to: RouteLocationNormalized) => {
  document.title = `${to.meta?.title ?? ''} · ${NavigationConst.nomApp}`;
});

function checkIsNotAuthenticated() {
  const authStore = useAuthenticationStore();
  authStore.loadUser();
  if (authStore.token) return { name: NavigationConst.nameHome };
}

function checkIsAuthenticated(to: RouteLocationNormalized) {
  const authStore = useAuthenticationStore();
  authStore.loadUser();
  if (!authStore.token) return { name: NavigationConst.nameLogin, query: { redirect: to.path } };
}

export default router;
