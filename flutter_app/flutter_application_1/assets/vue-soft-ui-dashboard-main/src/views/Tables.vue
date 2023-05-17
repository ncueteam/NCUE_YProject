<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-12">
        <authors-table />
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <projects-table />
      </div>
    </div>
    <div class="row">
      <div class="col-12"></div>
      <div class="pagescenter">
        <soft-pagination color="success">
          <soft-pagination-item prev />
          <soft-pagination-item label="1" active />
          <soft-pagination-item label="2" disabled />
          <soft-pagination-item label="3" />
          <soft-pagination-item next />
        </soft-pagination>
      </div>
    </div>
    <!-- <dialog-card> </dialog-card> -->
  </div>
</template>
<style>
.pagescenter {
  text-align: center;
}
</style>
<script>
import AuthorsTable from "./components/AuthorsTable";
// import DialogCard from "./components/DialogCard";
import ProjectsTable from "./components/ProjectsTable";
import SoftPagination from "@/components/SoftPagination.vue";
import SoftPaginationItem from "@/components/SoftPaginationItem.vue";

// import { useModal } from "jenesius-vue-modal";
// import WidgeTestModal from "WidgeTestModal.vue";

// const { openModal } = useModal();

// openModal(DialogCard, {
//   title: "Hello World!",
// });

export default {
  name: "tables",
  components: {
    AuthorsTable,
    ProjectsTable,
    SoftPagination,
    SoftPaginationItem,
    // DialogCard,
  },
};
</script>
