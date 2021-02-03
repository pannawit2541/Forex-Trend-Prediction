<template>
  <div>
    <div class="tile is-ancestor">
      <div class="tile is-parent">
        <article class="tile is-child box">
          <p class="subtitle is-5 has-text-grey-darker">Predict Graph</p>
          <hr>
          <div class="content pl-5">
            <trading-vue
              :data="this.chart_pred"
              :width="this.width * 0.7"
              :height="this.height * 0.5"
              :color-back="colors.colorBack"
              :color-grid="colors.colorGrid"
              :color-text="colors.colorText"
              :colorCandleUp="colors.colorCandleUp"
              :colorCadleDown="colors.colorCadleDown"
              :titleTxt="this.titleTxt"
              :showVolume="this.show"
              :colorTitle="colors.colorCandleUp"
            >
            </trading-vue>
          </div>
        </article>
      </div>
    </div>
    <div class="tile is-ancestor">
      <div class="tile is-parent">
        <article class="tile is-child box">
          <p class="subtitle is-5 has-text-grey-darker">Realtime Graph</p>
          <hr>
          <div class="content pl-5">
            <trading-vue
              :data="this.chart_true"
              :width="this.width * 0.7"
              :height="this.height * 0.5"
              :color-back="colors.colorBack"
              :color-grid="colors.colorGrid"
              :color-text="colors.colorText"
              :colorCandleUp="colors.colorCandleUp"
              :colorCadleDown="colors.colorCandleDown"
              :titleTxt="this.titleTxt"
              :showVolume="this.show"
              :colorTitle="colors.colorCandleDown"
            >
            </trading-vue>
          </div>
        </article>
      </div>
    </div>
  </div>
</template>

<script>
import TradingVue from "trading-vue-js";
import { api } from "../../api";
export default {
  name: "CandleStickChart",
  data() {
    return {
      titleTxt: "EUR/USD",
      chart_pred: {},
      chart_true: {},
      width: window.innerWidth,
      height: window.innerHeight,
      show: false,
      colors: {
        colorBack: "#fff",
        colorGrid: "#fff",
        colorText: "#333",
        colorCandleUp: "#63dbff",
        colorCandleDown: "#ffa8c4",
      },
    };
  },
  components: {
    TradingVue,
  },
  methods: {
    onResize() {
      this.width = window.innerWidth;
      this.height = window.innerHeight;
    },
    async predict_data() {
      try {
        const res = (await api.get("/EURUSD/evaluate")).data;
        const historical_predict = res.Predict_ohlc;
        const time_historical = res.Time_stamp;
        const historical = {
          chart: {
            type: "Candles",
            data: [],
          },
        };
        for (let i in historical_predict) {
          let timeStamp = ((time_historical[i] + 60*60*24)* 1000);
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
          let timeStamp = parseInt(response[i].t) * 1000;
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

        this.chart_true = historical;
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    window.addEventListener("resize", this.onResize);
    this.historical_data();
    this.predict_data();
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResize);
  },
};
</script>
