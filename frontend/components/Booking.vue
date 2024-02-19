<template>
  <div>
    <head>{{ date }}</head>
    <table class="table table-bordered">
      <thead>
      </thead>
      <tbody>

      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'calendar',
  props: ['date'],
};
</script>