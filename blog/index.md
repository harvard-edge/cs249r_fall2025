---
layout: default
title: "CS249r Blog: What We Learned"
permalink: /blog/
---

# CS249r Blog: What We Learned

*Weekly insights and reflections from Harvard's CS249r: Architecture 2.0*

---

## About This Blog

Every Monday, we share what we learned in the previous week of CS249r. These posts capture key insights, surprising discoveries, and the broader implications of how AI is transforming computer systems design.

**Target Audience**: Graduate CS students and practitioners interested in the future of AI-driven system design.

**Publication Rhythm**: Weekly Monday releases reflecting on the previous week's classes.

---

## Recent Posts

{% assign posts = site.posts %}
{% if posts.size > 0 %}
  {% for post in posts limit: 5 %}
  <article class="blog-preview">
    <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
    <div class="blog-meta">
      {{ post.date | date: "%B %d, %Y" }}
      {% if post.categories %}
        • {{ post.categories | join: ", " | capitalize }}
      {% endif %}
    </div>
    {% if post.excerpt %}
      <p>{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
    {% endif %}
    <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More →</a>
  </article>
  {% endfor %}
{% else %}
  <p><em>Blog posts coming soon! The first post will be published after our first week of classes.</em></p>
{% endif %}

---

## Archive

{% if posts.size > 5 %}
### Older Posts
{% for post in posts offset: 5 %}
- **[{{ post.title }}]({{ site.baseurl }}{{ post.url }})** - {{ post.date | date: "%B %d, %Y" }}
{% endfor %}
{% endif %}

---

## Subscribe & Share

Stay updated with our weekly insights:
- 🐦 Follow [@VJReddi](https://twitter.com/VJReddi) on Twitter for updates
- 📧 Subscribe to updates via [RSS](/cs249r_fall2025/feed.xml)
- 💬 Join discussions in the comments section of each post

<style>
.blog-preview {
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  background-color: #f8f9fa;
}

.blog-preview h2 {
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.blog-preview h2 a {
  color: #A51C30;
  text-decoration: none;
}

.blog-preview h2 a:hover {
  color: #8B1538;
  text-decoration: underline;
}

.blog-meta {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.read-more {
  color: #A51C30;
  font-weight: 500;
  text-decoration: none;
}

.read-more:hover {
  color: #8B1538;
  text-decoration: underline;
}
</style>