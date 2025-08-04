<template>
  <div class="fixed inset-0 bg-gray-800 bg-opacity-70 flex justify-center items-center z-50">
    <div class="bg-white rounded-lg p-6 max-w-xl w-full shadow-lg relative">
      <!-- Close Button -->
      <button class="absolute top-2 right-2 text-gray-500 hover:text-gray-700" @click="$emit('close')">&times;</button>
      
      <!-- Title -->
      <h2 class="text-2xl font-bold mb-4">{{ student.name }}'s Details</h2>

      <!-- Student Info -->
      <div class="grid grid-cols-2 gap-4 text-sm text-gray-700 mb-6">
        <p><strong>Roll No:</strong> {{ student.roll_no }}</p>
        <p><strong>Department:</strong> {{ student.department }}</p>
        <p><strong>Email:</strong> {{ student.email }}</p>
        <p><strong>Phone:</strong> {{ student.phone }}</p>
        <p><strong>Date of Birth:</strong> {{ student.dob }}</p>
        <p><strong>Age:</strong> {{ student.age }}</p>
        <p><strong>Attendance:</strong> {{ student.attendance_percentage }}%</p>
        <p><strong>Mark:</strong> {{ student.mark_percentage }}%</p>
      </div>
      
      
      <!-- Attendance Pie Chart -->
       <p><strong>Debug attendance:</strong> {{ student.attendance_percentage }}</p>
      <AttendanceChart :attendancePercent="Number(student.attendance_percentage)" />

      <!-- Show Results Button -->
      <div class="mt-4 flex justify-center">
        <button
          class="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
          @click="showResults = true"
        >
          Show Result
        </button>
      </div>

      <!-- Results Bar Chart -->
      <div v-if="showResults" class="mt-6">
        <ResultsChart :marks="Number(student.mark_percentage)" />
      </div>

      <!-- Actions -->
      <div class="mt-6 flex justify-end space-x-4">
        <button @click="$emit('edit', student)" class="px-4 py-2 bg-yellow-500 text-white rounded hover:bg-yellow-600">
          Edit
        </button>
        <button @click="handleDelete" class="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700">
          Delete
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import AttendanceChart from './AttendanceChart.vue';
import ResultsChart from './ResultsChart.vue';

const { student } = defineProps(['student']); // ✅ Destructured here
console.log("Student prop:", JSON.stringify(student, null, 2));

const emit = defineEmits(['close', 'edit', 'delete']);
const showResults = ref(false);

const handleDelete = () => {
  if (confirm(`Are you sure you want to delete ${student.name}?`)) {
    emit('delete', student.id);
  }
};
</script>




<style scoped>
/* same CSS as your original */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  z-index: 9999;
}

.modal-container {
  background: #fff;
  border-radius: 8px;
  max-width: 1000px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
}

.modal-content {
  padding: 24px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.modal-header h2 {
  font-size: 1.5rem;
  color: #333;
}

.close-button {
  background: transparent;
  border: none;
  cursor: pointer;
  color: #999;
  transition: color 0.2s ease;
}
.close-button:hover {
  color: #666;
}

.details-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 32px;
}

.student-info {
  flex: 2;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 16px;
}

.info-block label {
  font-size: 0.875rem;
  color: #666;
  margin-bottom: 4px;
  display: block;
}

.info-block p {
  font-size: 1rem;
  color: #222;
  margin: 0;
}

.photo-block {
  grid-column: 1 / -1;
}

.photo-block img {
  width: 128px;
  height: 128px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.chart-block {
  flex: 1;
}

.chart-block h3 {
  font-size: 1.125rem;
  color: #333;
  margin-bottom: 16px;
}

.chart-container {
  background: #f8f8f8;
  padding: 16px;
  border-radius: 8px;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 16px;
  margin-top: 32px;
  padding-top: 24px;
  border-top: 1px solid #eee;
}

.edit-btn,
.delete-btn {
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  color: #fff;
  cursor: pointer;
  font-weight: 500;
}

.edit-btn {
  background-color: #1d4ed8;
}
.edit-btn:hover {
  background-color: #1e40af;
}

.delete-btn {
  background-color: #dc2626;
}
.delete-btn:hover {
  background-color: #b91c1c;
}
</style>
