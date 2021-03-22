<template>
  <div class="wrapper">
    <div class="sidebar">
      <div class="header">
        <h3>Forex Prediction</h3>
      </div>
      <ul :class="active">
        <li class="Dashboard" v-on:click="makeActive('Dashboard')">
          <router-link id="router-link" :to="'/'">
            <div class="menu">
              <fa-icon
                class="icon"
                :icon="['fas', 'chart-pie']"
                size="lg"
              ></fa-icon>
              <span class="li-text">Overview</span>
            </div>
          </router-link>
        </li>
        <li class="EURUSD" v-on:click="makeActive('EURUSD')">
          <router-link id="router-link" :to="'/EURUSD'">
            <div class="menu">
              <fa-icon
                class="icon"
                :icon="['fas', 'euro-sign']"
                size="lg"
              ></fa-icon>
              <span class="li-text">EUR/USD</span>
            </div>
          </router-link>
        </li>
        <li class="GBPUSD" v-on:click="makeActive('GBPUSD')">
          <router-link id="router-link" :to="'/GBPUSD'">
            <div class="menu">
              <fa-icon
                class="icon"
                :icon="['fas', 'yen-sign']"
                size="lg"
              ></fa-icon>
              <span class="li-text">GBP/USD</span>
            </div>
          </router-link>
        </li>
        <li class="USDJPY" v-on:click="makeActive('USDJPY')">
          <router-link id="router-link" :to="'/USDJPY'">
            <div class="menu">
              <fa-icon
                class="icon"
                :icon="['fas', 'pound-sign']"
                size="lg"
              ></fa-icon
              ><span class="li-text"></span>
              USD/JPY
            </div>
          </router-link>
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
  /* width: 100%; */
  width: 250px;
}
.sidebar .header {
  height: 80px;
  /* width: 230px; */
  background-color: #3c3b54;
  /* margin-bottom: 30px; */
  /* position: relative; */
}
.sidebar .header h3 {
  color: #ffffff;
  font-weight: bold;
  text-transform: uppercase;
  padding: 25px 0px 0px 20px;
  letter-spacing: 0.2em;
}


.wrapper .sidebar ul li {
  /* padding-top: 25px; */
  height: 60px;
  position: relative;
}
#router-link {
  width: 250px;
  height: 60px;
}
.wrapper .sidebar ul li a {
  color: #a5a4bf;
  display: block;
}

.wrapper .sidebar ul li .menu {
  padding: 15px 0px 0px 30px;
  display: inline-block;
}

.wrapper .sidebar ul li .icon {
  width: 40px;
  height: 20px;
}

.wrapper .sidebar ul li:hover {
  background-color: #3c3b54;
}

.wrapper .sidebar ul li:hover .li-text {
  color: #ffffff;
}

.wrapper .sidebar ul li:hover .icon {
  color: #a3a0fb;
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
