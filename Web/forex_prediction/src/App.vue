<template>
  <div id="app">
    <div class="columns is-gapless is-mobile">
      <div class="column is-2" ><side-bar-component /></div>
      <div class="column">
        <nav-bar-component />
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import NavBarComponent from "./components/NavBarComponent.vue";
import SideBarComponent from "./components/SideBarComponent.vue";

export default {
  name: "app",
  components: {
    NavBarComponent,
    SideBarComponent,
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro');

#app{
  font-family: 'Source Sans Pro';
}
</style>
