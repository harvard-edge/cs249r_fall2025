---
layout: default
---

# Class Notes & Insights

*Post-class reflections, key insights, and the "why" behind what we're learning*

---

## 📚 Quick Navigation

| Date | Topic | Key Insight |
|------|-------|-------------|
| [Sep 3](#september-3---course-introduction--architecture-20) | Course Introduction & Architecture 2.0 | Design complexity crisis demands AI agents |
| Sep 8 | Architecture 2.0 & Foundations | *Coming soon* |
| Sep 15 | Code Generation & Software Engineering | *Coming soon* |
| Sep 22 | Performance Engineering & Code Optimization | *Coming soon* |
| Sep 29 | GPU Kernels & Parallel Programming | *Coming soon* |
| Oct 6 | Distributed Systems Integration | *Coming soon* |

---

## September 3 - Course Introduction & Architecture 2.0

We kicked off the class with a provocative question: *"Ask not what you can do for AI—ask what AI can do for you."* And honestly, after seeing AI generate everything from Warhol-style astronauts to working code, the question isn't whether AI can help us design computer systems—it's whether we can afford not to use it.

### The End of an Era

For decades, computer systems innovation followed a predictable playbook I call **TAO**: Technology innovation (thank you, Moore's Law), Architecture innovation (hello, parallelism), and Optimization (compiler tricks and hardware-software co-design). This worked beautifully when design spaces were manageable and human intuition could guide us toward good solutions.

But here's the thing—that era is over.

Moore's Law is sputtering. Dennard scaling is dead. We're dealing with dark silicon and diminishing returns from traditional approaches. Meanwhile, as Hennessy and Patterson famously declared, we've entered the age of domain-specific computing. Every application needs its own specialized solution, and the design spaces have exploded beyond anything a human can reasonably navigate.

### Welcome to Architecture 2.0

This brings us to **TAOS**—the same TAO, but with a crucial fourth pillar: **Specialization**. And this is where things get wild.

We're not talking about tweaking a few parameters anymore. Modern design spaces contain somewhere between 10^14 and 10^2300 possible configurations. To put that in perspective, that's more combinations than there are atoms in the observable universe. No human—no matter how brilliant—can systematically explore spaces like that.

This is why we need AI agents that can navigate these exponentially complex design spaces automatically. It's not about replacing human expertise; it's about augmenting it with systems that can explore solution spaces too vast for manual analysis.

### The North Star

Imagine being able to say: *"Act like an architect—design me a custom 64-bit RISC-V processor with full vector extension support and optimize it for less than 3 Watt TDP in a 7nm LP process node using the TSMC plugin library."* 

That's not science fiction. That's where we're heading.

### What's Next?

Next week, I will continue to cover some introductory material. And soon we'll start our class journey through the computing stack, beginning with AI for software. Code generation is the most accessible entry point as it's where we can clearly see both the incredible promise and the current limitations of AI in systems design. We'll explore what it really takes to move from "impressive demos" to "production-ready tools."

The slides are posted below, and I'm curious to hear your thoughts on the research challenges we outlined: datasets, algorithms, best practices, workforce training, and infrastructure. Which of these do you think will be the biggest bottleneck?

**Materials**: [Slides](https://github.com/harvard-edge/cs249r_fall2025/releases/download/sep-3/CS249r_.Architecture.2.0.-.Part.1.pdf) • [All materials](https://github.com/harvard-edge/cs249r_fall2025/releases/tag/sep-3)

---

## September 8 - Architecture 2.0 & Foundations

*Class notes will be added after the session.*

This week we'll dive deeper into Architecture 2.0 and the paradigm shift from human-designed heuristics to agentic design methodologies. We'll also introduce datasets and survey paper methodology that will be essential for your research projects.

**Key Topics to Cover:**
- The foundations of AI agents in computer system design
- Understanding design abstractions for intelligent systems
- Introduction to QuArch dataset and question-answering for architecture
- Deep learning's implications for computer architecture and chip design

**Materials**: *Will be posted after class*

---

## September 15 - Code Generation & Software Engineering

*Class notes will be added after the session.*

This week we explore code generation as the most accessible entry point for AI in systems. We'll examine how to evaluate whether AI can actually replace human programmers and what it means for code to be "correct" vs. "optimal."

**Key Topics to Cover:**
- Moving from "impressive demos" to "production-ready tools"
- Real-world GitHub issue resolution with SWE-bench
- Competition-level code generation with AlphaCode
- Multi-agent code generation and iterative optimization

**Guest Speaker**: Ofir Press (Author of SWE-bench)

**Materials**: *Will be posted after class*

---

## September 22 - Performance Engineering & Code Optimization

*Class notes will be added after the session.*

Moving beyond correctness to performance requires understanding both algorithmic complexity and system behavior. Can AI learn the subtle performance optimizations that expert programmers use?

**Key Topics to Cover:**
- LLM-driven code optimization for warehouse-scale computers
- Learning performance-improving code edits
- Compiler auto-tuning with reinforcement learning
- Understanding cache behavior and memory access patterns

**Materials**: *Will be posted after class*

---

## September 29 - GPU Kernels & Parallel Programming

*Class notes will be added after the session.*

GPU kernel optimization sits at the intersection of domain expertise and automated optimization - a space too complex for pure heuristics but requiring deep hardware understanding.

**Key Topics to Cover:**
- Can LLMs write efficient GPU kernels?
- Multi-turn reinforcement learning for CUDA kernel generation
- Benchmarking AI systems against hand-tuned libraries
- Hardware-specific optimization strategies

**Materials**: *Will be posted after class*

---

## October 6 - Distributed Systems Integration

*Class notes will be added after the session.*

Distributed systems represent the culmination of software engineering challenges - where code generation, performance optimization, and parallel programming must work together at scale.

**Key Topics to Cover:**
- Full-stack co-design and optimization of distributed ML systems
- Reinforcement learning for datacenter congestion control
- Co-designing algorithms and system architecture
- Handling failures, load balancing, and resource contention

**Materials**: *Will be posted after class*

---

*More class notes will be added after each session throughout the semester.*
