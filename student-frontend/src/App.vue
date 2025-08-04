<template>
  <div class="app-container">
    <!-- Header -->
    <div class="header">
      <h1 class="main-title">IT Department Student Details</h1>
    </div>

    <!-- Add Student Form -->
    <StudentForm @student-added="addStudentToList" />

    <!-- Student List -->
    <StudentList
    :students="students"
    @delete-student="removeStudentFromList"
    @update-student="updateStudentInList"
    @view-student="selectedStudent = $event"
    />



    <!-- Student Detail Modal -->
    <StudentDetail
      v-if="selectedStudent"
      :student="selectedStudent"
      @close="selectedStudent = null"
      @update="handleUpdateStudent"
      @delete="handleDeleteStudent"
    />
  </div>
</template>

<script>
import axios from 'axios'
import StudentForm from './components/StudentForm.vue'
import StudentList from './components/StudentList.vue'
import StudentDetail from './components/StudentDetail.vue'
import ResultsChart from './components/ResultsChart.vue'

export default {
  components: {
    StudentForm,
    StudentList,
    StudentDetail,
    ResultsChart
  },
  data() {
    return {
      students: [],
      selectedStudent: null,
      showResults: false
    }
  },
  async mounted() {
    await this.fetchStudents()
  },
  methods: {
    async fetchStudents() {
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/students/')
        this.students = res.data
        console.log("Fetched students:", res.data)

      } catch (error) {
        console.error('Fetch failed:', error)
      }
    },
    addStudentToList(student) {
      this.students.unshift(student)
    },
    removeStudentFromList(id) {
      this.students = this.students.filter(s => s.id !== id)
    },
    updateStudentInList(updatedStudent) {
      const index = this.students.findIndex(s => s.id === updatedStudent.id)
      if (index !== -1) {
        this.students.splice(index, 1, updatedStudent)
      }
    },
    handleUpdateStudent(updatedStudent) {
      this.updateStudentInList(updatedStudent)
      this.selectedStudent = null
    },
    handleDeleteStudent(id) {
      this.removeStudentFromList(id)
      this.selectedStudent = null
    }
  }
}
</script>

<style>
.app-container {
  min-height: 100vh;
  background-color: #f3f4f6;
  padding: 2rem;
  max-width: 1000px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
}

.header {
  text-align: center;
  margin-bottom: 2rem;
}

.main-title {
  font-size: 2.5rem;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.subtitle {
  color: #4b5563;
  font-size: 1rem;
}
</style>
