<template>
  <div id="EURUSD" class="has-background-light">
    <div class="container is-fluid">
      <p class="title is-3 has-text-grey-dark" style="padding-top: 20px">
        EUR/USD
      </p>
      <div class="tile is-ancestor">
        <div class="tile is-12 is-vertical">
          <div class="tile">
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title is-5 has-text-grey-light">MAE</p>
                <div>
                  <p class="title is-3">{{ eval.mae }} pips</p>
                  <fa-icon
                    :icon="['fas', 'coins']"
                    style="color: Tomato"
                    size="3x"
                  >
                  </fa-icon>
                </div>
                <div class="content">
                  <span>
                    <fa-icon
                      :icon="['fas', 'arrow-up']"
                      style="color: Tomato"
                    ></fa-icon>
                  </span>
                  <span class="title is-5" style="color: Tomato"> 2 pips </span>
                </div>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title is-5 has-text-grey-light">R2 Score</p>
                <div>
                  <p class="title is-3">{{ eval.r2 }} %</p>
                </div>
                <div>
                  <span>
                    <fa-icon
                      :icon="['fas', 'arrow-up']"
                      style="color: YellowGreen"
                    ></fa-icon>
                  </span>
                  <span class="title is-5" style="color: YellowGreen">
                    2.5%
                  </span>

                  <p class="title is-3" style="color: SlateBlue">
                    <var>R<sup>2</sup></var>
                  </p>
                </div>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title is-5 has-text-grey-light">Trend Accuracy</p>
                <div>
                  <p class="title is-3">{{ eval.trendAcc }} %</p>
                  <fa-icon
                    :icon="['fas', 'chart-bar']"
                    style="color: #55d8fb"
                    size="3x"
                  >
                  </fa-icon>
                </div>
                <div class="content">
                  <span>
                    <fa-icon
                      :icon="['fas', 'arrow-up']"
                      style="color: YellowGreen"
                    ></fa-icon>
                  </span>
                  <span class="title is-5" style="color: YellowGreen">
                    120%
                  </span>
                </div>
              </article>
            </div>
          </div>
        </div>
      </div>
      <div class="tile is-ancestor">
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="title is-5 has-text-grey-darker">Moving Average</p>
            <div class="content">
              <LineChart />
            </div>
          </article>
        </div>
        <div class="tile is-parent is-4">
          <article class="tile is-child box">
            <p class="title is-5 has-text-grey-darker">Trend Infomation</p>
            <div class="content" style="padding-left: 20px">
              <!-- <DoughnutChart /> -->
              <span>
                <p class="title is-3 has-text-grey-dark">{{ eval.trend }}</p>
                <p class="title is-5 has-text-grey-light">Trend Accuracy</p>
              </span>
            </div>
            <p class="title is-5 has-text-grey-darker">Trend Accuracy</p>
            <div class="content">
              <BarChart />
            </div>
          </article>
        </div>
      </div>
      <div class="tile is-ancestor">
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="title is-5 has-text-grey-darker">Predict Graph</p>
            <div class="content pl-5">
              <trading-vue
                :data="chart_pred"
                :width="0.75 * this.width"
                :height="0.5 * this.height"
                :color-back="colors.colorBack"
                :color-grid="colors.colorGrid"
                :color-text="colors.colorText"
                :colorCandleUp="colors.colorCandleUp"
                :colorCadleDown="colors.colorCadleDown"
                :titleTxt="this.titleTxt"
                :showVolume="this.show"
              >
              </trading-vue>
            </div>
          </article>
        </div>
      </div>
      <div class="tile is-ancestor">
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="title is-5 has-text-grey-darker">True Graph</p>
            <div class="content pl-5">
              <trading-vue
                :data="chart"
                :width="0.75 * this.width"
                :height="0.5 * this.height"
                :color-back="colors.colorBack"
                :color-grid="colors.colorGrid"
                :color-text="colors.colorText"
                :colorCandleUp="colors.colorCandleUp"
                :colorCadleDown="colors.colorCadleDown"
                :titleTxt="this.titleTxt"
                :showVolume="this.show"
              >
              </trading-vue>
            </div>
          </article>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BarChart from "../components/EURUSD/BarChart";
import LineChart from "../components/EURUSD/LineChart";

import TradingVue from "trading-vue-js";
// import Data from "../../data/data.json";
import { api } from "../api";

export default {
  name: "EURUSD",
  components: {
    TradingVue,
    BarChart,
    LineChart,
  },
  methods: {
    onResize() {
      this.width = window.innerWidth;
      this.height = window.innerHeight;
    },
    async historical_data() {
      try {
        const res = await (await api.get("/EURUSD/historical")).data;
        const { response } = res;
        const historical = {
          chart: {
            type: "Candles",
            data: [],
          },
        };

        for (let i in response) {
          // // let timeStamp = new Date(response[i].date).getTime()
          let timeStamp = parseInt(response[i].t);
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

        this.chart = historical;
      } catch (error) {
        console.log(error);
      }
    },
    async predict_data() {
      try {
        const res = (await api.get("/EURUSD/evaluate")).data;
        const historical_predict = res.Predict_ohlc;
        // console.log(historical_predict)
        const time_historical = res.Time_stamp;
        const historical = {
          chart: {
            type: "Candles",
            data: [],
          },
        };

        for (let i in historical_predict) {
          let timeStamp = time_historical[i];
          let open = historical_predict[i][0];
          let high = historical_predict[i][0];
          let close = historical_predict[i][1];
          let low = historical_predict[i][1];
          historical.chart.data.push([timeStamp, open, high, low, close]);
        }

        this.chart_pred = historical;
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    window.addEventListener("resize", this.onResize);
    // this.historical_data();
    this.predict_data();
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResize);
  },
  data() {
    return {
      titleTxt: "EUR/USD",
      chart: {},
      chart_pred: {},
      width: window.innerWidth,
      height: window.innerHeight,
      show: false,
      colors: {
        colorBack: "#fff",
        colorGrid: "#fff",
        colorText: "#333",
        colorCandleUp: "#63dbff",
        colorCadleDown: "#ffa8c4",
      },
      eval: {
        mae: 54,
        r2: 69,
        trendAcc: 200,
        trend: "Uptrend",
      },
    };
  },
};
</script>

<style></style>
