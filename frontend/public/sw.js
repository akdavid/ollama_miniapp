const cacheName = 'app-cache-v1';
const filesToCache = [
    '/',
    '/index.html',
    '/assets/styles/main.css',
    '/assets/styles/base.css',
    '/src/main.js',
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(cacheName).then(async cache => {
            try {
                return await cache.addAll(filesToCache);
            } catch (error) {
                console.error('Failed to cache files:', error);
            }
        }),
    );
});
