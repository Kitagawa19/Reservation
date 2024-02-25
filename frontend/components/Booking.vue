<script setup lang="ts">
</script>

<template>
  <div class="container-fluid p-3">
    <div class="card">
      <div class="card-header">
        予約表
      </div>
      <div class="card-body">
        <div class="form-floating mb-3">
          <input type="date" class="form-control" id="exampleDate" name="date">
        </div>
        <div class="form-floating mb-3">
          <input type="text" class="form-control" id="floatingInput" placeholder="" v-model="purpose">
          <label for="floatingInput">開始時刻</label>
        </div>
        <div class="form-floating mb-3">
          <input type="text" class="form-control" id="floatingInput" placeholder="" v-model="purpose">
          <label for="floatingInput">目的</label>
        </div>
      </div>
    </div>
  </div>
</template>
