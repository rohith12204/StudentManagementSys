import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
});

export default {
  getStudents: () => API.get('students/'),
  addStudent: (data) => API.post('students/', data),
  updateStudent: (id, data) => API.put(`students/${id}/`, data),
  deleteStudent: (id) => API.delete(`students/${id}/`)
};
