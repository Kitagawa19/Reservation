<script setup lang="ts">

const userName = ref('')
const password = ref('')

const login = async () => {
  if(userName.value === '' || password.value === '') {
    alert('学籍番号とパスワードを入力してください');
  }else {
    try{
      const res = await fetch('http://127.0.0.1:8000/student_login/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: userName.value,
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

const registeruserName = ref('')
const registerPassword = ref('')

const register = async () => {
  if(registeruserName.value === '' || registerPassword.value === '') {
    alert('学籍番号とパスワードを入力してください');
  }else {
    try{
      const res = await fetch('http://127.0.0.1:8000/student_register/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          student_number: registeruserName.value,
          password: registerPassword.value,
        }),
      });
      if (res.ok) {
        alert('登録に成功しました');
        navigateTo('/homepage');
      } else {
        alert('登録に失敗しました');
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
      <div class="col-md-6 ">
        <div class="header p-3">
          <h3>会員登録がお済みの方</h3>
        </div>
        <div class="form-floating mb-3">
          <input type="text" class="form-control" id="floatingInput" placeholder="" v-model="userName">
          <label for="floatingInput">お名前</label>
        </div>
        <div class="form-floating">
          <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="password">
          <label for="floatingPassword">パスワード</label>
        </div>
        <button type="submit" class="btn btn-primary mt-3" @click="login">ログイン</button>
      </div>
      <div class="col-md-1 p-4">
        <div class="d-flex" style="height: 200px;">
        <div class="vr d-none d-md-block"></div> <!-- 縦線 -->
        </div>
      </div>
      <div class="col-md-5 p-4">
        <div class="header">
          <h3>会員登録がお済みでない方へ</h3>
        </div>
      </div>
    </div>
  </div>
</template>