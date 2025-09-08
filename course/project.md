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
- Connection analysis between all three domains:

<div class="mermaid">
graph LR
    SW["🔧 Software Layer<br/>Code Generation<br/>Compiler Optimization<br/>Performance Engineering"]
    ARCH["🏗️ Architecture Layer<br/>Design Space Exploration<br/>Accelerator Design<br/>Memory Systems"]
    EDA["⚡ EDA Layer<br/>RTL Synthesis<br/>Physical Design<br/>Verification"]
    
    SW <-->|"Performance Feedback<br/>Hardware-Aware Optimization"| ARCH
    ARCH <-->|"Design Constraints<br/>Physical Feasibility"| EDA
    SW <-.->|"End-to-End Optimization<br/>Software-Hardware Co-design"| EDA
    
    style SW fill:#e1f5fe
    style ARCH fill:#f3e5f5
    style EDA fill:#e8f5e8
</div>

- **Software ↔ Architecture**: Performance feedback loops, hardware-aware code optimization
- **Architecture ↔ EDA**: Design constraint propagation, physical feasibility validation  
- **Software ↔ EDA**: End-to-end optimization, direct software-to-silicon workflows
- End-to-end agentic design workflows that span all three layers

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
flowchart TD
    A["Week 1-2: Course Setup<br/>Group Formation"] --> B["AI for Software Groups<br/>(2-3 students each)"]
    A --> C["AI for Architecture Groups<br/>(2-3 students each)"]
    A --> D["AI for Chip Design Groups<br/>(2-3 students each)"]
    
    B --> E["Weeks 2-5: Learn Software Topics<br/>+ Research Literature"]
    C --> F["Weeks 2-5: Learn Software Topics<br/>+ Plan Architecture Research"]
    D --> G["Weeks 2-5: Learn Software Topics<br/>+ Plan EDA Research"]
    
    E --> H["📋 Checkpoint 1: Oct 1<br/>Literature Review<br/>(Software Groups)"]
    
    F --> I["Weeks 6-9: Learn Architecture<br/>+ Research Literature"]
    G --> J["Weeks 6-9: Learn Architecture<br/>+ Plan EDA Research"]
    H --> K["Weeks 6-9: Continue Software<br/>Research & Writing"]
    
    I --> L["📊 Checkpoint 2: Oct 29<br/>Draft Sections<br/>(Architecture Groups)"]
    
    J --> M["Weeks 10-12: Learn EDA<br/>+ Research Literature"]
    K --> N["Weeks 10-12: Finalize Software<br/>Sections"]
    L --> O["Weeks 10-12: Finalize Architecture<br/>Sections"]
    
    M --> P["📖 Checkpoint 3: Nov 19<br/>Final Integration<br/>(EDA Groups)"]
    
    N --> Q["Week 13: Final Assembly<br/>All Groups Integrate"]
    O --> Q
    P --> Q
    
    Q --> R["🎯 Dec 1: Final Presentations<br/>Complete Survey Papers"]
    
    style H fill:#e1f5fe
    style L fill:#f3e5f5
    style P fill:#e8f5e8
    style R fill:#fff3e0
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
