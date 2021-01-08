<template>
  <div>
    <div class="sideStyle">
      <div class="title is-4 has-text-white-ter">Forex Prediction</div>
    </div>
    <div class="menuSideStyle">
      <div>
        <a class="has-text-light subtitle is-5" href="/">Dashboard</a>
      </div>
    </div>
    <div class="menuSideStyle">
      <div>
        <a class="has-text-light subtitle is-5" href="/EURUSD">EUR/USD</a>
      </div>
    </div>
    <div class="menuSideStyle">
      <div>
         <a class="has-text-light subtitle is-5" href="/GBPUSD">GBP/USD</a>
      </div>
    </div>
    <div class="menuSideStyle">
      <div>
        <a class="has-text-light subtitle is-5" href="/USDJPY">USD/JPY</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SideBarComponent",
};
</script>

<style scoped>
.sideStyle {
  background: #3c3b54;
  padding-left: 50px;
  padding-top: 25px;
  padding-bottom: 25px;
}
.menuSideStyle {
  background-color: #43425d;
  padding-left: 50px;
  padding-top: 20px;
  padding-bottom: 0px;
}
</style>
