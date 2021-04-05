<template>
  <div id="Dashboard" class="has-background-light">
    <div style="padding: 25px 25px 0px 50px">
      <p class="title is-3 has-text-grey-dark">Overview</p>
    </div>
    <div style="padding: 25px 50px 50px 50px">
      <div class="tile is-ancestor">
        <div class="tile is-parent">
          <article class="tile is-child box" style=" background-image: linear-gradient(to right, #55D8FE,transparent);">
            <p class="subtitle is-5 has-text-white-bis">EUR/USD</p>
          </article>
        </div>
      </div>
      <eurusd-suggest></eurusd-suggest>
      <div class="tile is-ancestor">
        <div class="tile is-parent">
          <article class="tile is-child box" style=" background-image: linear-gradient(to right, #A3A0FB,transparent);">
            <p class="subtitle is-5 has-text-white-bis">GBP/USD</p>
          </article>
        </div>
      </div>
      <gbpusd-suggest></gbpusd-suggest>
      <div class="tile is-ancestor">
        <div class="tile is-parent">
          <article class="tile is-child box" style=" background-image: linear-gradient(to right, #FFA7C4,transparent);">
            <p class="subtitle is-5 has-text-white-bis">USD/JPY</p>
          </article>
        </div>
      </div>
      <usdjpy-suggest></usdjpy-suggest>
    </div>
  </div>
</template>

<script>
import EurusdSuggest from "../components/Suugestion/EurusdSuggest.vue";
import GbpusdSuggest from "../components/Suugestion/GbpusdSuggest.vue";
import UsdjpySuggest from "../components/Suugestion/UsdjpySuggest.vue";

export default {
  name: "Dashboard",
  components: {
    EurusdSuggest,
    GbpusdSuggest,
    UsdjpySuggest,
  },
  data() {
    return {};
  },
};
</script>

<style></style>
