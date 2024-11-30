import { fileURLToPath, URL } from 'node:url'; // Import unique des utilitaires
import { defineConfig } from 'vite'; // Import unique de `defineConfig`
import vue from '@vitejs/plugin-vue'; // Import unique du plugin Vue

export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url)), // Alias pour `@`
        },
    },
});
