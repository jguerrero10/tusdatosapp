<template>
  <DashboardLayout>
    <div class="bg-white max-w-2xl mx-auto p-6 rounded-xl shadow space-y-6">
      <h1 class="text-2xl font-bold text-gray-800">Crear nuevo evento</h1>

      <form @submit.prevent="submit">
        <div class="space-y-4">
          <div>
            <label class="block mb-1 text-sm font-medium text-gray-700">Nombre del evento</label>
            <input
              v-model="name"
              type="text"
              required
              class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label class="block mb-1 text-sm font-medium text-gray-700">Capacidad</label>
            <input
              v-model.number="capacity"
              type="number"
              min="1"
              required
              class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div class="flex items-center gap-2">
            <input type="checkbox" v-model="state" id="state" class="rounded" />
            <label for="state" class="text-sm text-gray-700">Evento activo</label>
          </div>
        </div>

        <div class="mt-6">
          <button
            type="submit"
            class="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition"
          >
            Crear evento
          </button>
        </div>
      </form>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import DashboardLayout from '@/components/DashboardLayout.vue'
import api from '@/api'

const name = ref('')
const capacity = ref(1)
const state = ref(true)
const router = useRouter()

const submit = async () => {
  try {
    await api.post('/events/', {
      name: name.value,
      capacity: capacity.value,
      state: state.value,
    })
    alert('Evento creado exitosamente')
    router.push('/events')
  } catch (err) {
    const msg = err?.response?.data?.detail || 'Error al crear el evento'
    alert(msg)
  }
}
</script>
