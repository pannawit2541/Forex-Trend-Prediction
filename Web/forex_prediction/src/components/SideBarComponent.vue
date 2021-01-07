<template>
  <b-menu>
    <b-menu-list label="Forex Prediction">
      <b-menu-item icon="account" label="Dashboard" :active="isActive" tag="router-link" to="/"></b-menu-item>
      <b-menu-item icon="account" label="EURUSD" tag="router-link" to="/EURUSD"></b-menu-item>
      <b-menu-item icon="account" label="GBPUSD" tag="router-link" to="/GBPUSD"></b-menu-item>
      <b-menu-item icon="account" label="USDJPY" tag="router-link" to="/USDJPY"></b-menu-item>
    </b-menu-list>
  </b-menu>
</template>

<script>
export default {
  data() {
    return {
      isActive: true
    }
  }
}
</script>