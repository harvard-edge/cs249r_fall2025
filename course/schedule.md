---
layout: default
---

# Schedule & Readings

## Course Schedule

*"The goal isn't to read everything, but to read the right things deeply and connect them meaningfully."*

**📖 Reading Reflection Due**: Before each class session  

**📝 [Paper Presentation Signups](https://docs.google.com/spreadsheets/d/1k3P8j3hO-tmLXfk2zjROkHvXUi97LoAwszLcLheCoyQ/edit?gid=0#gid=0)** — Sign up for your paper presentations here!

---

### The Thematic Flow:
1. **AI for Software**: AI systems understand *what* needs to be computed efficiently
2. **AI for Architecture**: AI agents design *how* to compute it efficiently in hardware  
3. **AI for Chip Design**: AI tools implement the architecture *physically* in silicon

---

## Table of Contents

**📚 Quick Navigation:**

### Introduction & Foundations
- [Week 1 - Course Introduction & Logistics](#week-1---course-introduction--logistics)
- [Week 2 - Architecture 2.0 & Foundations](#week-2---architecture-20--foundations)

### Phase 1: AI for Software
- [Week 3 - Code Generation & Software Engineering](#week-3---code-generation--software-engineering)
- [Week 4 - Performance Engineering & Code Optimization](#week-4---performance-engineering--code-optimization)
- [Week 5 - GPU Kernels & Parallel Programming](#week-5---gpu-kernels--parallel-programming)
- [Week 6 - Distributed Systems Integration](#week-6---distributed-systems-integration)

### Phase 2: AI for Architecture
- [Week 7 - Performance Prediction & Design Space Exploration](#week-7---performance-prediction--design-space-exploration)
- [Week 8 - Hardware Accelerators & AI Mappings](#week-8---hardware-accelerators--ai-mappings)
- [Week 9 - Memory Systems & Data Management](#week-9---memory-systems--data-management)
- [Week 10 - LLM Systems & AI Workload Scheduling](#week-10---llm-systems--ai-workload-scheduling)

### Phase 3: AI for Chip Design
- [Week 11 - RTL Design & Logic Synthesis](#week-11---rtl-design--logic-synthesis)
- [Week 12 - Physical Design & Layout](#week-12---physical-design--layout)
- [Week 13 - Verification & Advanced Chip Design](#week-13---verification--advanced-chip-design)

---

## Week 1 - Course Introduction & Logistics
**Week of September 1 (first class: September 3)**

Course overview, logistics, syllabus, and introduction to the vision of AI-driven computing stack design.

**📋 Required Reading:**
- [Architecture 2.0: Foundations of Artificial Intelligence Agents for Modern Computer System Design](https://www.computer.org/csdl/magazine/co/2025/02/10857820/23VCdDhsEAo)
- [Architecture 2.0: Why Computer Architects Need a Data-Centric AI Gymnasium](https://www.sigarch.org/architecture-2-0-why-computer-architects-need-a-data-centric-ai-gymnasium/)

**📚 Background Reading:** [Ch 1. Intro](https://www.mlsysbook.ai/contents/core/introduction/introduction) • [Ch 2. ML Systems](https://www.mlsysbook.ai/contents/core/ml_systems/ml_systems)

**📓 Class Notes**: [September 3 - Course Introduction](../course/notes#september-3---course-introduction--architecture-20) • **Materials**: [Slides](https://github.com/harvard-edge/cs249r_fall2025/releases/download/sep-3/CS249r_.Architecture.2.0.-.Part.1.pdf) • [All materials](https://github.com/harvard-edge/cs249r_fall2025/releases/tag/sep-3)

**✍️ Blog Post**: [Week 1: The End of an Era, The Dawn of Architecture 2.0](/cs249r_fall2025/blog/2024/09/03/week-1-architecture-2-0/)

## Week 2 - Architecture 2.0 & Foundations
**Week of September 8**

Introduction to Architecture 2.0 and the paradigm shift from human-designed heuristics to agentic design methodologies. Introduction to datasets and survey paper methodology.


**📋 Main Papers:**
- [QuArch: A Question-Answering Dataset for AI Agents in Computer Architecture](https://arxiv.org/abs/2501.01892)
- [A Computer Architect's Guide to Designing Abstractions for Intelligent Systems](https://www.sigarch.org/a-computer-architects-guide-to-designing-abstractions-for-intelligent-systems/)

**📖 Supplemental Reading:**
- [The Deep Learning Revolution and Its Implications for Computer Architecture and Chip Design](https://arxiv.org/abs/1911.05289)

**📚 Background Reading:** [Ch 3. DL Primer](https://www.mlsysbook.ai/contents/core/dl_primer/dl_primer) • [Ch 4. DNN Arch](https://www.mlsysbook.ai/contents/core/dnn_architectures/dnn_architectures)

**✍️ Blog Post**: [Week 2: The Fundamental Challenges Nobody Talks About](/cs249r_fall2025/blog/2024/09/08/week-2-fundamental-challenges/)

---

# Phase 1: AI for Software {#phase-1-ai-for-software}
*AI systems understand what needs to be computed efficiently*

## Week 3 - Code Generation & Software Engineering
**Week of September 15**

*Why are we studying this? Code generation is the most accessible entry point for AI in systems - it's where LLMs have shown dramatic success, but also where we can clearly see the gap between "impressive demos" and "production-ready tools." This week examines: How do we evaluate whether AI can actually replace human programmers? What does it mean for code to be "correct" vs. "optimal"? How do we move from toy problems to real software engineering workflows?*

**🎤 Guest Speaker(s)**: Ofir Press (Princeton, Postdoc)

*Bio: Ofir Press is a Princeton postdoctoral researcher focused on large language models for code and evaluation, and is a creator of SWE-bench and SWE-agent.*

**🎯 Main Papers:**
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/pdf/2310.06770.pdf)
- [Competition-Level Code Generation with AlphaCode](https://arxiv.org/pdf/2203.07814.pdf)

**📖 Supplemental Reading:**
- [CodeBERT: A Pre-Trained Model for Programming and Natural Languages](https://arxiv.org/pdf/2002.08155.pdf)
- [Code Llama: Open Foundation Models for Code](https://arxiv.org/pdf/2308.12950.pdf)
- [AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation](https://arxiv.org/pdf/2312.13010.pdf)
- [code2vec: Learning Distributed Representations of Code](https://arxiv.org/pdf/1803.09473.pdf)

**📚 Background Reading:** [Ch 6. AI Frameworks](https://www.mlsysbook.ai/contents/core/frameworks/frameworks) • [Ch 5. Data Engr](https://www.mlsysbook.ai/contents/core/data_engineering/data_engineering.html)

## Week 4 - Performance Engineering & Code Optimization
**Week of September 22**

*Why are we studying this? Moving beyond correctness to performance requires understanding both algorithmic complexity and system behavior. This week explores: Can AI learn the subtle performance optimizations that expert programmers use? How do we teach machines to reason about cache behavior, instruction-level parallelism, and memory access patterns? What's the difference between micro-optimizations and architectural improvements?*

**🎤 Guest Speaker(s)**: Amir Yazdanbaksh (Google DeepMind, Research Scientist)

*Bio: Amir Yazdanbaksh is a research scientist at Google DeepMind working at the intersection of intelligent systems and computer architecture, with a focus on designing abstractions that enable AI-driven systems.*

**🎯 Main Papers:**
- [ECO: An LLM-Driven Efficient Code Optimizer for Warehouse Scale Computers](https://arxiv.org/pdf/2503.15669.pdf)
- [Learning Performance-Improving Code Edits](https://arxiv.org/pdf/2302.07867.pdf)

**📖 Supplemental Reading:**
- [Compiler-R1: Towards Agentic Compiler Auto-tuning with Reinforcement Learning](https://arxiv.org/pdf/2506.15701.pdf)
- [Ithemal: Accurate, Portable and Fast Basic Block Throughput Estimation](https://arxiv.org/pdf/1808.07412.pdf)
- [CompilerGym: Robust, Performant Compiler Optimization Environments for AI Research](https://arxiv.org/pdf/2109.08267.pdf)
- [MLIR: A Compiler Infrastructure for the End of Moore's Law](https://arxiv.org/pdf/2002.11054.pdf)
- [Learning to Optimize Tensor Programs](https://arxiv.org/pdf/1805.08166.pdf)

**📚 Background Reading:** [Ch 7. Efficient AI](https://www.mlsysbook.ai/contents/core/efficient_ai/efficient_ai) • [Ch 8. Model Opt](https://www.mlsysbook.ai/contents/core/model_optimizations/model_optimizations)

## Week 5 - GPU Kernels & Parallel Programming
**Week of September 29**

*Why are we studying this? GPU kernel optimization sits at the intersection of domain expertise and automated optimization - a space too complex for pure heuristics but requiring deep hardware understanding. This week explores: Can AI learn hardware-specific optimization strategies that human experts use? How do we benchmark AI systems against decades of hand-tuned libraries? What happens when the optimization space is so large that even experts disagree on "optimal" solutions?*

**🎤 Guest Speaker(s)**: Sasha Rush (Cursor, Researcher)

*Bio: Sasha Rush is a researcher at Cursor and Associate Professor at Cornell Tech working on building and improving language models, especially for code optimization*


**🎯 Main Papers:**
- [KernelBench: Can LLMs Write Efficient GPU Kernels?](https://arxiv.org/pdf/2502.10517.pdf)
- [Kevin: Multi-Turn RL for Generating CUDA Kernels](https://arxiv.org/pdf/2507.11948.pdf)

**📖 Supplemental Reading:**
- [AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms](https://research.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- [Ansor: Generating High-Performance Tensor Programs for Deep Learning](https://arxiv.org/pdf/2006.06762.pdf)
- [Reinforcement Learning for FPGA Placement](https://dl.acm.org/doi/pdf/10.1145/3400302.3415618)

**📚 Background Reading:** [Ch 9. AI Acceleration](https://www.mlsysbook.ai/contents/core/hw_acceleration/hw_acceleration) • [Ch 7. Efficient AI](https://www.mlsysbook.ai/contents/core/efficient_ai/efficient_ai)

## Week 6 - Distributed Systems Integration
**Week of October 6**

*Why are we studying this? Distributed systems are the culmination of software engineering challenges - where code generation, performance optimization, and parallel programming must work together at scale. This week examines: How do we optimize systems where the bottleneck might be network latency, not computation? Can AI learn to co-design algorithms and system architecture? What does "optimal" mean when dealing with failures, load balancing, and resource contention?*

**🎤 Guest Speaker(s)**: Martin Maas (Google DeepMind, Staff Research Scientist)

*Bio: Martin Maas is a Staff Research Scientist at Google DeepMind working on leveraging machine learning to improve runtime systems, operating systems and computer architecture*


**🎯 Main Papers:**
- [COSMIC: Enabling Full-Stack Co-Design and Optimization of Distributed Machine Learning Systems](https://arxiv.org/pdf/2505.15020.pdf)
- [Reinforcement Learning for Datacenter Congestion Control](https://arxiv.org/pdf/2102.09337.pdf)

**📖 Supplemental Reading:**
- [Spatio-Temporal Self-Supervised Learning for Traffic Flow Prediction](https://arxiv.org/pdf/2212.04475.pdf)
- [Remy: TCP ex Machina](https://web.mit.edu/remy/)
- [Learning Scheduling Algorithms for Data Processing Clusters (Decima)](https://arxiv.org/pdf/1810.01963.pdf)
- [Aurora: A Reinforcement Learning Perspective on Internet Congestion Control](https://dl.acm.org/doi/pdf/10.1145/3299729.3312488)

**📚 Background Reading:** [Ch 10. AI Training](https://www.mlsysbook.ai/contents/core/ai_training/ai_training) • [Ch 11. ML Ops](https://www.mlsysbook.ai/contents/core/ops/ops.html)

---

# Phase 2: AI for Architecture {#phase-2-ai-for-architecture}
*AI agents design how to compute efficiently in hardware*

## Week 7 - Performance Prediction & Design Space Exploration
**Week of October 13**

*Why are we studying this? Performance prediction and design space exploration are fundamental to AI-driven architecture design. This week bridges performance modeling with systematic design space navigation. Key questions: How do we model complex interactions between architectural components? Can AI systematically explore spaces too large for human analysis? How do we predict performance across different workloads and design points? What architectural insights can emerge from data that human designers might miss?*

**🎤 Guest Speaker(s)**: Suvinay Subramanian (Google DeepMind, Staff Software Engineer)

*Bio: Suvinay Subramanian is a Staff Software at Google working on designing and optimizing the performance of specialized hardware-accelerator systems (TPUs) for AI (LLMs, Recommendation Models)*


**🎯 Main Papers:**
- [Concorde: Fast and Accurate CPU Performance Modeling with Compositional Analytical-ML Fusion](https://arxiv.org/pdf/2503.23076.pdf)
- [ArchGym: An Open-Source Gymnasium for Machine Learning Assisted Architecture Design](https://arxiv.org/pdf/2306.08888.pdf)
- [Multi-Agent Reinforcement Learning for Microprocessor Design Space Exploration](https://arxiv.org/pdf/2211.16385.pdf)

**📚 Background Reading:** [Ch 12. Benchmarking AI](https://www.mlsysbook.ai/contents/core/benchmarking_ai/benchmarking_ai)

**✍️ Blog Post**: [Week 7: The Tacit Knowledge Problem - How AI Agents Learn What Architects Never Wrote Down](/cs249r_fall2025/blog/2024/10/15/tacit-knowledge-architecture/)

**📖 Supplemental Reading:**
- [DNNPerf: Runtime Performance Prediction for Deep Learning Models with Graph Neural Networks](https://ieeexplore.ieee.org/abstract/document/10172674?casa_token=G4jLZfZNu70AAAAA:ApmDhwWk_UAxbhY1TIwWYlrw6gddXvI06q49dHSIKsQ5jj7LJSnbv9DP4UHSk5PuLyAJwYk)
- [NeuSight: Forecasting GPU Performance for Deep Learning Training and Inference](https://www.microsoft.com/en-us/research/uploads/prod/2024/05/NeuSight.pdf)
- [Practical Design Space Exploration (HyperMapper 2.0)](https://arxiv.org/pdf/1810.05236.pdf)
- [AutoDSE: Enabling Software Programmers to Design Efficient FPGA Accelerators](https://arxiv.org/pdf/2009.14381.pdf)
- [Bayesian Optimization for Accelerator Design Space Exploration](https://proceedings.neurips.cc/paper_files/paper/2021/file/c59bdc99ccffe8d088b3c67cd7f6e5db-Paper.pdf)

## Week 8 - Hardware Accelerators & AI Mappings
**Week of October 20**

*Why are we studying this? Accelerator design is the ultimate co-design challenge - optimizing both the hardware architecture and the mapping of computations onto that hardware. This week explores: How do we jointly optimize dataflow, memory hierarchy, and compute units? Can AI learn the complex trade-offs between energy, performance, and area? What happens when the target workload is itself changing rapidly (like evolving DNN architectures)?*

**🎤 Guest Speaker(s)**: Jenny Huang (Nvidia, Research Scientist)

*Bio: Jenny Huang is a research scientist at Nvidia working on GPU architecture with the computer architecture research group. Her research focuses on accelerated computing and the co-optimization of algorithm, hardware, and mappings.*

**🎯 Main Papers:**
- [DOSA: Differentiable Model-Based One-Loop Search for DNN Accelerators](https://dl.acm.org/doi/abs/10.1145/3613424.3623797)
- [Learning to Optimize Tensor Programs (AutoTVM)](https://arxiv.org/pdf/1805.08166.pdf)

**📚 Background Reading:** [Ch 9. AI Acceleration](https://www.mlsysbook.ai/contents/core/hw_acceleration/hw_acceleration) • [Ch 8. Model Opt](https://www.mlsysbook.ai/contents/core/model_optimizations/model_optimizations)

**📖 Supplemental Reading:**
- [Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks](https://arxiv.org/pdf/1606.07480.pdf)
- [In-Datacenter Performance Analysis of a Tensor Processing Unit](https://arxiv.org/pdf/1704.04760.pdf)
- [SCNN: An Accelerator for Compressed-sparse Convolutional Neural Networks](https://arxiv.org/pdf/1708.04485.pdf)
- [MAERI: Enabling Flexible Dataflow Mapping over DNN Accelerators via Reconfigurable Interconnects](https://dl.acm.org/doi/pdf/10.1145/3296957.3173176)
- [Understanding Reuse, Performance, and Hardware Cost of DNN Dataflows: A Data-Centric Approach Using MAESTRO](https://arxiv.org/pdf/1805.02566.pdf)
- [Timeloop: A Systematic Approach to DNN Accelerator Evaluation](https://ieeexplore.ieee.org/document/8686236)

## Week 9 - Memory Systems & Data Management
**Week of October 27**

*Why are we studying this? Memory hierarchy design is where the theoretical meets the practical - where algorithmic access patterns meet physical constraints of latency, bandwidth, and energy. This week examines: Can AI learn to predict and optimize for complex memory access patterns? How do we design memory systems for workloads we can't fully characterize? What's the relationship between data structure design and memory hierarchy optimization?*

**🎤 Guest Speaker(s)**: Milad Hashemi (Google, Research Scientist)

*Bio: Milad Hashemi is a research scientist at Google working on the ML, Systems, and Cloud AI team.*

**🎯 Main Papers:**
- [Learning Memory Access Patterns](https://arxiv.org/pdf/1803.02329.pdf)
- [The Case for Learned Index Structures](https://arxiv.org/pdf/1712.01208.pdf)

**📚 Background Reading:** [Ch 5. Data Engr](https://www.mlsysbook.ai/contents/core/data_engineering/data_engineering.html) • [Ch 2. ML Systems](https://www.mlsysbook.ai/contents/core/ml_systems/ml_systems)

**📖 Supplemental Reading:**
- [ALEX: An Updatable Adaptive Learned Index](https://arxiv.org/pdf/1905.08898.pdf)
- [Learning-based Memory Allocation for C++ Server Workloads](https://research.google/pubs/pub49008/)
- [Designing a Cost-Effective Cache Replacement Policy Using Machine Learning](https://research.google/pubs/pub46599/)
- [Long Short-Term Memory (LSTM) Based Hardware Prefetcher](https://dl.acm.org/doi/abs/10.1145/3132402.3132405?casa_token=7OUJuN1RTbEAAAAA:HcAyXtX_RrbKn_L-SxPuriHksoJkiahI9BOtPg4KvLxM4h5JzzWcb64NZMK_a1LOWoBJqJMNRwU)
- [Lightweight ML-based Runtime Prefetcher Selection on Many-core Platforms](https://arxiv.org/pdf/2307.08635.pdf)

## Week 10 - LLM Systems & AI Workload Scheduling
**Week of November 3**

*Why are we studying this? AI workloads are a new class of computational patterns that challenge traditional system design assumptions. This week explores: How do we optimize systems for workloads that are themselves AI-driven? What new scheduling challenges emerge with transformer architectures and attention mechanisms? Can we co-design the AI algorithms and the systems that run them?*

**🎤 Guest Speaker(s)**: Esha Choukse (Microsoft Azure Research, Principal Researcher)

*Bio: Esha Choukse is a Principal Researcher in the Azure Research Systems team. She leads the efficient AI project that optimizes the GenAI workloads and systems for efficiency and sustainability.*

**🎯 Main Papers:**
- [Efficient LLM Scheduling by Learning to Rank](https://arxiv.org/pdf/2408.15792.pdf)
- [Performance Prediction for Large Systems via Text-to-Text Regression](https://arxiv.org/pdf/2506.21718.pdf)

**📚 Background Reading:** [Ch 10. AI Training](https://www.mlsysbook.ai/contents/core/ai_training/ai_training) • [Ch 11. ML Ops](https://www.mlsysbook.ai/contents/core/ops/ops.html)

**📖 Supplemental Reading:**
- [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/pdf/1611.01578.pdf)
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/pdf/2309.06180.pdf)
- [Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve](https://arxiv.org/pdf/2403.02310.pdf)
- [S-LoRA: Serving Thousands of Concurrent LoRA Adapters](https://arxiv.org/pdf/2311.03285.pdf)

---

# Phase 3: AI for Chip Design {#phase-3-ai-for-chip-design}
*AI tools implement the architecture physically in silicon*

## Week 11 - RTL Design & Logic Synthesis
**Week of November 10**

*Why are we studying this? RTL design and logic synthesis represent the transition from architectural intent to physical implementation. This week examines: Can AI learn the complex relationships between high-level hardware descriptions and optimized gate-level implementations? How do we teach machines to reason about timing, power, and area trade-offs? What does it mean for AI to "understand" hardware design languages?*

**🎤 Guest Speaker(s)**: Mark Ren (Nvidia, Director of Design Automation Research)

*Bio: Mark Ren leads Design Automation Research at Nvidia. His research interest is in AI for chip design and GPU-acceleration EDA.*

**🎯 Main Papers:**
- [Comprehensive Verilog Design Problems: A Next-Generation Benchmark Dataset for Evaluating Large Language Models and Agents on RTL Design and Verification](https://arxiv.org/pdf/2506.14074.pdf)
- [Make Every Move Count: LLM-based High-Quality RTL Code Generation Using MCTS](https://arxiv.org/pdf/2402.03289.pdf)

**📚 Background Reading:** [Ch 9. AI Acceleration](https://www.mlsysbook.ai/contents/core/hw_acceleration/hw_acceleration) • [Ch 16. Robust AI](https://www.mlsysbook.ai/contents/core/robust_ai/robust_ai)

**📖 Supplemental Reading:**
- [ChipNeMo: Domain-Adapted LLMs for Chip Design](https://research.nvidia.com/publication/2023-10_chipnemo-domain-adapted-llms-chip-design)
- [ChipAlign: Instruction Alignment in Large Language Models for Chip Design via Geodesic Interpolation](https://arxiv.org/pdf/2412.19819.pdf)
- [DRiLLS: Deep Reinforcement Learning for Logic Synthesis](https://arxiv.org/pdf/1911.04021.pdf)
- [BOiLS: Bayesian Optimisation for Logic Synthesis](https://arxiv.org/pdf/2111.06178.pdf)
- [MasterRTL: A Pre-Synthesis PPA Estimation Framework for Any RTL Design](https://arxiv.org/pdf/2311.08441.pdf)
- [AutoChip: Automating HDL Generation Using LLM Feedback](https://arxiv.org/pdf/2311.04887.pdf)
- [OpenABC-D: A Large-Scale Dataset for Machine Learning Guided Integrated Circuit Synthesis](https://arxiv.org/pdf/2110.11292.pdf)

## Week 12 - Physical Design & Layout
**Week of November 17**

*Why are we studying this? Physical design is the final translation from logical design to manufacturable silicon. This week explores: Can AI learn the complex geometric and electrical constraints of chip layout? How do we optimize for objectives that span multiple scales - from transistor placement to global routing? What happens when AI systems must reason about manufacturing variability and yield?*

**🎤 Guest Speaker(s)**: Richard Ho (OpenAI, Head of Hardware)

*Bio: Richard Ho is Head of Hardware at OpenAI working to co-optimize ML models and the massive compute hardware they run on.*

**🎯 Main Papers:**
- [Chip Placement with Deep Reinforcement Learning](https://arxiv.org/pdf/2004.10746.pdf)
- [DREAMPlace: Deep Learning Toolkit-Enabled GPU Acceleration for Modern VLSI Placement](https://dl.acm.org/doi/abs/10.1145/3316781.3317803?casa_token=mTj9T_lMwI8AAAAA:VBv0lb8QUwPcwcKZMoNWuEpDCC9pjxM9JSrGW9HsAjG3dlCqx9qK9lmEnVt0D_0uxXRHGEqoKTs)

**📚 Background Reading:** [Ch 9. AI Acceleration](https://www.mlsysbook.ai/contents/core/hw_acceleration/hw_acceleration) • [Ch 8. Model Opt](https://www.mlsysbook.ai/contents/core/model_optimizations/model_optimizations)

**📖 Supplemental Reading:**
- [Chip Placement with Deep Reinforcement Learning (Circuit Training)](https://arxiv.org/pdf/2004.10746.pdf)
- [MaskPlace: Fast Chip Placement via Reinforced Visual Representation Learning](https://arxiv.org/pdf/2211.13382.pdf)
- [Learning on distributed traces for data center storage systems](https://proceedings.mlsys.org/paper_files/paper/2021/file/efe0df3ea4a53a04614ad79e7a8a57de-Paper.pdf)

## Week 13 - Verification & Advanced Chip Design
**Week of November 24**

*Why are we studying this? Verification is the ultimate test of whether AI-designed systems actually work. This week examines: How do we verify systems that are too complex for traditional formal methods? Can AI help generate better test cases and assertions? What does it mean to "trust" an AI-designed chip? How do we close the loop from verification results back to design optimization?*

**🎤 Guest Speaker(s)**: Kartik Hegde (ChipStack, Co-Founder)

*Bio: Kartik Hegde is the co-founder of ChipStack, focusing on AI-assisted chip design and verification workflows that accelerate silicon development.*

**🎯 Main Papers:**
- [Using LLMs to Facilitate Formal Verification of RTL](https://arxiv.org/pdf/2309.09437.pdf)
- [SLDB: An End-To-End Heterogeneous System-on-Chip Benchmark Suite for LLM-Aided Design](https://arxiv.org/pdf/2507.06376.pdf)

**📚 Background Reading:** [Ch 16. Robust AI](https://www.mlsysbook.ai/contents/core/robust_ai/robust_ai) • [Ch 17. Responsible AI](https://www.mlsysbook.ai/contents/core/responsible_ai/responsible_ai)

**📖 Supplemental Reading:**
- [AssertLLM: Generating and Evaluating Hardware Verification Assertions from Design Specifications via Multi-LLMs](https://arxiv.org/pdf/2402.00386.pdf)
- [SpecLLM: Exploring Generation and Review of VLSI Design Specification with Large Language Model](https://arxiv.org/pdf/2401.13266.pdf)

*November 26: Thanksgiving Break - No Class*

## Week 13 - Final Projects & Integration

Student project synthesis.

**📝 Projects Due: December 10**

---

*Schedule subject to adjustment based on Guest Speaker(s) availability and emerging research developments.*
