import api from "@/api.js";


export const fetchEvents = () => api.get('/api/v1/events')
export const searchEvents = (name) => api.get(`/api/v1/events/search?name=${name}`)
export const getEvent = (id) => api.get(`/api/v1/events/${id}`)
export const registerToEvent = (id) => api.post(`/api/v1/events/${id}/register`)
export const getMyEvents = () => api.get('/api/v1/events/me/events')
export const createEvent = (eventData) => api.post('/api/v1/events', eventData)
export const updateEvent = (id, updatedData) => api.patch(`/api/v1/events/${id}`, updatedData)
export const inactivateEvent = (id) => api.delete(`/api/v1/events/${id}`)