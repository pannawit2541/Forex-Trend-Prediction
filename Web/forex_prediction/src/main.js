import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import './icon'

Vue.config.productionTip = false

import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

import VueApexCharts from 'vue-apexcharts'
Vue.use(VueApexCharts,Buefy)

Vue.component('apexchart', VueApexCharts)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
