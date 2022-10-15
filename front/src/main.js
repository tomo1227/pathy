import axios from "axios";
import { createPinia } from "pinia";
import { createApp } from "vue";
import VueAxios from "vue-axios";
import App from "./App.vue";
import router from "./router";

createApp(App)
  .use(VueAxios, axios)
  .use(router)
  .use(createPinia())
  .mount("#app");
axios.defaults.baseURL = "http://localhost:8000/api/v1/";
// process.env.PATHY_API_ENDPOINT;
