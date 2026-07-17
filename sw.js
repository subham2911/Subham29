const CACHE_NAME = 'sp-sangha-v1';
const STATIC_ASSETS = [
  './club.html',
  './manifest.json',
  './icon.svg'
];

// Cache static assets on install
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(STATIC_ASSETS))
  );
  self.skipWaiting();
});

// Remove old caches on activate
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const url = e.request.url;

  // Always go to network for live API calls — never cache these
  if (
    url.includes('jsonbin.io') ||
    url.includes('groq.com') ||
    url.includes('wikimedia.org') ||
    url.includes('wikipedia.org')
  ) {
    return;
  }

  // Network-first for HTML — always fetch latest, fall back to cache if offline
  if (url.endsWith('.html') || url.endsWith('/') || url === self.location.origin) {
    e.respondWith(
      fetch(e.request)
        .then(response => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
          return response;
        })
        .catch(() => caches.match(e.request))
    );
    return;
  }

  // Cache-first for other static assets (icon, manifest — rarely change)
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(response => {
        const clone = response.clone();
        caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
        return response;
      });
    })
  );
});
