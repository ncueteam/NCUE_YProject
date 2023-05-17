<template>
  <div class="hello">
    
    <div class="box">
      <round-slider 
    v-bind:change="chgHandler" 
    v-on:input="pInput" 
    v-model="sliderValue"
     min=16 
     max=32 
     step=1
     start-angle=330 
     end-angle=210 
     ></round-slider>
    </div>
    <!-- <input v-model="sliderValue" /> -->
  </div>
</template>

<script>
 import { RoundSlider } from "vue-round-slider/src/index2.js"

export default {
  name: 'CircleSlider',
  components: {
    RoundSlider,
  },
  computed: {
    version() {
      return RoundSlider.version;
    }
  },
  props: {
    msg: String
  },
  data() {
    return {
      sliderValue: 60
    };
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #213576;
}
.box {
  padding: 10px;
  display: inline-block;
}
</style>
