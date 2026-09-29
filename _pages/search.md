---
permalink: /search/
title: "Search"
author_profile: true
sitemap: false
---

<div class="site-search">
  <input id="site-search-input" type="search" placeholder="Search posts, publications, talks and projects…" aria-label="Search the site" autofocus>
  <p id="site-search-status" class="page__meta"></p>
  <ul id="site-search-results" class="search-results"></ul>
</div>

<script>
(function () {
  const input = document.getElementById('site-search-input');
  const list = document.getElementById('site-search-results');
  const status = document.getElementById('site-search-status');
  const labels = { posts: 'Blog post', publications: 'Publication', talks: 'Talk', portfolio: 'Project', teaching: 'Teaching' };
  let docs = [];
  const escape = (s) => String(s || '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  function render(query) {
    const words = query.toLowerCase().split(/\s+/).filter(Boolean);
    list.innerHTML = '';
    if (!words.length) { status.textContent = docs.length + ' items indexed.'; return; }
    const hits = docs.map((d) => {
      const title = (d.title || '').toLowerCase(), body = (d.body || '').toLowerCase();
      if (!words.every((w) => title.includes(w) || body.includes(w))) return null;
      return { d, score: words.reduce((s, w) => s + (title.includes(w) ? 3 : 1), 0) };
    }).filter(Boolean).sort((a, b) => b.score - a.score);
    status.textContent = hits.length ? hits.length + ' result' + (hits.length > 1 ? 's' : '') : 'No results.';
    list.innerHTML = hits.slice(0, 30).map(({ d }) =>
      '<li><span class="search-type">' + escape(labels[d.type] || d.type) + (d.date ? ' · ' + escape(d.date) : '') +
      '</span><br><a href="' + escape(d.url) + '">' + escape(d.title) + '</a><p>' + escape(d.text) + '</p></li>').join('');
  }

  fetch('{{ "/search.json" | relative_url }}').then((r) => r.json()).then((data) => {
    docs = data;
    const q = new URLSearchParams(location.search).get('q') || '';
    input.value = q; render(q);
  });
  input.addEventListener('input', () => render(input.value));
})();
</script>
