<template>
  <div class="modal-overlay">
    <div class="modal-container">
      <!-- Close Button -->
      <button class="close-button" @click="$emit('close')" aria-label="Close">
        &times;
      </button>

      <!-- Modal Title -->
      <h2 class="modal-title">Edit Student Details</h2>

      <!-- Form -->
      <form @submit.prevent="submitForm" enctype="multipart/form-data">
        <div class="form-grid">
          <div class="form-group">
            <label>Roll No</label>
            <input v-model="form.roll_no" type="text" class="input-field" required />
          </div>

          <div class="form-group">
            <label>Name</label>
            <input v-model="form.name" type="text" class="input-field" required />
          </div>

          <div class="form-group">
            <label>Department</label>
            <input v-model="form.department" type="text" class="input-field" />
          </div>

          <div class="form-group">
            <label>Date of Birth</label>
            <input v-model="form.dob" type="date" class="input-field" />
          </div>

          <div class="form-group">
            <label>Age</label>
            <input v-model="form.age" type="number" class="input-field" />
          </div>

          <div class="form-group">
            <label>Phone</label>
            <input v-model="form.phone" type="text" class="input-field" />
          </div>

          <div class="form-group">
            <label>Email</label>
            <input v-model="form.email" type="email" class="input-field" />
          </div>

          <div class="form-group">
            <label>Attendance %</label>
            <input v-model="form.attendance_percentage" type="number" class="input-field" />
          </div>

          <div class="form-group">
            <label>Mark %</label>
            <input v-model="form.mark_percentage" type="number" class="input-field" />
          </div>

          <div class="form-group full-width">
            <label>Upload Image</label>
            <input type="file" @change="handleFileUpload" class="file-input" />
          </div>
        </div>

        <!-- Submit Button -->
        <div class="form-actions">
          <button type="submit">Save Changes</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';
import { defineEmits, defineProps } from 'vue';

const emit = defineEmits(['close', 'student-updated']);
const props = defineProps({
  student: Object,
});

const form = ref({});
const imageFile = ref(null);

watch(
  () => props.student,
  (newVal) => {
    form.value = {
      id: newVal.id || '',
      roll_no: newVal.roll_no || '',
      name: newVal.name || '',
      department: newVal.department || '',
      dob: newVal.dob || '',
      age: newVal.age || '',
      phone: newVal.phone || '',
      email: newVal.email || '',
      attendance_percentage: newVal.attendance_percentage || '',
      mark_percentage: newVal.mark_percentage || '',
      image: null, // reset image file input
    };
  },
  { immediate: true, deep: true }
);



const handleFileUpload = (e) => {
  imageFile.value = e.target.files[0];
};

const submitForm = async () => {
  const formData = new FormData();

  formData.append('roll_no', form.value.roll_no || '');
  formData.append('name', form.value.name || '');
  formData.append('department', form.value.department || '');
  formData.append('dob', form.value.dob || '');
  formData.append('age', form.value.age || '');
  formData.append('phone', form.value.phone || '');
  formData.append('email', form.value.email || '');
  formData.append('attendance_percentage', form.value.attendance_percentage || '');
  formData.append('mark_percentage', form.value.mark_percentage || '');

  if (imageFile.value) {
    formData.append('image', imageFile.value);
  }

  try {
    const response = await axios.patch(
      `http://127.0.0.1:8000/api/students/${form.value.id}/`,
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }
    );

    // Emit updated student back to parent
    emit('student-updated', response.data);

    // Show success alert
    alert('✅ Student updated successfully!');

    // Emit close to close modal
    emit('close');

    // Reload page once after short delay
    setTimeout(() => {
      window.location.reload();
    }, 500); // wait 0.5s to ensure modal closes cleanly

  } catch (error) {
    if (error.response && error.response.data) {
      console.error('Validation error:', error.response.data);
      alert(JSON.stringify(error.response.data, null, 2));
    } else {
      console.error('Update failed:', error);
      alert('❌ Failed to update student.');
    }
  }
};


</script>

<style scoped>
/* Overlay */
.modal-overlay {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

/* Container */
.modal-container {
  background-color: white;
  padding: 2rem;
  border-radius: 12px;
  width: 100%;
  max-width: 800px;
  position: relative;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

/* Title */
.modal-title {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  color: #333;
  margin-bottom: 1.5rem;
}

/* Close button */
.close-button {
  position: absolute;
  top: 16px;
  right: 16px;
  background: none;
  border: none;
  font-size: 28px;
  cursor: pointer;
  color: #888;
  transition: color 0.3s;
}
.close-button:hover {
  color: #e53935;
}

/* Grid */
.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}

/* Input field */
.input-field {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 15px;
  background-color: #fafafa;
  transition: border-color 0.3s, box-shadow 0.3s;
}
.input-field:focus {
  border-color: #4a90e2;
  box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.2);
  background-color: #fff;
}

/* File input */
.file-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
  background-color: #f9f9f9;
}

/* Form group */
.form-group {
  display: flex;
  flex-direction: column;
}
.full-width {
  grid-column: span 2;
}

/* Labels */
label {
  font-weight: 600;
  font-size: 14px;
  margin-bottom: 5px;
  color: #444;
}

/* Submit button */
.form-actions {
  text-align: center;
  margin-top: 24px;
}
button[type="submit"] {
  background-color: #2563eb;
  color: white;
  padding: 10px 24px;
  font-size: 16px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}
button[type="submit"]:hover {
  background-color: #1e40af;
  transform: translateY(-1px);
}

/* Responsive adjustments */
@media (max-width: 600px) {
  .full-width {
    grid-column: span 1;
  }
}
</style>
