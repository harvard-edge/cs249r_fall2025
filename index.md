---
layout: default
---

# AI Agents for Computer Systems Design

**Harvard University • Fall 2025**  
**CS249r: Special Topics in Edge Computing**

**Instructor:** [Vijay Janapa Reddi](https://profvjreddi.github.io/homepage/)  
**Teaching Assistant:** Arya Tschand <aryatschand@g.harvard.edu>  
**Course Staff:** Zishen Wan and Chenyu Wang  
**Time:** Monday/Wednesday 2:15-3:30 • **Location:** SEC. Room 6.412  
**Office Hours:** Monday 4-5pm (Instructor), TA hours TBD  
**Canvas:** [Course Site](https://canvas.harvard.edu/courses/165367)

---

{: .course-goal}
## Course Goal

For decades, computer systems have been meticulously designed by human experts using intuition, heuristics, and manual optimization. Now we're witnessing a fundamental paradigm shift: AI agents are transforming how we design these systems, from software optimization to chip layout.

This transformation spans the entire computing stack—from AI agents that optimize compiler passes and generate high-performance code, to reinforcement learning agents that automatically design processor microarchitectures, to neural agents that solve chip placement and circuit synthesis. We're moving from human-designed heuristics to autonomous AI agents that can explore solution spaces too large for manual analysis.

**What you'll learn:**
- How AI agents are being applied across the complete computing stack
- Critical analysis of agent-driven design methodologies through systematic literature review
- Research synthesis skills by writing comprehensive survey papers on cutting-edge topics
- How to identify research gaps and propose future directions in AI agents for computer systems design
- Evaluation frameworks for AI agents in software, architecture, and chip design
- Collaborative research skills through team-based survey projects

## What is Computer Systems Design?

**Computer Systems Design** spans the complete computing stack - from software algorithms to physical silicon implementation. It encompasses three critical layers:

- **Software Systems**: Compilers, runtime systems, and algorithms that determine what computations to perform and how to optimize them
- **Computer Architecture**: Processors, memory hierarchies, and system organization that determine how computations are executed
- **Chip Design**: Physical layout, circuit synthesis, and manufacturing processes that implement systems in silicon

Traditional systems design relies on human expertise, heuristics, and manual optimization across vast design spaces with millions of possible configurations at each layer.

**In this course, we explore the complete computing stack:**
1. **AI for Software**: AI systems understand *what* needs to be computed efficiently
2. **AI for Architecture**: AI agents design *how* to compute it efficiently in hardware  
3. **AI for Chip Design**: AI tools implement the architecture *physically* in silicon

## What is Architecture 2.0?

**Architecture 2.0** is the paradigm shift where AI systems automatically explore, evaluate, and optimize design spaces across the entire computing stack. These AI approaches leverage reinforcement learning, neural networks, and Bayesian optimization to:

- **Generate and optimize code** by learning from millions of programs and performance patterns
- **Design compilers** that automatically discover better optimization strategies than human experts
- **Configure processors** by exploring cache sizes, pipeline depths, and execution unit combinations
- **Create accelerators** that co-optimize hardware architecture and algorithm mappings
- **Place and route circuits** by finding optimal chip layouts faster than traditional tools
- **Verify designs** by generating test cases and formal proofs automatically

The goal is to create AI systems that can design better computing systems than human experts across software, architecture, and chip implementation - while exploring design spaces too large for manual analysis.

## Course Overview

This course explores the shift from human-designed heuristics to **autonomous AI agents**. While conventional courses teach you how existing systems work, this seminar explores how **AI agents will design tomorrow's complete computing stack**.

This course is focused on exploring how AI agents enable the specialized, efficient systems that edge computing demands. We'll work hands-on with cutting edge research tools including CompilerGym (software), ArchGym (architecture), and DREAMPlace (chip design).

Students will systematically explore AI agent applications across the complete computing stack - from code generation and compiler optimization, through processor and accelerator design, to chip placement and verification - while identifying the most promising research directions for agent-driven computer systems design.

**Note**: This is a research intensive seminar with limited enrollment, focused on understanding how AI systems design complete computing systems rather than analyzing existing implementations.

## Prerequisites & Expectations

**Required Background:**
- **Computer Systems**: Must have completed courses in computer architecture, compilers, or systems programming. Strong foundation in at least one area: processor design, compiler optimization, or software systems is essential.
- **Machine Learning**: Familiarity with reinforcement learning, neural networks, and optimization methods
- **Programming**: Proficiency in Python and experience with ML frameworks (PyTorch, TensorFlow)

**Recommended:**
- Compilers: Experience with compiler design, optimization passes, and code generation
- Runtime Systems: Understanding of memory management, garbage collection, and system software
- Prior exposure to EDA tools, VLSI design, or compiler optimization
- Research experience in computer architecture, systems, or machine learning
- Familiarity with simulation tools (gem5, Synopsys, Cadence)

**Important**: This course assumes you already understand how computer systems work at some level of the stack. We focus on understanding how AI systems design them, not on learning systems fundamentals. Students should have strong background in at least one area: software systems, computer architecture, or chip design.

This seminar is designed for PhD students and advanced Master's students conducting research in computer architecture, systems, or related areas.

---

## Course Format

This is a **research paper reading seminar** focused on advanced topics at the intersection of AI and computer architecture. The course is structured around:

**📖 Paper-Intensive Learning:**
- Students read 2-3 cutting-edge research papers before each class
- Papers span recent work from top venues (ISCA, MICRO, DAC, MLSys, etc.)
- Focus on understanding methodology, contributions, and limitations

**🎯 Student-Led Presentations & Discussions:**
- Each student presents and leads discussion for assigned papers (20 min presentation + 20 min discussion)
- Presenters prepare critical analysis, discussion questions, and facilitate synthesis
- Flexible timing based on guest speaker availability and class dynamics
- Emphasis on critical analysis rather than passive consumption

**🔬 Research-Oriented Approach:**
- Advanced topics assume strong technical background
- Papers selected for research relevance and methodological innovation
- Goal is to identify research gaps and future opportunities

**📝 Active Participation:**
- Weekly reading reflections (1-2 pages) due before each class
- Group survey paper project synthesizing research across the computing stack
- Individual reflection papers connecting themes to personal research interests

**🔬 Research Project & Assignments:**
- **Group Survey Papers**: Teams of 4-5 students write comprehensive survey papers
- Each group covers one phase: AI for Software, AI for Architecture, or AI for Chip Design
- Mid-semester deliverable: Annotated bibliography + research questions
- Final deliverable: 15-20 page survey paper + presentation
- Goal is to produce publication-quality surveys that advance the field

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

*Last updated: September 3, 2025*
