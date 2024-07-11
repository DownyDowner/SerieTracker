import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import vuetify from './plugins/vuetify'

// Components
import App from './App.vue'

const pinia = createPinia()

createApp(App).use(vuetify).use(pinia).use(router).mount('#app')
