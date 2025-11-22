---
layout: post
title: "Week 12: When Physics Becomes the Bottleneck - Physical Design and the Architecture Constraint Problem"
date: 2024-11-19
author: "Vijay Janapa Reddi"
categories: [hardware, physical-design, chip-design]
permalink: /blog/2024/11/19/week-12-physical-design-bottleneck/
---

[Last week](/cs249r_fall2025/blog/2024/11/14/week-11-part-2-benchmarking-llms-hardware/), we examined how to evaluate AI systems for chip design. We saw that hardware benchmarks are fundamentally harder than software benchmarks because of multi-stage feedback loops, quality metrics beyond correctness, and the irrevocability constraint. RTL generation must consider not just functional correctness, but whether designs will synthesize, meet timing, and physically realize.

This week, we cross another threshold. We move from behavioral descriptions (RTL) to physical reality (layout). And here, something profound emerges that changes how we must think about the entire chip design process.

## The Constraint Inversion

In [Week 11 Part 1](/cs249r_fall2025/blog/2024/11/12/eda-fundamentals-code-to-silicon/), we walked through the chip design flow: specification → RTL → synthesis → physical design → tape out. We emphasized irrevocability: once you tape out, you can't patch hardware. Mistakes cost millions of dollars and months of time.

But there's something we didn't fully address, something one of my students articulated in class:

**"Architecture is now really constrained by lower-level problems."**

What does this mean technically? For decades, we thought about the design flow as hierarchical and top-down:

<div class="mermaid">
graph TD
    A[Architect Dreams Up Design] --> B[Writes Specification]
    B --> C[RTL Engineers Implement]
    C --> D[Synthesis Tools Optimize]
    D --> E[Physical Design Realizes]
    E --> F[Fabrication Builds It]
    
    style A fill:#e8f5e9
    style B fill:#e8f5e9
    style C fill:#fff3e0
    style D fill:#fff3e0
    style E fill:#ffebee
    style F fill:#A51C30,color:#fff
</div>

This mental model suggests that architecture is the creative, unconstrained part. You design the "what" and the "why," then hand it off to implementation teams to figure out the "how."

**This model is breaking down.**

At modern process nodes (5nm, 3nm, and beyond), the direction of constraint has inverted. Physical design limitations now fundamentally constrain what architectures are even viable. You cannot design an architecture in isolation from its physical implementation because physical effects dominate system behavior.

The flow hasn't just become bidirectional—it's become bottom-up constraint propagation:

<div class="mermaid">
graph TD
    A[Physical Design Constraints] --> B[Synthesis Constraints]
    B --> C[RTL Constraints]
    C --> D[Architectural Choices]
    D --> E[System Design]
    
    A -.feedback.-> D
    B -.feedback.-> D
    C -.feedback.-> E
    
    style A fill:#A51C30,color:#fff
    style B fill:#ffebee
    style C fill:#fff3e0
    style D fill:#e8f5e9
    style E fill:#e8f5e9
</div>

**Why is this happening now?** What changed to cause this constraint inversion? The answer lies in how physics scales—or doesn't scale.

## When Physics Caught Up

Moore's Law has driven transistor scaling for decades. Every new process node, transistors get smaller, faster, and more power-efficient. We pack more of them into the same die area. More transistors = more compute capability. Simple, right?

**Wrong.** This narrative misses a critical detail: **not everything scales together.**

### The Wire Delay Problem

As transistors shrink from 28nm to 5nm, gate delays improve by 2-3x—the good news Moore's Law celebrates. But wire delays don't scale proportionally. Wire resistance per unit length actually *increases* at advanced nodes due to scattering in thinner wires. Meanwhile, modern GPUs and server chips have grown to 600-800mm² dies, meaning longer maximum wire lengths.

The result? At modern nodes: **Wire delay > Gate delay**. For paths crossing significant die distances, wire delay can be 10-50x larger than gate delays.

### The Power Delivery Crisis

Higher transistor density and clock frequencies mean more power per unit area. Power rails have resistance, so at high current densities, voltage drops (IR drop) vary across the chip—different regions see different supply voltages. Thermal challenges intensify: removing 400W+ from a small die creates hotspots that affect timing and reliability.

### The Routing Complexity Explosion

