<script setup lang="ts">
const room_number = ref('');
const start_time = ref('');

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
  <div class="container-fluid p-3">
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
          <label for="floatingInput" v-show="!start_time">開始時間</label>
          <select class="form-select" aria-level="start_time" v-model="start_time">
            <option value="9:00">9:00</option>
            <option value="10:00">10:00</option>
            <option value="11:00">11:00</option>
            <option value="12:00">12:00</option>
            <option value="13:00">13:00</option>
            <option value="14:00">14:00</option>
            <option value="15:00">15:00</option>
            <option value="16:00">16:00</option>
            <option value="17:00">17:00</option>
            <option value="18:00">18:00</option>
            <option value="19:00">19:00</option>
            <option value="20:00">20:00</option>
          </select> 
        </div>
        <div class="form-floating mb-3">
          <input type="text" class="form-control" id="floatingInput" placeholder="" v-model="purpose">
          <label for="floatingInput">目的</label>
        </div>
      </div>
    </div>
  </div>
</template>
