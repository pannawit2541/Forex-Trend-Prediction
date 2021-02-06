<template>
  <div class="tile is-ancestor">
    <div class="tile is-parent">
      <article class="tile is-child box">
        <p class="subtitle is-5 has-text-grey-darker">Moving Average</p>
        <hr />
        <div class="content">
          <line-chart
          :date="sma_chart.date"
          :sma_predict="sma_chart.sma_predict"
          :sma_true="sma_chart.sma_true"
          v-if="renderComponent"
          ></line-chart>
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
              <p class="title is-4 has-text-grey-darker mt-5">{{ trend_info.trend }}</p>
            </span>
            <span>
              <p>The slope is {{ trend_info.slope }}</p>
            </span>
          </div>
          <div class="column">
            <doughnut-chart
              :series_percent="[trend_info.percent]"
              :fill_color="trend_info.color_bar"
              v-if="renderComponent"
            ></doughnut-chart>
          </div>
        </div>
        
        <div class="content has-text-centered"></div>
        <p class="subtitle is-5 has-text-grey-darker">Suggestion</p>
        <hr />
        <div class="content">
          <article class="message">
            <div
              class="message-header"
              :style="{ 'background-color': suggest_info.title_color }"
            >
              <p>{{ suggest_info.title }}</p>
            </div>
            <div class="message-body">
              <p>
                <strong>{{ suggest_info.highlight_word }}</strong>
                {{ suggest_info.message }}
              </p>
            </div>
          </article>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
import LineChart from "./LineChart.vue";
import DoughnutChart from "./DoughnutChart.vue";
// import { api } from "../../api";

export default {
  props: {
    trend_info: {
      trend: String,
      slope: Number,
      slope_score: Number,
      color_bar: Number,
    },
    suggest_info: {
      title: String,
      message: String,
      title_color: String,
      highlight_word: String,
    },
    sma_chart:{
      date : Array,
      sma_predict : Array,
      sma_true : Array
    }
  },
  data() {
    return {
      renderComponent: true,
    };
  },
  components: {
    LineChart,
    DoughnutChart,
  },
  name: "MiddleEvaluate",
  methods: {
    forceRerender() {
      // Remove my-component from the DOM
      this.renderComponent = false;

      this.$nextTick(() => {
        // Add the component back in
        this.renderComponent = true;
      });
    },
  },
  async mounted() {
    // console.log(this.sma_chart.date)
    this.forceRerender();
  },
};
</script>

