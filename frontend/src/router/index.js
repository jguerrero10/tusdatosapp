import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/store/auth'

import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Events from '@/views/Events.vue'
import EventDetail from '@/views/EventDetail.vue'
import MyEvents from '@/views/MyEvents.vue'

const routes = [
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  {
    path: '/events',
    name: 'Events',
    component: Events,
    meta: { requiresAuth: true },
  },
  {
    path: '/events/:id',
    name: 'EventDetail',
    component: EventDetail,
    meta: { requiresAuth: true },
  },
  {
    path: '/my-events',
    name: 'MyEvents',
    component: MyEvents,
    meta: { requiresAuth: true },
  },
  { path: '/', redirect: '/login' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const auth = useAuthStore()
  if (to.meta.requiresAuth && !auth.token) {
    next('/login')
  } else {
    next()
  }
})

export default router
