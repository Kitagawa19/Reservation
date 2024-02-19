<template>
  <div class="container-fluid p-3">
    <h1>{{ date }}</h1>
    <table class="table table-bordered">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">First</th>
          <th scope="col">Last</th>
          <th scope="col">Handle</th>
      </tr>
      </thead>
      <tbody>

      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'booking',
  props: ['date'],
};
</script>