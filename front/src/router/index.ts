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
      meta: { title:NavigationConst.titleSignup },
    },
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
})

export default router;
