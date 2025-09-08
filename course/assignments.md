---
layout: default
---

# Assignments & Deliverables

## Assignment Overview

This course emphasizes **active engagement** with cutting-edge research through four main components:

- **Survey Paper Checkpoints**: Three milestone checkpoints (45% total)
- **Final Paper Integration**: Collaborative review and finalization (15%)
- **Paper Presentations**: Individual presentations of assigned papers (20%)
- **Paper Discussion and Attendance**: Participation in class discussions (20%)

---

## 1. Survey Paper Checkpoints (45%)

**Format**: Three milestone checkpoints (15% each)  
**Purpose**: Progressive development and validation of your survey paper research  
**Timeline**: Aligned with course phases and survey paper development

### Checkpoint Structure
- **Checkpoint 1 (15%)**: Literature survey - Comprehensive review of relevant papers in your section
- **Checkpoint 2 (15%)**: Data-driven exercise - Gathering results, creating plots/tables, assembling raw data  
- **Checkpoint 3 (15%)**: First draft of your section - Complete draft of your survey section

Each checkpoint focuses on **systematic research development**, building toward a publication-quality survey paper through structured milestones.

<details>
<summary><strong>📋 Checkpoint 1 Details: Literature Survey</strong></summary>

**Deliverable**: Comprehensive review of relevant papers in your section (4-5 pages)  
**Requirements**:
- 20-25 key papers identified with data extraction plan
- Cross-cutting themes and quantitative analysis opportunities identified
- Detailed plan for tables/figures to be generated from existing data
- Methodology for data collection and analysis documented

</details>

<details>
<summary><strong>📊 Checkpoint 2 Details: Data-Driven Exercise</strong></summary>

**Deliverable**: Technical results with generated tables and figures (10-12 pages)  
**Requirements**:
- Completed data analysis with generated tables and figures
- Comparative analysis revealing new insights from existing literature
- Draft survey sections with quantitative findings integrated
- Cross-references and data connections to other sections identified

</details>

<details>
<summary><strong>📖 Checkpoint 3 Details: First Draft</strong></summary>

**Deliverable**: Complete draft of your survey section (12-15 pages)  
**Requirements**:
- Comprehensive cross-stack analysis with data-driven insights
- Quantitative analysis seamlessly integrated into narrative
- Cross-cutting themes supported by comparative data and visualizations
- Future research directions based on identified gaps and trends

</details>

---

## 2. Final Paper Integration (15%)

**Format**: Collaborative review and finalization of the complete survey paper  
**Purpose**: Ensure coherent, publication-quality final paper through group coordination  
**Timeline**: Final weeks of the semester

### Integration Process
- **Cross-section coordination**: Ensuring consistency and flow between sections
- **Final review and editing**: Collaborative refinement of the complete paper
- **Quality assurance**: Meeting publication standards for target venues

---

## 3. Paper Presentations (20%)

**Format**: Present and lead discussion for assigned papers (individually or in pairs)  
**Structure**: 20-minute presentation + 20-minute facilitated discussion per paper  
**Sign-up**: By Week 3

### Presentation Structure
**20-Minute Presentation:**
- Paper summary and key contributions (5-7 minutes)
- Critical analysis: strengths, limitations, methodology issues (8-10 minutes)
- Connections to course themes and other papers (3-5 minutes)

**20-Minute Discussion:**
- Facilitate Q&A and critical discussion
- Prepare 3-4 provocative discussion questions
- Guide synthesis and connections to broader themes

### Responsibilities
- **Preparation**: Meet with instructor 1 week before, prepare slides and discussion questions
- **Flexibility**: Timing may adjust based on guest speaker availability and class dynamics
- **Follow-up**: Brief reflection on presentation effectiveness and discussion insights

---

## 4. In-Class Paper Discussion and Attendance (20%)

**Format**: Active participation in class discussions and consistent attendance  
**Purpose**: Engage with course material through thoughtful discussion and peer interaction  
**Timeline**: Throughout the semester

### Participation Components
- **Class attendance**: Regular attendance at all sessions
- **Discussion engagement**: Thoughtful contributions to paper discussions
- **Peer interaction**: Constructive feedback and questions during presentations

---

## Survey Paper Project Overview

**We are creating the definitive cross-stack survey on "Agentic AI for Computer Systems Design"** - the first comprehensive analysis that examines how AI agents are transforming computer systems design across the complete computing stack, from software optimization to chip design.

**Why This Matters**: Current research is fragmented across venues (ISCA, MICRO, DAC, MLSys, ICLR). No one has written the systematic cross-stack analysis that shows how these methodologies connect and where the field is heading holistically.

**Target Impact**: Publication-quality paper suitable for top-tier venues like ISCA, MICRO, or Computer Architecture Letters.

