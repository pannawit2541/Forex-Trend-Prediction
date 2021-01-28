<template>
  <div id="EURUSD" class="has-background-light">
    <div class="container is-fluid">
      <p class="title is-3 has-text-grey-dark">EUR/USD</p>
      <div class="tile is-ancestor">
        <div class="tile is-12 is-vertical">
          <div class="tile">
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="title is-5  has-text-grey-light">MAE</p>
                <div>
                  <p class="title is-3">{{ eval.mae }} pips</p>
                  <fa-icon
                    :icon="['fas', 'coins']"
                    style="color:Tomato"
                    size="3x"
                  >
                  </fa-icon>
                </div>
                <div class="content">
                  <span>
                    <fa-icon
                      :icon="['fas', 'arrow-up']"
                      style="color:Tomato"
                    ></fa-icon>
                  </span>
                  <span class="title is-5" style="color:Tomato">
                    2 pips
                  </span>
                </div>
              </article>
            </div>
            <div class="tile is-parent ">
              <article class="tile is-child box ">
                <p class="title is-5  has-text-grey-light">R2 Score</p>
                <div>
                  <p class="title is-3">{{ eval.r2 }} %</p>
                </div>
                <div>
                  <span>
                    <fa-icon
                      :icon="['fas', 'arrow-up']"
                      style="color:YellowGreen"
                    ></fa-icon>
                  </span>
                  <span class="title is-5" style="color:YellowGreen">
                    2.5%
                  </span>

                  <p class="title is-3" style="color:SlateBlue">
                    <var>R<sup>2</sup></var>
                  </p>
                </div>
              </article>
            </div>
            <div class="tile is-parent ">
              <article class="tile is-child box">
                <p class="title is-5  has-text-grey-light">Trend Accuracy</p>
                <div>
                  <p class="title is-3  ">{{ eval.trendAcc }} %</p>
                  <fa-icon
                    :icon="['fas', 'chart-bar']"
                    style="color:#55D8FB"
                    size="3x"
                  >
                  </fa-icon>
                </div>
                <div class="content ">
                  <span>
                    <fa-icon
                      :icon="['fas', 'arrow-up']"
                      style="color:YellowGreen"
                    ></fa-icon>
                  </span>
                  <span class="title is-5" style="color:YellowGreen">
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
            <p class="title is-5  has-text-grey-darker">Moving Average</p>
            <div class="content">
              <LineChart />
            </div>
          </article>
        </div>
        <div class="tile is-parent is-4">
          <article class="tile is-child box">
            <p class="title is-5  has-text-grey-darker">Trend Infomation</p>
            <div class="content"></div>
            <p class="title is-5  has-text-grey-darker">Trend Accuracy</p>
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
            <div class="content pl-5 ">
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
      <div class="tile is-ancestor">
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="title is-5 has-text-grey-darker">True Graph</p>
            <div class="content pl-5 ">
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
import Data from "../../data/data.json";
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
  },
  mounted() {
    window.addEventListener("resize", this.onResize);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResize);
  },
  data() {
    return {
      titleTxt: "EUR/USD",
      chart: Data,
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
      },
    };
  },
};
</script>

<style></style>
