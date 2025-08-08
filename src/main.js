import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import 'recharts';

axios.defaults.baseURL = 'http://127.0.0.1:8000/api'  // Django backend

createApp(App).mount('#app')
