import { defineStore } from 'pinia'
import api from '../api'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    user: null,
  }),
  actions: {
    async login(email, password) {
      const form = new URLSearchParams()
      form.append('username', email)
      form.append('password', password)

      const { data } = await api.post('/auth/login', form)
      this.token = data.access_token
      localStorage.setItem('token', this.token)

      api.defaults.headers.common['Authorization'] = `Bearer ${this.token}`
    },
    async register(email, password) {
      await api.post('/auth/register', { email, password })
    },
    logout() {
      this.token = ''
      this.user = null
      localStorage.removeItem('token')
      delete api.defaults.headers.common['Authorization']
    }
  }
})
