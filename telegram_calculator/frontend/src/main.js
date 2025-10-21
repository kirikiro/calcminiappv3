import { createApp } from 'vue';
import App from './App.vue';

// Эта строка находит элемент <div id="app"> в вашем index.html
// и монтирует в него ваше главное Vue-приложение.
createApp(App).mount('#app');