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
          <input type="text" class="form-control" id="floatingInput" placeholder="" v-model="gag">
          <label for="floatingInput">お名前</label>
        </div>
      </div>
    </div>
  </div>
</template>
