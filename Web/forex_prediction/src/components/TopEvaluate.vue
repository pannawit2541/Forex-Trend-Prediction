<template>
  <div class="tile is-ancestor">
    <div class="tile is-12 is-vertical">
      <div class="tile">
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="subtitle is-5 has-text-grey-light">MAE</p>
            <div class="columns">
              <div class="column is-two-thirds">
                <div> <p class="title is-4">{{MAE}} pips</p> </div>
                <div style="padding-top : 5px">
                  <span class="title is-6" style="color: Tomato"> 2 pips </span>
                  <span>
                    <fa-icon
                      :icon="['fas', 'arrow-up']"
                      style="color: #FF6565"
                    ></fa-icon>
                  </span>
                </div>
              </div>
              <div class="column">
                <span>
                  <fa-icon
                    :icon="['fas', 'coins']"
                    style="color: Tomato"
                    size="3x"
                  >
                  </fa-icon>
                </span>
              </div>
            </div>
          </article>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="subtitle is-5 has-text-grey-light">R2 Score</p>
            <div class="columns">
              <div class="column is-two-thirds">
                <div>
                  <p class="title is-4 ">{{R2_score}} %</p>
                </div>
                <div style="padding-top : 5px">
                  <span class="title is-6" style="color: YellowGreen">
                    2 %
                  </span>
                  <span>
                    <fa-icon
                      :icon="['fas', 'arrow-up']"
                      style="color: YellowGreen"
                    ></fa-icon>
                  </span>
                </div>
              </div>
              <div class="column">
                <span>
                  <p class="title is-3 has-text-weight-bold " style="color: #8162E1">
                    <var>R<sup> 2</sup></var>
                  </p>
                </span>
              </div>
            </div>
          </article>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="subtitle is-5 has-text-grey-light">Trend Accuracy</p>
            <div class="columns">
              <div class="column is-two-thirds">
                <div><p class="title is-4">{{Trend_acc}} %</p></div>
                <div style="padding-top : 5px">
                  <span class="title is-6" style="color: YellowGreen">
                    5 %
                  </span>
                  <span>
                    <fa-icon
                      :icon="['fas', 'arrow-up']"
                      style="color: YellowGreen"
                    ></fa-icon>
                  </span>
                </div>
              </div>
              <div class="column">
                <span>
                  <fa-icon
                    :icon="['fas', 'chart-bar']"
                    :style="{'color': icon_color}"
                    size="3x"
                  >
                  </fa-icon>
                </span>
              </div>
            </div>
          </article>
        </div>
      </div>
    </div>
  </div>
</template>

<script>



export default {
  name: "TopEvaluate",
  props:{
    MAE : Number,
    R2_score : Number,
    Trend_acc : Number,
    icon_color : String
  },
};
</script>

<style>

</style>
