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
| [Sep 8](#september-8---fundamental-challenges-in-ai-for-system-design) | Fundamental Challenges in AI for System Design | Data quality crisis & algorithm evolution |
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

## September 8 - Fundamental Challenges in AI for System Design

Today we tackled the fundamental question that defines our field: **Why is AI for system design so uniquely challenging?** This isn't just about needing more compute or better algorithms—it's about confronting challenges that are fundamentally different from every other AI success story you've encountered.

### The Dataset Problem That Nobody Talks About

Here's what became clear to me early in my research: we can't simply "scrape the internet" for system design data the way we do for computer vision. Consider ImageNet—it exists because millions of people uploaded cat photos to Flickr. But where are the equivalent repositories of high-quality processor design datasets waiting to be downloaded?

They simply don't exist. And even if they did, we'd face a fundamental quality problem.

In computer vision, if you mislabel a few cat photos as dogs, your classifier still works pretty well. But in system design? One bad performance measurement or incorrect architectural parameter can send your entire optimization down the wrong path. **Data quality isn't just important—it's everything.**

Then there's the simulation bottleneck. To generate training data, you fire up your cycle-accurate simulator and wait... and wait... and wait. You're constantly forced to choose between fast simulations that miss critical details or accurate simulations that take an eternity to produce meaningful datasets. Meanwhile, computer vision researchers generate millions of training examples simply by pointing cameras at the world.

### Fifty Years of Algorithm Evolution

The second challenge that should concern us deeply is the algorithm evolution problem. We've witnessed this pattern repeatedly throughout our field's history:

- **1970s-1990s**: Classical optimization ruled the world
- **1990s-2000s**: Bio-inspired methods were the hot new thing  
- **2000s-2010s**: Machine learning took over
- **2010s-present**: Deep learning revolution

Each time, we believed we'd discovered "the answer." But here's the critical insight: **not all algorithms are created equal**, and we lack systematic methodologies to determine which approaches work best for specific problems.

Just because transformers revolutionized natural language processing doesn't mean they're optimal for cache replacement policies. Yet how do we make this determination? Too often, we're applying algorithms to problems without rigorous frameworks for evaluation. This approach lacks the systematic rigor our field demands.

### The Validation Challenge

This brings us to perhaps the most critical question: **How do we verify that our AI systems are actually working correctly?** 

In other domains, we can tolerate some uncertainty. An image classifier achieving 95% accuracy is excellent. A language model that occasionally hallucinates is acceptable for many applications. But in system design, decisions cascade through the entire computing stack. An incorrect cache policy doesn't just affect one application—it degrades the performance of every piece of software running on that processor.

This requires us to address questions that other AI fields rarely consider:
- What are the true computational costs of training and deploying these agents?
- How well do they generalize to hardware configurations they've never encountered?
- How do we define "good performance" when the design space is effectively infinite?
- What are the failure modes, and how do we detect and recover from them?

### Why This Matters for Architecture 2.0

I want to be clear: these challenges aren't roadblocks—they define our research agenda. They're what makes Architecture 2.0 both necessary and profoundly exciting.

We're not simply trying to automate existing design processes. We're building AI agents that can navigate design spaces so vast that humans cannot comprehend them—spaces containing 10^14 to 10^2300 possible configurations. To put this in perspective, that's more combinations than there are atoms in the observable universe.

Our goal isn't to replace human expertise but to augment it with systems capable of exploring solution spaces too complex for manual analysis. However, achieving this vision requires us to solve these fundamental problems first.

### Looking Forward

As we progress through this course, I want you to keep these challenges at the forefront of your thinking. With every paper we read, every dataset we examine, and every algorithm we study, ask yourself these critical questions:

- Is this data truly representative of real-world systems?
- Does this algorithm align with the specific requirements of this problem domain?
- How would we rigorously validate this approach in production environments?

The students who will make meaningful contributions to this field won't simply be those who can implement the latest algorithmic advances. They'll be the researchers who can thoughtfully bridge the gap between AI capabilities and the unique, complex constraints of real system design.

**Materials**: [Architecture 2.0 Slides](https://github.com/harvard-edge/cs249r_fall2025/releases/download/sep-8/Architecture.2.0.slides.pdf) • [All materials](https://github.com/harvard-edge/cs249r_fall2025/releases/tag/sep-8)

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
