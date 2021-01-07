import Vue from 'vue'
import VueRouter from 'vue-router'
import EURUSD from '../views/EURUSD/index.vue'
import GBPUSD from '../views/GBPUSD/index.vue'
import USDJPY from '../views/USDJPY/index.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'APP',
    component: EURUSD
  },
  {
    path: '/',
    name: 'EURUSD',
    component: EURUSD
  },
  {
    path: '/GBPUSD',
    name: 'GBPUSD',
    component: GBPUSD
  },
  {
    path: '/USDJPY',
    name: 'USDJPY',
    component: USDJPY
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
