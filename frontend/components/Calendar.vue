<template>
  <div class="calendar-container p-3">
    <div class="controls position-relative d-flex justify-content-center align-items-center">
      <div class="row align-items-center">
        <div class="col-auto">
          <button  class="btn btn-outline-primary" @click="prevMonth"><</button>
        </div>
        <div class="col-auto">
        {{ currentYear }}年{{ currentMonth + 1 }}月
        </div>
        <div class="col-auto">
          <button class="btn btn-outline-primary justify-content-md-end" @click="nextMonth">></button>
        </div>
      </div>
    </div>
    <table class="calendar my-4">
      <thead>
        <tr>
          <th v-for="day in ['日', '月', '火', '水', '木', '金', '土']" :key="day">{{ day }}</th>
        </tr>
      </thead>
      <tbody>
      <td>
        <tr v-for="day in day">
      {{  day.getDate() }}
      </tr>
      </td>
</tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, defineEmits } from 'vue'

let currentYear = ref(new Date().getFullYear())
let currentMonth = ref(new Date().getMonth())
let weeks = ref<(Date | null)[]>([])

const emit = defineEmits(['update-date'])

const selectDate = (day: Date) => {
  if (day) {
    const date = day.toISOString().split('T')[0]  // YYYY-MM-DD形式に変換
    emit('update-date', date)
  }
}

const generateCalendar = () => {
  const daysInMonth = new Date(currentYear.value, currentMonth.value + 1, 0).getDate()
  const firstDayOfWeek = new Date(currentYear.value, currentMonth.value, 1).getDay()

  let days = []
  for (let i = 0; i < firstDayOfWeek; i++) {
    days.push(null)
  }

  for (let day = 1; day <= daysInMonth; day++) {
    days.push(new Date(currentYear.value, currentMonth.value, day))
  }

  while (days.length % 7 !== 0) {
    days.push(null)
  }

  weeks.value = []
  for (let i = 0; i < days.length; i += 7) {
    weeks.value.push(days.slice(i, i + 7))
  }
}

const prevMonth = () => {
  currentMonth.value--
  if (currentMonth.value < 0) {
    currentMonth.value = 11
    currentYear.value--
  }
  generateCalendar()
}

const nextMonth = () => {
  currentMonth.value++
  if (currentMonth.value > 11) {
    currentMonth.value = 0
    currentYear.value++
  }
  generateCalendar()
}

onMounted(() => {
  generateCalendar()
})
</script>

<style>
.calendar-container {
  max-width: 600px;
  margin: auto;
}

.calendar {
  width: 100%;
  border-collapse: collapse;
}

.calendar th, .calendar td {
  border: 1px solid #ccc;
  text-align: center;
  padding: 8px;
}

.is-other-month {
  background-color: #f9f9f9;
}

.is-today {
  background-color: #ff0;
}
</style>
