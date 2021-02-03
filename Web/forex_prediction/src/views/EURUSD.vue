<template>
  <div id="EURUSD" class="has-background-light">
    <div style="padding: 50px">
      <top-evaluate></top-evaluate>
      <middle-evaluate></middle-evaluate>
      <candle-stick-chart></candle-stick-chart>
    </div>
  </div>
</template>

<script>
import CandleStickChart from '../components/EURUSD/CandleStickChart.vue';
import MiddleEvaluate from "../components/EURUSD/MiddleEvaluate.vue";
import TopEvaluate from "../components/EURUSD/TopEvaluate";

export default {
  name: "EURUSD",
  components: {
    TopEvaluate,
    MiddleEvaluate,
    CandleStickChart,
  },
};
</script>

<style></style>
