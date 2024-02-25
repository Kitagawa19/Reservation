<script setup lang="ts">

const isNavOpen = ref(false)

const toggleNav = () => {
  isNavOpen.value = !isNavOpen.value
}

onMounted(() => {
  const myNav = document.getElementById('navbarSupportedContent')
  if (myNav) {
    myNav.classList.remove('show')
  }
})

const logout = async () => {
  try{
    const res = await fetch('http://127.0.0.1:8000/logout/',
    {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    if (res.ok) {
      alert('ログアウトしました');
      navigateTo('/');
    } else {
      alert('ログアウトに失敗しました');
    }
  }catch (error) {
      console.log(error);
  }
}
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="/homepage">サンプルサイト</a>
    <button class="navbar-toggler" type="button" @click="toggleNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" :class="{ 'show': isNavOpen }" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/homepage">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/calendar">カレンダー</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/booking">予約</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" @click="logout">ログアウト</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
</template>