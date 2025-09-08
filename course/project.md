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

**Section 1: AI Agents for Software Systems** (4-5 pages)
- Code generation, optimization, and performance engineering
- *Cross-cutting theme: Agent-driven software-hardware co-optimization*

**Section 2: AI Agents for Architecture Design** (4-5 pages)  
- Performance prediction, design space exploration, and accelerator design
- *Cross-cutting theme: Multi-objective optimization and design trade-offs*

**Section 3: AI Agents for Physical Implementation** (4-5 pages)
- RTL synthesis, placement & routing, and verification
- *Cross-cutting theme: Constraint satisfaction and manufacturing considerations*

**Section 4: Cross-Stack Integration & Future Directions** (3-4 pages)
- Methodological connections, API design, and holistic system design
- *Cross-cutting theme: End-to-end agentic design workflows*

**Section 5: Evaluation Frameworks & Benchmarking** (2-3 pages)
- Comparative analysis, metrics, and reproducibility
- *Cross-cutting theme: Standardized evaluation across abstraction levels*

---

## Your Role: Data-Driven Analysis

### What Every Student Contributes

**You will be assigned to one section (2-3 students per section) and must provide:**

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
    title Survey Paper Project Timeline
    dateFormat  YYYY-MM-DD
    
    section Setup Phase
    Section Assignment           :milestone, assign, 2025-09-08, 0d
    Technical Planning Meetings  :planning, 2025-09-15, 2025-09-19
    
    section Software Phase
    Software Learning & Research :active, sw_research, 2025-09-08, 2025-10-01
    Checkpoint 1 Reviews        :milestone, cp1, 2025-10-01, 2025-10-03
    
    section Architecture Phase
    Architecture Learning & Research :active, arch_research, 2025-10-06, 2025-10-29
    Software Continued Analysis     :continue1, 2025-10-06, 2025-10-29
    Checkpoint 2 Reviews           :milestone, cp2, 2025-10-29, 2025-10-31
    
    section Chip Design Phase
    EDA Learning & Research        :active, eda_research, 2025-11-03, 2025-11-19
    Software Final Integration     :final1, 2025-11-03, 2025-11-19
    Architecture Final Integration :final2, 2025-11-03, 2025-11-19
    Checkpoint 3 Reviews          :milestone, cp3, 2025-11-19, 2025-11-21
    
    section Final Phase
    Paper Integration & Polish     :integration, 2025-11-24, 2025-12-01
    Final Presentations           :milestone, present, 2025-12-01, 0d
</div>

---

## Detailed Timeline & Deadlines

| Date | Checkpoint | Who | Deliverable | Page Count | Key Requirements |
|------|------------|-----|-------------|------------|------------------|
| **Sep 8** | Section Assignment | All Students | - | - | Preference ranking submitted |
| **Sep 15-19** | Planning Meetings | All Teams | Meeting with faculty | - | Technical work plan approved |
| **Oct 1** | **Checkpoint 1** | Software Teams | Literature Foundation | 4-5 pages | 20-25 papers analyzed, data extraction plan, preliminary figures |
| **Oct 29** | **Checkpoint 2** | Architecture Teams | Draft Analysis | 10-12 pages | Complete data analysis, comparative tables/figures, draft sections |
| **Nov 19** | **Checkpoint 3** | Chip Design Teams | Section Integration | 15-18 pages | Polished sections, cross-references, integration with other sections |
| **Dec 1** | **Final Presentation** | All Teams | Complete Survey | 18-22 pages | Publication-ready paper + 15-minute presentations |

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
- **Weekly office hours** with TAs for technical guidance
- **Cross-team integration meetings** to ensure coherent narrative
- **Faculty review sessions** at each checkpoint
- **Peer feedback** through structured review process

### Quality Assurance
- **Data analysis review sessions** with TAs to validate methodology
- **Cross-team presentations** of key findings and visualizations  
- **Faculty review of analytical contributions** before integration
- **External reviewer feedback** on final paper before submission

---

**Remember**: We're not just writing a survey paper - we're establishing the research agenda for agentic AI in computer systems design. Every table, figure, and insight you contribute helps create the definitive reference that will guide the field for years to come.
