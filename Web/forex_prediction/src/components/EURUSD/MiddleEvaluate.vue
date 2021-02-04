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
              <p class="title is-4 has-text-grey-darker mt-5">{{ trend }}</p>
            </span>
            <span>
              <p>The slope is {{ slope }}</p>
            </span>
          </div>
          <div class="column">
            <doughnut-chart
              :series_percent="[percent]"
              :fill_color="color_bar"
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
              :style="{ 'background-color': identification.title_color }"
            >
              <p>{{ identification.title }}</p>
            </div>
            <div class="message-body">
              <p>
                <strong>{{ identification.highlight_word }}</strong>
                {{ identification.message }}
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
import { api } from "../../api";

export default {
  data() {
    return {
      trend: "",
      slope: 0,
      percent: null,
      color_bar: "",
      renderComponent: true,
      identification: {
        title: "",
        message: "",
        title_color: "",
        highlight_word: "",
      },
    };
  },
  components: {
    LineChart,
    DoughnutChart,
  },
  name: "MiddleEvaluate",
  methods: {
    async trend_evaluate() {
      try {
        const res = (await api.get("/EURUSD/evaluate")).data;
        const len = res.Slope_values.length - 1;
        this.slope = Number(res.Slope_values[len]).toFixed(3);
        console.log(res.Slope_values)
        if (this.slope > 0) {
          this.trend = "Uptrend";
          this.color_bar = "#63dbff";
        } else {
          this.trend = "Downtrend";
          this.color_bar = "#FFA7C4";
        }
        this.percent = Math.round(
          (Math.pow(this.slope, 2) / (0.4 + Math.pow(this.slope, 2))) * 100
        );
      } catch (error) {
        console.log(error);
      }
    },
    forceRerender() {
      // Remove my-component from the DOM
      this.renderComponent = false;

      this.$nextTick(() => {
        // Add the component back in
        this.renderComponent = true;
      });
    },
    identify_trend() {
      if (this.percent <= 70) {
        this.identification.title = "Sideway";
        this.identification.message = " Because the slope is " +
          this.slope +
          " and the slope score is " +
          this.percent +
          "%, which is not very high.";
          " because the slope is " +
          this.slope +
          " and the slope score is " +
          this.percent +
          "%, which is not very high.";
        this.identification.title_color = "#4a4a4a";
        this.identification.highlight_word = "Please be careful.";
      } else {
        if (this.trend == "Uptrend") {
          this.identification.title = "Uptrend";
          this.identification.title_color = "#63dbff";
          this.identification.highlight_word = "You should buy it now.";
        }else{
          this.identification.title = "Downtrend";
          this.identification.title_color = "#FFA7C4";
          this.identification.highlight_word = "You should sell it now.";
        }
        this.identification.message =
          " because the slope is " +
          this.slope +
          " and the slope score is " +
          this.percent +
          "%, which very high.";
      }
    },
  },
  async mounted() {
    await this.trend_evaluate();
    this.identify_trend();
    this.forceRerender();
  },
};
</script>

<style scoped></style>
