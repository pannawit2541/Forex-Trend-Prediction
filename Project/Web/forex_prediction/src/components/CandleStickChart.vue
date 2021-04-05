<template>
  <div>
    <div class="tile is-ancestor">
      <div class="tile is-parent">
        <article class="tile is-child box">
          <p class="subtitle is-5 has-text-grey-darker">Predict Graph</p>
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
              :indexBased="this.flag"
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
// import Data from "../../data/data_copy.json"

export default {
  name: "CandleStickChart",
  props:{
    chart_pred : Object,
    chart_true : Object,
    titleTxt: String,
  },
  data() {
    return {
      // chart : Data,
      flag : true,
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
    
  },
  mounted() {
    window.addEventListener("resize", this.onResize);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.onResize);
  },
};
</script>
