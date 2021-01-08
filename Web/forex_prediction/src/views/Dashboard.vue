<template>
  <div id="Dashboard" class="has-background-light">
    <div class="container is-fluid">
      <p class="title is-3 has-text-grey-dark">Overview</p>
      <div class="tile is-ancestor">
        <div class="tile">
          <div class="tile is-parent">
            <article class="tile is-child box">
              <p class="subtitle has-text-grey-light">EUR/USD</p>
               <div class="content">
            </div>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child box">
              <p class="subtitle has-text-grey-light">GBP/USD</p>
               <div class="content">
            </div>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child box">
              <p class="subtitle has-text-grey-light">USD/JPY</p>
               <div class="content">
            </div>
            </article>
          </div>
        </div>
      </div>
      <div class="tile is-ancestor">
        <div class="tile">
          <div class="tile is-parent">
            <article class="tile is-child box">
              <p class="subtitle has-text-grey-darker">Statistics</p>
              <div class="content"></div>
            </article>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: "Dashboard",
};
</script>

<style></style>
