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
          <div>
            {% assign target_url = paper.arxiv_url | default: paper.url %}
            <a class="talk-title-link" href="{{ target_url }}" target="_blank" rel="noopener noreferrer">Details <i class="bi bi-box-arrow-up-right"></i></a>
          </div>
          <details>
            <summary>Abstract</summary>
            <div class="paper-abstract">
              {{ paper.abstract }}
            </div>
          </details>
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
}
.paper-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}
.paper-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  justify-content: flex-end;
  max-width: 30%;
}
.paper-tag {
  background-color: #eee;
  color: #333;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 0.8em;
  white-space: nowrap;
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


