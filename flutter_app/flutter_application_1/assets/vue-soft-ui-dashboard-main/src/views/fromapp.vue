<template>
  <div>
    获取到的Flutter传入信息： <span>{{ infoFromFlutter }}</span>
  </div>
</template>
<style scoped>
</style>

<script>
export default{
  name: "flutter",
  data: function () {
    return {
      infoFromFlutter: "",
    };
  },
  mounted: function () {
    //将getInfoFromFlutter（）方法挂载到window以供给Flutter调用
    window["getInfoFromFlutter"] = (info) => {
      this.getInfoFromFlutter(info);
    };
    window["getInfoFromVue"].postMessage("Hello,Flutter");
  },
  methods: {
    getInfoFromFlutter(info) {
      this.infoFromFlutter = info;
    },
  },
};
</script>