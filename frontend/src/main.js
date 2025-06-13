import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import App from './App.vue'
import './assets/main.css'

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')

import { useAuthStore } from './store/auth'
import api from "@/api.js";
const auth = useAuthStore()

if (auth.token) {
  api.defaults.headers.common['Authorization'] = `Bearer ${auth.token}`
}