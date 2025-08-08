<template>
  <div class="chart-container">
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

interface Props {
  attendancePercent: number;
}

const props = defineProps<Props>();
const chartCanvas = ref<HTMLCanvasElement>();
let chartInstance: Chart | null = null;

const renderChart = () => {
  if (!chartCanvas.value) return;

  const presentPercent = Number(props.attendancePercent);
  const absentPercent = 100 - presentPercent;

  if (chartInstance) {
    chartInstance.destroy();
  }

  chartInstance = new Chart(chartCanvas.value, {
    type: 'pie',
    data: {
      labels: ['Present', 'Absent'],
      datasets: [{
        data: [presentPercent, absentPercent],
        backgroundColor: ['#10B981', '#EF4444'],
        borderColor: ['#059669', '#DC2626'],
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            padding: 20,
            usePointStyle: true
          }
        },
        tooltip: {
          callbacks: {
            label: function (context) {
              return `${context.label}: ${context.parsed}%`;
            }
          }
        }
      },
      animation: {
        animateRotate: true,
        duration: 1000
      }
    }
  });
};

onMounted(() => {
  if (props.attendancePercent != null) {
    renderChart();
  }
});

// Reactively watch for updates to attendancePercent
watch(() => props.attendancePercent, (newVal) => {
  if (newVal != null) {
    renderChart();
  }
});

onUnmounted(() => {
  if (chartInstance) {
    chartInstance.destroy();
  }
});

</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 250px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
  box-sizing: border-box;
}

canvas {
  width: 100% !important;
  height: 100% !important;
}
</style>
