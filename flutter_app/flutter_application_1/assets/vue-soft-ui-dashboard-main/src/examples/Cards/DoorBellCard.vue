<template>
      <div class="d-flex directionReverse" >
        <div class="p-1">
          <div
            class="text-center icon "
          >
            <i
              class="text-lg opacity-10"
              :class="typeof icon === 'string' ? icon : icon.component"
              aria-hidden="true"
            ></i>
          </div>
        </div>
        <div :class="classContent">
          <div class="numbers">
            <h5 class="mb-0 font-weight-bolder"  :class="title.color">
              
               {{ typeof title === "string" ? title : title.text }}
            </h5>
            <p
              class="mb-0 text-sm text-capitalize font-weight-bold"
             :class="value.color"
            >
              {{
                typeof value === "string" || typeof value === "number"
                  ? value
                  : value.text
              }}
            </p>
          </div>
        </div>
      </div>
</template>

<script>
export default {
  name: "DoorbellCard",
  props: {
    title: {
      type: [Object, String],
      default: null,
      text: {
        type: String,
      },
      color: {
        type: String,
      },
    },
    value: {
      type: [Object, String],
      required: true,
      text: {
        type: String,
      },
      color: {
        type: String,
      },
    },
   
    icon: {
      type: [String, Object],
      component: {
        type: String,
      },
      background: {
        type: String,
      },
      default: () => ({
        background: "bg-white",
      }),
    },
    classContent: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      reverseDirection: "flex-row-reverse justify-content-between",
    };
  },
};
</script>