Modern chips have 10-15 metal layers for routing billions of nets, each with strict design rules. Congestion hotspots emerge where many signals squeeze through limited resources. The question isn't just "can we route this?" but "can we route this while meeting timing on critical paths, staying within power budgets, and satisfying every manufacturing rule?"

### What This Means for Architects

These physical realities fundamentally reshape how architects must think. If your design requires high-bandwidth communication between units, they must be placed close together—this isn't an optimization goal, it's physics. Wire delay and wire energy dominate at modern nodes, making physical proximity a hard architectural requirement. You can have brilliant microarchitecture, but if your floorplan puts frequently-communicating units far apart, the design will fail timing closure.

Power delivery imposes its own spatial constraints. High-power units must be located where the power grid can supply stable voltage, constraining architectural floorplanning in ways that have nothing to do with computational requirements. Even basic questions—one large shared cache or multiple distributed caches?—get reframed by wire delay rather than cache miss rates.

This is the technical reality behind "architecture is constrained by lower-level problems." Physical effects are no longer secondary implementation details—they are primary architectural constraints that shape what designs are even viable to attempt.

But here's the problem: How do you know if your architectural decisions will satisfy these physical constraints? You have to actually do physical design. And physical design comes late in the flow and takes a long time.

This creates a feedback loop crisis.

## The Feedback Loop Crisis

