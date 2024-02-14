<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const isNavOpen = ref(false)

const toggleNav = () => {
  isNavOpen.value = !isNavOpen.value
}

const goBack = () => {
  router.go(-1)
}

onMounted(() => {
  const myNav = document.getElementById('navbarSupportedContent')
  if (myNav) {
    myNav.classList.remove('show')
  }
})
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">サンプルサイト</a>
    <button class="navbar-toggler" type="button" @click="toggleNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" :class="{ 'show': isNavOpen }" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/studentlogin">生徒</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/adminlogin">管理者</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click="goBack">一つ前に戻る</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>