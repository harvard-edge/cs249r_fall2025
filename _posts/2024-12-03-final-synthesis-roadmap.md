---
layout: post
title: "Week 14: Course Synthesis — The Architecture 2.0 Roadmap"
date: 2024-12-03
author: "Vijay Janapa Reddi"
categories: [synthesis, architecture, systems]
permalink: /blog/2024/12/03/architecture-20-roadmap-synthesis/
---

We set out thirteen weeks ago with an ambitious question: Can AI agents become co-designers of computer systems? Not just tools that optimize within fixed constraints, but true collaborators that reason across the full computing stack—from code to silicon, from algorithms to physical layout, from specifications to verified implementations.

The answer, as is often the case with profound questions, is both simpler and more complex than we anticipated.

**The simple part**: Yes, AI can meaningfully contribute to system design in ways that were impossible even two years ago. We've seen concrete examples at every layer of the stack.

**The complex part**: The challenges that remain aren't just technical hurdles to overcome with bigger models or more compute. They're fundamental questions about the nature of system design itself—questions about circular dependencies that resist decomposition, tacit knowledge that exists only in experienced architects' intuitions, and trust in systems whose complexity exceeds human comprehension.

This isn't a conclusion. It's a roadmap.

<div class="key-takeaways">
<h3>🔑 Key Takeaways</h3>
<ul>
<li><strong>AI amplifies, not replaces:</strong> The most successful approaches combine AI exploration with human judgment, not autonomous AI design</li>
<li><strong>Three types of tacit reasoning:</strong> Co-design (circular dependencies), predictive (uncertain futures), and adaptive (continuous adjustment) reasoning define architectural expertise</li>
<li><strong>Trust requires diversity:</strong> Validation through multiple independent approaches, not blind faith in any single AI system</li>
<li><strong>Feedback loops are the bottleneck:</strong> Closing the gap between design decisions and their consequences enables faster iteration</li>
<li><strong>Hybrid approaches win:</strong> Combine analytical models (what we know) with learning (what we can't articulate) rather than pure ML or pure analysis</li>
</ul>
</div>

## Where We Started: The Architecture 2.0 Vision

[Week 1](/cs249r_fall2025/blog/2024/09/03/week-1-architecture-2-0/) introduced the **TAO to TAOS** framework. Traditional computer systems innovation followed TAO: **T**echnology (Moore's Law), **A**rchitecture (exploiting parallelism), and **O**ptimization (compiler advances). This worked when design spaces were tractable and human intuition could guide exploration.

But three converging forces made this insufficient:

1. **Demand explosion**: Every domain now needs specialized hardware (LLMs, autonomous vehicles, cryptocurrency, video transcoding). One-size-fits-all computing is over.

2. **Talent crisis**: Training competent architects takes years. Demand for specialized hardware grows exponentially. We can't train architects fast enough.

3. **AI inflection point**: For the first time, AI systems can understand code, reason about performance, and generate functional designs.

The **S** in TAOS stands for **Specialization**—not as another optimization technique, but as a fundamental shift requiring AI assistance. Modern design spaces contain 10^14 to 10^2300 possible configurations. If you evaluated one design every nanosecond, exploring 10^14 possibilities would take over three years. For 10^2300 configurations, you'd need more time than has elapsed since the Big Bang—by a factor larger than the number of atoms in the universe.

This isn't hyperbole. It's the mathematical reality of the design spaces we now face.

[Week 2](/cs249r_fall2025/blog/2024/09/08/week-2-fundamental-challenges/) then confronted us with five fundamental challenges that make Architecture 2.0 uniquely difficult: the **dataset crisis** (we must deliberately create every training example through expensive simulation), the **algorithm evolution treadmill** (ML techniques evolve faster than we can build systems around them), the **tools infrastructure gap** (our simulators weren't designed for AI agents), the **reproducibility crisis**, and **real-world robustness requirements**. These challenges compound each other, creating feedback loops that have kept AI-assisted architecture perpetually "five years away." Understanding these obstacles was essential before diving into solutions.

## The Three-Phase Journey: From Code to Silicon

The course structure wasn't arbitrary. We deliberately moved from software (where AI already shows promise) through architecture (where tacit knowledge dominates) to chip design (where irrevocability creates existential constraints). Each phase revealed different challenges and different forms of reasoning required for system design.

<div class="mermaid">
graph LR
    subgraph Phase1["Phase 1: AI for Software"]
    A[Week 3<br/>Code Generation] --> B[Week 4<br/>CPU Optimization]
    B --> C[Week 5<br/>GPU Kernels]
    C --> D[Week 6<br/>Distributed Systems]
    end
    
    subgraph Phase2["Phase 2: AI for Architecture"]
    E[Week 7<br/>Tacit Knowledge] --> F[Week 8<br/>Co-Design]
    F --> G[Week 9<br/>Prediction]
    G --> H[Week 10<br/>Adaptation]
    end
    
    subgraph Phase3["Phase 3: AI for Chip Design"]
    I[Week 11<br/>RTL Generation] --> J[Week 12<br/>Physical Design]
    J --> K[Week 13<br/>Verification]
    end
    
    D --> E
    H --> I
    
    style Phase1 fill:#e8f5e9
    style Phase2 fill:#fff3e0
    style Phase3 fill:#ffebee
</div>

### Phase 1: AI for Software (Weeks 3-6)

Software provided our entry point because the artifacts are explicit—literally written as text—and feedback loops are relatively tight. You can compile, test, iterate. Mistakes are fixable.

**[Week 3](/cs249r_fall2025/blog/2024/09/17/software-engineering-reality-gap/)** confronted us with the reality gap: AI that wins programming contests struggles with production code. The insight wasn't that contests are easy—they're not. It's that contest problems have clear specifications, deterministic verification, and isolated scope. Real software engineering demands understanding system context, navigating technical debt, and making architectural tradeoffs across codebases evolved over years.

SWE-bench exposed this gap systematically. Even frontier models struggle with real GitHub issues because production software exists in complex ecosystems where the "correct" solution depends on constraints never written down.

**[Week 4](/cs249r_fall2025/blog/2024/09/24/performance-engineering/)** showed us production reality at Google scale with ECO. CPU performance optimization isn't just about finding faster algorithms—it's about validation pipelines, continuous monitoring, rollback mechanisms, and human review. ECO made 6,400 commits in production, saving 500,000 CPU cores of compute. But every single change required human expert review.

The lesson: AI doesn't eliminate human expertise. It amplifies it. And the infrastructure to deploy AI-generated optimizations safely is often more complex than the optimization algorithms themselves.

**[Week 5](/cs249r_fall2025/blog/2024/10/01/gpu-performance-engineering/)** dove into GPU kernel optimization, where complexity actually favors AI. Kevin's multi-turn RL approach showed that mimicking expert iterative refinement beats single-shot generation. KernelBench revealed that even frontier models struggle to match PyTorch baselines, but the trajectory is clear: when human expertise is bottlenecked (GPU optimization experts are scarce and expensive), AI assistance becomes economically compelling.

**[Week 6](/cs249r_fall2025/blog/2024/10/08/ai-co-design-distributed-systems/)** marked a fundamental shift—from deterministic single-machine optimization to probabilistic distributed system adaptation. COSMIC's co-design of workload mapping and network topology demonstrated something crucial: optimal design requires reasoning across traditional abstraction boundaries. You cannot optimize workload and infrastructure separately. The artificial boundaries we created for human comprehension limit what's achievable.

The transition from [Week 3](/cs249r_fall2025/blog/2024/09/17/software-engineering-reality-gap/) to [Week 6](/cs249r_fall2025/blog/2024/10/08/ai-co-design-distributed-systems/) traced an arc: from explicit artifacts (code) to implicit behaviors (distributed system dynamics), from static optimization (fix the code once) to continuous adaptation (adjust to changing conditions), from testing (does it work?) to formal reasoning (can we prove properties hold?).

### Phase 2: AI for Architecture (Weeks 7-10)

Architecture forced us to confront knowledge that exists nowhere in written form—the tacit expertise accumulated by senior architects through decades of building systems.

**[Week 7](/cs249r_fall2025/blog/2024/10/15/tacit-knowledge-architecture/)** asked the fundamental epistemological question: How do AI agents learn what was never written down? We examined two approaches. Concorde encodes domain knowledge explicitly through analytical models (roofline, queueing theory) combined with ML for second-order effects. ArchGym creates experiential learning environments where agents develop intuition through exploration.

Both work, but they capture fundamentally different types of knowledge. Concorde represents what we *can* articulate. ArchGym attempts to learn what we *cannot*. The gap between them defines the frontier of current capabilities.

**[Week 8](/cs249r_fall2025/blog/2024/10/22/mapping-codesign-reasoning/)** introduced **co-design reasoning**—the first type of tacit architectural knowledge. Through the lens of hardware/software mapping, we saw how circular dependencies emerge: tile sizes depend on memory hierarchy, which depends on access patterns, which depend on dataflow, which depends on bandwidth, which depends on tile sizes. You're back where you started.

This isn't just hard. It's a different kind of problem. Traditional optimization assumes you can decompose into independent subproblems. Co-design problems resist decomposition. Everything depends on everything else.

DOSA and AutoTVM showed contrasting approaches: encode relationships explicitly and use gradients (analytical), or learn from experience and generalize (experiential). Neither fully solves the problem. Both reveal what solving it would require.

**[Week 9](/cs249r_fall2025/blog/2024/10/29/week-9-memory-systems-prediction/)** examined **predictive reasoning**—the second type of tacit knowledge. Memory system architects must design for access patterns they cannot fully observe or characterize. The patterns are sparse (1% signal, 99% noise), heterogeneous (different workloads behave completely differently), and time-sensitive (predict too early or too late and prefetching fails).

The contrast between learned prefetchers and learned indexes was illuminating. Prefetching struggles because patterns are unstable and timing is critical. Learned indexes succeed because data distributions are relatively stable and timing is flexible. The lesson: ML works when patterns exist and remain relatively constant. When patterns shift continuously or timing constraints are nanosecond-scale, traditional approaches often win.

**[Week 10](/cs249r_fall2025/blog/2024/11/05/week-10-optimizing-optimizers/)** explored **adaptive reasoning**—the third type of tacit knowledge. LLM serving systems must continuously adjust as conditions change: workload patterns shift, resource needs emerge during execution (KV-cache grows with every token), and optimal strategies evolve. Learning to rank treats scheduling as a continuously learning system. Text-to-text regression shows that semantic understanding of configurations outperforms numerical feature engineering.

Here's what made [Week 10](/cs249r_fall2025/blog/2024/11/05/week-10-optimizing-optimizers/) unique: **nobody has decades of experience**. LLM serving at scale only emerged 2-3 years ago. The tacit knowledge doesn't exist yet—it's being created right now through current experience. This creates both challenge (no established playbook) and opportunity (humans and AI learning together, systems that explain their own behavior, optimization through semantic understanding rather than black-box tuning).

The progression from [Week 7](/cs249r_fall2025/blog/2024/10/15/tacit-knowledge-architecture/) to [Week 10](/cs249r_fall2025/blog/2024/11/05/week-10-optimizing-optimizers/) revealed that architectural thinking isn't monolithic. It's a collection of distinct reasoning types:
- **Co-design**: Handle circular dependencies
- **Predictive**: Design for uncertain futures with incomplete information  
- **Adaptive**: Continuously adjust as conditions change

Current AI systems possess fragments of these capabilities but don't integrate them. Analytical models (like DOSA) encode structural understanding but lack adaptation. Learning-based approaches (like AutoTVM, Learning to Rank) recognize patterns but need structural guidance. The path forward requires knowing when to apply which type of reasoning.

### Phase 3: AI for Chip Design (Weeks 11-13)

Chip design confronted us with the irrevocability constraint: once you tape out, you can't patch hardware. Software engineers fix bugs with updates. Hardware engineers recall products and lose hundreds of millions of dollars.

**[Week 11](/cs249r_fall2025/blog/2024/11/14/week-11-part-2-benchmarking-llms-hardware/)** established the stakes. RTL generation isn't just about writing syntactically correct Verilog. It's about creating designs that synthesize efficiently, meet timing, physically realize, and work correctly. Multi-stage feedback loops mean problems discovered in physical design (weeks later) require architectural changes (restart from scratch). Benchmarking is fundamentally harder than software because correctness is necessary but not sufficient—performance, power, and area all matter, and you only know final quality after months of implementation.

**[Week 12](/cs249r_fall2025/blog/2024/11/19/week-12-physical-design-bottleneck/)** revealed the constraint inversion: at modern process nodes (5nm, 3nm, beyond), physical design limitations fundamentally constrain what architectures are viable. Wire delay exceeds gate delay. Power delivery limits density. Routing congestion constrains connectivity. Physics dominates.

You cannot design architecture independently from physical implementation anymore. But physical design takes months. This creates a feedback loop crisis: by the time you discover your architecture won't physically realize, you've invested months. With a 2-3 year design cycle, you can explore maybe 10-20 architectural alternatives—sampling 10^-13 of the design space.

The philosophical divide between RL-based placement and GPU-accelerated optimization (DREAMPlace) crystallizes a broader tension: learn strategies through experience versus encode domain knowledge explicitly. Both aim to close feedback loops from months to hours. Neither fully succeeds yet. But both suggest directions for AI's real opportunity—not autonomous chip design, but enabling rapid exploration of physically-viable architectures.

**[Week 13](/cs249r_fall2025/blog/2024/11/26/week-13-verification-trust-problem/)** closed the loop with verification: does the chip actually work correctly? The state space explosion means a simple 32-bit processor has more possible states than there are atoms in 10^3,700 universes. You cannot test your way to correctness. Formal verification offers mathematical proof but faces scalability limits and the specification problem (who verifies the specification?).

LLM-assisted verification promises to lower barriers—generating assertions from natural language properties, suggesting common properties for design patterns, accelerating debug. But it introduces the circular verification problem: if AI helps design and verify chips, how do we ensure we're not systematically introducing correlated errors?

The trust problem pervades Phase 3. We need validation at every stage, but the irrevocability constraint means we can't afford to be wrong. Trust must be earned through diversity (multiple independent approaches), transparency (make reasoning visible), bounded domains (use AI only for well-defined tasks), and empirical validation (silicon remains the final arbiter).

## The Five Fundamental Challenges: A Systems Perspective

Stepping back from the week-by-week narrative, five meta-challenges emerged that cut across all domains:

<div class="mermaid">
graph TD
    A[Five Fundamental Challenges] --> B[1. Feedback Loop Crisis<br/>Information arrives too late]
    A --> C[2. Tacit Knowledge<br/>Expertise never written down]
    A --> D[3. Trust & Validation<br/>How do we know it's correct?]
    A --> E[4. Co-Design Boundaries<br/>Everything depends on everything]
    A --> F[5. Determinism to Dynamism<br/>Static vs continuous adaptation]
    
    style A fill:#1a365d,color:#fff
    style B fill:#2563eb,color:#fff
    style C fill:#7c3aed,color:#fff
    style D fill:#dc2626,color:#fff
    style E fill:#059669,color:#fff
    style F fill:#d97706,color:#fff
</div>

### Challenge 1: The Feedback Loop Crisis

At every layer, slow feedback loops limit iteration:
- **Software**: ECO needs weeks of validation before deployment
- **GPU kernels**: Profile, refine, repeat—hours per iteration
- **Architecture**: Physical design feedback takes months
- **Verification**: Bugs discovered late are exponentially expensive

The common pattern: critical information arrives too late to inform decisions. Architecture decisions made without knowing physical realizability. Design choices made without verification feedback. Optimizations deployed without understanding production impact.

**AI's opportunity**: Close feedback loops by predicting outcomes faster. Not perfect accuracy—directional correctness is often sufficient. If a fast model can predict "Design A will likely meet timing but Design B won't," that's actionable guidance even if the frequency predictions are imprecise.

But there's a deeper insight: maybe we're optimizing the wrong thing. Instead of making slow processes faster, should we redesign processes to provide continuous feedback? Verification-in-the-loop rather than verification-at-the-end. Physical-awareness during architectural design rather than discovering constraints months later. Systems designed for AI-assisted workflows rather than AI retrofitted into human workflows.

### Challenge 2: The Tacit Knowledge Problem

The most valuable insights about system design exist only in experienced architects' heads:
- Memory system experts "just know" which patterns are worth optimizing for
- Physical designers have intuition about what floorplans will route well
- Verification engineers recognize which properties are important to check
- Performance engineers understand when to trust models versus empirical data

This knowledge was developed through decades of seeing what works and what fails. It's relational (how components interact), context-dependent (when strategies apply), and often subconscious (experts struggle to articulate their reasoning).

We identified three types of tacit architectural reasoning:
- **Co-design reasoning**: Handle circular dependencies where you cannot optimize components independently
- **Predictive reasoning**: Design for uncertain futures with fundamentally incomplete information
- **Adaptive reasoning**: Continuously adjust as conditions change, learning from live system behavior

<div class="mermaid">
graph LR
    subgraph CoDesign["Co-Design Reasoning"]
    A1[Tile Size] --> A2[Memory]
    A2 --> A3[Access Patterns]
    A3 --> A4[Dataflow]
    A4 --> A1
    end
    
    subgraph Predictive["Predictive Reasoning"]
    B1[Incomplete<br/>Information] --> B2[Pattern<br/>Recognition]
    B2 --> B3[Informed<br/>Bets]
    end
    
    subgraph Adaptive["Adaptive Reasoning"]
    C1[Observe] --> C2[Learn]
    C2 --> C3[Adjust]
    C3 --> C1
    end
    
    style CoDesign fill:#e8f5e9
    style Predictive fill:#fff3e0
    style Adaptive fill:#e3f2fd
</div>

Current AI approaches struggle with all three. Supervised learning can't easily learn reasoning that experts can't articulate. Reinforcement learning requires expensive exploration and struggles with sparse rewards. Analytical models work when we can codify relationships but miss emergent behaviors.

**The path forward**: Hybrid approaches that combine structure and learning. Concorde shows how to compose analytical models (first principles) with ML (empirical corrections). Kevin demonstrates learning iterative refinement strategies rather than one-shot generation. Text-to-text regression reveals semantic understanding beating numerical feature engineering.

But there's a humbling realization: some knowledge may remain tacit. The philosophical frameworks about where to locate complexity, the intuitions about which design patterns will age well, the judgment calls under uncertainty—these may always require human architects. Architecture 2.0 isn't about eliminating human expertise. It's about creating interfaces for human-AI collaboration where agents handle systematic exploration and humans provide philosophical guidance.

### Challenge 3: Trust and Validation

At every layer, we confronted the question: How do we know AI-generated designs are correct?

The irrevocability constraint makes this existential. Software bugs are fixable. Hardware bugs cost millions. But the trust problem goes deeper than just avoiding mistakes:

**Circular validation**: If AI generates RTL and AI generates verification assertions, and both misinterpret the specification identically, verification will pass despite the design being wrong. Using AI to check AI's work doesn't eliminate errors if both make correlated mistakes.

**Simulation-reality gaps**: Models that predict physical design outcomes must be validated against actual implementations. But you only know ground truth after months of implementation. Fast evaluation is inaccurate. Accurate evaluation is too slow for exploration.

**Black-box reasoning**: When an RL agent places macros or a learned policy schedules requests, we see outputs but not reasoning. This makes debugging hard and trust harder. If something goes wrong, we don't know why or how to fix it.

The approaches that work:
- **Diversity**: Use multiple independent tools, different AI models, different approaches. Cross-check for consistency. If multiple independent methods agree, confidence increases.
- **Transparency**: Analytical methods (DREAMPlace) are auditable—you can inspect the objective function. Learned policies (RL placement) are black boxes. For production deployment, transparency often trumps raw performance.
- **Bounded domains**: Apply AI assistance only for well-defined, limited-scope tasks where validation is straightforward. Use it for non-critical modules while using traditional methods for critical paths.
- **Empirical validation**: Ultimately, trust comes from building systems and testing them extensively. No amount of modeling eliminates this final step.

But here's the insight that matters: **trust isn't binary**. You don't need perfect confidence to make progress. You need enough confidence to make the next decision. If AI can provide "Design A is probably better than Design B" with 80% confidence, that's sufficient to guide exploration even if you'll validate thoroughly before committing.

The future of trustworthy AI for systems: not autonomous design, but decision support that amplifies human judgment.

### Challenge 4: Co-Design Across Boundaries

The artificial boundaries we created for human comprehension—abstraction layers separating software from architecture from physical implementation—limit what's achievable.

We saw this escalate across the course:
- **[Week 6](/cs249r_fall2025/blog/2024/10/08/ai-co-design-distributed-systems/)**: COSMIC co-designs workload mapping and network topology. Optimizing either independently leaves performance on the table.
- **[Week 8](/cs249r_fall2025/blog/2024/10/22/mapping-codesign-reasoning/)**: Hardware/software mapping creates circular dependencies where tile sizes, memory hierarchy, dataflow, and bandwidth constraints form an interdependent web.
- **[Week 10](/cs249r_fall2025/blog/2024/11/05/week-10-optimizing-optimizers/)**: LLM serving demands co-optimizing model architecture, system software, and hardware together. Request scheduling depends on model behavior depends on hardware capabilities depends on scheduling decisions.
- **[Week 12](/cs249r_fall2025/blog/2024/11/19/week-12-physical-design-bottleneck/)**: Architecture, physical layout, and workload characteristics form a three-way co-design problem. You cannot design architecture without knowing physical constraints. You cannot optimize physical layout without understanding workload priorities. You cannot characterize workloads without knowing what architecture will run them.

Traditional approaches solve these problems sequentially: design architecture, then implement it, discover problems, iterate. When iterations take months and cost millions, you can only afford a few iterations per generation.

**AI's opportunity**: Reason across boundaries simultaneously. Not replacing human decision-making, but exploring the coupled space faster. "If I make the cache this size, what mappings become possible? If I optimize for these mappings, what does that imply about the hardware I should build? If I build that hardware, will my target workloads run efficiently?"

But there's a deeper challenge: current ML frameworks assume you can define a clear objective function and search for solutions that maximize it. Co-design problems don't work this way. The objective itself changes depending on design choices you haven't made yet. The evaluation function depends on decisions you're trying to make.

This suggests we need new optimization frameworks that handle coupled objectives, emergent constraints, and circular dependencies. Not just better search algorithms within existing paradigms, but new paradigms that match the structure of real design problems.

### Challenge 5: From Determinism to Dynamism

The progression from Phase 1 to Phase 2 to Phase 3 traced an arc from deterministic (software, where code either works or doesn't) to probabilistic (distributed systems, where behavior emerges from interactions) to irrevocable (hardware, where mistakes are permanent).

But there's another dimension: from static optimization (find the best solution once) to continuous adaptation (adjust as conditions change). This distinction matters because it determines what role AI can play:

**Static optimization domains**:
- Compiler optimization: analyze code, apply transformations, emit binary
- Physical design: place macros, route nets, verify timing
- RTL generation: translate specification to hardware description

**Here**, AI augments human expertise by exploring vast design spaces and suggesting optimizations humans might miss. Success means finding better solutions faster. The goal is a better static artifact.

**Dynamic adaptation domains**:
- Distributed system scheduling: workload patterns shift continuously
- LLM serving: resource needs emerge during execution, optimal strategies evolve
- Power management: voltage/frequency decisions depend on thermal state and workload

**Here**, AI must learn and adapt continuously. Success means maintaining performance as conditions change. The goal isn't a static solution but a policy that adjusts.

The insight: these domains need fundamentally different AI approaches. Static optimization benefits from analytical methods, careful search, and extensive validation. Dynamic adaptation requires online learning, safe exploration, and graceful degradation.

Current AI research often conflates these. Papers show offline learning on fixed datasets, then claim the approach will work for online adaptation. But online adaptation faces exploration-exploitation tradeoffs, distribution shift, delayed rewards, and safety constraints that offline learning never encounters.

**The path forward**: Recognize which type of problem you're solving and design AI approaches accordingly. Don't apply static optimization techniques to dynamic adaptation domains. Don't require continuous adaptation when static optimization suffices. Match the AI approach to the problem structure.

## Synthesizing Insights: What Makes This Hard?

Stepping back from specific technical challenges, what fundamental properties of computer systems make AI-assisted design genuinely difficult?

<div class="mermaid">
graph TD
    A[Why AI for Systems<br/>is Fundamentally Hard] --> B[1. Circular<br/>Dependencies]
    A --> C[2. Emergent<br/>Behavior]
    A --> D[3. Multi-Objective<br/>Optimization]
    A --> E[4. Incomplete<br/>Information]
    A --> F[5. Temporal<br/>Dynamics]
    A --> G[6. Scale<br/>Dependence]
    A --> H[7. Irrevocability]
    
    style A fill:#1a365d,color:#fff
    style B fill:#dc2626,color:#fff
    style C fill:#7c3aed,color:#fff
    style D fill:#059669,color:#fff
    style E fill:#d97706,color:#fff
    style F fill:#2563eb,color:#fff
    style G fill:#db2777,color:#fff
    style H fill:#0891b2,color:#fff
</div>

### Property 1: Circular Dependencies

Traditional optimization assumes you can decompose problems into independent subproblems, optimize each, and combine the results. But many systems problems don't decompose:
- Compiler design: register allocation ↔ instruction scheduling  
- Database systems: index design ↔ query optimization
- Hardware mapping: tile sizes ↔ memory hierarchy ↔ access patterns ↔ dataflow
- Chip design: architecture ↔ physical layout ↔ workload characteristics

Each decision constrains and is constrained by every other decision. You cannot fix one variable and optimize the rest. The circular structure means traditional optimization techniques fail. You need approaches that reason about the coupled space simultaneously.

**This is fundamentally different from the pattern matching tasks that current ML excels at.** Image classification doesn't have circular dependencies—a cat is a cat regardless of other objects in the image. System design has deep interdependencies where optimal choices for one component depend on choices for all other components.

### Property 2: Emergent Behavior

System behavior emerges from interactions between components in ways you cannot predict from local information:
- Distributed systems: throughput emerges from workload placement, network topology, congestion patterns
- Memory hierarchies: performance emerges from cache design, access patterns, prefetching strategies  
- Physical design: timing closure emerges from placement, routing, power delivery, thermal effects

You need global understanding to predict system-level properties. But global understanding requires simulating or analyzing the complete system, which is expensive.

**Current ML typically learns from local patterns.** Transformers have attention mechanisms that consider context, but they're designed for sequences with relatively local dependencies (language, time series). System behavior can have long-range, non-obvious dependencies where changes in one module affect seemingly unrelated modules through subtle interaction chains.

### Property 3: Multi-Objective Optimization

Systems never optimize for a single metric:
- Performance vs power vs area (the "PPA" tradeoff)  
- Throughput vs latency vs fairness (distributed systems)
- Accuracy vs speed vs memory footprint (ML inference)
- Functionality vs verifiability vs maintainability (software)

Worse, objectives often conflict. The highest-performance solution wastes power. The most general design sacrifices efficiency. Objectives have different units and importance depends on context.

**Standard ML loss functions don't capture this.** You can't just weight objectives and sum them—the relative importance changes with constraints that aren't known until later. And there's rarely a single "optimal" solution—there's a Pareto frontier of tradeoffs where improving one objective hurts others.

Human designers navigate these tradeoffs through judgment, philosophical preferences, and organizational constraints. Can AI learn this kind of meta-reasoning? Or will humans always make the final tradeoff decisions while AI explores the feasible space?

### Property 4: Incomplete Information

System designers face irreducible uncertainty:
- Workloads that don't exist yet (designing hardware for ML models that won't be invented for 3 years)
- Emergent application patterns (who predicted transformers would dominate in 2024 back in 2020?)
- Manufacturing variation (each chip slightly different despite same design)
- Deployment conditions (datacenters in different climates, network conditions that vary)

You cannot optimize for known requirements. You must make informed bets about uncertain futures.

**ML typically assumes train and test distributions match.** When distributions shift, learned models fail. But system design is inherently about designing for distributions you haven't seen. The robustness challenge isn't handling outliers in a known distribution—it's handling entirely new distributions.

### Property 5: Temporal Dynamics

Systems exist in time in ways that complicate optimization:
- Timing constraints: prefetching is useless if predictions arrive nanoseconds too late
- Temporal dependencies: decisions made early affect what's possible later (path dependence)
- Adaptation timescales: some decisions change slowly (architecture), others continuously (scheduling)
- Learning from delayed feedback: actions taken now have consequences hours or months later

**Most ML treats time as just another feature.** But time is fundamental to whether optimizations work. In systems, timing isn't a property you can model approximately—it's a hard constraint that determines whether solutions are viable.

### Property 6: Scale Dependence

What works at small scale fails at large scale:
- Algorithms with good asymptotic complexity but high constants (fine for n=100, terrible for n=10^9)
- Designs that function correctly but don't meet timing at scale (too much wire delay)
- Protocols that work in simulations but create congestion cascades in production

**Worse, scale changes which problems matter.** At small scale, algorithm choice dominates. At large scale, data movement dominates. At datacenter scale, energy dominates. The optimization objective changes with scale.

ML models trained on small examples don't automatically generalize to scale. And you can't just train on large examples—simulation is too expensive and real data is scarce.

### Property 7: Irrevocability

Some decisions can't be undone:
- Tape out a chip with bugs: costly recall or live with issues  
- Deploy hardware architecture: no patching silicon
- Set ISA: decades of software compatibility depend on it
- Choose process node: committed for 2-3 year design cycle

**This changes the risk calculus entirely.** In software, you can ship fast and fix bugs later. In hardware, you get one shot. This demands higher confidence before committing, more validation, and conservative design margins.

AI must not just optimize for expected value. It must bound worst-case behavior and understand the cost of different failure modes. Being wrong about software optimization might waste compute. Being wrong about hardware design wastes millions of dollars and years of time.

## Rethinking AI for Systems: A Methodological Framework

Given these challenges, what would it mean to design AI approaches specifically for system design, rather than adapting techniques from other domains?

### Principle 1: Embrace Hybrid Approaches

The dichotomy between "analytical models" and "learned policies" is false. Real progress requires composition:

**For co-design reasoning**: Use analytical models to encode first principles (physics, queuing theory, fundamental tradeoffs) and ML to capture second-order interactions that resist analytical modeling. Concorde demonstrates this beautifully—5 orders of magnitude speedup by combining what we know explicitly (analytical) with what we learn empirically (ML).

**For predictive reasoning**: Use learned prefetchers for pattern recognition but traditional heuristics for timing control. Semantic models (text-to-text regression) for high-level understanding but numerical models for precise predictions. Don't replace 50 years of systems knowledge—augment it.

**For adaptive reasoning**: Use RL for exploration but provide structure through action spaces, reward shaping, and safety constraints informed by domain knowledge. Learning to rank combines learned preferences with explicit constraints about fairness and safety.

The pattern: **use structure when you have it, learn when you don't**. Don't force every problem into pure learning or pure analytical modeling. The art is knowing which representation suits which aspect of the problem.

### Principle 2: Design for Continuous Feedback

Instead of speeding up existing flows, redesign flows for continuous feedback:

**Verification-in-the-loop**: Instead of verifying after you're done, verify continuously as you design. Generate assertions incrementally. Check properties as you write RTL. Catch bugs immediately instead of weeks later.

**Physical-awareness during architecture**: Instead of discovering physical problems months later, predict physical realizability during architectural design. Fast models that give directional guidance: "This communication pattern will struggle with wire delay. Consider co-locating these units."

**Co-design exploration**: Instead of sequential design (architecture → implementation → discovery of problems), explore the coupled space. "If I make these architectural choices, what physical designs become viable? If I target these physical constraints, what architectures work?"

This requires new tools designed for AI-assisted workflows, not AI retrofitted into human workflows. The tooling determines what's possible.

### Principle 3: Separate Concerns by Role, Not by Tool

The question isn't "should AI design chips autonomously?" It's "what role does AI play in the design process?"

<div class="mermaid">
graph TD
    subgraph AI["AI Roles"]
    A1[🔍 Explorer<br/>Search vast spaces<br/>Find patterns]
    A2[✓ Validator<br/>Verify properties<br/>Find counterexamples]
    end
    
    subgraph Human["Human Roles"]
    H1[🧭 Guide<br/>Philosophical frameworks<br/>Tradeoff decisions]
    H2[⚖️ Arbiter<br/>Risk assessment<br/>Final commitments]
    end
    
    A1 <-->|"presents options"| H1
    H1 <-->|"guides search"| A1
    A2 <-->|"reports findings"| H2
    H2 <-->|"sets criteria"| A2
    
    style AI fill:#e3f2fd
    style Human fill:#fff3e0
</div>

**AI as explorer**: Systematically search vast design spaces humans can't comprehend. Find interesting regions. Identify patterns. Present options.

**Humans as guides**: Provide philosophical frameworks, make tradeoff decisions, supply context, validate results, handle edge cases.

**AI as validator**: Verify properties, find counterexamples, check consistency, identify coverage gaps. Amplify formal methods.

**Humans as arbiters**: Decide when validation is sufficient, determine acceptable risk, make final commitments.

The collaboration is multiplicative, not additive. AI explores spaces humans couldn't search. Humans guide exploration toward meaningful regions. Together they achieve what neither could alone.

But this requires new interfaces. Current tools assume either "human does everything" or "AI does everything." We need interfaces for fluid collaboration where control shifts dynamically based on the task.

### Principle 4: Match Approach to Problem Structure

Different system design problems need different AI approaches:

**For problems with circular dependencies** (mapping, co-design): Use methods that reason about the coupled space. Gradient-based optimization if you can make the problem differentiable. Game-theoretic approaches for multi-agent design. Meta-learning to discover optimization strategies.

**For problems with emergent behavior** (performance, distributed systems): Use simulation + surrogate models. Fast approximate evaluation to guide search. Bayesian optimization with uncertainty quantification. Don't trust predictions—validate on full simulation for promising candidates.

**For problems with incomplete information** (architecture for future workloads): Design for robustness over optimality. Multi-task learning across diverse scenarios. Sensitivity analysis to understand what breaks designs. Graceful degradation strategies.

**For problems with temporal dynamics** (scheduling, adaptation): Use online learning with safe exploration. Counterfactual reasoning to disentangle cause and effect. Meta-learning to adapt quickly to distribution shift.

**For irrevocable decisions** (chip design): Use conservative design margins. Formal verification where possible. Extensive validation before committing. Worst-case analysis, not just expected value.

Don't apply the same ML hammer to every problem. Understand the problem structure and choose approaches that match it.

### Principle 5: Build on Decades of Systems Knowledge

The biggest mistake would be assuming AI makes 50 years of systems research irrelevant. The wisdom accumulated by the systems community—about abstraction, modularity, end-to-end principles, measurement methodology, evaluation—remains valid.

**What changes**: The bottlenecks shift. Design space exploration that was intractable becomes feasible. Optimizations too complex for humans become accessible. Cross-layer reasoning that violated abstraction boundaries becomes possible.

**What doesn't change**: The fundamental principles about what makes systems robust, maintainable, debuggable, evolvable. The need for clear specifications. The importance of evaluation methodology. The reality that "it works on my machine" proves nothing.

AI should accelerate progress, not throw away decades of accumulated understanding. The LLM that reinvents TCP from first principles because it never read the original papers will make all the mistakes we made in the 1980s.

### Principle 6: Acknowledge What We Don't Know

Humility matters. There are questions we can't answer yet:

**Can AI learn tacit architectural knowledge from examples?** Or does some knowledge fundamentally resist learning—requiring human intuition developed through decades of experience?

**When does AI generalize versus memorize?** If an LLM generates a correct FIFO because it saw thousands of FIFOs in training, is that generalization or memorization? How do we tell?

**Where should human judgment remain essential?** Not just because AI can't do it yet, but because human oversight is inherently necessary? The philosophical tradeoffs, the risk decisions, the accountability?

**How do we validate AI-assisted designs without circular reasoning?** If AI helps design and verify, are we systematically introducing correlated errors?

These aren't just open research questions. They're foundational questions about the nature of design, the limits of learning, and the role of human expertise.

## What We Heard from Industry

One of the privileges of teaching this course was bringing in practitioners who live these challenges daily. Nine industry experts joined us across the semester, and their perspectives consistently reinforced one theme: **the gap between research papers and production reality is vast**.

[Amir Yazdanbakhsh](/cs249r_fall2025/blog/2024/09/24/performance-engineering/) from Google DeepMind told us that ECO's infrastructure for deploying optimizations safely was more complex than the optimization algorithms themselves. Every AI-generated change required human expert review. The lesson: production isn't about clever algorithms. It's about trust, validation, and integration with existing workflows.

[Martin Maas](/cs249r_fall2025/blog/2024/10/08/ai-co-design-distributed-systems/) from Google DeepMind emphasized that distributed systems require *continuous adaptation*, not one-shot optimization. The environment changes. Workloads shift. What worked yesterday might fail tomorrow. AI for systems can't just find good solutions—it needs to keep finding them as conditions evolve.

[Suvinay Subramanian](/cs249r_fall2025/blog/2024/10/15/tacit-knowledge-architecture/) from Google's TPU team articulated something we rarely see in papers: hardware design involves "subjective bets" about where to locate complexity. Google's philosophy—simpler hardware, more complex software—isn't mathematically derived. It's a bet about organizational capabilities and future flexibility. How does an AI agent learn these philosophical frameworks?

[Milad Hashemi](/cs249r_fall2025/blog/2024/10/29/week-9-memory-systems-prediction/) explained why learned prefetchers that look great in papers struggle in production. The patterns are too sparse, too noisy, and too time-sensitive. When you need predictions in nanoseconds and accuracy in the 99th percentile, the gap between "works in simulation" and "works in silicon" becomes a chasm.

[Esha Choukse](/cs249r_fall2025/blog/2024/11/05/week-10-optimizing-optimizers/) from Microsoft Research grounded our discussion of LLM serving in the reality of operating at scale. The KV-cache grows with every token. Memory becomes the bottleneck. Request patterns are unpredictable. The neat abstractions in papers dissolve when you're running inference for millions of users.

[Mark Ren](/cs249r_fall2025/blog/2024/11/14/week-11-part-2-benchmarking-llms-hardware/) from NVIDIA painted a picture of an EDA industry at an inflection point. Traditional tools encode decades of expertise, but they're struggling with modern design complexity. The opportunity for AI isn't replacing that expertise—it's augmenting it, using differentiable optimization where analytical models exist and RL where the search space is too large for hand-crafted heuristics.

[Kartik Hegde](/cs249r_fall2025/blog/2024/11/26/week-13-verification-trust-problem/) from ChipStack brought the verification perspective: AI can lower barriers to formal methods by generating assertions from natural language. But generated assertions must still be validated, and validation requires expertise. AI augments verification engineers; it doesn't replace them.

The consistent message across all these conversations: **AI for systems is about collaboration, not automation**. The practitioners who are actually deploying these techniques aren't trying to remove humans from the loop. They're trying to make humans more effective by handling the tedious parts, exploring spaces humans can't search, and providing decision support rather than decisions.

## A Note on Model Size: Frontier vs. Specialized

One question we didn't fully resolve: do you need GPT-4 to design chips, or would a fine-tuned 7B model work better?

The honest answer is "it depends." Frontier models bring broad knowledge and cross-domain reasoning—useful when translating natural language specs to formal properties or debugging across abstraction layers. But they're slow (milliseconds when prefetching needs nanoseconds), expensive (prohibitive at datacenter scale), and opaque (hard to audit for safety-critical applications).

Specialized smaller models trained on domain-specific data might outperform frontier models for narrow tasks. Do you really need to understand Shakespeare to optimize memory access patterns? Probably not.

The practical path forward: use frontier models where their breadth matters (specification understanding, novel scenarios, interactive assistance), specialized models where latency and cost matter (real-time decisions, production deployment), and distillation to transfer frontier model reasoning into efficient specialized models. Match the tool to the task.

## A Roadmap for the Field: The Next Five Years

Given what we've learned, what should the research community prioritize? Where are the highest-leverage opportunities?

<div class="mermaid">
graph LR
    subgraph Near["Near-Term (1-2 Years)"]
    N1[Benchmarks]
    N2[Surrogate Models]
    N3[Collaboration Interfaces]
    end
    
    subgraph Medium["Medium-Term (2-4 Years)"]
    M1[Circular Dependency<br/>Methods]
    M2[Compositional<br/>Frameworks]
    M3[Trust & Validation]
    end
    
    subgraph Long["Long-Term (4+ Years)"]
    L1[Learning<br/>Reasoning Types]
    L2[Verification<br/>at Scale]
    L3[Self-Improving<br/>Systems]
    end
    
    Near --> Medium --> Long
    
    style Near fill:#e8f5e9
    style Medium fill:#fff3e0
    style Long fill:#ffebee
</div>

### Near-Term (1-2 Years): Building Foundations

**1. Benchmarks that measure genuine understanding, not memorization**
- End-to-end flows from specification to validated implementation
- Novel designs sufficiently different from training data to test generalization
- Metrics that predict real-world success, not just academic scores
- Open datasets for architectural exploration, physical design, and verification

[Week 11](/cs249r_fall2025/blog/2024/11/14/week-11-part-2-benchmarking-llms-hardware/) and [Week 13](/cs249r_fall2025/blog/2024/11/26/week-13-verification-trust-problem/) emphasized: evaluation methodology determines what progress looks like. Bad benchmarks lead research astray.

**2. Fast surrogate models for expensive simulations**
- Physical design: predict timing/routing without full place-and-route
- Performance: estimate behavior without cycle-accurate simulation  
- Power: model energy consumption from high-level descriptions

The feedback loop crisis demands faster evaluation. But fast models must be validated against ground truth continuously. The research question isn't just "can we build fast models?" but "how do we know when to trust them?"

**3. Human-AI collaboration interfaces**
- Tools designed for fluid control-sharing between human and AI
- Visualization of AI reasoning to support human oversight
- Mechanisms for humans to guide AI exploration toward meaningful regions
- Workflows that make AI assistance feel natural, not bolted-on

Current tools assume binary control: either human does everything or AI does everything. We need interfaces that support the spectrum between these extremes.

### Medium-Term (2-4 Years): Solving Core Challenges

**4. Methods for reasoning about circular dependencies**
- Differentiable co-design frameworks that handle coupled objectives
- Game-theoretic approaches for multi-agent system design
- Meta-learning to discover optimization strategies rather than just solutions

[Week 8's co-design reasoning](/cs249r_fall2025/blog/2024/10/22/mapping-codesign-reasoning/) showed circular dependencies are fundamental. Current optimization methods assume decomposability. We need new frameworks that match the problem structure.

**5. Compositional approaches that blend structure and learning**
- Frameworks that make it easy to encode domain knowledge where you have it
- Learning architectures that incorporate physical constraints, conservation laws, causality
- Methods that explain *why* optimizations work, not just *that* they work

Concorde and similar work show the power of composition. We need to systematize this rather than treating each instance as a custom one-off.

**6. Trust and validation frameworks for AI-assisted design**
- Diverse ensemble approaches to reduce correlated errors
- Formal methods for verifying learned components
- Methodologies for validating that AI assistance improves rather than harms quality

The trust problem will determine adoption. Technical capabilities mean nothing if practitioners don't trust the results.

### Long-Term (4+ Years): Transformative Capabilities

**A note to PhD students**: If you're starting your PhD now, these "long-term" problems aren't abstract future concerns—they're *your* problems. In 4-5 years when you graduate, industry and academia will need people who have deeply thought about these challenges. The near-term problems will be solved (or at least well-understood) by then. The researchers who will have the most impact are those working today on what the field will need tomorrow. These are the dissertation topics that will matter when you're on the job market.

**7. AI systems that learn types of reasoning, not just patterns**
- Co-design reasoning: handle circular dependencies
- Predictive reasoning: make informed bets about uncertain futures  
- Adaptive reasoning: continuous learning under distribution shift

We've characterized what these reasoning types require. Can we build AI systems that develop these capabilities? Or are they fundamentally beyond current ML paradigms?

**8. Verification and synthesis at scale**
- Formal verification that scales to billion-transistor designs
- Synthesis that optimizes across the full stack simultaneously  
- Proof techniques that work for AI-generated designs

[Week 13](/cs249r_fall2025/blog/2024/11/26/week-13-verification-trust-problem/) showed verification is the ultimate bottleneck. State space explosion is fundamental. Can we make breakthroughs in formal methods, or must we accept probabilistic guarantees?

**9. Self-improving systems that learn from deployment**
- Production systems that adapt based on actual workload behavior
- Designs that get better through field experience
- Feedback loops from silicon back to architecture  

Currently, we design once and deploy forever. What if systems could learn from deployment? Not just adapting runtime behavior (which [Week 10](/cs249r_fall2025/blog/2024/11/05/week-10-optimizing-optimizers/) explored) but feeding insights back into future design iterations?

**10. Democratization: making AI-assisted design accessible**
- Open-source tools competitive with commercial EDA
- Educational platforms that teach AI-assisted design methodology
- Frameworks that work without requiring Google-scale infrastructure

Currently, only a few companies have the resources to effectively use AI for systems design. How do we broaden access without requiring massive infrastructure investment?

## Closing Thoughts: What Have We Actually Learned?

Thirteen weeks ago, we asked: Can AI agents become co-designers of computer systems?

The answer is yes—but with critical qualifications that reshape the question itself.

**AI can**:
- Explore design spaces too vast for human comprehension
- Find optimizations humans would never consider  
- Accelerate iteration by closing feedback loops
- Lower barriers to formal verification and sophisticated optimization
- Amplify human expertise by handling routine tasks

**AI cannot (yet)**:
- Replace the philosophical judgment about where to locate complexity
- Make tradeoff decisions when objectives conflict and priorities aren't quantifiable
- Develop the intuitive understanding that comes from decades of experience  
- Verify its own work without risking circular validation
- Design for radically uncertain futures where patterns from the past don't apply

**The frontier isn't autonomous AI designing systems alone**. It's human-AI collaboration where:
- AI explores, humans guide
- AI optimizes locally, humans reason globally  
- AI handles systematic search, humans apply judgment
- AI generates artifacts, humans validate and decide

This isn't a disappointing compromise. It's recognition that system design is fundamentally about judgment under uncertainty, tradeoffs among conflicting objectives, and bets about unknowable futures—domains where human cognition remains essential.

But the partnership is transformative. An architect working with AI assistance can explore design spaces that were previously intractable, validate ideas in hours that previously took months, and reason across abstraction boundaries that previously required separate expert teams.

**The course revealed five meta-insights**:

1. **Circular dependencies are fundamental**: Many real problems don't decompose into independent subproblems. AI must reason about coupled spaces.

2. **Tacit knowledge resists codification**: The most valuable expertise exists in experienced architects' intuitions. Learning from experience might work where explicit encoding fails.

3. **Trust requires validation at every layer**: The irrevocability constraint means we can't afford to be wrong. Trust must be earned through diversity, transparency, and empirical validation.

4. **Co-design across boundaries unlocks capability**: The artificial abstractions we created for human comprehension limit what's achievable. AI can reason across boundaries.

5. **The right abstraction for the problem matters**: Static optimization, dynamic adaptation, and co-design under uncertainty need fundamentally different AI approaches.

These insights point toward a future where:
- **Design tools** are built for AI-assisted workflows from first principles
- **Abstraction boundaries** become porous, allowing optimization across traditional layers
- **Feedback loops** operate at timescales matching decision-making  
- **Validation** is continuous and integrated, not staged and separate
- **Expertise** is amplified and democratized, not replaced or gatekept

## What We Didn't Cover

Intellectual honesty requires acknowledging scope. This course focused on AI for *performance-oriented* system design—making things faster, more efficient, more capable. We deliberately didn't cover:

- **AI for security**: Hardware security, side-channel analysis, secure enclave design
- **AI for reliability**: Fault tolerance, error correction, graceful degradation
- **AI for sustainability**: Carbon-aware design, lifecycle optimization, e-waste reduction
- **AI for other system layers**: Networking, storage systems, databases, operating systems
- **The societal implications**: Job displacement, concentration of capability, democratization vs. gatekeeping

These aren't less important—they're different courses. The frameworks we developed (co-design reasoning, trust through diversity, hybrid analytical-ML approaches) likely transfer, but the specific challenges differ.

## The Path Ahead

Architecture 2.0 isn't a destination. It's a direction of travel.

The field will evolve iteratively:
- **Phase 1**: AI assists with isolated tasks (generate RTL, optimize code, place macros)
- **Phase 2**: AI reasons across traditional boundaries (co-design workload and hardware, optimize from code to silicon)
- **Phase 3**: AI develops the types of reasoning that define architectural expertise (co-design, predictive, adaptive)

We're early in Phase 1, with glimpses of Phase 2. Phase 3 remains aspirational.

But the trajectory is clear. The techniques that work aren't those that replace human expertise. They're those that amplify it. The progress that matters isn't autonomous AI design. It's human-AI collaboration that achieves what neither could alone.

The questions that will determine success aren't just technical. They're about:
- What workflows make collaboration natural?
- How do we maintain trust as systems become more complex?
- Where should human judgment remain essential?  
- How do we train the next generation to work with AI co-designers?

**This course was preparation, not conclusion**. You've seen the landscape. You understand the challenges. You know where current capabilities fall short.

## What You Can Do This Week

Don't wait for the field to evolve. Start now:

1. **Pick one paper from this course and implement something**. Not just read—build. Clone a repo, run the code, modify it, break it, understand it deeply.

2. **Find your community**. Join the MLSys, ISCA, or MICRO communities. Follow researchers on social media. Attend reading groups. The field moves fast; staying connected matters.

3. **Identify your unique angle**. What domain expertise do you have that others don't? AI for systems needs people who understand specific application domains, not just ML generalists.

4. **Start a research notebook**. Document your ideas, experiments, and failures. The PhD students who succeed aren't smarter—they're more systematic about learning from what doesn't work.

5. **Talk to practitioners**. The gap between academic papers and production reality is vast. Find engineers at companies doing this work. Understand what problems they actually face.

Now the work begins.

The systems you design over the next decade will determine whether AI truly transforms computer architecture or remains a marginal tool for narrow applications. Whether the expertise accumulated over 50 years of systems research amplifies or atrophies. Whether the next generation of architects works with AI as partners or struggles against AI as competitors.

The choice is yours. The tools are emerging. The challenges are clear.

**Architecture 2.0 isn't about AI replacing architects. It's about architects who understand AI becoming more capable than any individual could be alone.**

Go build it.

---

*This synthesis reflects on the thirteen-week journey through AI for software, architecture, and chip design. For detailed technical content, see the individual week posts linked throughout. For course materials and future updates, see the [course schedule](/cs249r_fall2025/course/schedule/).*

*A note on timing: This was written in Fall 2024. The field of AI for systems is evolving rapidly—some techniques discussed here may already be outdated, while new capabilities may have emerged that weren't possible when this was written. The conceptual frameworks (types of reasoning, trust through diversity, hybrid approaches) should age better than specific technical approaches. If you're reading this in the future, use the frameworks to evaluate whatever new techniques have emerged.*




