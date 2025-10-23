---
layout: default
title: "CS249r Notes: What We Learned"
permalink: /blog/
---

# CS249r Notes: What We Learned

*Weekly recaps and reflections from Harvard's CS249r: Architecture 2.0*

---


{% assign posts = site.posts %}
{% if posts.size > 0 %}
  {% for post in posts %}
  <article class="blog-preview">
    <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
    <div class="blog-meta">
      {{ post.date | date: "%B %d, %Y" }}
      {% if post.categories %}
        • {{ post.categories | join: ", " | capitalize }}
      {% endif %}
      {% assign words = post.content | strip_html | number_of_words %}
      {% assign reading_time = words | divided_by: 200 | plus: 1 %}
      • {{ reading_time }} min read
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

## Follow the Frontier

New posts drop every Monday. Don't miss the insights:
- 🐦 Follow [@aryatschand](https://twitter.com/aryatschand) and [@profvjreddi](https://twitter.com/profvjreddi) for weekly post announcements and class highlights
- 📧 Subscribe to updates via [RSS]({{ "/feed.xml" | prepend: site.baseurl }})
- 💬 Join discussions in the comments—this is where the best ideas get refined

*These are the conversations that will define the next decade of computer systems. Be part of them.*

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

.key-takeaways {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  border-left: 4px solid #A51C30;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 2rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.key-takeaways h3 {
  margin-top: 0;
  color: #A51C30;
  font-size: 1.1rem;
  font-weight: 600;
}

.key-takeaways ul {
  margin-bottom: 0;
  padding-left: 1.2rem;
}

.key-takeaways li {
  margin-bottom: 0.8rem;
  line-height: 1.5;
}

/* Mobile optimization */
@media (max-width: 768px) {
  .blog-preview {
    padding: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .blog-preview h2 {
    font-size: 1.3rem;
    line-height: 1.3;
  }
  
  .key-takeaways {
    padding: 1rem;
    margin: 1.5rem 0;
  }
  
  .key-takeaways h3 {
    font-size: 1rem;
  }
}

/* Reading time styling */
.reading-time {
  color: #666;
  font-weight: 500;
}

/* Details/summary styling */
details {
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 1rem;
  margin: 1.5rem 0;
  background-color: #f8f9fa;
}

summary {
  cursor: pointer;
  font-size: 1.1rem;
  color: #A51C30;
  margin-bottom: 0;
  padding: 0.5rem 0;
  list-style: none;
}

summary::-webkit-details-marker {
  display: none;
}

summary::before {
  content: "▶ ";
  margin-right: 0.5rem;
  transition: transform 0.2s ease;
}

details[open] summary::before {
  transform: rotate(90deg);
}

details[open] summary {
  margin-bottom: 1rem;
  border-bottom: 1px solid #dee2e6;
  padding-bottom: 1rem;
}
</style>