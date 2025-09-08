---
layout: default
---

# Survey Paper Project: Agentic AI for Computer Systems Design

## The Vision: Our Goal

**We are creating the definitive cross-stack survey on "Agentic AI for Computer Systems Design"** - the first comprehensive analysis that examines how AI agents are transforming computer systems design across the complete computing stack, from software optimization to chip design.

**Why This Matters**: Current research is fragmented across venues (ISCA, MICRO, DAC, MLSys, ICLR). No one has written the systematic cross-stack analysis that shows how these methodologies connect and where the field is heading holistically. This survey will establish the research agenda for the next decade.

**Target Impact**: Publication-quality paper suitable for top-tier venues like ISCA, MICRO, or Computer Architecture Letters.

---

## Project Structure: Working Backwards from Excellence

### The Complete Survey Paper (18-22 pages)

**"Agentic AI for Computer Systems Design: A Holistic Cross-Stack Perspective"**

**Tentative Paper Outline:**

**1. Introduction** (1-2 pages)
- Problem motivation: Why generative AI changes everything for systems design
- Cross-stack perspective and unique contributions of this survey

**2. Background** (2-3 pages)
- Focus on **generative/agentic AI** (LLMs, diffusion models, RL agents)
- Distinction from traditional ML-driven approaches (which have existing surveys)
- Evolution from heuristic-based → ML-driven → agentic design paradigms

