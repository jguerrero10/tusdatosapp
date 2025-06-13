<template>
  <DashboardLayout>
    <div class="bg-white p-6 md:p-8 rounded-xl shadow max-w-3xl mx-auto">
      <div v-if="loading" class="text-gray-600">Cargando evento...</div>

      <div v-else>
        <h1 class="text-3xl font-bold text-gray-800 mb-4">{{ event.name }}</h1>
        <div class="space-y-2 mb-6">
          <p class="text-gray-700">{{ event.description }}</p>
          <p class="text-gray-600 text-sm">
            Fecha: {{ new Date(event.start_date).toLocaleDateString() }} -
            Hora: {{ new Date(event.start_date).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) }}
          </p>
        </div>
        <div class="space-y-2 mb-6">
          <p class="text-gray-700">Capacidad: <span class="font-medium">{{ event.capacity }}</span></p>
          <p class="text-gray-700">
            Estado:
            <span
              :class="event.state ? 'text-green-600 font-semibold' : 'text-red-600 font-semibold'"
            >
              {{ event.state ? 'Activo' : 'Inactivo' }}
            </span>
          </p>
        </div>

        <!-- Botón o mensajes -->
        <div>
          <button
            v-if="!registered && event.state && event.capacity > 0"
            @click="register"
            class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition font-semibold"
          >
            Registrarse a este evento
          </button>

          <p
            v-else-if="registered"
            class="text-green-700 font-semibold bg-green-50 border border-green-200 p-3 rounded"
          >
            Ya estás registrado en este evento.
          </p>

          <p
            v-else-if="!event.state"
            class="text-red-600 font-semibold bg-red-50 border border-red-200 p-3 rounded"
          >
            Este evento está inactivo.
          </p>

          <p
            v-else
            class="text-red-600 font-semibold bg-red-50 border border-red-200 p-3 rounded"
          >
            No hay cupos disponibles para este evento.
          </p>
        </div>
      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getEvent, registerToEvent } from '@/api/event'
import DashboardLayout from '@/components/DashboardLayout.vue'

const route = useRoute()
const event = ref(null)
const loading = ref(true)
const registered = ref(false)

const fetchEvent = async () => {
  try {
    const { data } = await getEvent(route.params.id)
    event.value = data
  } catch (err) {
    console.error('Error al obtener evento:', err)
  } finally {
    loading.value = false
  }
}

const register = async () => {
  try {
    await registerToEvent(route.params.id)
    registered.value = true
    alert('¡Te has registrado con éxito!')
  } catch (err) {
    const detail = err?.response?.data?.detail || 'Error al registrarse.'
    alert(detail)
  }
}

onMounted(fetchEvent)
</script>
