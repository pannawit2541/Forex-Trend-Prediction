<template>
  <div id="app">
    <router-view />
    <div id="button-currency">
      <ul>
        <li>
          <button><router-link to="/">EUR/USD</router-link></button>
        </li>
        <li>
          <button><router-link to="/USDJPY">USD/JPY</router-link></button>
        </li>
        <li>
          <button><router-link to="/GBPUSD">GBP/USD</router-link></button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>

export default {
  name: "app",
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
li {
  display: inline;
  margin-left: 10px;
}
</style>
