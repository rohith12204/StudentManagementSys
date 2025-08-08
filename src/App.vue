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
      @delete-student="deleteStudentFromList"
      @update-student="updateStudentInList"
      @view-student="selectedStudent = $event"
      @edit-student="editStudent"
    />

    <!-- Detail Modal -->
    <StudentDetail
      v-if="selectedStudent"
      :student="selectedStudent"
      @close="selectedStudent = null"
      @edit="editStudent"
    />

    <!-- Edit Modal -->
    <StudentEdit
  v-if="studentBeingEdited"
  :student="studentBeingEdited"
  @student-updated="updateStudentInList"
  @close="studentBeingEdited = null"
/>

  </div>
</template>

<script>
import StudentForm from './components/StudentForm.vue'
import StudentList from './components/StudentList.vue'
import StudentDetail from './components/StudentDetail.vue'
import StudentEdit from './components/StudentEdit.vue'
import axios from 'axios'

export default {
  components: {
    StudentForm,
    StudentList,
    StudentDetail,
    StudentEdit,
  },
  data() {
    return {
      students: [],
      selectedStudent: null,
      isDetailModalOpen: false,
      isEditModalOpen: false,
      studentBeingEdited: null,
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
      } catch (error) {
        console.error('Fetch failed:', error)
      }
    },
    addStudentToList(newStudent) {
      this.students.unshift(newStudent)
    },
    deleteStudentFromList(id) {
      this.students = this.students.filter(s => s.id !== id)
    },
    updateStudentInList(updatedStudent) {
      const index = this.students.findIndex(s => s.id === updatedStudent.id)
      if (index !== -1) {
        this.students.splice(index, 1, updatedStudent)
      }
    },
    editStudent(student) {
      this.studentBeingEdited = student
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


