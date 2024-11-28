import { createRouter, createWebHistory } from 'vue-router';
import Chat from './components/Chat.vue';
import ImageDescription from './components/ImageDescription.vue';

const routes = [
  { path: '/', component: Chat },
  { path: '/image-description', component: ImageDescription },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
