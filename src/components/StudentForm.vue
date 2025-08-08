

<template>
  <div class="student-form-container">
    <h2>{{ isEdit ? 'Edit Student' : 'Add Student' }}</h2>

    <form @submit.prevent="submitForm" enctype="multipart/form-data">
      <div class="form-grid">
        <div class="form-group">
          <label>Roll Number</label>
          <input v-model="roll_no" type="text" required placeholder="Enter roll number" />
        </div>

        <div class="form-group">
          <label>Name</label>
          <input v-model="name" type="text" required placeholder="Enter full name" />
        </div>

        <div class="form-group">
          <label>Department</label>
          <select v-model="department" required>
            <option value="">Select Department</option>
            <option value="Computer Science">Computer Science</option>
            <option value="Information Technology">Information Technology</option>
            <option value="Software Engineering">Software Engineering</option>
            <option value="Data Science">Data Science</option>
            <option value="Cybersecurity">Cybersecurity</option>
          </select>
        </div>

        <div class="form-group">
          <label>Date of Birth</label>
          <input v-model="dob" type="date" required @change="calculateAge" />
        </div>

        <div class="form-group">
          <label>Age</label>
          <input v-model="age" type="number" readonly placeholder="Auto-calculated" />
        </div>

        <div class="form-group">
          <label>Phone</label>
          <input v-model="phone" type="tel" required pattern="[0-9]{10}" placeholder="Enter 10-digit phone number" />
        </div>

        <div class="form-group">
          <label>Email</label>
          <input v-model="email" type="email" required placeholder="Enter email address" />
        </div>

        <div class="form-group">
          <label>Attendance %</label>
          <input v-model="attendance_percentage" type="number" min="0" max="100" step="0.1" required />
        </div>

        <div class="form-group">
          <label>Mark %</label>
          <input v-model="mark_percentage" type="number" min="0" max="100" step="0.1" required />
        </div>

        <div class="form-group full-width">
          <label>Photo</label>
          <input type="file" @change="onFileChange" accept="image/*" />
          <div v-if="imagePreview" class="preview">
            <img :src="imagePreview" alt="Preview" />
          </div>
        </div>
      </div>

      <div class="actions">
        <button type="submit">{{ isEdit ? 'Update Student' : 'Add Student' }}</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      roll_no: '',
      name: '',
      department: '',
      dob: '',
      age: 0,
      phone: '',
      email: '',
      attendance_percentage: null,
      mark_percentage: null,
      image: null,
      imagePreview: null,
      isEdit: false
    };
  },
  methods: {
    calculateAge() {
      if (this.dob) {
        const today = new Date();
        const birthDate = new Date(this.dob);
        let age = today.getFullYear() - birthDate.getFullYear();
        const m = today.getMonth() - birthDate.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
          age--;
        }
        this.age = age;
      }
    },
    onFileChange(event) {
      this.image = event.target.files[0];
      if (this.image) {
        this.imagePreview = URL.createObjectURL(this.image);
      }
    },
    async submitForm() {
  const formData = new FormData();

  formData.append('roll_no', this.roll_no);
  formData.append('name', this.name);
  formData.append('age', this.age);
  if (this.dob) formData.append('dob', this.dob);
  formData.append('email', this.email);
  formData.append('phone', this.phone);
  formData.append('department', this.department);
  formData.append('attendance_percentage', this.attendance_percentage || 0.0);
  formData.append('mark_percentage', this.mark_percentage || 0.0);
  formData.append('is_active', true);

  if (this.image) {
    formData.append('image', this.image);
  }

  try {
    const res = await axios.post('http://127.0.0.1:8000/api/students/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });

    this.$emit('student-added', res.data);
    alert('Student added successfully!');
    this.resetForm();
  } catch (error) {
    console.error('Add failed:', error.response?.data || error.message);
    alert('Failed to add student. Check console for details.');
  }
},
    resetForm() {
      this.roll_no = '';
      this.name = '';
      this.department = '';
      this.dob = '';
      this.age = 0;
      this.phone = '';
      this.email = '';
      this.attendance_percentage = null;
      this.mark_percentage = null;
      this.image = null;
      this.imagePreview = null;
    }
  }
};
</script>

<style scoped>
.student-form-container {
  background: #fff;
  border-radius: 10px;
  padding: 24px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.student-form-container h2 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
}
.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 20px;
}
.form-group {
  display: flex;
  flex-direction: column;
}
.form-group label {
  margin-bottom: 6px;
  font-weight: 500;
  color: #444;
}
.form-group input,
.form-group select {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
}
.form-group input:read-only {
  background-color: #f9f9f9;
  color: #999;
}
.full-width {
  grid-column: span 2;
}
.preview img {
  margin-top: 10px;
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 5px;
}
.actions {
  margin-top: 24px;
}
.actions button {
  padding: 10px 20px;
  background-color: #2563eb;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 15px;
  cursor: pointer;
}
.actions button:hover {
  background-color: #1d4ed8;
}
</style>