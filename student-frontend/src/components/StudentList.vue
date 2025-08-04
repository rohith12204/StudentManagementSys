<template>
  <div class="student-list-container">
    <div class="header">
      <h2>Student List</h2>
      <button @click="toggleResults">{{ showResults ? 'Hide Results' : 'Show Results' }}</button>
    </div>

    <div v-if="showResults" class="results-chart">
      <ResultsChart :students="students" />
    </div>

    <div v-if="students.length === 0" class="no-students">
      <p>No students added yet.</p>
      <p>Add your first student using the form above.</p>
    </div>

    <table v-else class="student-table">
      <thead>
        <tr>
          <th>Roll No</th>
          <th>Name</th>
          <th>Department</th>
          <th>Email</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id">
          <td>{{ student.roll_no }}</td>
          <td>{{ student.name }}</td>
          <td>{{ student.department }}</td>
          <td>{{ student.email }}</td>
          <td>
            <button class="view-btn" @click="viewDetails(student)">View Details</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal -->
    <div v-if="selectedStudent" class="modal-overlay" @click.self="selectedStudent = null">
      <div class="modal-content">
        <h3>Details for {{ selectedStudent.name }}</h3>
        <p><strong>Roll No:</strong> {{ selectedStudent.roll_no }}</p>
        <p><strong>Age:</strong> {{ selectedStudent.age }}</p>
        <p><strong>DOB:</strong> {{ selectedStudent.dob }}</p>
        <p><strong>Email:</strong> {{ selectedStudent.email }}</p>
        <p><strong>Phone:</strong> {{ selectedStudent.phone }}</p>
        <p><strong>Department:</strong> {{ selectedStudent.department }}</p>
        <p><strong>Marks %:</strong> {{ selectedStudent.mark_percentage ?? 'N/A' }}</p>
        <p><strong>Attendance %:</strong> {{ selectedStudent.attendance_percentage ?? 'N/A' }}</p>
        <div>
          <canvas ref="attendanceChart" width="250" height="250"></canvas>
        </div>
        <div class="modal-actions">
          <button class="edit-btn" @click="editStudent(selectedStudent)">Edit</button>
          <button class="delete-btn" @click="deleteStudent(selectedStudent.id)">Delete</button>
        </div>
        <button class="close-btn" @click="selectedStudent = null">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import ResultsChart from './ResultsChart.vue';

export default {
  name: 'StudentList',
  props: ['students'],
  components: { ResultsChart },
  data() {
    return {
      selectedStudent: null,
      showResults: false,
      chartInstance: null,
    };
  },
  methods: {
    toggleResults() {
      this.showResults = !this.showResults;
    },
    viewDetails(student) {
    console.log('Viewing student details:', student);
    console.log('Student object keys:', Object.keys(student));
    console.log('Attendance value:', student.attendance);
    this.selectedStudent = student;
    this.$nextTick(this.renderChart);
    },
    renderChart() {
      if (!this.selectedStudent || this.selectedStudent.attendance_percentage === undefined) return;

      if (this.chartInstance) {
        this.chartInstance.destroy();
      }

      const present = this.selectedStudent.attendance_percentage;
      const absent = 100 - present;

      const ctx = this.$refs.attendanceChart.getContext('2d');
      this.chartInstance = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ['Present %', 'Absent %'],
          datasets: [{
            data: [present, absent],
            backgroundColor: ['#4CAF50', '#FF5252']
          }]
        },
        options: {
          responsive: false,
        }
      });
    },
    editStudent(student) {
      this.$emit('edit-student', student);
      this.selectedStudent = null;
    },
    deleteStudent(id) {
      this.$emit('delete-student', id);
      this.selectedStudent = null;
    }
  }
};
</script>



<style scoped>
.student-list-container {
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h2 {
  font-size: 24px;
  color: #333;
}

.header button {
  padding: 8px 16px;
  background-color: #4CAF50;
  border: none;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}

.header button:hover {
  background-color: #45a049;
}

.results-chart {
  margin-top: 20px;
}

.no-students {
  text-align: center;
  color: #666;
  margin: 20px 0;
}

.student-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.student-table th,
.student-table td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}

.student-table th {
  background-color: #f2f2f2;
}

.view-btn {
  background-color: #2196F3;
  color: white;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.view-btn:hover {
  background-color: #0b7dda;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 90%;
  max-width: 500px;
}

.modal-content h3 {
  margin-bottom: 10px;
}

.modal-content p {
  margin: 5px 0;
}

.modal-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.edit-btn {
  background-color: #ffc107;
  color: black;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.edit-btn:hover {
  background-color: #e0a800;
}

.delete-btn {
  background-color: #f44336;
  color: white;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.delete-btn:hover {
  background-color: #d32f2f;
}

.close-btn {
  margin-top: 15px;
  padding: 8px 12px;
  background: #777;
  color: #fff;
  border: none;
  border-radius: 4px;
  float: right;
  cursor: pointer;
}

.close-btn:hover {
  background: #555;
}
</style>