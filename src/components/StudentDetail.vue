<template>
  <transition name="modal">
    <div class="modal-overlay" v-if="visible">
      <div class="modal-container">
        <!-- Close Button -->
        <button class="close-button" @click="$emit('close')">&times;</button>

        <!-- Title -->
        <h2 class="modal-title">{{ localStudent.value.name }}'s Details</h2>

        <!-- Student Info Grid -->
        <div class="student-info-grid">
          <p><strong>Roll No:</strong> {{ localStudent.value.roll_no }}</p>
          <p><strong>Department:</strong> {{ localStudent.value.department }}</p>
          <p><strong>Email:</strong> {{ localStudent.value.email }}</p>
          <p><strong>Phone:</strong> {{ localStudent.value.phone }}</p>
          <p><strong>Date of Birth:</strong> {{ localStudent.value.dob }}</p>
          <p><strong>Age:</strong> {{ localStudent.value.age }}</p>
          <p><strong>Attendance:</strong> {{ localStudent.value.attendance_percentage }}%</p>
          <p><strong>Mark:</strong> {{ localStudent.value.mark_percentage }}%</p>
        </div>

<!-- Edit Button -->
<button class="btn btn-yellow" @click="$emit('edit', localStudent.value)">Edit</button>




        <!-- Attendance Pie Chart -->
        <p><strong>Debug Attendance:</strong> {{ localStudent.value.attendance_percentage }}</p>
        <AttendanceChart :attendancePercent="Number(localStudent.value.attendance_percentage)" />

        <!-- Image Preview -->
        <p><strong>DEBUG image_url:</strong> {{ localStudent.value.image_url }}</p>
        <div class="student-photo-container">
          <p><strong>Photo Preview:</strong></p>
          <img
            v-if="localStudent.value.image_url"
            :src="localStudent.value.image_url + '?t=' + Date.now()"
            alt="Student Photo"
            class="student-photo"
            @click="openPreview = true"
          />
          <p v-else><em>No photo available for this student.</em></p>
        </div>

        <!-- Full Image Preview -->
        <div v-if="openPreview" class="image-preview-overlay" @click="openPreview = false">
          <img :src="localStudent.value.image_url + '?t=' + Date.now()" class="full-image" />
        </div>

        <!-- Show Result Button -->
        <div class="button-center">
          <button class="btn btn-green" @click="showResults = true">Show Result</button>
        </div>

        <!-- Results Chart -->
        <div v-if="showResults" class="chart-wrapper">
          <ResultsChart :marks="Number(localStudent.value.mark_percentage)" />
        </div>

        <!-- Edit/Delete Buttons -->
        <div class="modal-actions">
          <button class="btn btn-yellow" @click="startEdit">Edit</button>
          <button class="btn btn-red" @click="handleDelete">Delete</button>
        </div>

        <!-- DEBUG: Student JSON -->
        <pre style="font-size: 12px; margin-top: 20px; background: #f8f8f8; padding: 10px; border: 1px solid #ddd; overflow: auto;">
{{ localStudent.value }}
        </pre>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import AttendanceChart from './AttendanceChart.vue';
import ResultsChart from './ResultsChart.vue';
import StudentEdit from './StudentEdit.vue'; // ✅ NOT './components/StudentEdit.vue'


const props = defineProps(['student']);
const emit = defineEmits(['close', 'edit', 'delete']);

const localStudent = ref({ ...props.student });
const isEditing = ref(false);
const studentBeingEdited = ref(null);
const showResults = ref(false);
const openPreview = ref(false);
const visible = ref(false);

// Sync with prop
watch(
  () => props.student,
  (newVal) => {
    localStudent.value = { ...newVal };
  },
  { immediate: true }
);

// Show modal after mount
onMounted(() => {
  setTimeout(() => {
    visible.value = true;
  }, 10);
});

// Start editing
const startEdit = () => {
  isEditing.value = true;
  studentBeingEdited.value = { ...localStudent.value };
};

// Handle updated student
const updateStudentInList = (updatedStudent) => {
  localStudent.value = { ...updatedStudent };
  isEditing.value = false;
};

// Delete student
const handleDelete = () => {
  if (confirm(`Are you sure you want to delete ${localStudent.value.name}?`)) {
    emit('delete', localStudent.value.id);
  }
};
</script>

<style scoped>
/* All styles remain unchanged */
.modal-overlay {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.modal-container {
  background: #fff;
  padding: 30px;
  border-radius: 10px;
  width: 90%;
  max-width: 900px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
  animation: fadeIn 0.3s ease;
}
.close-button {
  position: absolute;
  top: 15px;
  right: 20px;
  background: none;
  border: none;
  font-size: 24px;
  color: #666;
  cursor: pointer;
}
.close-button:hover {
  color: #000;
}
.modal-title {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
}
.student-info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px 24px;
  font-size: 14px;
  color: #444;
  margin-bottom: 20px;
}
.student-photo-container {
  margin-top: 20px;
  text-align: center;
}
.student-photo {
  width: 120px;
  height: 120px;
  object-fit: cover;
  border-radius: 10px;
  border: 2px solid #ccc;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  cursor: pointer;
}
.student-photo:hover {
  transform: scale(1.05);
}
.image-preview-overlay {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.8);
  z-index: 1050;
  display: flex;
  justify-content: center;
  align-items: center;
}
.full-image {
  max-width: 90%;
  max-height: 90%;
  border-radius: 10px;
  box-shadow: 0 0 15px #fff;
}
.button-center {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
.chart-wrapper {
  margin-top: 25px;
}
.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 15px;
  margin-top: 30px;
}
.btn {
  padding: 10px 18px;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  color: #fff;
  transition: background-color 0.3s ease;
}
.btn-green {
  background-color: #28a745;
}
.btn-green:hover {
  background-color: #218838;
}
.btn-yellow {
  background-color: #ffc107;
  color: #000;
}
.btn-yellow:hover {
  background-color: #e0a800;
}
.btn-red {
  background-color: #dc3545;
}
.btn-red:hover {
  background-color: #c82333;
}
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
</style>
