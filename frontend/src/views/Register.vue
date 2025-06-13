<template>
  <div class="min-h-screen w-screen flex items-center justify-center bg-gradient-to-br from-green-100 to-blue-200">
    <div class="w-full max-w-xl bg-white rounded-xl shadow-xl p-10">
      <h1 class="text-3xl font-bold text-center text-gray-800 mb-8">Crear cuenta</h1>

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
            class="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500 text-gray-800"
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
            class="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500 text-gray-800"
          />
        </div>

        <!-- Botón de registro -->
        <button
          type="submit"
          class="w-full bg-green-600 text-white py-3 px-4 rounded-lg font-semibold hover:bg-green-700 transition duration-200"
        >
          Registrarse
        </button>
      </form>

      <p class="text-sm text-center text-gray-600 mt-6">
        ¿Ya tienes cuenta?
        <router-link to="/login" class="text-green-600 hover:underline">Inicia sesión</router-link>
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
    await auth.register(email.value, password.value)
    await auth.login(email.value, password.value)
    await router.push('/')
  } catch (err) {
    alert('Error al registrarse')
  }
}
</script>
