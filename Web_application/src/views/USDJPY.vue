<template>
  <div id="USDJPY">
    <li>USD/JPY</li>
    <li>H1</li>
    <li>1.22 3.22 4.22 6.22</li>
    <trading-vue
      :data="chart"
      :width="0.7*this.width"
      :height="0.8*this.height"
      :color-back="colors.colorBack"
      :color-grid="colors.colorGrid" 
      :color-text="colors.colorText"
      :colorCandleUp="colors.colorCandleUp"
      :colorCadleDown="colors.colorCadleDown"
      :titleTxt="this.titleTxt"
    >
    </trading-vue>
  </div>
</template>

<script>
import TradingVue from "trading-vue-js";
// import Data from '../../data/data.json'
import { api } from "../api";

export default {
  name: "USDJPY",
  components: { TradingVue },
  methods: {
    onResize() {
      this.width = window.innerWidth;
      this.height = window.innerHeight;
    },
    async historical_data() {
      try {
        const res = await (await api.get("/USDJPY/historical")).data;
        const {quotes} = res
        const historical = {
          chart : {
            type : "Candles",
            data : []
          }
        }
        console.log(res);

        for(let i=0;i<quotes.length;i++){
            let timeStamp = new Date(quotes[i].date).getTime()
            let open = parseFloat(quotes[i].open)
            let high = parseFloat(quotes[i].high)
            let low = parseFloat(quotes[i].low)
            let close = parseFloat(quotes[i].close)
            // let volume = parseInt(quotes[i].v)
            historical.chart.data.push([
              timeStamp,open,high,low,close
            ])
        }
        console.log(historical)
        this.chart = historical

      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.historical_data();
  },
  mounted() {
    window.addEventListener("resize", this.onResize);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResize);
  },
  data() {
    return {
      titleTxt:"USD/JPY",
      chart: {},
      width: window.innerWidth,
      height: window.innerHeight,
      colors: {
        colorBack: "#fff",
        colorGrid: "#eee",
        colorText: "#333",
        colorCandleUp: "#337e92",
        colorCadleDown: "#fc6d78"
      },
    };
  },
};
</script>

<style></style>>
