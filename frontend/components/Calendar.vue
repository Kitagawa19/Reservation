<template>
  <div class="backgroundSetting">
    <div class="calendar-container p-3">
      <div class="controls position-relative d-flex justify-content-center align-items-center">
        <div class="row align-items-center">
          <div class="col-auto">
            <button class="btn btn-outline-primary" @click="prevMonth"><</button>
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
            <th v-for="day in weekDays" :key="day">{{ day }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(week, index) in weeks" :key="index">
            <td v-for="day in week" :key="day" :class="{ 'is-other-month': day.getMonth() !== currentMonth }"
              @click="navigateToWeekSchedule(day)">
              {{ day ? day.getDate() : '' }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">

const currentYear = ref(new Date().getFullYear());
const currentMonth = ref(new Date().getMonth());
const weeks = ref([]);

const weekDays = ['日', '月', '火', '水', '木', '金', '土'];

function generateCalendar() {
  const daysInMonth = new Date(currentYear.value, currentMonth.value + 1, 0).getDate();
  const firstDayOfWeek = new Date(currentYear.value, currentMonth.value, 1).getDay();

  let days: (Date | null)[] = [];
  let day = 1 - firstDayOfWeek;

  // 前月の日付を埋める
  while (day <= 0) {
    days.push(new Date(currentYear.value, currentMonth.value, day++));
  }

  // 当月の日付を追加
  for (day = 1; day <= daysInMonth; day++) {
    days.push(new Date(currentYear.value, currentMonth.value, day));
  }

  // 次月の日付を追加して週の長さを7にする
  day = 1;
  while (days.length % 7 !== 0) {
    days.push(new Date(currentYear.value, currentMonth.value + 1, day++));
  }

  // 週ごとに分割
  weeks.value = [];
  for (let i = 0; i < days.length; i += 7) {
    weeks.value.push(days.slice(i, i + 7));
  }
}

function prevMonth() {
  currentMonth.value--;
  if (currentMonth.value < 0) {
    currentMonth.value = 11;
    currentYear.value--;
  }
  generateCalendar();
}

function nextMonth() {
  currentMonth.value++;
  if (currentMonth.value > 11) {
    currentMonth.value = 0;
    currentYear.value++;
  }
  generateCalendar();
}

onMounted(() => {
  generateCalendar();
});


function navigateToWeekSchedule(day) {
  if (!day) return; // 空のセルをクリックした場合は何もしない
  const dateStr = `${day.getFullYear()}-${day.getMonth() + 1}-${day.getDate()}`;
  navigateTo(`/week/${dateStr}`);
}

</script>

<style>
.calendar-container {
  max-width: 600px;
  margin: auto;
}

.calendar {
  width: 100%;
  border-collapse: collapse;
  background-color: #e0ffff;
}

.calendar th,
.calendar td {
  border: 1px solid #ccc;
  text-align: center;
  padding: 8px;
  height: 60px;
}

.is-other-month {
  background-color: #f9f9f9;
}

.is-today {
  background-color: #ff0;
}
.is-other-month {
  visibility: hidden;
}
</style>
