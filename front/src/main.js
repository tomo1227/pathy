import axios from "axios";
import { createPinia } from "pinia";
import { createApp } from "vue";
import VueAxios from "vue-axios";
import App from "./App.vue";
import router from "./router";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

createApp(App)
  .use(VueAxios, axios)
  .use(router)
  .use(createPinia().use(piniaPluginPersistedstate))
  .mount("#app");

axios.defaults.baseURL = "http://localhost:8000/api/v1/";
// axios.defaults.headers.post["Content-Type"] = "application/json";
// axios.defaults.xsrfCookieName = "csrftoken";
// axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
// process.env.PATHY_API_ENDPOINT;
