import './assets/main.css'

// My Style
import "./assets/scss/style.scss"

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
// Axios  Import
// Axios  استيراد
import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000";

// Page [ messenger/messenger_vue/src/main.js ]

// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// Add Free Icons Styles To SVG Core
library.add(fas, far, fab);


const app = createApp(App)

// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon);
app.use(createPinia())
app.use(router, axios);


app.mount('#app')
