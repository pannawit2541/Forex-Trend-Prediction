<template>
  <div id="app">
    <b-container class="text-light text-center">
      <div>
        <h1>Forex Prediction</h1>
      </div>
      <b-card title="Card Title" no-body>
        <b-card-header card-header header-tag="nav">
          <div>
            <b-nav tabs align="center">
              <b-nav-item active><router-link to="/">EUR/USD</router-link></b-nav-item>
              <b-nav-item><router-link to="/USDJPY">USD/JPY</router-link></b-nav-item>
              <b-nav-item><router-link to="/GBPUSD">GBP/USD</router-link></b-nav-item>
            </b-nav>
          </div>
        </b-card-header>
        <b-card-body class="text-center">
          <b-card-text>
            <router-view />
          </b-card-text>
        </b-card-body>
      </b-card>
    </b-container>
  </div>
</template>

<script>
export default {
  name: "app",
};
</script>

<style></style>
