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
          component: () => import('../views/home/Home.vue'),
          meta: { title: NavigationConst.titleHome },
        },
        {
          path: NavigationConst.routeSerie,
          name: NavigationConst.nameSerie,
          component: () => import('../views/home/HomeSerie.vue'),
          meta: { title: NavigationConst.titleSerie },
        }
      ],
    },
    {
      path: NavigationConst.routeArchive,
      component: LayoutConnected,
      beforeEnter: checkIsAuthenticated,
      children: [
        {
          path: '',
          name: NavigationConst.nameArchive,
          component: () => import('../views/home/Archive.vue'),
          meta: { title: NavigationConst.titleArchive },
        },
        {
          path: NavigationConst.routeSerie,
          name: NavigationConst.nameSerie,
          component: () => import('../views/home/HomeSerie.vue'),
          meta: { title: NavigationConst.titleSerie },
        },
      ],
    },
    {
      path: NavigationConst.routeFollowed,
      component: LayoutConnected,
      beforeEnter: checkIsAuthenticated,
      children: [
        {
          path: '',
          name: NavigationConst.nameFollowed,
          component: () => import('../views/followedSeries/FollowedSeries.vue'),
          meta: { title: NavigationConst.titleFollowed },
        },
        {
          path: NavigationConst.routeFollowedDetail,
          name: NavigationConst.nameFollowedDetail,
          component: () => import('../views/followedSeries/FollowedSeriesDetail.vue'),
          meta: { title: NavigationConst.titleFollowedDetail },
        },
      ],
    },
    {
      path: NavigationConst.routeShare,
      component: LayoutConnected,
      beforeEnter: checkIsAuthenticated,
      children: [
        {
          path: '',
          name: NavigationConst.nameShare,
          component: () => import('../views/partage/Partage.vue'),
          meta: { title: NavigationConst.titleShare },
        },
      ]
    },
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
})

router.afterEach((to: RouteLocationNormalized) => {
  document.title = `${to.meta?.title ?? ''} · ${NavigationConst.nomApp}`;
});

async function checkIsNotAuthenticated() {
  const authStore = useAuthenticationStore();
  await authStore.loadUser();
  if (authStore.token) return { name: NavigationConst.nameHome };
}

async function checkIsAuthenticated(to: RouteLocationNormalized) {
  const authStore = useAuthenticationStore();
  await authStore.loadUser();
  if (!authStore.token) return { name: NavigationConst.nameLogin, query: { redirect: to.path } };
}

export default router;
