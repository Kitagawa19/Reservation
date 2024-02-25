<script setup lang="ts">
const room_number = ref('');
const start_time = ref(null);
const end_time = ref(null);
const purpose = ref('');
const times = ['9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30',
                '13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30',
                '17:00','17:30','18:00','18:30','19:00','19:30','20:00',];

let roomData = ref({
  rooms: [],
});

onMounted(async () => {
  try{
    const res = await fetch('http://127.0.0.1:8000/Classroom/',{
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    const data = await res.json();
    roomData.value.rooms = data;
  }catch (error) {
    console.log(error);
  }
});
</script>

<template>
  <div class="container p-3">
    <div class="card">
      <div class="card-header">
        予約表
      </div>
      <div class="card-body">
        <div class="form-floating mb-3">
          <label for="floatingInput" v-show="!room_number">借りる教室番号</label>
          <select class='form-select' id="floatingInput" v-model="room_number">
            <option v-for="room in roomData.rooms" :key="room.id">
              {{ room.name }}
            </option>
          </select> 
        </div>
        <div class="form-floating mb-3">
          <input type="date" class="form-control" id="exampleDate" name="date">
        </div>
        <div class="form-floating mb-3">
          <label for="floatingInput" v-show="!start_time">いつ頃からにしますか？</label>
          <select class="form-select" aria-level="start_time" v-model="start_time">
            <option v-for="time in times" :key="time" :value="time">{{ time }}</option>
          </select> 
        </div>
        <div class="form-floating mb-3">
          <label for="floatingInput" v-show="!start_time">いつまでいますか？</label>
          <select class="form-select" aria-level="start_time" v-model="start_time">
            <option v-for="time in times" :key="time" :value="time">{{ time }}</option>
          </select> 
        </div>
        <div class="form-floating mb-3">
          <input type="text" class="form-control" id="floatingInput" placeholder="" v-model="purpose">
          <label for="floatingInput">目的</label>
        </div>
        <button type="submit" class="btn btn-primary mt-3" @click="register">申請</button>
      </div>
    </div>
  </div>
</template>
