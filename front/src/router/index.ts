import { RouteRecordRaw, createRouter, createWebHistory } from 'vue-router';
import { NavigationConst } from './routeConst';

const routes: Array<RouteRecordRaw> = [
    {
      path: NavigationConst.routeLogin,
      name: NavigationConst.nameLogin,
      component: () => import('../views/authentication/Login.vue'),
      // beforeEnter: checkIsNotAuthenticated,
      meta: { title: NavigationConst.titleLogin },
    },
    {
      path: NavigationConst.routeSignUp,
      name: NavigationConst.nameSignUp,
      component: () => import('../views/authentication/SignUp.vue'),
      // beforeEnter: checkIsNotAuthenticated,
      meta: { title: NavigationConst.titleSignup },
    },
    {
      path: NavigationConst.routeHome,
      name: NavigationConst.nameHome,
      component: () => import('../views/Home.vue'),
      meta: { title: NavigationConst.titleHome },
    },
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
})

export default router;
