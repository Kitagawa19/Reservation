<script setup lang="ts">

const userName = ref('')
const password = ref('')

const login = async () => {
  if(userName.value === '' || password.value === '') {
    alert('学籍番号とパスワードを入力してください');
  }else {
    try{
      const res = await fetch('http://127.0.0.1:8000/superuser_login/', {
        method: 'POST',
        mode: 'cors',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          student_number: userName.value,
          password: password.value,
        }),
      });
      if (res.ok) {
        alert('ログインに成功しました');
        navigateTo('/homepage');
      } else {
        alert('ログインに失敗しました');
      }
    } catch (error) {
      console.log(error);
    }
  }
}
</script>

<template>
  <div class="container-fluid  text-center mt-4 b-4 px-4" style="width: auto; margin: auto;">
    <div class="row gx-5">
      <div class="col-md-6">
        <span class="border">
          <img src="/admin.jpg" class="center" style="width: 400px; border: none;" alt="...">
        </span>
      </div>
      <div class="col-md-6">
        <div class="card ">
          <div class="card-header">
            管理者ログイン
          </div>  
          <div class="card-body">
            <div class="form-floating mb-3">
              <input type="text" class="form-control" id="floatingInput" placeholder="" v-model="userName">
              <label for="floatingInput">学籍番号</label>
            </div>
            <div class="form-floating">
              <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password">
              <label for="floatingPassword">Password</label>
            </div>
            <button type="submit" class="btn btn-primary mt-3" @click="login">ログイン</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>