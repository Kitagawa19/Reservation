<template>
  <div class="backgroundSetting">
    <div class="container p-3">
      <div class="card">
        <div class="card-header text-center">
          予約表
        </div>
        <div class="card-body">
          <div class="row">
            <div class="col-md-6">
              <div class="form-floating mb-3">
                <label for="floatingInput" v-show="!room_number">借りる教室</label>
                <select class='form-select' id="floatingInput" v-model="room_number">
                  <option v-for="room in roomData.rooms" :key="room.id">
                    {{ room.name }}
                  </option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating mb-3">
                <input type="date" class="form-control" id="exampleDate" name="date" v-model="date">
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating mb-3">
                <label for="floatingInput" v-show="!start_time">いつ頃から借りますか？</label>
                <select class="form-select" aria-level="start_time" v-model="start_time">
                  <option v-for="time in startTimes" :key="time" :value="time">{{ time }}</option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-floating mb-3">
                <label for="floatingInput" v-show="!end_time">いつまでいますか？</label>
                <select class="form-select" aria-level="end_time" v-model="end_time">
                  <option v-for="time in endTimes" :key="time" :value="time">{{ time }}</option>
                </select>
              </div>
            </div>
            <div class="col-md-12">
              <div class="form-floating mb-3">
                <input type="text" class="form-control" id="floatingInput" placeholder="" v-model="purpose">
                <label for="floatingInput">目的</label>
              </div>
            </div>
            <button type="submit" class="btn btn-primary mt-3" @click="apply">申請</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const room_number = ref('');
const start_time = ref(null);
const end_time = ref(null);
const date = ref('');
const purpose = ref('');
const startTimes = ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
  '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30',
  '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00',];
const endTimes = ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
  '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30',
  '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00',];

let roomData = ref({
  rooms: [],
});

onMounted(async () => {
  try {
    const res = await fetch('http://127.0.0.1:8000/Classroom/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    const data = await res.json();
    roomData.value.rooms = data;
  } catch (error) {
    console.log(error);
  }
});


const apply = async () => {
  const startTime = new Date(`1970-01-01T${start_time.value}:00`);
  const endTime = new Date(`1970-01-01T${end_time.value}:00`);
  const UpdateDate = new Date(`${date.value}`);
  if (room_number.value === '' || start_time.value === '' || end_time.value === '' || purpose.value === '') {
    alert('全ての項目を入力してください');
  } else if (startTime >= endTime) {
    alert('開始時間と終了時間を正しく入力してください');
  } else {
    try {
      const res = await fetch('http://127.0.0.1:8000/Booking/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: localStorage.getItem('username'),
          date : UpdateDate.toISOString().split('T')[0], 
          classroom_name: room_number.value,
          start_time: start_time.value,
          end_time: end_time.value,
          purpose: purpose.value,
        }),
      });
      if (res.ok) {
        alert('予約に成功しました');
      } else {
        alert('予約に失敗しました');
      }
    } catch (error) {
      console.log(error);
    }
  }
};
</script>

<style>
.card {
  margin-top: 20px;
  margin-bottom: 20px;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}
</style>