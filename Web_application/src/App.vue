<template>
  <div id="app">
    <section class="hero is-medium is-info is-bold">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            FOREX MARKET PREDICTION
          </h1>
          <h2 class="subtitle is-4">
            24 hours in advance
          </h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container is-max-widescreen ">
            <router-view />
        
        <router-link to="/">EUR/USD</router-link>
        <router-link to="/USDJPY">USD/JPY</router-link>
        <router-link to="/GBPUSD">GBP/USD</router-link>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "app",
};
</script>

<style></style>
