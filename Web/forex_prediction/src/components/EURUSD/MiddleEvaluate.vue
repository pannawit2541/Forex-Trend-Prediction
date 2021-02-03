<template>
  <div class="tile is-ancestor">
    <div class="tile is-parent">
      <article class="tile is-child box">
        <p class="subtitle is-5 has-text-grey-darker">Moving Average</p>
        <hr />
        <div class="content">
          <line-chart></line-chart>
        </div>
      </article>
    </div>
    <div class="tile is-parent is-4">
      <article class="tile is-child box">
        <p class="subtitle is-5 has-text-grey-darker">Trend Infomation</p>
        <hr />
        <div class="columns">
          <div class="column is-half has-text-centered">
            <span>
              <p class="title is-4 has-text-grey-darker mt-5">Downtrend</p>
            </span>
            <span>
              <p>18 of total 24</p>
            </span>
          </div>
          <div class="column">
            <doughnut-chart></doughnut-chart>
          </div>
        </div>
        <div class="content has-text-centered"></div>
        <p class="title is-5 has-text-grey-darker">Trend Accuracy</p>
        <div class="content"></div>
      </article>
    </div>
  </div>
</template>

<script>
import LineChart from "./LineChart.vue";
import DoughnutChart from "./DoughnutChart.vue";

export default {
  data() {
    return {};
  },
  components: {
    LineChart,
    DoughnutChart,
  },
  name: "MiddleEvaluate",
};
</script>

<style scoped></style>
