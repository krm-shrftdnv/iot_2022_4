<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-4">
        <form>
          CO2:<input v-model="co2" placeholder="CO2" type="number" min="0"><br>
          tVOC:<input v-model="tvoc" placeholder="tVOC" type="number" min="0">
        </form>
        <button @click="save">Установить критические значения</button>
        <br>
        <button @click="stop">Stop</button>
        <br>
        <button @click="start">Start</button>
        <div v-for="alert in alerts" :key="alert.id" class="alert alert-danger" role="alert">
          Date: {{alert.created_at}}: CO2 {{alert.co2}} tVOC: {{alert.tvoc}}
        </div>
      </div>
      <div class="col-8">
        <canvas id="chart-co2"></canvas>
        <canvas id="chart-tvoc"></canvas>
      </div>
    </div>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import {Chart, registerables} from 'chart.js'
import axios from 'axios'
import mqtt from 'mqtt/dist/mqtt'

Chart.register(...registerables)
export default {
  name: 'App',
  components: {},
  props: {
    msg: String
  },
  data: () => ({
    alerts: [
      {
        "id": 0,
        "co2": 1000,
        "tvoc": 9,
        "created_at": "21.04.2022 10:10:00.00"
      }
    ],
    indications: [
      {
        "id": 0,
        "co2": 1000,
        "tvoc": 9,
        "created_at": "21.04.2022 10:10:00.00"
      }
    ],
    mqttClient: {},

  }),
  computed: {
    chartDataCo2() {
      return this.indications.map(e => ({
        y: e.co2,
        x: e.created_at
      }))
    },
    chartDataTVOC() {
      return this.indications.map(e => ({
        y: e.tvoc,
        x: e.created_at
      }))
    },
    co2: {
      get() {
        return this.$store.getters.co2
      },
      set(n) {
        this.$store.commit('SET_CO2', n)
      }
    },
    tvoc: {
      get() {
        return this.$store.getters.tvoc
      },
      set(n) {
        this.$store.commit('SET_TVOC', n)
      }
    }
  },
  async mounted() {
    let response = await axios.get('http://localhost:8080/indications')
    this.indications = response.data
    response = await axios.get('http://localhost:8080/alerts')
    this.alerts = response.data
    let ctx = document.getElementById('chart-co2').getContext('2d')
    new Chart(ctx, {
      type: 'line',
      data: {
        datasets: [{
          label: 'CO2',
          data: this.chartDataCo2
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
    let ctx1 = document.getElementById('chart-tvoc').getContext('2d')
    new Chart(ctx1, {
      type: 'line',
      data: {
        datasets: [{
          label: 'tVOC',
          data: this.chartDataTVOC
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
    this.mqttClient = mqtt.connect('ws://broker.hivemq.com:8000/mqtt')
    this.mqttClient.on('message', function (topic, message) {
      let payload = JSON.parse(message.toString())
      if (payload.command === 'alert'){
       console.log('co2 too high')
      }
    });
    this.mqttClient.subscribe('itis_team_4/control')
  },

  methods: {
    async save() {
      await axios.post('http://localhost:8080/set_criticals',
          {
            "co2": this.co2,
            "tvoc": this.tvoc
          }
      )
    },
    async start() {
      await axios.get('http://localhost:8080/start')
    },
    async stop() {
      await axios.get('http://localhost:8080/stop')
    },
  }
}
</script>


