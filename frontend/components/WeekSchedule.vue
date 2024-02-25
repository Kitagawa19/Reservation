<template>
  <div>
    <h1>{{ weekStartDate }} から {{ weekEndDate }} のスケジュール</h1>
    <!-- スケジュール表示ロジック -->
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const selectedDate = ref(new Date(route.params.date));

const weekStartDate = computed(() => {
  const start = new Date(selectedDate.value);
  start.setDate(start.getDate() - start.getDay());
  return start.toISOString().split('T')[0];
});

const weekEndDate = computed(() => {
  const end = new Date(selectedDate.value);
  end.setDate(end.getDate() - end.getDay() + 6);
  return end.toISOString().split('T')[0];
});
</script>
