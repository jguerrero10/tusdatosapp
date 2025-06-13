<template>
  <div class="min-h-screen bg-gray-100 flex flex-col">
    <!-- Navbar -->
    <header class="bg-white shadow px-6 py-4 flex items-center justify-between">
      <h1 class="text-xl font-bold text-gray-800">Mis Eventos</h1>
      <nav class="flex gap-4">
        <router-link to="/events" class="text-gray-700 hover:text-blue-600">Eventos</router-link>
        <router-link to="/my-events" class="text-gray-700 hover:text-blue-600">Mis eventos</router-link>
        <button @click="logout" class="text-red-600 hover:underline">Salir</button>
      </nav>
    </header>

    <!-- Contenido -->
    <main class="flex-1 p-6">
      <slot />
    </main>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/store/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

const logout = () => {
  auth.logout()
  router.push('/login')
}
</script>
