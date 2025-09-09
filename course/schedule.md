---
layout: default
---

# Schedule & Readings

## Course Schedule

*"The goal isn't to read everything, but to read the right things deeply and connect them meaningfully."*

*Autonomous AI agents designing the complete computing stack - from code to silicon*

**📖 Reading Reflection Due**: Before each class session  


---

### The Thematic Flow:
1. **AI for Software**: AI systems understand *what* needs to be computed efficiently
2. **AI for Architecture**: AI agents design *how* to compute it efficiently in hardware  
3. **AI for Chip Design**: AI tools implement the architecture *physically* in silicon

---

## Table of Contents

**📚 Quick Navigation:**

### Introduction & Foundations
- [Week 1 — Course Introduction & Logistics](#week-1--course-introduction--logistics)
- [Week 2 — Architecture 2.0 & Foundations](#week-2--architecture-20--foundations)

### Phase 1: AI for Software
- [Week 3 — Code Generation & Software Engineering](#week-3--code-generation--software-engineering)
- [Week 4 — Performance Engineering & Code Optimization](#week-4--performance-engineering--code-optimization)
- [Week 5 — GPU Kernels & Parallel Programming](#week-5--gpu-kernels--parallel-programming)
- [Week 6 — Distributed Systems Integration](#week-6--distributed-systems-integration)

### Phase 2: AI for Architecture
- [Week 7 — Performance Prediction and Design Space Exploration](#week-7--performance-prediction-and-design-space-exploration)
- [Week 8 — Hardware Accelerators & AI Mappings](#week-8--hardware-accelerators--ai-mappings)
- [Week 9 — Memory Systems & Data Management](#week-9--memory-systems--data-management)
- [Week 10 — LLM Systems & AI Workload Scheduling](#week-10--llm-systems--ai-workload-scheduling)

### Phase 3: AI for Chip Design
- [Week 11 — RTL Design & Logic Synthesis](#week-11--rtl-design--logic-synthesis)
- [Week 12 — Physical Design & Layout](#week-12--physical-design--layout)
- [Week 13 — Verification & Advanced Chip Design](#week-13--verification--advanced-chip-design)

---

## Week 1 — Course Introduction & Logistics
**Week of September 1 (first class: September 3)**

Course overview, logistics, syllabus, and introduction to the vision of AI-driven computing stack design.

**📋 Foundational Reading:**
- [Architecture 2.0: Foundations of Artificial Intelligence Agents for Modern Computer System Design](https://www.computer.org/csdl/magazine/co/2025/02/10857820/23VCdDhsEAo)
- [Architecture 2.0: Why Computer Architects Need a Data-Centric AI Gymnasium](https://www.sigarch.org/architecture-2-0-why-computer-architects-need-a-data-centric-ai-gymnasium/)

**🎤 Guest Speaker(s)**: TBD

**📓 Class Notes**: [September 3 - Course Introduction](../course/notes#september-3---course-introduction--architecture-20) • **Materials**: [Slides](https://github.com/harvard-edge/cs249r_fall2025/releases/download/sep-3/CS249r_.Architecture.2.0.-.Part.1.pdf) • [All materials](https://github.com/harvard-edge/cs249r_fall2025/releases/tag/sep-3)

## Week 2 — Architecture 2.0 & Foundations
**Week of September 8**

Introduction to Architecture 2.0 and the paradigm shift from human-designed heuristics to agentic design methodologies. Introduction to datasets and survey paper methodology.

**📋 Foundational Reading:**
- [QuArch: A Question-Answering Dataset for AI Agents in Computer Architecture](https://arxiv.org/abs/2501.01892)
- [A Computer Architect's Guide to Designing Abstractions for Intelligent Systems](https://www.sigarch.org/a-computer-architects-guide-to-designing-abstractions-for-intelligent-systems/)

**📖 Sampling of Related Papers:**
- [The Deep Learning Revolution and Its Implications for Computer Architecture and Chip Design](https://arxiv.org/abs/1911.05289)

---

# Phase 1: AI for Software
*AI systems understand what needs to be computed efficiently*

## Week 3 — Code Generation & Software Engineering
**Week of September 15**

*Why are we studying this? Code generation is the most accessible entry point for AI in systems - it's where LLMs have shown dramatic success, but also where we can clearly see the gap between "impressive demos" and "production-ready tools." This week examines: How do we evaluate whether AI can actually replace human programmers? What does it mean for code to be "correct" vs. "optimal"? How do we move from toy problems to real software engineering workflows?*

**🎯 Main Papers:**
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/pdf/2310.06770.pdf)
- [Competition-Level Code Generation with AlphaCode](https://arxiv.org/pdf/2203.07814.pdf)

**📖 Sampling of Related Papers:**
- [CodeBERT: A Pre-Trained Model for Programming and Natural Languages](https://arxiv.org/pdf/2002.08155.pdf)
- [Code Llama: Open Foundation Models for Code](https://arxiv.org/pdf/2308.12950.pdf)
- [AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation](https://arxiv.org/pdf/2312.13010.pdf)
- [code2vec: Learning Distributed Representations of Code](https://arxiv.org/pdf/1803.09473.pdf)

**🎤 Guest Speaker(s)**: Ofir Press (Author of SWE-bench)

## Week 4 — Performance Engineering & Code Optimization
**Week of September 22**

*Why are we studying this? Moving beyond correctness to performance requires understanding both algorithmic complexity and system behavior. This week explores: Can AI learn the subtle performance optimizations that expert programmers use? How do we teach machines to reason about cache behavior, instruction-level parallelism, and memory access patterns? What's the difference between micro-optimizations and architectural improvements?*

**🎯 Main Papers:**
- [ECO: An LLM-Driven Efficient Code Optimizer for Warehouse Scale Computers](https://arxiv.org/pdf/2410.15736.pdf)
- [Learning Performance-Improving Code Edits](https://arxiv.org/pdf/2302.07867.pdf)

**📖 Sampling of Related Papers:**
- [Compiler-R1: Towards Agentic Compiler Auto-tuning with Reinforcement Learning](https://arxiv.org/pdf/2506.15701.pdf)
- [Ithemal: Accurate, Portable and Fast Basic Block Throughput Estimation](https://arxiv.org/pdf/1808.07412.pdf)
- [CompilerGym: Robust, Performant Compiler Optimization Environments for AI Research](https://arxiv.org/pdf/2109.08267.pdf)
- [MLIR: Scaling Compiler Infrastructure for Domain Specific Computation](https://arxiv.org/pdf/2002.11054.pdf)
- [Learning to Optimize Tensor Programs](https://arxiv.org/pdf/1805.08166.pdf)


**🎤 Guest Speaker(s)**: TBD

## Week 5 — GPU Kernels & Parallel Programming
**Week of September 29**

*Why are we studying this? GPU kernel optimization sits at the intersection of domain expertise and automated optimization - a space too complex for pure heuristics but requiring deep hardware understanding. This week explores: Can AI learn hardware-specific optimization strategies that human experts use? How do we benchmark AI systems against decades of hand-tuned libraries? What happens when the optimization space is so large that even experts disagree on "optimal" solutions?*

**🎯 Main Papers:**
- [KernelBench: Can LLMs Write Efficient GPU Kernels?](https://arxiv.org/pdf/2411.14594.pdf)
- [Kevin: Multi-Turn RL for Generating CUDA Kernels](https://arxiv.org/pdf/2411.16922.pdf)

**📖 Sampling of Related Papers:**
- [AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms](https://research.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- [Ansor: Generating High-Performance Tensor Programs for Deep Learning](https://arxiv.org/pdf/2006.06762.pdf)
- [Reinforcement Learning for FPGA Placement](https://dl.acm.org/doi/pdf/10.1145/3400302.3415618)

**🎤 Guest Speaker(s)**: TBD

## Week 6 — Distributed Systems Integration
**Week of October 6**

*Why are we studying this? Distributed systems are the culmination of software engineering challenges - where code generation, performance optimization, and parallel programming must work together at scale. This week examines: How do we optimize systems where the bottleneck might be network latency, not computation? Can AI learn to co-design algorithms and system architecture? What does "optimal" mean when dealing with failures, load balancing, and resource contention?*

**🎯 Main Papers:**
- [COSMIC: Enabling Full-Stack Co-Design and Optimization of Distributed Machine Learning Systems](https://arxiv.org/pdf/2401.13466.pdf)
- [Reinforcement Learning for Datacenter Congestion Control](https://arxiv.org/pdf/2102.09337.pdf)

**📖 Sampling of Related Papers:**
- [Spatio-Temporal Self-Supervised Learning for Traffic Flow Prediction](https://arxiv.org/pdf/2212.04475.pdf)
- [Remy: TCP ex Machina](https://web.mit.edu/remy/)
- [Decima: Learning Scheduling Algorithms for Data Processing Clusters](https://arxiv.org/pdf/1810.01963.pdf)
- [Aurora: A Reinforcement Learning Perspective on Internet Congestion Control](https://dl.acm.org/doi/pdf/10.1145/3299729.3312488)

**🎤 Guest Speaker(s)**: TBD

---

# Phase 2: AI for Architecture
*AI agents design how to compute efficiently in hardware*

## Week 7 — Performance Prediction & Design Space Exploration
**Week of October 13**

*Why are we studying this? Performance prediction and design space exploration are fundamental to AI-driven architecture design. This week bridges performance modeling with systematic design space navigation. Key questions: How do we model complex interactions between architectural components? Can AI systematically explore spaces too large for human analysis? How do we predict performance across different workloads and design points? What architectural insights can emerge from data that human designers might miss?*

**🎯 Main Papers:**
- [Concorde: Fast and Accurate CPU Performance Modeling with Compositional Analytical-ML Fusion](https://arxiv.org/pdf/2410.06603.pdf)
- [ArchGym: An Open-Source Gymnasium for Machine Learning Assisted Architecture Design](https://arxiv.org/pdf/2206.08515.pdf)
- [Multi-Agent Reinforcement Learning for Microprocessor Design Space Exploration](https://arxiv.org/pdf/2211.16385.pdf)

**📖 Sampling of Related Papers:**
- [DNNPerf: Runtime Performance Prediction for Deep Learning Models with Graph Neural Networks](https://arxiv.org/pdf/2010.11823.pdf)
- [NeuSight: Forecasting GPU Performance for Deep Learning Training and Inference](https://www.microsoft.com/en-us/research/uploads/prod/2024/05/NeuSight.pdf)
- [HyperMapper 2.0: Interactive and Adaptive Design Space Exploration for Multi-objective Optimization](https://arxiv.org/pdf/2105.12826.pdf)
- [AutoDSE: Enabling Automatic Design Space Exploration for High-Level Synthesis with Machine Learning](https://arxiv.org/pdf/2101.04808.pdf)
- [Bayesian Optimization for Accelerator Design Space Exploration](https://proceedings.neurips.cc/paper_files/paper/2021/file/c59bdc99ccffe8d088b3c67cd7f6e5db-Paper.pdf)

**🎤 Guest Speaker(s)**: TBD

## Week 8 — Hardware Accelerators & AI Mappings
**Week of October 20**

*Why are we studying this? Accelerator design is the ultimate co-design challenge - optimizing both the hardware architecture and the mapping of computations onto that hardware. This week explores: How do we jointly optimize dataflow, memory hierarchy, and compute units? Can AI learn the complex trade-offs between energy, performance, and area? What happens when the target workload is itself changing rapidly (like evolving DNN architectures)?*

**🎯 Main Papers:**
- [DOSA: Differentiable Model-Based One-Loop Search for DNN Accelerators](https://arxiv.org/pdf/2403.13677.pdf)
- [Learning to Optimize Tensor Programs (AutoTVM)](https://arxiv.org/pdf/1805.08166.pdf)

**📖 Sampling of Related Papers:**
- [Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks](https://arxiv.org/pdf/1606.07480.pdf)
- [In-Datacenter Performance Analysis of a Tensor Processing Unit](https://arxiv.org/pdf/1704.04760.pdf)
- [SCNN: An Accelerator for Compressed-sparse Convolutional Neural Networks](https://arxiv.org/pdf/1708.04485.pdf)
- [MAERI: Enabling Flexible Dataflow Mapping over DNN Accelerators via Reconfigurable Interconnects](https://dl.acm.org/doi/pdf/10.1145/3296957.3173176)
- [MAESTRO: An Open-source Infrastructure for Modeling Dataflows within Deep Learning Accelerators](https://arxiv.org/pdf/1805.02566.pdf)
- [Timeloop: A Systematic Approach to DNN Accelerator Evaluation](https://ieeexplore.ieee.org/document/8686236)

**🎤 Guest Speaker(s)**: TBD

## Week 9 — Memory Systems & Data Management
**Week of October 27**

*Why are we studying this? Memory hierarchy design is where the theoretical meets the practical - where algorithmic access patterns meet physical constraints of latency, bandwidth, and energy. This week examines: Can AI learn to predict and optimize for complex memory access patterns? How do we design memory systems for workloads we can't fully characterize? What's the relationship between data structure design and memory hierarchy optimization?*

**🎯 Main Papers:**
- [Learning Memory Access Patterns](https://arxiv.org/pdf/1803.02329.pdf)
- [The Case for Learned Index Structures](https://arxiv.org/pdf/1712.01208.pdf)

**📖 Sampling of Related Papers:**
- [ALEX: An Updatable Adaptive Learned Index](https://arxiv.org/pdf/1905.08898.pdf)
- [Learning-based Memory Allocation for C++ Server Workloads](https://research.google/pubs/pub49008/)
- [Designing a Cost-Effective Cache Replacement Policy Using Machine Learning](https://research.google/pubs/pub46599/)
- [Long Short-Term Memory (LSTM) Based Memory Hardware Prefetcher](https://arxiv.org/pdf/1906.08699.pdf)
- [Lightweight ML-based Runtime Prefetcher Selection on Many-core Platforms (2023)](https://arxiv.org/pdf/2307.08635.pdf)

**🎤 Guest Speaker(s)**: TBD

## Week 10 — LLM Systems & AI Workload Scheduling
**Week of November 3**

*Why are we studying this? AI workloads are a new class of computational patterns that challenge traditional system design assumptions. This week explores: How do we optimize systems for workloads that are themselves AI-driven? What new scheduling challenges emerge with transformer architectures and attention mechanisms? Can we co-design the AI algorithms and the systems that run them?*

**🎯 Main Papers:**
- [Efficient LLM Scheduling by Learning to Rank](https://arxiv.org/pdf/2408.15792.pdf)
- [Performance Prediction for Large Systems via Text-to-Text Regression](https://arxiv.org/pdf/2402.13785.pdf)

**📖 Sampling of Related Papers:**
- [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/pdf/1611.01578.pdf)
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/pdf/2309.06180.pdf)
- [Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve](https://arxiv.org/pdf/2403.02310.pdf)
- [S-LoRA: Serving Thousands of Concurrent LoRA Adapters](https://arxiv.org/pdf/2311.03285.pdf)

**🎤 Guest Speaker(s)**: TBD

---

# Phase 3: AI for Chip Design
*AI tools implement the architecture physically in silicon*

## Week 11 — RTL Design & Logic Synthesis
**Week of November 10**

*Why are we studying this? RTL design and logic synthesis represent the transition from architectural intent to physical implementation. This week examines: Can AI learn the complex relationships between high-level hardware descriptions and optimized gate-level implementations? How do we teach machines to reason about timing, power, and area trade-offs? What does it mean for AI to "understand" hardware design languages?*

**🎯 Main Papers:**
- [CVDP: Comprehensive Verilog Design Problems Benchmark](https://arxiv.org/pdf/2506.14074.pdf)
- [Make every move count: LLM-based high-quality RTL code generation using MCTS](https://arxiv.org/pdf/2402.03289.pdf)

**📖 Sampling of Related Papers:**
- [ChipNeMo: Domain-Adapted LLMs for Chip Design](https://research.nvidia.com/publication/2023-10_chipnemo-domain-adapted-llms-chip-design) - NVIDIA's domain-specific LLM for chip design
- [ChipAlign: Instruction Alignment in Large Language Models for Chip Design via Geodesic Interpolation](https://arxiv.org/pdf/2412.19819.pdf)
- [DRiLLS: Deep Reinforcement Learning for Logic Synthesis (ASP-DAC'20)](https://arxiv.org/pdf/1911.04021.pdf)
- [BOiLS: Bayesian Optimisation for Logic Synthesis](https://arxiv.org/pdf/2111.06178.pdf)
- [MasterRTL: Pre-Synthesis PPA Estimation for RTL Designs (ICCAD'22/TCAD'24)](https://arxiv.org/pdf/2211.14348.pdf)
- [AutoChip: Automating HDL Generation Using LLM Feedback (2023–24)](https://arxiv.org/pdf/2311.04887.pdf)
- [OpenABC-D: A Large-Scale Dataset for Machine Learning Guided Integrated Circuit Synthesis](https://arxiv.org/pdf/2110.11292.pdf)


**🎤 Guest Speaker(s)**: TBD

## Week 12 — Physical Design & Layout
**Week of November 17**

*Why are we studying this? Physical design is the final translation from logical design to manufacturable silicon. This week explores: Can AI learn the complex geometric and electrical constraints of chip layout? How do we optimize for objectives that span multiple scales - from transistor placement to global routing? What happens when AI systems must reason about manufacturing variability and yield?*

**🎯 Main Papers:**
- [Chip Placement with Deep Reinforcement Learning](https://arxiv.org/pdf/2004.10746.pdf)
- [DREAMPlace: Deep Learning Toolkit-Enabled GPU Acceleration for VLSI Placement](https://arxiv.org/pdf/1912.10415.pdf)

**📖 Sampling of Related Papers:**
- [Chip Placement with Deep Reinforcement Learning (Circuit Training)](https://arxiv.org/pdf/2004.10746.pdf)
- [MaskPlace: Fast Chip Placement via Reinforcement Learning](https://arxiv.org/pdf/2211.13382.pdf)
- [Learning on distributed traces for data center storage systems (routing optimization perspective)](https://arxiv.org/pdf/2210.14706.pdf)

**🎤 Guest Speaker(s)**: TBD

## Week 13 — Verification & Advanced Chip Design
**Week of November 24**

*Why are we studying this? Verification is the ultimate test of whether AI-designed systems actually work. This week examines: How do we verify systems that are too complex for traditional formal methods? Can AI help generate better test cases and assertions? What does it mean to "trust" an AI-designed chip? How do we close the loop from verification results back to design optimization?*

**🎯 Main Papers:**
- [Using LLMs to Facilitate Formal Verification of RTL](https://arxiv.org/pdf/2309.09437.pdf)
- [SLDB: An End-To-End Heterogeneous System-on-Chip Benchmark Suite for LLM-Aided Design](https://arxiv.org/pdf/2410.15431.pdf)

**📖 Sampling of Related Papers:**
- [AssertLLM: Generating Hardware Verification Assertions from Design Specifications via Multi-LLMs (2024)](https://arxiv.org/pdf/2402.00386.pdf)
- [SpecLLM: Exploring Generation and Review of Architecture Specifications with Large Language Models (2024)](https://arxiv.org/pdf/2402.13990.pdf)

**🎤 Guest Speaker(s)**: TBD

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

---

*Schedule subject to adjustment based on Guest Speaker(s) availability and emerging research developments.*
