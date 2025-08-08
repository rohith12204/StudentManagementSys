import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue' // your main component managing list
import StudentEdit from '../components/StudentEdit.vue'

const routes = [
  { path: '/', component: App }, // dashboard with list and form
  { path: '/students/edit/:id', component: StudentEdit, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
