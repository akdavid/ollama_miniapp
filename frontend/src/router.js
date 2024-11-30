import { createRouter, createWebHistory } from 'vue-router';
import ChatPage from './pages/ChatPage.vue';
import ImagePage from './pages/ImagePage.vue';
import HomePage from './pages/HomePage.vue';

const routes = [
    { path: '/', name: 'Home', component: HomePage },
    { path: '/chat', name: 'Chat', component: ChatPage },
    { path: '/image-description', name: 'Image', component: ImagePage },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
