<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-3">
        <form>
          <input v-model="co2" placeholder="CO2" type="number" min="0">
          <input v-model="tvoc" placeholder="tVOC" type="number" min="0">
        </form>
        <button @click="save">Установить критические значения</button>
      </div>
      <div class="col-9">
        <canvas id="chart"></canvas>
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
        "CO2": 1000,
        "tVOC": 9,
        "created_at": "21.04.2022 10:10:00.00"
      }
    ],
    indications: [
      {
        "id": 0,
        "CO2": 1000,
        "tVOC": 9,
        "created_at": "21.04.2022 10:10:00.00"
      }
    ],
    mqttClient: {},

  }),
  computed: {
    chartData() {
      return this.indications.map(e => ({
        y: e.CO2,
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
    let response = await axios.get('https://virtserver.swaggerhub.com/krm-shrftdnv/itis_team_4/0.0.1/indications')
    this.indications = response.data
    let ctx = document.getElementById('chart').getContext('2d')
    new Chart(ctx, {
      type: 'line',
      data: {
        datasets: [{
          label: 'CO2',
          data: this.chartData
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
      if (message.toString() === 'alert') {
        alert('CO2 is too high')
      }
    });
    this.mqttClient.subscribe('itis_team_4/control')
  },
  methods: {
    async save() {
      await axios.post('https://virtserver.swaggerhub.com/krm-shrftdnv/itis_team_4/0.0.1/set_criticals',
          {
            "CO2": this.co2,
            "tVOC": this.tvoc
          }
      )
    }
  }
}
</script>


