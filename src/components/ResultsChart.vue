<template>
  <div class="results-chart-container">
    <h3 class="results-chart-title">Student Mark Results </h3>
    <div class="chart-wrapper">
      <canvas ref="chartCanvas"></canvas>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const props = defineProps(['students']);
const chartCanvas = ref(null);
let chartInstance = null;

const createChart = () => {
  if (!chartCanvas.value || !props.students || props.students.length === 0) return;

  const labels = props.students.map(student => student.name);
  const data = props.students.map(student => student.mark_percentage);

  chartInstance = new Chart(chartCanvas.value, {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        label: 'Mark Percentage',
        data,
        backgroundColor: '#4B9CD3',
        borderColor: '#2E6DA4',
        borderWidth: 1,
        borderRadius: 4,
        borderSkipped: false
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              return `${context.parsed.y}%`;
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          max: 100,
          ticks: {
            callback: function(value) {
              return value + '%';
            }
          },
          title: {
            display: true,
            text: 'Mark Percentage'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Students'
          },
          ticks: {
            maxRotation: 45,
            minRotation: 0
          }
        }
      },
      animation: {
        duration: 1000,
        easing: 'easeOutQuart'
      }
    }
  });
};

onMounted(() => {
  createChart();
});

onUnmounted(() => {
  if (chartInstance) {
    chartInstance.destroy();
  }
});

watch(() => props.students, () => {
  if (chartInstance) {
    chartInstance.destroy();
  }
  createChart();
}, { deep: true });
</script>

<style scoped>
.results-chart-container {
  background-color: #f9fafb;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  margin: 16px 0;
}

.results-chart-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 16px;
}

.chart-wrapper {
  width: 100%;
  height: 400px;
  position: relative;
}

.chart-wrapper canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100% !important;
  height: 100% !important;
}
</style>
