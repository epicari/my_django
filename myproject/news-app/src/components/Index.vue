<template>
  <div class="">
</template>

<scrept>
import axios from 'axios';

export default {
    data() {
        return {
            news: []
        }
    },
    create() {
        this.all();
    },
    methods: {
        all: function () {
            axios.get('http://127.0.0.1:8000/api/news/')
            .then( response => {
                this.news = response.data
            });
        }
    },
}
</scrept>