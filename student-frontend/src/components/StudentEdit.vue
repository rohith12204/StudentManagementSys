<template>
  <div>
    <h2>Edit Student</h2>
    <form @submit.prevent="updateStudent" enctype="multipart/form-data">
      <input v-model="roll_no" placeholder="Roll No (e.g., 001)" required />
      <input v-model="name" placeholder="Name" required />
      <input v-model.number="age" type="number" placeholder="Age" required />
      <input v-model="dob" type="date" placeholder="Date of Birth" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="phone" placeholder="Phone" required />
      <input v-model="department" placeholder="Department" required />
      <input v-model.number="attendance_percentage" type="number" step="0.01" placeholder="Attendance %" required />
      <input v-model.number="mark_percentage" type="number" step="0.01" placeholder="Mark %" required />
      <input type="file" @change="onFileChange" />

      <div v-if="imagePreview">
        <p>New Image Preview:</p>
        <img :src="imagePreview" alt="Preview" width="100" />
      </div>
      <div v-else-if="existingImage">
        <p>Current Image:</p>
        <img :src="'http://127.0.0.1:8000' + existingImage" width="100" />
      </div>

      <button type="submit">Update Student</button>
      <button type="button" @click="$router.push('/')">Cancel</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['id'],
  data() {
    return {
      roll_no: '',
      name: '',
      age: null,
      dob: '',
      email: '',
      phone: '',
      department: '',
      attendance_percentage: null,
      mark_percentage: null,
      image: null,
      imagePreview: null,
      existingImage: null
    }
  },
  async mounted() {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/api/students/${this.id}/`)
      const student = res.data
      this.roll_no = student.roll_no
      this.name = student.name
      this.age = student.age
      this.dob = student.dob
      this.email = student.email
      this.phone = student.phone
      this.department = student.department
      this.attendance_percentage = student.attendance_percentage
      this.mark_percentage = student.mark_percentage
      this.existingImage = student.image  // Should be a relative path
    } catch (error) {
      console.error('Failed to fetch student:', error)
    }
  },
  methods: {
    onFileChange(e) {
      this.image = e.target.files[0]
      this.imagePreview = URL.createObjectURL(this.image)
    },
    async updateStudent() {
      const formData = new FormData()
      formData.append('roll_no', this.roll_no)
      formData.append('name', this.name)
      formData.append('age', this.age)
      formData.append('dob', this.dob)
      formData.append('email', this.email)
      formData.append('phone', this.phone)
      formData.append('department', this.department)
      formData.append('attendance_percentage', this.attendance_percentage)
      formData.append('mark_percentage', this.mark_percentage)
      formData.append('is_active', true)
      if (this.image) {
        formData.append('image', this.image)
      }

      try {
        await axios.put(`http://127.0.0.1:8000/api/students/${this.id}/`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        })
        alert('Student updated successfully!')
        this.$router.push('/')
      } catch (error) {
        console.error('Failed to update student:', error)
        alert('Failed to update student.')
      }
    }
  }
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 400px;
}
input[type="file"] {
  margin-top: 10px;
}
button {
  width: 120px;
  padding: 8px;
  background-color: #1976d2;
  color: white;
  border: none;
  border-radius: 4px;
}
button:hover {
  background-color: #1565c0;
}
img {
  margin-top: 10px;
  border-radius: 5px;
}
</style>