**3. Related Work** (2-3 pages)
- Existing surveys on ML for systems (what we're NOT doing)
- Gap analysis: Why cross-stack agentic perspective is missing
- Positioning our unique contribution

**4. Agentic AI for Software Systems** (4-5 pages)
- Code generation, optimization, and performance engineering
- *Team Focus: Software vertical*

**5. Agentic AI for Architecture Design** (4-5 pages)  
- Performance prediction, design space exploration, and accelerator design
- *Team Focus: Architecture vertical*

**6. Agentic AI for Physical Implementation** (4-5 pages)
- RTL synthesis, placement & routing, and verification
- *Team Focus: EDA vertical*

**7. Cross-Stack Connections & Integration** (3-4 pages)
- **The key insight**: How knowledge propagates between layers
- Software ↔ Architecture ↔ EDA connection analysis
- End-to-end agentic design workflows

**8. Conclusion & Future Directions** (1-2 pages)
- Research roadmap and concrete opportunities
- Vision for unified agentic design ecosystem

---

## Your Role: Focused Vertical Analysis

### What Every Student Contributes

**You will be assigned to one vertical track (2-3 students per track) and must provide:**

1. **Comprehensive Literature Analysis** (20-25 key papers in your section)
2. **Data-Driven Insights** through systematic extraction and analysis of existing results
3. **Visual Synthesis** via tables, figures, and charts that reveal new patterns
4. **Cross-Stack Connections** linking your section to others

### Data-Driven Analysis Requirements

**Your analytical work must include:**
- **Systematic data extraction** from papers, GitHub repos, benchmark leaderboards
- **Synthesis tables and figures** that reveal patterns not visible in individual papers  
- **Trend analysis and timeline visualizations** showing technique evolution
- **Performance landscape mapping** using aggregated results from multiple sources
- **Gap identification** through systematic coverage analysis

**Examples of What You'll Create:**

<div class="mermaid">
graph LR
    A[Literature Review<br/>20-25 Papers] --> B[Data Extraction<br/>Performance Results]
    B --> C[Comparative Analysis<br/>Tables & Figures]
    C --> D[Trend Analysis<br/>Timeline Visualizations]
    D --> E[Gap Identification<br/>Research Opportunities]
    E --> F[Cross-Stack Insights<br/>Novel Connections]
</div>

**Concrete Examples by Section:**

**Software Section:**
- Comparative performance tables from HumanEval, MBPP, SWE-bench results across LLM code generators
- Timeline analysis of compiler optimization techniques adoption (2020-2025)
- GPU kernel performance comparison matrices from published benchmarks

**Architecture Section:**
- Design space exploration visualizations aggregated from accelerator papers
- Memory system performance trend analysis from ISCA/MICRO papers
- Energy-performance Pareto frontier analysis across AI accelerators

**Chip Design Section:**
- EDA tool capability comparison matrix (features, supported designs, performance)
- Synthesis QoR improvement trends over time from published results
- Verification coverage analysis across different AI-assisted approaches

---

## Timeline: Three-Checkpoint Pipeline

<div class="mermaid">
gantt
    title Staggered Pipeline - Teams Start When Learning Their Domain
    dateFormat  X
    axisFormat %s
    
    section All Students
    Track Assignment           :milestone, assign, 2, 0
    Planning Meetings          :planning, 3, 1
    
    section Software Track
    Learn Software Topics      :active, sw_learn, 2, 6
    Deep Research Work         :sw_research, 4, 4
    Checkpoint 1 Due           :milestone, cp1, 8, 0
    Continue Writing           :sw_write, 9, 8
    
    section Architecture Track
    Plan While Learning        :arch_plan, 2, 4
    Learn Architecture Topics  :active, arch_learn, 6, 6
    Deep Research Work         :arch_research, 8, 4
    Checkpoint 2 Due           :milestone, cp2, 12, 0
    Continue Writing           :arch_write, 13, 4
    
    section EDA Track
    Plan While Learning        :eda_plan, 2, 8
    Learn EDA Topics           :active, eda_learn, 10, 6
    Deep Research Work         :eda_research, 12, 4
    Checkpoint 3 Due           :milestone, cp3, 16, 0
    
    section Final Integration
    All Teams Integrate        :integration, 17, 1
    Final Presentations        :milestone, present, 17, 0
</div>

**The Pipeline Logic:**
- **Software teams** start intensive work early (Weeks 2-8) while learning software topics
- **Architecture teams** begin their deep work in the middle (Weeks 6-12) while learning architecture  
- **EDA teams** start their intensive work later (Weeks 10-16) while learning EDA topics
- **Staggered deadlines** prevent bottlenecks and align with course learning phases

---

## Detailed Timeline & Deadlines

| Week | Checkpoint | Who | Deliverable | Page Count | Key Requirements |
|------|------------|-----|-------------|------------|------------------|
| **Week 2** | Section Assignment | All Students | Preference Form | - | Rank your top 3 section preferences |
| **Week 3** | Planning Meetings | All Teams | Meeting with TAs & Instructor | - | Data analysis plan approved |
| **Week 8** | **Checkpoint 1** | Software Teams | Literature Foundation | 4-5 pages | 20-25 papers analyzed, data extraction plan, preliminary figures |
| **Week 12** | **Checkpoint 2** | Architecture Teams | Draft Analysis | 10-12 pages | Complete data analysis, comparative tables/figures, draft sections |
| **Week 16** | **Checkpoint 3** | Chip Design Teams | Section Integration | 15-18 pages | Polished sections, cross-references, integration with other sections |
| **Week 17** | **Final Presentation** | All Teams | Complete Survey | 18-22 pages | Publication-ready paper + 15-minute presentations |

---

## Assessment Rubric

### How You'll Be Evaluated

**Data-Driven Analysis (40%)**
- Quality and insight of generated tables/figures (15%)
- Rigor of data extraction and analysis methodology (15%)  
- Integration of quantitative findings with survey narrative (10%)

**Survey Writing (35%)**
- Literature comprehension and synthesis (15%)
- Cross-cutting analysis and novel insights (10%)
- Writing quality and technical communication (10%)

**Collaboration & Integration (25%)**
- Cross-team coordination and referencing (10%)
- Checkpoint deliverable quality (10%)
- Final presentation and Q&A (5%)

---

## Quality Standards: Publication-Ready Work

### What "Publication Quality" Means

**Analytical Rigor:**
- All major claims supported by tables, figures, or quantitative analysis
- Systematic comparisons revealing trends and gaps across literature
- Quantitative findings that connect insights across abstraction levels

**Survey Excellence:**
- Comprehensive coverage of 100+ papers across all areas (2020-2025)
- Novel cross-cutting analysis identifying methodological connections
- Original insights through systematic data synthesis
- Rich visualizations revealing patterns invisible in individual papers
- 5-7 concrete research opportunities with technical justification

**Publication Standards:**
- Target venues: ISCA, MICRO, Computer Architecture Letters, ACM Computing Surveys
- Professional formatting and citation management
- Reproducible analysis methodology with documented data sources

---

## Getting Started: Your Next Steps

### Week 1-2: Section Assignment
1. **Review all five sections** and understand the cross-cutting themes
2. **Rank your preferences** (1-5) considering your background and interests
3. **Submit preference form** by September 8

### Week 3: Technical Planning
1. **Attend your team's planning meeting** (45 minutes with faculty/TAs)
2. **Define your data extraction and analysis plan**
3. **Identify key papers and data sources** for your section
4. **Establish individual responsibilities** within your team

### Week 4+: Execute Your Plan
1. **Begin systematic literature review** and data extraction
2. **Attend weekly cross-team integration meetings**
3. **Develop tables, figures, and analysis** according to your timeline
4. **Prepare for your checkpoint deliverable**

---

## Support & Resources

### Getting Help
- **Weekly TA office hours** for technical guidance and methodology support
- **Cross-team integration meetings** to ensure coherent narrative across sections
- **Instructor review sessions** at each major checkpoint
- **Peer feedback sessions** through structured cross-team reviews

### Quality Assurance
- **TA-led methodology review sessions** to validate data analysis approaches
- **Cross-team presentations** of key findings and visualizations  
- **Instructor review of all analytical contributions** before final integration
- **External expert feedback** on complete draft before submission

---

**Remember**: We're not just writing a survey paper - we're establishing the research agenda for agentic AI in computer systems design. Every table, figure, and insight you contribute helps create the definitive reference that will guide the field for years to come.