Recall [Week 11's chip design flow diagram](/cs249r_fall2025/blog/2024/11/12/eda-fundamentals-code-to-silicon/#chip-design-flow). We showed iteration cycles where problems discovered in later stages require going back to earlier stages. Physical design is where many architectural problems get discovered.

Let's trace through what happens when you design a new processor architecture:

<div class="mermaid">
graph TD
    A[Design Architecture<br/>Weeks of work] --> B[Write RTL<br/>Weeks-months of work]
    B --> C[Verify Functionality<br/>Weeks of work]
    C --> D[Synthesize to Gates<br/>Days of work]
    D --> E[Physical Design<br/>Weeks-months of work]
    E --> F{Does it meet<br/>timing/power/area?}
    
    F -->|No| G[Identify Problems]
    G --> H{Can we fix in<br/>physical design?}
    H -->|No| I[Back to Architecture]
    I --> A
    
    H -->|Maybe| J[Try Different<br/>Placement/Routing]
    J --> E
    
    F -->|Yes| K[Signoff & Tape Out]
    
    style A fill:#e8f5e9
    style E fill:#A51C30,color:#fff
    style F fill:#ffebee
    style I fill:#ffebee
    style K fill:#e8f5e9
</div>

The problem is stark: by the time you discover your architecture won't physically realize, you've already invested months. Let's quantify this. Architecture definition, RTL implementation, and functional verification: three to six months. Synthesis and physical design: another two to four months. So you're five to ten months in when you discover timing doesn't close, routing is congested, or power delivery can't handle your design. Now you iterate back to architecture and restart. That's another five to ten months minimum.

This isn't just inefficiency in the abstract. It fundamentally limits how much architectural innovation is possible within realistic development timelines.

### The Exploration Problem

Remember [Week 7](/cs249r_fall2025/blog/2024/10/15/tacit-knowledge-architecture/) where we discussed design spaces with 10^14 possible configurations? We asked: how do AI agents explore such vast spaces?

**But here's the catch**: If each architectural evaluation requires 5-10 months to discover whether it physically realizes, how many designs can you actually evaluate per chip generation?

With a 2-3 year design cycle and multiple engineers, maybe you can thoroughly explore 10-20 architectural alternatives. That's sampling 10^-13 of the design space.

**This is absurd.** We're making billion-dollar bets about chip architecture based on exploring a microscopic fraction of the possible designs, and we don't even know if those designs will physically work until months into implementation.

The constraint inversion means you can't evaluate architectures without understanding their physical implementation. But physical design is too slow to enable rapid architectural exploration.

**We need fast, accurate feedback about physical design outcomes early in the architecture process.**

This is where AI enters the picture. But not in the way you might expect.

## Two Technical Approaches to the Feedback Problem

Both papers this week attack the feedback loop problem, but with fundamentally different philosophies. Understanding these philosophies reveals deeper questions about how AI should assist with physically-constrained design.

### Approach 1: Learn to Place (Reinforcement Learning)

[Chip Placement with Deep Reinforcement Learning](https://arxiv.org/abs/2004.10746) takes an RL perspective on placement. The core insight: placement is a sequential decision-making process. At each step, you decide where to place the next macro (large circuit block). These decisions have long-term consequences that only become apparent after the entire design is placed and routed.

This sounds familiar. Remember [Week 11's MCTS paper](/cs249r_fall2025/blog/2024/11/14/week-11-part-2-benchmarking-llms-hardware/) for RTL generation? The key challenge was delayed feedback: early design decisions have consequences you don't see until much later. Physical placement has the exact same structure.

The RL formulation treats placement as a Markov Decision Process. At each step, the agent sees the current state: which macros have been placed, where they sit, what space remains. It chooses an action—where to place the next macro. Only after the entire design is placed and routed do you know how good this placement is. The reward captures wirelength (which affects timing and power), congestion (whether the design will route), and timing metrics like critical path delays.

The goal: learn a policy—a neural network mapping states to actions—that maximizes cumulative reward across many different chip designs. The implementation represents the floorplan as a grid, uses graph neural networks to encode the netlist structure (which gates connect to which), and trains with policy gradients on diverse designs.

The promise is compelling. Once trained, the policy places new designs in hours instead of weeks. Architects get rapid feedback about whether their ideas will meet timing, power, and area targets. The system learns from experience, potentially discovering placement strategies human experts would never consider. It handles complex multi-objective optimization—balancing timing, power, and area simultaneously. And inference is fast.

But the technical challenges are formidable. The reward function must capture timing on thousands of paths, congestion, power delivery, thermal constraints, and hundreds of design rules. Miss a critical constraint, and your learned policy might optimize brilliantly for the wrong objective. Transfer learning is uncertain—policies trained on CPUs might fail spectacularly on GPUs or custom accelerators, and different design styles have fundamentally different placement characteristics. The black-box nature means when placement fails, you get no insight into what went wrong or what architectural changes might help. And validation poses a chicken-and-egg problem: you must run complete flows to verify placement quality, which undermines the speed advantage that motivated using RL in the first place.

### Approach 2: Accelerate Classical Methods (GPU-Powered Optimization)

[DREAMPlace: Deep Learning Toolkit-Enabled GPU Acceleration for Modern VLSI Placement](https://dl.acm.org/doi/abs/10.1145/3316781.3317803) takes a completely different approach. The insight: we have decades of placement algorithms that work. They're based on solid optimization theory (simulated annealing, analytical placement, force-directed methods). **The problem is they're too slow for rapid iteration.**

What if instead of replacing these algorithms with learned policies, we **accelerate** them with modern hardware and optimization techniques?

DREAMPlace takes three key technical steps. First, it makes placement differentiable. Traditional placement algorithms treat macro positions as discrete choices—each macro goes in one specific location. DREAMPlace instead gives macros "soft" positions that can be continuously adjusted. This reformulation transforms placement from a discrete combinatorial problem into a continuous optimization problem where you can use gradient descent.

<span class="margin-note">**PyTorch Without Deep Learning**: As Alex observed in class, DREAMPlace uses PyTorch not for neural networks, but to leverage its automatic differentiation engine and stochastic gradient descent optimizers. This is a clever architectural choice—PyTorch provides mature, GPU-accelerated implementations of gradient computation and optimization algorithms that would take years to build from scratch. DREAMPlace essentially treats placement as a massive optimization problem and uses PyTorch's infrastructure to solve it. This highlights how ML frameworks have become general-purpose optimization toolkits, useful far beyond training neural networks.</span>

Second, it exploits GPU parallelism. Instead of placing macros sequentially on a CPU, DREAMPlace structures all its computations—wirelength calculations, density gradients, legalization steps—to run in parallel across thousands of GPU cores. This is the key to its speed advantage.

Third, it maintains an analytical formulation. The objective function explicitly encodes what's being optimized: minimize total wirelength while respecting density constraints and alignment requirements. This isn't a black-box neural network. It's transparent optimization where you can see exactly what's happening.

The results are impressive: 10-100x speedup compared to traditional CPU-based placers, while maintaining or even improving solution quality.

Transparency is DREAMPlace's first major advantage. You can inspect the objective function, understand what's being optimized, diagnose problems. When placement fails, you can analyze the objective landscape and see why it got stuck in certain local minima. This interpretability matters for production—you need to trust and debug your tools.

DREAMPlace builds on decades of validated methods. It's not inventing new placement algorithms. It's accelerating analytical techniques the EDA community has refined over many years—force-directed placement, analytical solving, wirelength optimization. Physical designers trust these approaches. DREAMPlace just makes them faster.

Integration is straightforward. DREAMPlace produces standard placement outputs (coordinates for each macro, no proprietary formats). It slots into existing EDA tool chains. You don't rebuild your entire infrastructure. Low barrier to deployment.

Predictability matters. Same netlist + same hyperparameters = same results. No randomness, no neural network sampling. This determinism is valuable for debugging and reproducibility.

But DREAMPlace has its own challenges. Despite being faster, it still needs hyperparameter tuning: penalty weights for density violations, annealing schedules, density targets, convergence thresholds. These parameters affect solution quality and need adjustment for different designs. Unlike RL approaches that might learn good settings through experience, DREAMPlace needs human expertise to set them.

DREAMPlace doesn't learn across designs. Each placement starts fresh. It doesn't remember what worked well before or transfer insights from one chip to another. It's faster per iteration, but it doesn't get smarter over time.

Effective use still needs human expertise. Experienced physical designers know which placement strategies work for different design styles, how to set up initial floorplan constraints, when to adjust parameters mid-flow, how to interpret results. DREAMPlace accelerates the optimization. The strategic decisions stay human-driven.

### The Philosophical Divide

These approaches represent a deeper tension in AI for systems. The reinforcement learning path says: discover strategies through experience, trust the learned policy to generalize, and accept black-box nature in exchange for potential superhuman performance. The GPU optimization path says: encode domain knowledge explicitly, make optimization transparent, and preserve decades of validated methods while making them faster.

This is the same tension we saw in [Week 8 with DOSA vs. AutoTVM](/cs249r_fall2025/blog/2024/10/22/mapping-codesign-reasoning/). DOSA encoded analytical models explicitly, while AutoTVM learned from experience. Both worked, but they captured fundamentally different types of knowledge—one transparent and interpretable, the other emergent and learned.

**The question isn't which is "better" in absolute terms. It's which provides better feedback for architectural design.**

For rapid architectural exploration, architects need to quickly evaluate whether an architecture will meet physical constraints. When a design fails, they need to understand what architectural changes would help. The tool must generalize to novel architectures they haven't seen before. And crucially, architects must trust the results enough to make early architectural decisions based on them. These requirements point to a deeper issue: What are we really trying to optimize?

## The Co-Design Challenge Deepens

Physical design isn't just a later stage in the flow. It's part of a deeply coupled optimization problem that spans the entire design stack. This connects directly to [Week 8's co-design reasoning](/cs249r_fall2025/blog/2024/10/22/mapping-codesign-reasoning/).

Remember Week 8's circular dependencies in hardware/software mapping? We couldn't choose tile sizes without knowing the memory hierarchy, couldn't design the memory hierarchy without knowing access patterns, couldn't determine access patterns without knowing the dataflow. Each decision depended on all the others.

**Physical design creates even deeper circular dependencies**:

<div class="mermaid">
graph LR
    A[Architecture<br/>Design] --> B[RTL<br/>Structure]
    B --> C[Synthesis<br/>Choices]
    C --> D[Physical<br/>Placement]
    D --> E[Routing<br/>Patterns]
    E --> F[Timing<br/>Closure]
    
    F -.timing fails.-> G[Need faster<br/>gates]
    G -.-> C
    
    F -.congestion.-> H[Need better<br/>placement]
    H -.-> D
    
    H -.can't route.-> I[Need different<br/>structure]
    I -.-> B
    
    I -.fundamental<br/>issue.-> J[Need different<br/>architecture]
    J -.-> A
    
    style A fill:#e8f5e9
    style D fill:#A51C30,color:#fff
    style F fill:#ffebee
    style J fill:#ffebee
</div>

Let's trace through how these dependencies interlock. Architecture depends on placement outcomes. Will frequently-communicating units end up close enough for low wire delay? Will routing push them apart? Can critical timing paths be placed to minimize detours, or will congestion force signals through slow regions? Will the power delivery network reach high-power units, or will IR drop force you to relocate them? You can't answer these without actually doing placement. But placement happens months after you've locked in major architectural decisions.

Simultaneously, placement depends on architectural priorities. Which signal paths are truly performance-critical? What timing margins do you actually need—pushing for maximum frequency or leaving slack for voltage scaling? Where can you trade area for performance? You can't optimize placement without understanding these priorities. But you don't know the priorities until you see what physically realizes and which constraints actually bind.

Both architecture and placement depend on workload characteristics. Which execution paths are hot? What memory access patterns dominate? Which functional units see highest utilization? These workload behaviors determine what architectural features matter and what placement strategies deliver real-world performance. But workloads evolve, and future applications might behave differently from today's benchmarks.

### Physical Proximity as an Architectural Constraint

At advanced nodes, this circular dependency manifests as a hard constraint: **Physical proximity becomes an architectural requirement, not an optimization goal.**

Consider a concrete example. You're designing a processor with a high-bandwidth connection between the L2 cache and execution units. Your target frequency is 3 GHz, giving you a clock period of 333 picoseconds. After accounting for clock skew and setup time requirements, you have roughly 250 picoseconds of delay budget for any signal path.

At 5nm, gate delays run 10-30 picoseconds per gate. Wire delay is about 10 picoseconds per millimeter of optimally-buffered routing (congested routes are much worse). Say your cache-to-execution path traverses 10 gates, consuming 150 picoseconds. You've got 100 picoseconds left for wires.

Simple arithmetic: maximum 10 millimeters of optimally-buffered routing. But that's optimistic. Real routing isn't perfectly straight. Wires detour around obstacles, navigate congested regions, deal with less-than-optimal buffering. A realistic safe budget? More like 5-7 millimeters of maximum separation.

This isn't a suggestion or an optimization target. It's physics. If your architectural floorplan places these units farther apart than this budget allows, timing will fail. You'll be forced into unpleasant choices: reduce clock frequency (direct performance loss), add pipeline stages (increased latency and complexity), or redesign the architecture (months of wasted work).

Physical proximity has become an architectural constraint that must be satisfied, not merely optimized.

This is fundamentally different from the past. In older process nodes (90nm, 65nm), wire delay was smaller relative to gate delay. You had more flexibility. Placement optimization could often fix timing issues without architectural changes.

**At modern nodes, this flexibility has disappeared.** Architecture must be designed with physical implementation in mind from day one.

### The Three-Way Co-Design Problem

This creates a three-way co-design challenge:

<div class="mermaid">
graph TD
    A[Architecture Design] <--> B[Physical Layout]
    B <--> C[Workload Characteristics]
    C <--> A
    
    A -.must be<br/>physically<br/>realizable.-> B
    B -.determines<br/>achievable<br/>performance.-> A
    
    C -.determines<br/>what to<br/>optimize.-> A
    A -.determines<br/>workload<br/>performance.-> C
    
    C -.affects<br/>critical<br/>paths.-> B
    B -.affects<br/>workload<br/>efficiency.-> C
    
    style A fill:#2563eb,color:#fff
    style B fill:#dc2626,color:#fff
    style C fill:#16a34a,color:#fff
</div>

Each vertex of this triangle affects the other two. Architecture shapes what workloads run efficiently—a design optimized for dense matrix operations fails on sparse graph algorithms. Workloads determine which architectural features matter—prediction accuracy is useless if your workloads are unpredictable. Physical layout determines which architectures are even viable—a brilliant design that can't meet timing is just an expensive lesson. Architecture constrains what physical layouts are possible—you can't arbitrarily rearrange components if connectivity is fixed. Workloads affect which physical paths become critical—the paths that matter depend on what executes. Physical layout affects workload performance through proximity, routing quality, and power delivery.

You cannot optimize these three dimensions independently. This is Week 8's co-design reasoning taken to its logical extreme, where the circular dependencies span from high-level algorithms down to micrometer-scale wire routing.

Traditional design flow handles this through iteration: design architecture, implement it, discover problems, iterate. But when iterations take months and cost millions, you can only afford a few iterations per generation.

**What if we could close these feedback loops faster?** What if architects could rapidly evaluate architectural ideas against physical constraints? What if physical designers could quickly explore layout alternatives and feed insights back to architects?

This is what AI-accelerated physical design could enable. Not replacing human designers, but closing the feedback loops that currently span months into loops that take hours or days.

But doing this requires rethinking the entire design flow.

## Inverting the Design Flow: A Different Approach

The traditional design flow is top-down: start with high-level architecture, progressively refine down to physical implementation. This made sense when physical effects were secondary. **At modern nodes, it increasingly doesn't work.**

What if we invert the flow? What if we start from physical constraints and ask: **What architectures are viable given these constraints?**

### Constraint-First Design

Consider a different approach that inverts the traditional flow. Begin by characterizing the physical constraints at your target process node. What's the wire delay per millimeter? What power delivery density can your package and cooling system support? How much routing resource exists in each region of the die? What are the thermal dissipation limits?

Next, model the critical architectural dependencies. Which components absolutely must communicate with high bandwidth? What structures will form critical timing paths? Where will power density hotspots emerge based on the workload? These dependencies shape what floorplans are even feasible.

With physical constraints and dependencies understood, you can now explore the space of architectures that actually satisfy these constraints. Which floorplans allow critical paths to meet timing without heroic efforts? Which communication patterns can be physically realized given your interconnect resources? What's the shape of the viable design space once you eliminate architectures that physics rules out?

Finally, among the architectures that are physically viable, optimize for workload performance. Which designs best serve your target applications? What trade-offs exist between different viable approaches? You're still making creative architectural choices, but you're making them within a space you know is implementable.

This is constraint-first design rather than architecture-first design. You don't start by imagining the perfect architecture and then struggling to implement it. You start by understanding what's physically possible, then optimize within that space. The creativity shifts from "what do I want to build?" to "what's the best thing I can build given these constraints?"

### The Co-Optimization Perspective

<span class="margin-note"><img src="/cs249r_fall2025/assets/images/blog_images/week_12/richard_ho.jpg" alt="Richard Ho" style="width: 80px; height: 80px; border-radius: 8px; float: left; margin-right: 10px; margin-bottom: 10px; margin-top: 5px;"> **Richard Ho** is Head of Hardware at OpenAI, where he works on co-optimizing ML models and the massive compute infrastructure they run on. His unique perspective comes from approaching chip design from the workload side—knowing exactly what models need to run and designing hardware specifically for those requirements. This inverts the traditional chip design problem in interesting ways.</span>

Industry practitioners working on AI hardware often approach this from the opposite direction from traditional chip companies. Traditional chip design builds a general-purpose chip and hopes it runs ML workloads efficiently. The co-optimization approach instead starts with specific workload knowledge—you know exactly what models you need—and asks what chip would run them optimally.

This inversion is powerful because you have complete information about both sides of the boundary. You can co-design the model architecture and the hardware together, letting physical constraints inform decisions on both sides simultaneously.

Consider what this opens up. If physical layout demands certain units be close together to meet timing, can you restructure the model to exploit that proximity? If wire delays favor certain communication patterns, can you design model architectures that align with the fast paths? If power delivery constrains compute density, can you adjust model size, sparsity, and activation functions to fit within those constraints while maintaining quality?

The key insight: when you control both sides of the hardware-software boundary, you can navigate the constraint space in ways traditional chip designers cannot.

You're not just asking "how do I implement this fixed algorithm efficiently?" You're asking "how do I co-design algorithm and hardware to achieve my goal within physical constraints?"

This is the deepest form of co-design reasoning: simultaneous optimization across algorithms, architecture, and physical implementation.

### Why This Is Hard

Of course, most chip designers don't control both sides. You're building a general-purpose CPU or GPU that must run diverse workloads, many not known at design time.

But the principle still applies: **Starting from physical constraints and working up might be more effective than starting from architecture and working down.**

The challenge: our current design tools were built for the traditional top-down flow. Architects define the microarchitecture. RTL engineers implement it. Physical designers try to realize what was handed to them. When it doesn't work—timing fails, routing congests, power delivery can't handle the hotspots—you iterate backward. This works, but it's slow and expensive.

What would tools look like if we built them for constraint-first design? You'd need early performance models that predict physical realizability from architectural sketches, before committing to detailed RTL. You'd need fast exploration to evaluate many physically-viable alternatives in hours, not months. You'd need feedback loops that operate at architectural timescales, not implementation timescales. And you'd need co-optimization frameworks that reason across the entire stack simultaneously.

This is where AI could have real impact: enabling rapid exploration of physically-viable architectures. Not replacing human judgment about what to build, but answering crucial questions quickly: Will this idea physically realize at your target node? Where are the bottlenecks? What modifications would improve feasibility? Which of these alternatives is most likely to close timing?

These are exactly the questions architects need answered early, before investing months in detailed design.

## The Evaluation Challenge

[Week 11 Part 2](/cs249r_fall2025/blog/2024/11/14/week-11-part-2-benchmarking-llms-hardware/) asked: "How do we know if AI is getting better at chip design?"

For physical design, this evaluation challenge is acute. What should we actually measure?

### The Metrics Problem

The most obvious metric—total wirelength—is just a proxy. What actually matters is timing closure, power, and routability. A placement with slightly longer wirelength might meet timing better if it shortens critical paths. But timing slack isn't known until after routing completes, so placement algorithms optimize proxies and predict impact. Final QoR (quality of results) after the complete flow is the true metric, but requires weeks per evaluation—too slow for rapid exploration. And matching human expert placement assumes humans are optimal, when the goal is to exceed human performance.

### The Validation Problem

Physical design evaluation has a deeper issue: **You don't know if placement is good until routing finishes. You don't know if routing works until timing signoff. You don't know if timing models are accurate until silicon returns.**

This creates a validation hierarchy:

<div class="mermaid">
graph TD
    A[Fast Placement Prediction<br/>Seconds-minutes] --> B[Complete Placement<br/>Hours]
    B --> C[Routing<br/>Days]
    C --> D[Timing Signoff<br/>Days-weeks]
    D --> E[Silicon Validation<br/>Months after tape-out]
    
    A -.how accurate?.-> B
    B -.will it route?.-> C
    C -.meets timing?.-> D
    D -.matches silicon?.-> E
    
    style A fill:#e8f5e9
    style B fill:#fff3e0
    style C fill:#ffe8e0
    style D fill:#ffebee
    style E fill:#A51C30,color:#fff
</div>

At each level, you trade speed for accuracy. Fast models evaluate thousands of alternatives but have huge gaps. Complete placement is accurate but doesn't tell you if the design will route or meet timing. Full signoff gives high confidence but is way too slow for exploration. Silicon validation provides ground truth—but only once, after you've committed.

The dilemma is fundamental: fast evaluation has large gaps to reality, accurate evaluation is too slow for exploration. This is the simulation-reality gap from [Week 11](/cs249r_fall2025/blog/2024/11/12/eda-fundamentals-code-to-silicon/#stage-5-signoff-the-final-validation). Physical design has especially large gaps because physical effects resist modeling—process variation, parasitic extraction, IR drop dynamics, thermal effects, cross-talk all add uncertainty. These interactions compound nonlinearly.

### What Should We Actually Evaluate?

Given these challenges, what's the right way to evaluate AI for physical design?

For rapid architectural exploration—the main use case we care about—we need fast, approximate models that can predict whether designs will meet constraints. Accuracy doesn't need to be perfect; we need to correctly identify which architectural alternatives are viable versus non-viable, which have fundamental problems versus which are promising.

The metrics that matter for this use case are different from traditional placement metrics. Ranking correlation matters more than absolute accuracy: if a fast model says design A is better than design B, and full implementation confirms that ranking, the model is useful even if its numerical predictions were off. Constraint satisfaction prediction is key: the fast models should correctly classify which designs will meet timing, power, and area targets—a "will work" versus "won't work" prediction rather than precise frequency numbers. Critical path identification helps architects understand where to focus optimization efforts, identifying the same bottlenecks that human experts would find after full implementation.

What doesn't matter for architectural exploration is exact numerical prediction of final achievable frequency—that requires full implementation anyway. For early-stage exploration, approximate but directionally correct predictions are sufficient to guide decisions.

For final implementation in production use, the requirements change entirely. AI tools must produce results that can be validated against established methods through head-to-head comparison with commercial EDA tools on production designs. Quality of results becomes paramount—does AI placement achieve comparable or better frequency, power, and area than mature commercial tools? Robustness is critical: the tool must work across diverse design styles (CPUs, GPUs, accelerators, custom ASICs) rather than only the specific types it was trained on. Integration feasibility determines adoption: can it fit into existing design flows without requiring wholesale infrastructure changes?

The key distinction is that evaluation criteria must match use case. For architectural exploration, we need speed and reasonable accuracy to guide design decisions. For production implementation, we need validated quality and robustness to justify replacing proven tools.

Current AI placement research often conflates these. Papers show improved wirelength on academic benchmarks, but don't validate on production flows or demonstrate value for architectural exploration.

**The evaluation challenge isn't just technical. It's about understanding what problem you're actually solving.**

## Looking Ahead to Week 13

Physical design reveals the constraint inversion at the heart of modern chip design: at advanced process nodes, physical realities increasingly dictate what architectures are viable. We can no longer design the architecture and then implement it—we must co-optimize architecture and physical layout simultaneously. This is Week 8's co-design reasoning taken to its logical extreme, with circular dependencies spanning the entire stack.

But there's a deeper question lurking beneath: **"Does what we built actually work?"**

[Week 13's verification]({{ site.baseurl }}/course/schedule/#week-13---verification--advanced-chip-design) completes the loop from architectural intent to working silicon:

<div class="mermaid">
graph LR
    A[Architecture] --> B[Intent]
    B --> C[RTL] 
    C --> D[Behavioral<br/>Description]
    D --> E[Synthesis]
    E --> F[Logical<br/>Implementation]
    F --> G[Physical<br/>Design]
    G --> H[Geometric<br/>Reality]
    H --> I[Verification]
    I --> J{Matches<br/>Intent?}
    
    J -->|No| K[Debug &<br/>Fix]
    K --> C
    
    J -->|Yes| L[Tape Out]
    
    style A fill:#e8f5e9
    style G fill:#A51C30,color:#fff
    style I fill:#fff3e0
    style L fill:#A51C30,color:#fff
</div>

Physical design tells us we *can* build the chip physically. Verification tells us we *should* build it—that it will actually work correctly once fabricated.

Verification faces its own feedback loop crisis. Traditional approaches—testbenches, simulation, coverage analysis—take months and can never achieve completeness for billion-transistor designs. The verification gap grows wider with each generation. How do you prove the absence of bugs in a system too complex to exhaustively test?

Together, physical design and verification complete Phase 3's picture. Both face slow feedback loops that limit iteration. Both require reasoning about emergent properties not obvious from local information. Both make irrevocable commitments based on incomplete validation. And Week 13 will show us why verification might be the hardest problem of all—because you're not optimizing metrics anymore, you're trying to prove correctness.

---

## Key Takeaways

**The Constraint Inversion**: At modern process nodes, physical design limitations fundamentally constrain what architectures are viable. The design flow is no longer top-down but bottom-up constraint propagation.

**Physics Dominates**: Wire delay exceeds gate delay, power delivery limits density, routing congestion constrains connectivity. Physical effects are primary architectural constraints, not secondary implementation details.

**The Feedback Loop Crisis**: Discovering whether architectures physically realize takes months. This limits architectural exploration to a tiny fraction of the design space (10^-13 of possible configurations).

**Two Philosophies**: Learn placement policies (RL) versus accelerate classical algorithms (GPU optimization). Both aim to provide faster feedback, but with different trade-offs in transparency, generalization, and validation.

**Co-Design Deepens**: Physical design creates three-way co-optimization of architecture, implementation, and workload. Week 8's circular dependencies taken to the extreme.

**Evaluation Is Hard**: Physical design has especially large simulation-reality gaps. Fast evaluation is inaccurate, accurate evaluation is too slow for exploration.

**AI's Real Opportunity**: Not autonomous chip design, but closing feedback loops from months to hours, enabling rapid exploration of physically-viable architectures—potentially inverting the flow to start from constraints rather than abstract intent.

---

## Discussion Questions

**For researchers:** How do we build performance models that are fast enough for exploration yet accurate enough for architectural decisions? What's the right fidelity for different design stages?

**For practitioners:** What feedback would be most valuable early in architectural design? Is it "will this meet timing?" or "what are the physical bottlenecks?" or "how do I modify the architecture to be more physically viable?"

**For everyone:** Should we be trying to make AI better at traditional placement, or should we rethink the entire physical design problem given modern AI capabilities? What would physical design tools look like if designed from scratch with AI in mind?

**The deeper question:** When physical constraints fundamentally limit architecture, and we use AI models to predict those constraints, how much does model inaccuracy limit architectural innovation? Are we optimizing within the wrong constraints because our models are wrong?

---

*Next week: Verification and Advanced Chip Design - where we close the loop and ask: does what we built actually work?*

*For detailed readings, slides, and materials for this week, see [Week 12 in the course schedule]({{ site.baseurl }}/course/schedule/#week-12---physical-design--layout).*

