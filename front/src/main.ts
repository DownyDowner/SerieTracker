import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import vuetify from './plugins/vuetify'

// Components
import App from './App.vue'
import Vue3Toastify, { type ToastContainerOptions } from 'vue3-toastify';

const pinia = createPinia()

createApp(App)
    .use(vuetify)
    .use(pinia)
    .use(router)
    .use(Vue3Toastify, {
        autoClose: 3000,
    } as ToastContainerOptions)
    .mount('#app')
