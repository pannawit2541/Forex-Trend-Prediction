<template>
  <div id="GBPUSD" class="has-background-light">
    <div style="padding: 25px 25px 0px 50px">
      <p class="title is-4 has-text-grey-dark">GBP/USD</p>
    </div>
    <div style="padding: 25px 50px 50px 50px">
      <top-evaluate
        :MAE="header.MAE"
        :R2_score="header.R2_score"
        :Trend_acc="header.Trend_acc"
        :icon_color="header.icon_color"
        v-if="renderComponent"
      ></top-evaluate>
      <gbpusd-suggest></gbpusd-suggest>
      <candle-stick-chart
        :chart_pred="footer.OHLC_predict"
        :chart_true="footer.OHLC_true"
        :titleTxt="footer.titleTxt"
        v-if="renderComponent"
      ></candle-stick-chart>
    </div>
  </div>
</template>

<script>
import CandleStickChart from "../components/CandleStickChart.vue";
// import MiddleEvaluate from "../components/MiddleEvaluate.vue";
import TopEvaluate from "../components/TopEvaluate";
import { api } from "../api";
import GbpusdSuggest from '../components/Suugestion/GbpusdSuggest.vue';

export default {
  name: "GBPUSD",
   data() {
    return {
      response: null,
      renderComponent: true,
      header: {
        MAE: null,
        R2_score: null,
        Trend_acc: null,
        icon_color: "#A3A0FB"
      },
      middle: {
        trend_info: {
          trend: null,
          slope: null,
          slope_score: null,
          color_bar: null,
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
      },
      footer: {
        titleTxt : "GBPUSD",
        OHLC_predict: null,
        OHLC_true: null,
      },
    };
  },
  components: {
    TopEvaluate,
    // MiddleEvaluate,
    CandleStickChart,
    GbpusdSuggest,
  },
 
  methods: {
    async REST_api() {
      this.response = (await api.get("/GBPUSD/evaluate")).data;
    },
    // --------------------- Header ---------------------
    async Evaluate_score() {
      try {
        this.header.MAE = this.response.MAE;
        this.header.R2_score = this.response.R2_SCORE;
        this.header.Trend_acc = this.response.Slope_acc;
      } catch (error) {
        console.log(error);
      }
    },

    // --------------------- Middle ---------------------
    async Trend_predict() {
      try {
        // const res = (await api.get("/EURUSD/evaluate")).data;
        let data = this.middle.trend_info;
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
      let data = this.middle.suggest_info;
      let trend_info = this.middle.trend_info;
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
        let data = this.middle.sma_chart;

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
    async OHLC_predict() {
      try {
        const historical_predict = this.response.Predict_ohlc;
        const time_historical = this.response.Time_stamp;
        const historical = {
          chart: {
            type: "Candles",
            data: [],
          },
        };
        for (let i in historical_predict) {
          let timeStamp = (time_historical[i] + 60 * 60 * 24) * 1000;
          // console.log(timeStamp)
          let open = historical_predict[i][0];
          let high = historical_predict[i][0];
          let close = historical_predict[i][1];
          let low = historical_predict[i][1];
          historical.chart.data.push([timeStamp, open, high, low, close]);
        }

        this.footer.OHLC_predict = historical;
      } catch (error) {
        console.log(error);
      }
    },
    async OHLC_true() {
      try {
        const res = await (await api.get("/GBPUSD/historical")).data;
        const { response } = res;
        const historical = {
          chart: {
            type: "Candles",
            data: [],
          },
        };
        for (let i in response) {
          let timeStamp = (response[i].t)* 1000;
          let open = parseFloat(response[i].o);
          let high = parseFloat(response[i].h);
          let low = parseFloat(response[i].l);
          let close = parseFloat(response[i].c);
          let volume = parseInt(response[i].v);
          historical.chart.data.push([
            timeStamp,
            open,
            high,
            low,
            close,
            volume,
          ]);
        }

        this.footer.OHLC_true = historical;
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
    await this.REST_api();
    
    await this.Evaluate_score();
    // this.Trend_suggest();
    // await this.Trend_predict();
    // await this.SMA_chart();
    await this.OHLC_predict();
    await this.OHLC_true()
    
    this.forceRerender();
  },
};
</script>

<style></style>
