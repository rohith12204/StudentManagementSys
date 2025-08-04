<template>
  <div>
    <StudentForm @student-added="addStudentToList" />
    <StudentList 
      :students="students" 
      @delete-student="deleteStudentFromList" 
      @update-student="updateStudentInList" 
    />
  </div>
</template>

<script>
//import StudentForm from './StudentForm.vue'
//import StudentList from './StudentList.vue'
import axios from 'axios'

export default {
  components: { StudentForm, StudentList },
  data() {
    return {
      students: []
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
        // Replace the old student data with the updated one
        this.students.splice(index, 1, updatedStudent)
      }
    }
  }
}
</script>