<details>
<summary><strong>📋 Tentative Paper Outline (20-25 pages)</strong></summary>

**"Agentic AI for Computer Systems Design: A Holistic Cross-Stack Perspective"**

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

**4. Agentic AI for Software Systems** (3-4 pages)
- Code generation, optimization, and performance engineering
- *Team Focus: Software vertical*

**5. Agentic AI for Architecture Design** (3-4 pages)  
- Performance prediction, design space exploration, and accelerator design
- *Team Focus: Architecture vertical*

**6. Agentic AI for Physical Implementation** (3-4 pages)
- RTL synthesis, placement & routing, and verification
- *Team Focus: EDA vertical*

**7. Cross-Stack Integration & Future Directions** (2-3 pages)
- Methodological connections and system-level insights
- Research gaps and opportunities

**8. Conclusion** (1 page)
- Summary of key findings and impact

</details>

### Project Structure & Timeline

**Survey Paper Pipeline**: The project follows a structured pipeline that aligns with course learning phases, allowing students to research topics as they learn them in class.

<div class="mermaid">
flowchart TD
    A["Week 1-2: Course Setup<br/>Group Formation"] --> B["AI for Software<br/>(3-5 students per group)"]
    A --> C["AI for Architecture<br/>(3-5 students per group)"]
    A --> D["AI for Chip Design<br/>(3-5 students per group)"]
    
    B --> F1["📋 Checkpoint 1: Literature Survey"]
    C --> F2["📋 Checkpoint 1: Literature Survey"]
    D --> F3["📋 Checkpoint 1: Literature Survey"]
    
    F1 --> G1["📊 Checkpoint 2: Data-Driven Exercise"]
    F2 --> G2["📊 Checkpoint 2: Data-Driven Exercise"]
    F3 --> G3["📊 Checkpoint 2: Data-Driven Exercise"]
    
    G1 --> H1["📖 Checkpoint 3: First Draft"]
    G2 --> H2["📖 Checkpoint 3: First Draft"]
    G3 --> H3["📖 Checkpoint 3: First Draft"]
    
    H1 --> I["🎯 Final Integration"]
    H2 --> I
    H3 --> I
    
    I --> J["🎯 Dec 1: Final Presentations<br/>Complete Survey Paper"]
    
    style F1 fill:#e1f5fe
    style F2 fill:#e1f5fe
    style F3 fill:#e1f5fe
    style G1 fill:#f3e5f5
    style G2 fill:#f3e5f5
    style G3 fill:#f3e5f5
    style H1 fill:#e8f5e8
    style H2 fill:#e8f5e8
    style H3 fill:#e8f5e8
    style J fill:#fff3e0
</div>


### Survey Structure: Cross-Stack Sections (3-5 students per group)

**The paper will examine agentic AI methodologies across three abstraction levels, with emphasis on cross-cutting themes and system-level insights:**

**Section 1: AI Agents for Software Systems**
- Code generation, optimization, and performance engineering
- Cross-cutting theme: *Agent-driven software-hardware co-optimization*

**Section 2: AI Agents for Architecture Design**  
- Performance prediction, design space exploration, and accelerator design
- Cross-cutting theme: *Multi-objective optimization and design trade-offs*

**Section 3: AI Agents for Physical Implementation**
- RTL synthesis, placement & routing, and verification
- Cross-cutting theme: *Constraint satisfaction and manufacturing considerations*

**Section 4: Cross-Stack Integration & Future Directions**
- Methodological connections, API design, and holistic system design
- Cross-cutting theme: *End-to-end agentic design workflows*

**Section 5: Evaluation Frameworks & Benchmarking**
- Comparative analysis, metrics, and reproducibility
- Cross-cutting theme: *Standardized evaluation across abstraction levels*

### Data-Driven Analysis Requirements

**Every student must contribute quantitative analysis and data visualization:**

**Required Analytical Contributions (flexible based on section needs):**
- **Systematic data extraction** from papers, GitHub repos, benchmark leaderboards, and conference proceedings
- **Synthesis tables and figures** that reveal patterns not visible in individual papers
- **Trend analysis and timeline visualizations** showing technique evolution and adoption
- **Performance landscape mapping** using aggregated results from multiple sources
- **Gap identification** through systematic coverage analysis of evaluation spaces

**Technical Work Guidelines:**
- **Data-driven approach**: Every major claim supported by tables, figures, or analysis
- **Code for analysis**: Scripts for data processing, visualization, and statistical analysis
- **Reproducible methodology**: Documented approach for extracting and analyzing data
- **Visual synthesis**: Charts, graphs, and tables that reveal new insights from existing data

**Concrete Examples of Data-Driven Contributions:**

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

