<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-100 to-indigo-200">
    <div class="w-full max-w-xl bg-white rounded-xl shadow-xl p-10">
      <h1 class="text-3xl font-bold text-center text-gray-800 mb-8">Iniciar sesión</h1>

      <form @submit.prevent="submit" class="space-y-6">
        <!-- Email -->
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Correo electrónico</label>
          <input
            v-model="email"
            id="email"
            type="email"
            placeholder="usuario@ejemplo.com"
            required
            class="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800"
          />
        </div>

        <!-- Password -->
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Contraseña</label>
          <input
            v-model="password"
            id="password"
            type="password"
            placeholder="••••••••"
            required
            class="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800"
          />
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-3 px-4 rounded-lg font-semibold hover:bg-blue-700 transition duration-200"
        >
          Entrar
        </button>
      </form>

      <p class="text-sm text-center text-gray-600 mt-6">
        ¿No tienes cuenta?
        <router-link to="/register" class="text-blue-600 hover:underline">Regístrate aquí</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../store/auth'

const email = ref('')
const password = ref('')
const router = useRouter()
const auth = useAuthStore()

const submit = async () => {
  try {
    await auth.login(email.value, password.value)
    await router.push('/events')
  } catch (err) {
    alert('Credenciales inválidas')
  }
}
</script>
