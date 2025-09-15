---
layout: default
title: Papers
---

<div class="community-page">
  <h1>Papers</h1>
  
  <div class="papers-description">
    <p><strong>About this collection:</strong> This is a curated repository of recent research papers at the intersection of AI and computer systems design. The collection focuses specifically on <em>AI for Hardware</em> — papers that demonstrate how artificial intelligence techniques are being applied to optimize, design, and verify hardware systems, from analog circuits to chip architecture to system-level optimization.</p>
    
    <p><strong>Why we maintain this:</strong> Finding relevant Architecture 2.0 papers scattered across conferences like DAC, ICCAD, ASPLOS, ISCA, and arXiv can be time-consuming. This centralized, searchable collection makes it easy for students and researchers to quickly discover papers relevant to AI-driven hardware design, whether you're looking for the latest in LLM-assisted verification, neural architecture search for accelerators, or ML-driven chip placement algorithms.</p>
    
    <p>The collection is updated periodically throughout the semester as new relevant papers emerge. Use the category filters and search function to quickly find papers in your area of interest.</p>
  </div>
  
  <p>Total papers: <span id="total-papers">{{ site.data.tagged_papers | size }}</span></p>

  <div id="tag-filters">
    <button class="tag-filter-btn active" data-tag="all">All Topics</button>
    {% assign all_tags_str = site.data.tagged_papers | map: "tags" | join: "," %}
    {% assign tags = all_tags_str | split: "," | uniq | sort %}
    {% for tag in tags %}
      {% if tag != "" %}
        <button class="tag-filter-btn" data-tag="{{ tag | downcase }}">{{ tag }}</button>
      {% endif %}
    {% endfor %}
  </div>

  <input type="text" id="paper-search" placeholder="Search papers by title or abstract...">

  <div class="talk-list" id="papers-list">
      {% assign papers = site.data.tagged_papers %}
      {% for paper in papers %}
        <div class="talk list-group-item paper-item" data-tags="{{ paper.tags | join: ',' | downcase }}" data-date="{{ paper.date }}">
          <div class="paper-header">
            <div class="paper-title">{{ paper.title }}</div>
            <div class="paper-tags">
              {% for tag in paper.tags %}
                <span class="paper-tag">{{ tag }}</span>
              {% endfor %}
            </div>
          </div>
          <div class="paper-date" style="display:none;">{{ paper.date | date: '%B %Y' }}</div>
          <div class="paper-actions">
            {% assign target_url = paper.arxiv_url | default: paper.url %}
            <a class="talk-title-link" href="{{ target_url }}" target="_blank" rel="noopener noreferrer">Paper ↗</a>
            <details style="display: inline-block; margin-left: 0.5rem;">
              <summary>Abstract</summary>
              <div class="paper-abstract">
                {{ paper.abstract }}
              </div>
            </details>
          </div>
        </div>
      {% endfor %}
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('paper-search');
    const papersList = document.getElementById('papers-list');
    const totalPapersSpan = document.getElementById('total-papers');
    const tagFilterButtons = document.querySelectorAll('.tag-filter-btn');

    const allPaperElements = Array.from(papersList.getElementsByClassName('paper-item'));
    const papersData = allPaperElements.map(el => {
        return {
            element: el,
            title: el.querySelector('.paper-title').textContent.toLowerCase(),
            abstract: el.querySelector('.paper-abstract').textContent.toLowerCase(),
            tags: (el.dataset.tags || '').split(','),
            date: el.dataset.date
        };
    });

    // Sort papers by date, newest first
    papersData.sort((a, b) => new Date(b.date) - new Date(a.date));

    let filteredPapers = papersData;
    let currentTag = 'all';

    function displayPapers() {
        // Filter by tag first
        let papersToShow = papersData;
        if (currentTag !== 'all') {
            papersToShow = papersData.filter(paper => paper.tags.includes(currentTag));
        }

        // Then, filter by search term
        const searchTerm = searchInput.value.toLowerCase();
        filteredPapers = papersToShow.filter(paper => {
            return paper.title.includes(searchTerm) || paper.abstract.includes(searchTerm);
        });

        totalPapersSpan.textContent = filteredPapers.length;

        // Hide all papers first
        allPaperElements.forEach(el => el.style.display = 'none');

        // Show filtered papers
        filteredPapers.forEach(paper => paper.element.style.display = 'block');
    }

    searchInput.addEventListener('input', () => {
        displayPapers();
    });

    tagFilterButtons.forEach(button => {
        button.addEventListener('click', () => {
            currentTag = button.dataset.tag;
            tagFilterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            displayPapers();
        });
    });

    // Initial display - show all papers sorted by date
    allPaperElements.forEach(p => papersList.appendChild(p));
    displayPapers();
});
</script>

<style>
.papers-description {
  background-color: #f8f9fa;
  border-left: 4px solid #A51C30;
  padding: 1.5rem;
  margin: 1.5rem 0;
  border-radius: 0 8px 8px 0;
}

.papers-description p {
  margin-bottom: 1rem;
  line-height: 1.7;
}

.papers-description p:last-child {
  margin-bottom: 0;
}

.talk-list {
  max-height: 800px;
  overflow-y: auto;
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.paper-item {
  background-color: white;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 0.75rem 1rem;
  margin-bottom: 0.5rem;
  transition: box-shadow 0.2s ease, border-color 0.2s ease;
}

.paper-item:hover {
  box-shadow: 0 2px 8px rgba(165, 28, 48, 0.08);
  border-color: #A51C30;
}

.paper-item:last-child {
  margin-bottom: 0;
}

.paper-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 0.4rem;
  gap: 1rem;
}
.paper-title {
  font-size: 0.95rem;
  font-weight: 600;
  color: #2c3e50;
  line-height: 1.3;
  flex: 1;
}

.paper-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  justify-content: flex-end;
  flex-shrink: 0;
}

.paper-tag {
  background-color: #f5f5f5;
  color: #666;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 0.7rem;
  font-weight: 500;
  white-space: nowrap;
}

.paper-abstract {
  color: #666;
  line-height: 1.5;
  padding: 0.75rem;
  background-color: #f8f9fa;
  border-radius: 4px;
  margin-top: 0.5rem;
  font-size: 0.85rem;
}

.talk-title-link {
  display: inline-block;
  padding: 4px 10px;
  background-color: #A51C30;
  color: white !important;
  text-decoration: none;
  border-radius: 3px;
  font-size: 0.75rem;
  font-weight: 500;
  transition: background-color 0.2s ease;
  margin-top: 0.3rem;
}

.talk-title-link:hover {
  background-color: #8B1538;
}

details summary {
  cursor: pointer;
  color: #A51C30;
  font-weight: 500;
  font-size: 0.85rem;
  padding: 0.3rem 0;
  user-select: none;
  transition: color 0.2s ease;
  display: inline-block;
}

details summary:hover {
  color: #8B1538;
}

details[open] summary {
  margin-bottom: 0;
}

.paper-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
#tag-filters {
  margin-bottom: 20px;
  display: flex;
  flex-wrap: wrap;
}
#tag-filters .tag-filter-btn {
  margin-right: 10px;
  margin-bottom: 10px;
  padding: 8px 12px;
  cursor: pointer;
  border: 1px solid #ddd;
  background-color: #fff;
  border-radius: 16px;
}
#tag-filters .tag-filter-btn.active {
  background-color: #A51C30; /* Harvard red */
  color: white;
  border-color: #A51C30;
}
#paper-search {
    width: 100%;
    padding: 10px;
    margin: 20px 0;
    font-size: 1em;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
}
</style>


