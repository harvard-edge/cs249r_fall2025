---
layout: default
---

# Architecture 2.0
## Agentic Approaches to System Design

**Harvard University • Fall 2025**  
**CS249r: Special Topics in Edge Computing**

**Instructor:** [Vijay Janapa Reddi](https://profvjreddi.github.io/homepage/)  
**Teaching Assistant:** Chenyu Wang  
**Time:** Monday/Wednesday [Time TBD] • **Location:** [Room TBD]  
**Office Hours:** [Schedule TBD]

*Note: Course schedule and logistics are subject to confirmation. Likely start date is September 3rd or 4th, 2025.*

---

{: .course-goal}
## Course Goal

For decades, computer systems have been meticulously designed by human experts to enable and accelerate AI workloads. We've optimized processors for neural networks, built specialized accelerators for machine learning, and crafted software stacks to support AI applications. Now we're witnessing a fundamental paradigm shift: AI itself is becoming the architect, designing the very systems that will run future computations.

This transformation spans the entire computing stack—from agentic systems that optimize compiler passes and generate high-performance code, to AI-driven approaches that automatically design processor microarchitectures and explore vast design spaces, to intelligent tools that use machine learning for chip placement and circuit synthesis. We're moving from human-designed heuristics to agentic design methodologies that can explore solution spaces too large for manual analysis.

**What you'll learn:**
- How agentic approaches are being applied across the complete computing stack
- Critical analysis of AI-driven design methodologies versus traditional approaches
- The research landscape and emerging opportunities in agentic system design
- How to identify promising research directions in this rapidly evolving field
- Evaluation frameworks for agentic systems in architecture, compilation, and EDA tools

## What is Computer Architecture?

**Computer Architecture** is the science and art of designing computer systems that efficiently execute computational tasks. It encompasses the design of processors (CPUs, GPUs, accelerators), memory hierarchies, interconnection networks, and the interfaces between hardware and software. Architecture decisions determine how fast programs run, how much power systems consume, and what applications are feasible.

Traditional architecture design relies on human expertise, heuristics, and manual optimization across a vast design space with millions of possible configurations.

**In this course, we explore the complete computing stack:**
1. **AI for Software**: Agents understand *what* needs to be computed efficiently
2. **AI for Architecture**: Agents design *how* to compute it efficiently in hardware  
3. **AI for EDA**: Agents implement the architecture *physically* in silicon

## What are Agentic Approaches to System Design?

**Agentic approaches** represent intelligent, autonomous systems that can automatically explore, evaluate, and optimize system design spaces. These approaches leverage machine learning techniques—reinforcement learning, neural networks, Bayesian optimization—to:

- **Design processors** by automatically configuring cache sizes, pipeline depths, and execution units
- **Optimize compilers** by learning better instruction scheduling and register allocation strategies  
- **Place and route circuits** by finding optimal chip layouts faster than traditional EDA tools
- **Explore design spaces** by intelligently sampling configurations rather than exhaustive search
- **Predict performance** by learning from simulation data to guide design decisions

The goal is to create agentic systems that can design better computing systems than human experts, while exploring design spaces too large for manual analysis.

## Course Overview

**Architecture 2.0** represents the paradigm shift from human-designed heuristics to **agentic design methodologies**. While conventional architecture courses teach you how existing systems work, this seminar explores how **agentic approaches will design tomorrow's systems**.

This course connects directly to **CS249r: Special Topics in Edge Computing** by exploring how AI driven architecture design enables the specialized, efficient systems that edge computing demands. We'll work hands-on with cutting edge research tools including ArchGym, DREAMPlace, and CompilerGym.

Students will systematically explore AI applications across complete design abstraction levels from algorithms to circuits while identifying the most promising research directions for AI driven computer systems design.

**Note**: This is a research intensive seminar with limited enrollment, focused on understanding how AI agents design systems rather than analyzing existing architectures.

## Prerequisites & Expectations

**Required Background:**
- **Computer Architecture**: Must have completed Advanced Computer Architecture and Computer Systems Engineering or equivalent courses. Strong foundation in processor design, memory hierarchy, cache coherence, and system organization is essential.
- **Machine Learning**: Familiarity with reinforcement learning, neural networks, and optimization methods
- **Programming**: Proficiency in Python and experience with ML frameworks (PyTorch, TensorFlow)

**Recommended:**
- Compilers: Experience with compiler design, optimization passes, and code generation
- Runtime Systems: Understanding of memory management, garbage collection, and system software
- Prior exposure to EDA tools, VLSI design, or compiler optimization
- Research experience in computer architecture, systems, or machine learning
- Familiarity with simulation tools (gem5, Synopsys, Cadence)

**Important**: This course assumes you already understand how computer architectures work. We focus on understanding how AI agents design them, not on learning architecture fundamentals. Students without strong architecture background will struggle with the material.

This seminar is designed for PhD students and advanced Master's students conducting research in computer architecture, systems, or related areas.

---

## Course Format

This is a **research paper reading seminar** focused on advanced topics at the intersection of AI and computer architecture. The course is structured around:

**📖 Paper-Intensive Learning:**
- Students read 2-3 cutting-edge research papers before each class
- Papers span recent work from top venues (ISCA, MICRO, DAC, MLSys, etc.)
- Focus on understanding methodology, contributions, and limitations

**🎯 Student-Led Discussions:**
- Each student leads discussion for 1-2 sessions during the semester
- Discussion leaders prepare questions, facilitate debate, and synthesize key insights
- Emphasis on critical analysis rather than passive consumption

**🔬 Research-Oriented Approach:**
- Advanced topics assume strong technical background
- Papers selected for research relevance and methodological innovation
- Goal is to identify research gaps and future opportunities

**📝 Active Participation:**
- Weekly reading reflections (1-2 pages) due before each class
- Final project connecting course themes to your research vision
- Collaborative research matrix mapping the AI-for-architecture landscape

**🔬 Research Project & Assignments:**
- 3-4 progressive assignments building toward **GenAISys**: a unified modular agentic framework
- Each assignment contributes a component to the larger GenAISys ecosystem
- Final project integrates your component into the modular framework
- Goal is to collectively build a comprehensive AI-for-systems research platform

**Note:** This is not a traditional lecture-based course. Students drive the learning through paper analysis, critical discussion, and research synthesis. The course is designed for students who want to produce research outcomes, not just complete coursework.

---

## What Makes This Different from Traditional Architecture Courses?

> *"Traditional architecture courses teach you how architectures work. Architecture 2.0 teaches you how to build AI agents that design architectures."*

### **Traditional Advanced Computer Architecture:**
- Analyze existing processor designs and memory hierarchies
- Understand performance trade-offs in current systems
- Study established design principles and optimization techniques

### **Architecture 2.0 (This Course):**
- Build AI agents that automatically design processors and memory hierarchies
- Create new design methodologies using machine learning
- Develop tools and frameworks for AI-driven architecture exploration

**The Goal**: By the end of this course, you won't just understand how architectures work—you'll know how to build intelligent systems that can design better architectures than humans can.

---

## Contact & Communication

- **Course Email**: TBD
- **Discussion Forum**: TBD
- **Office Hours**: TBD

*Last updated: TBD*
