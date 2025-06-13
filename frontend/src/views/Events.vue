<template>
  <DashboardLayout>
    <div class="min-h-screen bg-gray-100 py-10 px-4 flex justify-center">
      <div class="w-full max-w-6xl bg-white p-6 md:p-10 rounded-xl shadow">
        <h1 class="text-3xl font-bold text-gray-800 text-center mb-8">Eventos disponibles</h1>

        <!-- Buscador -->
        <div class="mb-6">
          <input
              v-model="search"
              @input="performSearch"
              type="text"
              placeholder="Buscar eventos por nombre..."
              class="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800 bg-white"
          />
        </div>

        <!-- Botón crear -->
        <div class="flex justify-end mt-6 mb-8">
          <button
              class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition"
              @click="formVisible = true; resetForm()"
          >
            + Crear evento
          </button>
        </div>

        <!-- Formulario crear/editar -->
        <div v-if="formVisible" class="mb-10 p-4 border rounded bg-gray-50 space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Nombre</label>
            <input v-model="form.name" placeholder="Nombre del evento"
                   class="w-full border rounded px-3 py-2 text-gray-800 placeholder-gray-400"/>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Descripción</label>
            <input v-model="form.description" placeholder="Descripción"
                   class="w-full border rounded px-3 py-2 text-gray-800 placeholder-gray-400"/>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Capacidad</label>
            <input type="number" min="1" v-model="form.capacity" placeholder="Ej. 100"
                   class="w-full border rounded px-3 py-2 text-gray-800 placeholder-gray-400"/>
          </div>
          <div class="flex items-center space-x-2">
            <input type="checkbox" v-model="form.state" id="state"/>
            <label for="state" class="text-sm text-gray-700">Evento activo</label>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Fecha de inicio</label>
            <input
                v-model="form.start_date"
                type="datetime-local"
                class="w-full border rounded px-3 py-2 text-gray-800"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Fecha de fin</label>
            <input
                v-model="form.end_date"
                type="datetime-local"
                class="w-full border rounded px-3 py-2 text-gray-800"
            />
          </div>
          <div class="flex flex-wrap gap-3 mt-4">
            <button
                @click="submitForm"
                class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            >
              {{ editingEvent ? 'Actualizar' : 'Crear' }}
            </button>
            <button
                @click="formVisible = false"
                class="bg-gray-300 text-gray-800 px-4 py-2 rounded hover:bg-gray-400"
            >
              Cancelar
            </button>
          </div>
        </div>

        <!-- Sin eventos -->
        <div v-if="events.length === 0" class="text-center text-gray-600">
          No hay eventos disponibles.
        </div>

        <!-- Tabla -->
        <div v-else class="overflow-x-auto border-t pt-6">
          <table class="min-w-full table-auto border-collapse">
            <thead>
            <tr class="bg-gray-200 text-gray-700">
              <th class="py-3 px-6 text-left">Nombre</th>
              <th class="py-3 px-6 text-left">Descripción</th>
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
              <td class="py-3 px-6 text-gray-900">{{ event.description }}</td>
              <td class="py-3 px-6 text-center text-gray-900">{{ event.capacity }}</td>
              <td class="py-3 px-6 text-center">
                  <span
                      :class="event.state ? 'text-green-600 font-semibold' : 'text-red-600 font-semibold'"
                  >
                    {{ event.state ? 'Activo' : 'Inactivo' }}
                  </span>
              </td>
              <td class="py-3 px-6 text-center">
                <div class="flex flex-wrap justify-center gap-2">
                  <button
                      @click="startEdit(event)"
                      class="bg-yellow-400 text-white px-3 py-1 rounded hover:bg-yellow-500 text-sm"
                  >
                    Editar
                  </button>
                  <button
                      @click="inactivate(event.id)"
                      class="bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700 text-sm"
                  >
                    Inactivar
                  </button>
                  <router-link
                      :to="`/events/${event.id}`"
                      class="bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700 text-sm"
                  >
                    Ver
                  </router-link>
                </div>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import DashboardLayout from '@/components/DashboardLayout.vue'
import {ref, onMounted} from 'vue'
import {
  fetchEvents,
  searchEvents,
  createEvent,
  updateEvent,
  inactivateEvent,
} from '@/api/event'

const events = ref([])
const search = ref('')
const formVisible = ref(false)
const editingEvent = ref(null)
const form = ref({
  name: '',
  description: '',
  capacity: 1,
  state: true
})

const resetForm = () => {
  form.value = {
    name: '',
    description: '',
    capacity: 1,
    state: true
  }
  editingEvent.value = null
}

const loadEvents = async () => {
  const {data} = await fetchEvents()
  events.value = data
}

const performSearch = async () => {
  if (!search.value.trim()) {
    await loadEvents()
    return
  }
  const {data} = await searchEvents(search.value)
  events.value = data
}

const submitForm = async () => {
  try {
    if (editingEvent.value) {
      await updateEvent(editingEvent.value.id, form.value)
      alert('Evento actualizado')
    } else {
      await createEvent(form.value)
      alert('Evento creado')
    }
    formVisible.value = false
    resetForm()
    await loadEvents()
  } catch (err) {
    alert(err?.response?.data?.detail || 'Error')
  }
}

const startEdit = (event) => {
  editingEvent.value = event
  form.value = {...event}
  formVisible.value = true
}

const inactivate = async (id) => {
  if (confirm('¿Estás seguro de inactivar este evento?')) {
    await inactivateEvent(id)
    await loadEvents()
  }
}

onMounted(() => {
  loadEvents()
})
</script>