<template>
  <div class="wrapper">
    <div class="sidebar">
      <div class="header">
        <h3>Forex Prediction</h3>
      </div>
      <ul :class="active">
    
          <li class="Dashboard" v-on:click="makeActive('Dashboard')">
          <router-link :to="'/'"
            ><fa-icon
              class="icon"
              :icon="['fas', 'chart-pie']"
              size="lg"
            ></fa-icon>
            Dashboard</router-link
          ></li>
         
        <li class="EURUSD" v-on:click="makeActive('EURUSD')">
          <router-link :to="'/EURUSD'"
            ><fa-icon
              class="icon"
              :icon="['fas', 'euro-sign']"
              size="lg"
            ></fa-icon
            >EUR/USD</router-link
          >
        </li>
        <li class="GBPUSD" v-on:click="makeActive('GBPUSD')">
          <router-link :to="'/GBPUSD'"
            ><fa-icon
              class="icon"
              :icon="['fas', 'yen-sign']"
              size="lg"
            ></fa-icon>
            GBP/USD</router-link
          >
        </li>
        <li class="USDJPY" v-on:click="makeActive('USDJPY')">
          <router-link :to="'/USDJPY'"
            ><fa-icon
              class="icon"
              :icon="['fas', 'pound-sign']"
              size="lg"
            ></fa-icon
            >USD/JPY</router-link
          >
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "SideBarComponent",

  data() {
    return {
      active: "Dashboard",
    };
  },
  methods: {
    makeActive(item) {
      this.active = item;
      console.log(item);
    },
  },
};
</script>

<style scoped>
.wrapper {
  display: flex;
  position: relative;
}
.wrapper .sidebar {
  position: fixed;
}
.sidebar .header {
  height: 65px;
  width: 225px;
  background-color: #3c3b54;
  /* margin-bottom: 30px; */
  /* position: relative; */
}
.sidebar .header h3 {
  color: #ffffff;
  font-weight: bold;
  /* font-size: 18px; */
  text-transform: uppercase;
  padding: 18px 0px 0px 20px;
  letter-spacing: 0.2em;
}

.wrapper .sidebar ul li {
  padding: 15px 10px 0px 30px;
  height: 55px;
  /* display: inline-block; */
  position: relative;
}
.wrapper .sidebar ul li a {
  color: #a5a4bf;
  display: block;
  height: 35px;
}

.wrapper .sidebar ul li a .icon {
  width: 40px;
  height: 20px;
  /* color: red; */
}

.wrapper .sidebar ul li:hover {
  background-color: #3c3b54;
}

.wrapper .sidebar ul li:hover a {
  color: #ffffff;
}

.wrapper .sidebar ul li:visited {
  background-color: #3c3b54;
}


.wrapper .sidebar ul.Dashboard .Dashboard,
.wrapper .sidebar ul.EURUSD .EURUSD,
.wrapper .sidebar ul.GBPUSD .GBPUSD,
.wrapper .sidebar ul.USDJPY .USDJPY {
  background-color: #3c3b54;
}

.wrapper .sidebar ul.Dashboard .Dashboard .icon,
.wrapper .sidebar ul.EURUSD .EURUSD .icon,
.wrapper .sidebar ul.GBPUSD .GBPUSD .icon,
.wrapper .sidebar ul.USDJPY .USDJPY .icon {
  color: #a3a0fb;
}
</style>
