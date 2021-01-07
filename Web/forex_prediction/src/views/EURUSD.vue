<template>
  <div id="EURUSD" class="has-background-light">
    <div class="container is-fluid">
      <p class="title is-3 has-text-grey-dark">EUR/USD</p>
      <div class="tile is-ancestor">
        <div class="tile is-12 is-vertical">
          <div class="tile">
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="subtitle has-text-grey-light">MAE</p>
                <div class="content"></div>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="subtitle has-text-grey-light">R2 Score</p>
                <div class="content"></div>
              </article>
            </div>
            <div class="tile is-parent">
              <article class="tile is-child box">
                <p class="subtitle has-text-grey-light">Trend Accuracy</p>
                <div class="content"></div>
              </article>
            </div>
          </div>
        </div>
      </div>
      <div class="tile is-ancestor">
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="subtitle has-text-grey-darker">Moving Average</p>
            <div class="content">
              <p></p>
            </div>
          </article>
        </div>
        <div class="tile is-parent is-4">
          <article class="tile is-child box">
            <p class="subtitle has-text-grey-darker">Trend Infomation</p>
            <div class="content">
              
            </div>
            <p class="subtitle has-text-grey-darker">Trend Accuracy</p>
            <div class="content">
              
            </div>
          </article>
        </div>
      </div>
      <div class="tile is-ancestor">
        <div class="tile is-parent">
          <article class="tile is-child box">
            <p class="subtitle has-text-grey-darker">Predict Graph</p>
            <div class="content">
              <p>
               
              </p>
            </div>
          </article>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EURUSD",
};
</script>

<style></style>
