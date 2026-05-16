const CACHE_NAME = 'gastarin-v1.12';

const urlsToCache = [
    '/',
    '/static/css/style.css',
    '/static/js/header.js',
    '/static/js/index.js',
    '/static/img/icon_gastarin.png',
    '/static/img/icon-192.png',
    '/static/img/icon-512.png',
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
    );
});