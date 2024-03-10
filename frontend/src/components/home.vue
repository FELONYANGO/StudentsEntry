<template>


    <h1 class="text-3xl font-bold underline"> {{ msg  }}</h1>
    

</template>
    
    
<script>
import axios from 'axios';

export default {
  name: 'home',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {

          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
