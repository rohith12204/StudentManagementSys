<template>
  <div class="modal-overlay">
    <div class="modal-content">
      <h3>Edit Student: {{ form.name }}</h3>
      <form @submit.prevent="submitForm">
        <input v-model="form.name" placeholder="Name" required />
        <input v-model="form.email" placeholder="Email" required />
        <input v-model="form.phone" placeholder="Phone" required />
        <input v-model="form.department" placeholder="Department" />
        <input v-model="form.age" type="number" placeholder="Age" />
        <input v-model="form.roll_no" placeholder="Roll No" />
        <input v-model="form.dob" type="date" placeholder="DOB" />
        <input v-model="form.mark_percentage" type="number" step="0.1" placeholder="Marks %" />
        <input v-model="form.attendance_percentage" type="number" step="0.1" placeholder="Attendance %" />
        <input type="file" @change="handleFile" />

        <div class="modal-actions">
          <button type="submit">Save</button>
          <button type="button" @click="$emit('close')">Cancel</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';

const props = defineProps(['student']);
const emit = defineEmits(['updated', 'close']);

const form = ref
const imageFile = ref(null);

watch(() => props.student, (newVal) => {
  form.value = { ...newVal };
});

const handleFile = (event) => {
  imageFile.value = event.target.files[0];
};

const submitForm = async () => {
  const formData = new FormData();
  Object.keys(form.value).forEach((key) => {
    if (form.value[key] !== null && form.value[key] !== undefined) {
      formData.append(key, form.value[key]);
    }
  });
  if (imageFile.value) {
    formData.append('image', imageFile.value);
  }

  try {
    for (const [key, value] of formData.entries()) {
        console.log(key, value);
    }

    await axios.put(`http://localhost:8000/api/students/${form.value.id}/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    emit('updated');
    emit('close');
  } catch (err) {
    console.error('Update failed:', err);
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex; align-items: center; justify-content: center;
}
.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  width: 400px;
}
.modal-content input {
  display: block;
  width: 100%;
  margin: 8px 0;
  padding: 6px;
}
.modal-actions {
  display: flex;
  justify-content: space-between;
}
</style>
