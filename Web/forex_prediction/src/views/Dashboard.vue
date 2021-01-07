<template>
  <div id="Dashboard">
    <div class="tile is-ancestor">
      <div class="tile is-12 is-vertical">
        <div class="tile">
          <div class="tile is-parent">
            <article class="tile is-child notification is-primary">
              <p class="title">Vertical...</p>
              <p class="subtitle">Top tile</p>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child notification is-info">
              <p class="title">Middle tile</p>
              <p class="subtitle">With an image</p>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child notification is-danger">
              <p class="title">Middle tile</p>
              <p class="subtitle">With an image</p>
            </article>
          </div>
        </div>
        <div class="title">
          <article class="tile is-child notification is-success">
      <div class="content">
        <p class="title">Tall tile</p>
        <p class="subtitle">With even more content</p>
      </div>
    </article>
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