**Integration Section:**
- Cross-stack methodology taxonomy with quantitative adoption analysis
- Timeline of end-to-end design flow evolution
- Gap analysis matrix showing unexplored cross-layer optimization opportunities

**The key insight**: Students extract, synthesize, and visualize data that already exists in the literature but hasn't been systematically compared or analyzed across the full stack.

### Three-Checkpoint System

{: .checkpoint-list}
#### 📋 Checkpoint 1: Foundation & Technical Planning (October 1)
**Who**: All students working on software-related sections  
**Deliverable**: Literature foundation + technical work proposal (4-5 pages)  
**Requirements**:
- 20-25 key papers identified with data extraction plan
- Cross-cutting themes and quantitative analysis opportunities identified
- Detailed plan for tables/figures to be generated from existing data
- Methodology for data collection and analysis documented

{: .checkpoint-list}
#### 📊 Checkpoint 2: Technical Results & Draft Analysis (October 29)
**Who**: All students working on architecture-related sections  
**Deliverable**: Technical results + draft survey sections (10-12 pages)  
**Requirements**:
- Completed data analysis with generated tables and figures
- Comparative analysis revealing new insights from existing literature
- Draft survey sections with quantitative findings integrated
- Cross-references and data connections to other sections identified

{: .checkpoint-list}
#### 📖 Checkpoint 3: Integrated Survey Paper (November 19)
**Who**: All students working on chip design & integration sections  
**Deliverable**: Complete integrated survey paper (18-22 pages)  
**Requirements**:
- Comprehensive cross-stack analysis with data-driven insights
- Quantitative analysis seamlessly integrated into narrative
- Cross-cutting themes supported by comparative data and visualizations
- Future research directions based on identified gaps and trends
- Publication-ready quality with reproducible analysis methodology

{: .checkpoint-list}
#### 🎯 Final Presentations (December 1)
**Who**: All groups  
**Deliverable**: 15-minute presentation + Q&A  
**Requirements**:
- Clear communication of survey findings
- Novel insights and research contributions
- Future directions and open problems
- Professional presentation quality

### Execution Process

**Section Assignment (Week 2):**
- Students rank preferences for survey sections (1-5)
- Instructor assigns students balancing technical backgrounds and interests
- Teams of 3-5 students per group for comprehensive coverage

**Technical Work Planning Meeting (Week 3):**
- 45-minute meeting with instructor and TAs per team
- Discuss section scope, cross-cutting themes, and technical work plans
- Approve programming/analysis projects and methodologies
- Establish individual technical responsibilities and integration strategy

**Cross-Team Coordination:**
- **Weekly integration meetings** to ensure coherent narrative
- **Shared technical infrastructure** (code repositories, data formats)
- **Cross-referencing protocols** to highlight connections between sections

**Ongoing Support:**
- **Bi-weekly check-ins** with TAs during office hours
- **Peer review sessions** between groups working on related topics
- **Cross-group presentations** to share insights and get feedback
- **Mandatory progress updates** at each checkpoint

### Assessment Rubric

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

**Quality Assurance Mechanisms:**
- **Data analysis review sessions** with TAs to validate methodology
- **Cross-team presentations** of key findings and visualizations
- **Faculty review of analytical contributions** before survey integration
- **External reviewer feedback** on final paper before submission

### Survey Paper Standards

**Analytical Rigor:**
- **Data-Driven Insights**: All major claims supported by tables, figures, or quantitative analysis
- **Comparative Analysis**: Systematic comparisons revealing trends and gaps across literature
- **Cross-Stack Synthesis**: Quantitative findings that connect insights across abstraction levels

**Survey Quality:**
- **Comprehensive Coverage**: Systematic review of 100+ papers across all areas (2020-2025)
- **Novel Cross-Cutting Analysis**: Identification of methodological connections across stack
- **Original Technical Insights**: New benchmarking results, comparative analysis, or unified frameworks
- **Rich Visualizations**: Technical diagrams, performance comparisons, and taxonomy figures
- **Actionable Future Directions**: 5-7 concrete research opportunities with technical justification

**Publication Standards:**
- **Venue Target**: ISCA, MICRO, Computer Architecture Letters, or ACM Computing Surveys
- **Length**: 18-22 pages with comprehensive technical appendix
- **Reproducibility Package**: Complete code repository with documentation and datasets

---

## Course Policies

### Late Work
- Survey paper checkpoints: 10% penalty per day late
- Survey paper project: Extensions require advance notice from entire team
- Discussion leadership: Must reschedule in advance

### Collaboration
- **Survey paper checkpoints**: Individual work within collaborative project framework
- **Survey paper project**: Required group work (entire class collaboration)
- **Discussion leadership**: Pairs allowed and encouraged

---

