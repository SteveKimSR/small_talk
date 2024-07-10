<template>
  <div>
    <div>
      <label for="region">Region:</label>
      <input id="region" v-model="inputData.region" placeholder="Enter region" />
    </div>
    <div>
      <label for="gender">Gender:</label>
      <input id="gender" v-model="inputData.gender" placeholder="Enter gender" />
    </div>
    <div>
      <label for="age">Age:</label>
      <input id="age" v-model="inputData.age" placeholder="Enter age" type="number" />
    </div>
    <div>
      <label for="departure_time">Departure Time:</label>
      <input id="departure_time" v-model="inputData.departure_time" placeholder="Enter departure time" type="number" />
    </div>
    <div>
      <label for="arrival_time">Arrival Time:</label>
      <input id="arrival_time" v-model="inputData.arrival_time" placeholder="Enter arrival time" type="number" />
    </div>
    <div>
      <label for="msg">Message:</label>
      <textarea id="msg" v-model="inputData.msg" placeholder="Enter your message"></textarea>
    </div>
    <button @click="submitData">Submit</button>
    <button @click="goToHelloWorld">Back to Hello World</button>

    <div v-if="submitted">
      <h3>Submitted Data:</h3>
      <p><strong>Region:</strong> {{ submittedData.region }}</p>
      <p><strong>Gender:</strong> {{ submittedData.gender }}</p>
      <p><strong>Age:</strong> {{ submittedData.age }}</p>
      <p><strong>Departure Time:</strong> {{ submittedData.departure_time }}</p>
      <p><strong>Arrival Time:</strong> {{ submittedData.arrival_time }}</p>
      <p><strong>Message:</strong> {{ submittedData.msg }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      inputData: {
        region: '',
        gender: '',
        age: '',
        departure_time: '',
        arrival_time: '',
        msg: ''
      },
      submitted: false,
      submittedData: {}
    };
  },
  methods: {
    goToHelloWorld() {
      this.$emit('change-view', 'HelloWorld');
    },
    submitData() {
      axios.post('http://localhost:5000/submit', this.inputData)
        .then(response => {
          this.submittedData = response.data.data;
          this.submitted = true;
          setTimeout(() => {
            this.message = '3초가 지났습니다!';
            }, 3000);
          this.$emit('change-view', 'PictureOut');
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    },
    
  }
};
</script>

<style scoped>
input, textarea {
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  font-size: 16px;
}
button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
}
label {
  font-weight: bold;
}
</style>
