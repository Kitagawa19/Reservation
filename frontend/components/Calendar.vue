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
        <tr v-for="(week, index) in weeks" :key="index">
          <td v-for="day in week" :key="day" 
          :class="{ 'is-other-month': day && day.getMonth() !== currentMonth }" @click="selectDate(day)">
          {{ day ? day.getDate() : '' }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentYear: new Date().getFullYear(),
      currentMonth: new Date().getMonth(),
      currentDate: new Date().getDate(),
      weeks: [],
    };
  },
  created() {
    this.currentYear = new Date().getFullYear();
    this.currentMonth = new Date().getMonth();
    this.generateCalendar();
  },
  methods: {
    selectDate(day) {
      if (day) {
        const date = day.toISOString().split('T')[0];  // YYYY-MM-DD形式に変換
        this.$router.push({ name: 'booking', params: { date }});
      }
    },


    generateCalendar() {
      const daysInMonth = new Date(this.currentYear, this.currentMonth + 1, 0).getDate();
      const firstDayOfWeek = new Date(this.currentYear, this.currentMonth, 1).getDay();

      let days = [];
      // 先月の日付をスキップするための空のセルを追加
      for (let i = 0; i < firstDayOfWeek; i++) {
        days.push(null); // 空のセルを追加
      }

      // 当月の日付を追加
      for (let day = 1; day <= daysInMonth; day++) {
        days.push(new Date(this.currentYear, this.currentMonth, day));
      }

      // 次月の日付をスキップするために、週の終わりまで空のセルを追加
      while (days.length % 7 !== 0) {
        days.push(null); // 空のセルを追加
      }

      // 週ごとに分割
      this.weeks = [];
      for (let i = 0; i < days.length; i += 7) {
        this.weeks.push(days.slice(i, i + 7));
      }
    },
    prevMonth() {
      this.currentMonth--;
      if (this.currentMonth < 0) {
        this.currentMonth = 11;
        this.currentYear--;
      }
      this.generateCalendar();
    },
    nextMonth() {
      this.currentMonth++;
      if (this.currentMonth > 11) {
        this.currentMonth = 0;
        this.currentYear++;
      }
      this.generateCalendar();
    },
  },
};
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
