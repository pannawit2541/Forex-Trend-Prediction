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
              <p class="title is-4 has-text-grey-darker mt-5">
                {{ trend_info.trend }}
              </p>
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
import LineChart from "../LineChart.vue";
import DoughnutChart from "../DoughnutChart.vue";
import { api } from "../../api";

export default {
  name: "MiddleEvaluate",
  data() {
    return {
      trend_info: {
        trend: "",
        slope: 0,
        slope_score: 0,
        color_bar: "",
      },
      suggest_info: {
        title: "",
        message: "",
        title_color: "",
        highlight_word: "",
      },
      sma_chart: {
        date: [],
        sma_predict: [],
        sma_true: [],
      },
      response: null,
      renderComponent: true,
    };
  },
  components: {
    LineChart,
    DoughnutChart,
  },
  
  methods: {
    async REST_api() {
      this.response = (await api.get("/USDJPY/evaluate")).data;
    },
    // --------------------- Middle ---------------------
    async Trend_predict() {
      try {
        // const res = (await api.get("/EURUSD/evaluate")).data;
        let data = this.trend_info;
        const len = this.response.Slope_values.length - 1;
        const slope = Number(this.response.Slope_values[len]).toFixed(3);
        data.slope = slope;

        if (slope > 0) {
          data.trend = "Uptrend";
          data.color_bar = "#63dbff";
        } else {
          data.trend = "Downtrend";
          data.color_bar = "#FFA7C4";
        }
        data.percent = Math.round(
          (Math.pow(slope, 2) / (0.4 + Math.pow(slope, 2))) * 100
        );

      } catch (error) {
        console.log(error);
      }
    },
    Trend_suggest() {
      let data = this.suggest_info;
      let trend_info = this.trend_info;
      if (trend_info.percent <= 60) {
        data.title = "Sideway";
        data.message =
          " Because the slope is " +
          trend_info.slope +
          " and the slope score is " +
          trend_info.percent +
          "%, which is not very high.";
        data.title_color = "#4a4a4a";
        data.highlight_word = "Please be careful.";
      } else {
        if (trend_info.trend == "Uptrend") {
          data.title = "Uptrend";
          data.title_color = "#63dbff";
          data.highlight_word = "You should buy it now.";
        } else {
          data.title = "Downtrend";
          data.title_color = "#FFA7C4";
          data.highlight_word = "You should sell it now.";
        }
        data.message =
          " because the slope is " +
          trend_info.slope +
          " and the slope score is " +
          trend_info.percent +
          "%, which very high.";
      }
    },
    async SMA_chart() {
      try {
        let data = this.sma_chart;

        const len_date = this.response.Time_stamp.length - 1;
        const len_pre = this.response.SMA_predict.length - 1;
        const len_true = this.response.SMA_true.length - 1;

        const sma_predict = this.response.SMA_predict;
        const sma_true = this.response.SMA_true;
        const date = this.response.Time_stamp;

        var months = [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec",
        ];

        for (let i = 5; i >= 0; i--) {
          data.sma_predict.push(sma_predict[len_pre - 24 * i]);
          let date_str = new Date(
            (date[len_date - 24 * i] + 60 * 60 * 24) * 1000
          );
          let month = months[date_str.getMonth()];
          data.date.push(
            date_str.getDate() +
              " " +
              month +
              " " +
              (date_str.getFullYear() - 2000)
          );

          if (i == 0) {
            data.sma_true.push(null);
          } else {
            data.sma_true.push(sma_true[len_true - 24 * i]);
          }
        }
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
  },
  async mounted() {
    // console.log(this.sma_chart.date)
    await this.REST_api();
    await this.Trend_predict();
    console.log("slope is : ",this.trend_info.slope)
    await this.SMA_chart();
    this.Trend_suggest();
    this.forceRerender();
  },
};
</script>
