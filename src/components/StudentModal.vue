<template>
  <div class="modal-overlay">
    <div class="modal-content">
      <h2>{{ student.name }}</h2>
      <p><strong>Attendance %:</strong> {{ student.attendance_percentage }}</p>
      <p><strong>Marks %:</strong> {{ student.mark_percentage }}</p>

      <canvas ref="attendanceChart" width="200" height="200"></canvas>

      <button @click="$emit('close')">Close</button>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
  name: 'StudentModal',
  props: {
    student: {
      type: Object,
      required: true
    }
  },
  mounted() {
    this.renderChart();
  },
  methods: {
    renderChart() {
  if (!this.student || this.student.attendance_percentage == null) return;

  const present = this.student.attendance_percentage;
  const absent = 100 - present;

  if (this.chartInstance) {
    this.chartInstance.destroy();
  }

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
      responsive: false
    }
  });
}

  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
}
.modal-content {
  background: white;
  margin: 10% auto;
  padding: 20px;
  width: 300px;
  border-radius: 10px;
}
</style>
