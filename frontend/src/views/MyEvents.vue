<template>
  <DashboardLayout>
    <div class="bg-white p-6 rounded-xl shadow">
      <h1 class="text-3xl font-bold text-gray-800 mb-6">Mis eventos registrados</h1>

      <div v-if="loading" class="text-gray-600">Cargando eventos...</div>

      <div v-else-if="events.length === 0" class="text-gray-600">No estás registrado a ningún evento.</div>

      <div v-else class="overflow-x-auto">
        <table class="min-w-full table-auto border-collapse">
          <thead>
            <tr class="bg-gray-200 text-gray-700">
              <th class="py-3 px-6 text-left">Nombre</th>
              <th class="py-3 px-6 text-center">Capacidad</th>
              <th class="py-3 px-6 text-center">Estado</th>
              <th class="py-3 px-6 text-center">Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="event in events"
              :key="event.id"
              class="border-b hover:bg-gray-50 transition"
            >
              <td class="py-3 px-6 text-gray-900">{{ event.name }}</td>
              <td class="py-3 px-6 text-center text-gray-900">{{ event.capacity }}</td>
              <td class="py-3 px-6 text-center">
                <span :class="event.state ? 'text-green-600 font-semibold' : 'text-red-600 font-semibold'">
                  {{ event.state ? 'Activo' : 'Inactivo' }}
                </span>
              </td>
              <td class="py-3 px-6 text-center">
                <router-link
                  :to="`/events/${event.id}`"
                  class="text-blue-600 hover:underline"
                >
                  Ver detalles
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getMyEvents } from '@/api/event'
import DashboardLayout from '@/components/DashboardLayout.vue'

const events = ref([])
const loading = ref(true)

const loadMyEvents = async () => {
  try {
    const { data } = await getMyEvents()
    events.value = data
  } catch (error) {
    console.error('Error al cargar eventos del usuario:', error)
  } finally {
    loading.value = false
  }
}

onMounted(loadMyEvents)
</script>
