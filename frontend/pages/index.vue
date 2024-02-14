<script setup lang="ts">
definePageMeta({
  layout: false,
});

</script>

<template>
  <div class="container-fluid  text-center mt-4 b-4 px-4" style="width: auto; margin: auto;">
    <div class="row gx-5">
      <div class="col-md-6">
        <div class="card ">
          <div class="card-header">
            生徒用
          </div>  
          <div class="card-body">
            <p>こちらは生徒用のアカウントです</p>
            <NuxtLink to="/studentlogin" class="btn btn-primary mt-3">生徒用</NuxtLink>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card ">
          <div class="card-header">
            管理者用
          </div>  
          <div class="card-body">
            <p>こちらは管理者用のアカウントです</p>
            <NuxtLink to="/adminlogin" class="btn btn-primary mt-3">管理者用</NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>