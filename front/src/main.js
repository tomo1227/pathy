import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import VueAxios from "vue-axios";

createApp(App).use(VueAxios, axios).use(router).mount("#app");
axios.defaults.baseURL = "http://localhost:8000/api/v1/";
// process.env.PATHY_API_ENDPOINT;
