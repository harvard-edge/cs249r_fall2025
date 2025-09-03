---
layout: default
---

# Schedule & Readings

---

## Course Schedule

*"The goal isn't to read everything, but to read the right things deeply and connect them meaningfully."*

*AI agents designing the complete computing stack - from code to silicon*

**📖 Reading Reflection Due**: Before each class session  


---

### The Thematic Flow:
1. **AI for Software**: AI systems understand *what* needs to be computed efficiently
2. **AI for Architecture**: AI agents design *how* to compute it efficiently in hardware  
3. **AI for Chip Design**: AI tools implement the architecture *physically* in silicon

---

## Table of Contents

**📚 Quick Navigation:**

### Phase 1: AI for Software
- [Week 1 — Course Introduction & Foundations](#week-1--course-introduction--foundations)
- [Week 2 — Code Generation & Software Engineering](#week-2--code-generation--software-engineering)
- [Week 3 — Performance Engineering & Code Optimization](#week-3--performance-engineering--code-optimization)
- [Week 4 — GPU Kernels & Parallel Programming](#week-4--gpu-kernels--parallel-programming)
- [Week 5 — Distributed Systems Integration](#week-5--distributed-systems-integration)

### Phase 2: AI for Architecture
- [Week 6 — Performance Prediction and Design Space Exploration](#week-6--performance-prediction-and-design-space-exploration)
- [Week 7 — Hardware Accelerators & DNN Mappings](#week-7--hardware-accelerators--dnn-mappings)
- [Week 8 — Memory Systems & Data Management](#week-8--memory-systems--data-management)
- [Week 9 — LLM Systems & AI Workload Scheduling](#week-9--llm-systems--ai-workload-scheduling)

### Phase 3: AI for Chip Design
- [Week 10 — RTL Design & Logic Synthesis](#week-10--rtl-design--logic-synthesis)
- [Week 11 — Physical Design & Layout](#week-11--physical-design--layout)
- [Week 12 — Verification & Advanced Chip Design](#week-12--verification--advanced-chip-design)
- [Week 13 — Final Projects & Integration](#week-13--final-projects--integration)

---

## Week 1 — Course Introduction & Foundations
**September 3**

Course overview, vision, and foundational concepts. Introduction to Architecture 2.0 and the paradigm shift from human-designed heuristics to agentic design methodologies.

**📋 Foundational Reading:**
- [Architecture 2.0: Foundations of Artificial Intelligence Agents for Modern Computer System Design](https://www.computer.org/csdl/magazine/co/2025/02/10857820/23VCdDhsEAo)
- [A Computer Architect's Guide to Designing Abstractions for Intelligent Systems](https://www.sigarch.org/a-computer-architects-guide-to-designing-abstractions-for-intelligent-systems/)

---

# Phase 1: AI for Software
*AI systems understand what needs to be computed efficiently*

## Week 2 — Code Generation & Software Engineering
**September 8 & 10**

*Why are we studying this? Code generation is the most accessible entry point for AI in systems - it's where LLMs have shown dramatic success, but also where we can clearly see the gap between "impressive demos" and "production-ready tools." This week examines: How do we evaluate whether AI can actually replace human programmers? What does it mean for code to be "correct" vs. "optimal"? How do we move from toy problems to real software engineering workflows?*

**🎯 Presentation Papers:**
- SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- Competition-Level Code Generation with AlphaCode

**📚 Context & Background:**
- CodeBERT: A Pre-Trained Model for Programming and Natural Languages
- Code Llama: Open Foundation Models for Code
- AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation
- Code2vect: An efficient heterogenous data classifier and nonlinear regression technique

## Week 3 — Performance Engineering & Code Optimization
**September 15 & 17**

*Why are we studying this? Moving beyond correctness to performance requires understanding both algorithmic complexity and system behavior. This week explores: Can AI learn the subtle performance optimizations that expert programmers use? How do we teach machines to reason about cache behavior, instruction-level parallelism, and memory access patterns? What's the difference between micro-optimizations and architectural improvements?*

**🎯 Presentation Papers:**
- ECO: An LLM-Driven Efficient Code Optimizer for Warehouse Scale Computers
- Learning Performance-Improving Code Edits

**📚 Context & Background:**
- Ithemal: Accurate, Portable and Fast Basic Block Throughput Estimation
- CompilerGym: Robust, Performant Compiler Optimization Environments for AI Research
- MLIR: Scaling Compiler Infrastructure for Domain Specific Computation
- Learning to Optimize Tensor Programs

## Week 4 — GPU Kernels & Parallel Programming
**September 22 & 24**

*Why are we studying this? GPU kernel optimization sits at the intersection of domain expertise and automated optimization - a space too complex for pure heuristics but requiring deep hardware understanding. This week explores: Can AI learn hardware-specific optimization strategies that human experts use? How do we benchmark AI systems against decades of hand-tuned libraries? What happens when the optimization space is so large that even experts disagree on "optimal" solutions?*

**🎯 Presentation Papers:**
- KernelBench: Can LLMs Write Efficient GPU Kernels?
- Kevin: Multi-Turn RL for Generating CUDA Kernels

**📚 Context & Background:**
- AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms
- Learning to Optimize Tensor Programs (AutoTVM)
- Ansor: Generating High-Performance Tensor Programs for Deep Learning
- Reinforcement Learning for FPGA Placement

## Week 5 — Distributed Systems Integration
**September 29 & October 1**

*Why are we studying this? Distributed systems are the culmination of software engineering challenges - where code generation, performance optimization, and parallel programming must work together at scale. This week examines: How do we optimize systems where the bottleneck might be network latency, not computation? Can AI learn to co-design algorithms and system architecture? What does "optimal" mean when dealing with failures, load balancing, and resource contention?*

**🎯 Presentation Papers:**
- COSMIC: Enabling Full-Stack Co-Design and Optimization of Distributed Machine Learning Systems
- Reinforcement Learning for Datacenter Congestion Control

**📚 Context & Background:**
- Spatio-Temporal Self-Supervised Learning for Traffic Flow Prediction
- Remy: TCP ex Machina
- Decima: Learning Scheduling Algorithms for Data Processing Clusters
- Aurora: A Reinforcement Learning Perspective on Internet Congestion Control

---

# Phase 2: AI for Architecture
*AI agents design how to compute efficiently in hardware*

## Week 6 — Performance Prediction and Design Space Exploration
**October 6 & 8**

*Why are we studying this? Performance prediction and design space exploration are fundamental to AI-driven architecture design. This week bridges performance modeling with systematic design space navigation. Key questions: How do we model complex interactions between architectural components? Can AI systematically explore spaces too large for human analysis? How do we predict performance across different workloads and design points? What architectural insights can emerge from data that human designers might miss?*

**🎯 Presentation Papers:**
- Concorde: Fast and Accurate CPU Performance Modeling with Compositional Analytical-ML Fusion
- ArchGym: An Open-Source Gymnasium for Machine Learning Assisted Architecture Design

**📚 Context & Background:**
- DNNPerf: Runtime Performance Prediction for Deep Learning Models with Graph Neural Networks
- NeuSight: Forecasting GPU Performance for Deep Learning Training and Inference
- HyperMapper 2.0: Interactive and Adaptive Design Space Exploration for Multi-objective Optimization
- AutoDSE: Enabling Automatic Design Space Exploration for High-Level Synthesis with Machine Learning
- Bayesian Optimization for Accelerator Design Space Exploration

## Week 7 — Hardware Accelerators & DNN Mappings
**October 13 & 15**

*Why are we studying this? Accelerator design is the ultimate co-design challenge - optimizing both the hardware architecture and the mapping of computations onto that hardware. This week explores: How do we jointly optimize dataflow, memory hierarchy, and compute units? Can AI learn the complex trade-offs between energy, performance, and area? What happens when the target workload is itself changing rapidly (like evolving DNN architectures)?*

**🎯 Presentation Papers:**
- DOSA: Differentiable Model-Based One-Loop Search for DNN Accelerators
- Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks

**📚 Context & Background:**
- In-Datacenter Performance Analysis of a Tensor Processing Unit
- SCNN: An Accelerator for Compressed-sparse Convolutional Neural Networks
- MAERI: Enabling Flexible Dataflow Mapping over DNN Accelerators via Reconfigurable Interconnects
- MAESTRO: An Open-source Infrastructure for Modeling Dataflows within Deep Learning Accelerators
- Timeloop: A Systematic Approach to DNN Accelerator Evaluation

## Week 8 — Memory Systems & Data Management
**October 20 & 22**

*Why are we studying this? Memory hierarchy design is where the theoretical meets the practical - where algorithmic access patterns meet physical constraints of latency, bandwidth, and energy. This week examines: Can AI learn to predict and optimize for complex memory access patterns? How do we design memory systems for workloads we can't fully characterize? What's the relationship between data structure design and memory hierarchy optimization?*

**🎯 Presentation Papers:**
- Learning Memory Access Patterns
- The Case for Learned Index Structures

**📚 Context & Background:**
- ALEX: An Updatable Adaptive Learned Index
- Designing a Cost-Effective Cache Replacement Policy Using Machine Learning
- Long Short-Term Memory (LSTM) Based Memory Hardware Prefetcher
- Lightweight ML-based Runtime Prefetcher Selection (2023)

## Week 9 — LLM Systems & AI Workload Scheduling
**October 27 & 29**

*Why are we studying this? AI workloads are a new class of computational patterns that challenge traditional system design assumptions. This week explores: How do we optimize systems for workloads that are themselves AI-driven? What new scheduling challenges emerge with transformer architectures and attention mechanisms? Can we co-design the AI algorithms and the systems that run them?*

**🎯 Presentation Papers:**
- Efficient LLM Scheduling by Learning to Rank
- Performance Prediction for Large Systems via Text-to-Text Regression

**📚 Context & Background:**
- Efficient Memory Management for Large Language Model Serving with PagedAttention
- Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve
- S-LoRA: Serving Thousands of Concurrent LoRA Adapters

---

# Phase 3: AI for Chip Design
*AI tools implement the architecture physically in silicon*

## Week 10 — RTL Design & Logic Synthesis
**November 3 & 5**

*Why are we studying this? RTL design and logic synthesis represent the transition from architectural intent to physical implementation. This week examines: Can AI learn the complex relationships between high-level hardware descriptions and optimized gate-level implementations? How do we teach machines to reason about timing, power, and area trade-offs? What does it mean for AI to "understand" hardware design languages?*

**🎯 Presentation Papers:**
- VerilongEval/CVDP
- Make every move count: LLM-based high-quality RTL code generation using MCTS

**📚 Context & Background:**
- DRiLLS: Deep Reinforcement Learning for Logic Synthesis (ASP-DAC'20)
- BOiLS: Bayesian Optimisation for Logic Synthesis
- MasterRTL: Pre-Synthesis PPA Estimation for RTL Designs (ICCAD'22/TCAD'24)
- AutoChip: Automating HDL Generation Using LLM Feedback (2023–24)
- OpenABC-D: A Large-Scale Dataset for Machine Learning Guided Integrated Circuit Synthesis

## Week 11 — Physical Design & Layout
**November 10 & 12**

*Why are we studying this? Physical design is the final translation from logical design to manufacturable silicon. This week explores: Can AI learn the complex geometric and electrical constraints of chip layout? How do we optimize for objectives that span multiple scales - from transistor placement to global routing? What happens when AI systems must reason about manufacturing variability and yield?*

**🎯 Presentation Papers:**
- Chip Placement with Deep Reinforcement Learning
- DREAMPlace: Deep Learning Toolkit-Enabled GPU Acceleration for VLSI Placement

**📚 Context & Background:**
- Chip Placement with Deep Reinforcement Learning (Circuit Training)
- MaskPlace: Fast Chip Placement via Reinforcement Learning
- Learning on distributed traces for data center storage systems (routing optimization perspective)

## Week 12 — Verification & Advanced Chip Design
**November 17**

*Why are we studying this? Verification is the ultimate test of whether AI-designed systems actually work. This week examines: How do we verify systems that are too complex for traditional formal methods? Can AI help generate better test cases and assertions? What does it mean to "trust" an AI-designed chip? How do we close the loop from verification results back to design optimization?*

**🎯 Presentation Papers:**
- AssertionForge: Enhancing Formal Verification Assertion Generation
- SLDB: An End-To-End Heterogeneous System-on-Chip Benchmark Suite for LLM-Aided Design

**📚 Context & Background:**
- AssertLLM (2024)
- SpecLLM: Exploring Generation and Review of Architecture Specifications with Large Language Models (2024)

*November 26: Thanksgiving Break - No Class*

## Week 13 — Final Projects & Integration
**November 24 & December 1**

Student project presentations and course synthesis. Integration of AI techniques across the complete computing stack.

**📝 Projects Due: December 1**

---

## Reading Access

- **Primary Sources**: Papers available through Harvard Library, ACM Digital Library, IEEE Xplore
- **Course Reserves**: Key papers uploaded to course management system
- **Supplemental Materials**: Additional resources linked from course website

## Discussion Format

Each session follows a structured format:
1. **Opening** (10 min): Key takeaways and questions from readings
2. **Deep Dive** (45 min): Structured discussion led by students or instructor  
3. **Matrix Mapping** (15 min): How do these papers fit in our framework?
4. **Synthesis** (5 min): Connections to previous sessions and upcoming topics

---

*Schedule subject to adjustment based on guest speaker availability and emerging research developments.*
