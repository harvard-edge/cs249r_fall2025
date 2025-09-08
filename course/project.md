---
layout: default
---

# Survey Paper Project: Agentic AI for Computer Systems Design

## The Vision: Our Goal

**We are creating the definitive cross-stack survey on "Agentic AI for Computer Systems Design"** - the first comprehensive analysis that examines how AI agents are transforming computer systems design across the complete computing stack, from software optimization to chip design.

**Why This Matters**: Current research is fragmented across venues (ISCA, MICRO, DAC, MLSys, ICLR). No one has written the systematic cross-stack analysis that shows how these methodologies connect and where the field is heading holistically. This survey will establish the research agenda for the next decade.

**Target Impact**: Publication-quality paper suitable for top-tier venues like ISCA, MICRO, or Computer Architecture Letters.

---

## Project Structure

### The Complete Survey Paper (35-45 pages)

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

**8. Conclusion & Future Directions** (2 pages)
- Research roadmap and concrete opportunities
- Vision for unified agentic design ecosystem

**Expected Total Length: 25-30 pages** (substantial publication-quality survey)

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

**Group Structure for 16 Students:**

**🔧 Software Group (5-6 students):**
- **Focus Areas**: Code generation, compiler optimization, performance engineering
- **Architecture 2.0 Components**: 
  - Benchmarks & evaluation frameworks (HumanEval, MBPP, SWE-bench)
  - ML tools & development practices (LLM-based tools, optimization techniques)
  - Best practices for agentic software development workflows

**🏗️ Architecture Group (5-6 students):**
- **Focus Areas**: Performance prediction, design space exploration, accelerator design
- **Architecture 2.0 Components**:
  - Design space exploration methodologies and modeling frameworks
  - AI accelerator architecture analysis and performance comparisons
  - Memory system optimization and energy-performance trade-offs

**⚡ EDA Group (5-6 students):**
- **Focus Areas**: RTL synthesis, physical design, verification
- **Architecture 2.0 Components**:
  - Synthesis & optimization tool capabilities and QoR analysis
  - Physical design automation and placement/routing techniques
  - AI-assisted verification and design rule checking evolution

**Total: 16 students across 3 groups (5-6 students each)**

**The Template Structure**: Each group covers the full Architecture 2.0 framework within their domain - analyzing benchmarks/datasets, tools/methodologies, and best practices, then contributes to the cross-stack integration analysis.

---

## Timeline: Three-Checkpoint Pipeline

<div class="mermaid">
flowchart TD
    A["Weeks 1-2: Foundations<br/>Sep 3-15: Architecture 2.0 + Group Formation"] --> B["🔧 Software Group<br/>(5-6 students)"]
    A --> C["🏗️ Architecture Group<br/>(5-6 students)"]
    A --> D["⚡ EDA Group<br/>(5-6 students)"]
    
    B --> E["Weeks 3-5: Learn Software Topics<br/>Sep 15 - Oct 1: Research Literature<br/>(Benchmarks, Tools, Best Practices)"]
    C --> F["Weeks 3-5: Learn Software Topics<br/>Sep 15 - Oct 1: Plan Architecture Research<br/>(Modeling, Accelerators, Memory)"]
    D --> G["Weeks 3-5: Learn Software Topics<br/>Sep 15 - Oct 1: Plan EDA Research<br/>(Synthesis, Physical Design, Verification)"]
    
    E --> H["📋 Checkpoint 1: Oct 1<br/>Literature Review<br/>(Software Group)"]
    
    F --> I["Weeks 6-9: Learn Architecture<br/>Oct 6-29: Research Literature<br/>(Modeling, Accelerators, Memory)"]
    G --> J["Weeks 6-9: Learn Architecture<br/>Oct 6-29: Plan EDA Research<br/>(Synthesis, Physical Design, Verification)"]
    H --> K["Weeks 6-9: Continue Software<br/>Oct 6-29: Research & Writing"]
    
    I --> L["📊 Checkpoint 2: Oct 29<br/>Draft Sections<br/>(Architecture Group)"]
    
    J --> M["Weeks 10-12: Learn EDA<br/>Nov 3-19: Research Literature<br/>(Synthesis, Physical Design, Verification)"]
    K --> N["Weeks 10-12: Finalize Software<br/>Nov 3-19: Complete Sections"]
    L --> O["Weeks 10-12: Finalize Architecture<br/>Nov 3-19: Complete Sections"]
    
    M --> P["📖 Checkpoint 3: Nov 19<br/>Final Integration<br/>(EDA Group)"]
    
    N --> Q["Week 13: Final Assembly<br/>Nov 24-Dec 1: All 3 Groups Integrate"]
    O --> Q
    P --> Q
    
    Q --> R["🎯 Dec 1: Final Submission<br/>Complete Survey Papers"]
    
    style H fill:#e1f5fe
    style L fill:#f3e5f5
    style P fill:#e8f5e8
    style R fill:#fff3e0
</div>

**The Pipeline Logic:**
- **Weeks 1-2 (Sep 3-15)**: Foundations & Architecture 2.0 + Group formation
- **Software group** starts intensive work in Weeks 3-5 (Sep 15 - Oct 1) while learning software topics
- **Architecture group** begins deep work in Weeks 6-9 (Oct 6-29) while learning architecture  
- **EDA group** starts intensive work in Weeks 10-12 (Nov 3-19) while learning EDA topics
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
| **Week 17** | **Final Submission** | All Teams | Complete Survey | 25-30 pages | Publication-ready paper submitted |

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

## Student-Driven Paper Presentations

**Throughout the semester, your group will present papers from the course schedule related to your specialization area:**

- **Software Group**: Present papers during Weeks 3-5 (Sep 15 - Oct 1, Software phase)
- **Architecture Group**: Present papers during Weeks 6-9 (Oct 6-29, Architecture phase)  
- **EDA Group**: Present papers during Weeks 10-12 (Nov 3-19, EDA phase)

**Presentation Responsibilities:**
- **Lead the discussion** of assigned papers in your domain
- **Connect papers to your survey research** and identify relevant data/insights
- **Guide class analysis** of methodologies and findings
- **Facilitate Q&A** and synthesis with other course themes
- **Extract data and insights** for your survey section during presentations

This integration ensures your survey research is directly informed by the papers you're presenting and discussing in class.

---

**Remember**: We're not just writing a survey paper - we're establishing the research agenda for agentic AI in computer systems design. Every table, figure, and insight you contribute helps create the definitive reference that will guide the field for years to come.
