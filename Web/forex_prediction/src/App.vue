<template>
  <div id="app">
    <div class="columns">
      <div class="column is-2"><side-bar-component /></div>
      <div class="column">
        <nav-bar-component />
        <router-view />
        </div>
    </div>
    
  </div>
</template>

<script>
// import NavBarComponent from './components/NavBarComponent'
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

<style></style>
