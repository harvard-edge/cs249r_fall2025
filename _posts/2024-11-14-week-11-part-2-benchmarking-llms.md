---
layout: post
title: "Week 11 Part 2: The Data Challenge - How Do We Actually Measure AI's Ability to Design Hardware?"
date: 2024-11-14
author: "Vijay Janapa Reddi"
categories: [hardware, eda, benchmarks, datasets]
permalink: /blog/2024/11/14/week-11-part-2-benchmarking-llms-hardware/
---

*Note: I wasn't in class this week, but the papers you read raise fundamental questions about how we evaluate AI systems for chip design. This post explores the challenges of creating meaningful benchmarks for hardware generation.*

## The Evaluation Problem

Last week, Mark Ren told us about the scaling crisis in chip design and why AI might help. This week's papers ask a more fundamental question: **How do we actually know if AI is getting better at chip design?**

For code generation in software, we have benchmarks like HumanEval, MBPP, and SWE-bench. You give the model a problem description, it generates code, you run tests, and you get a pass/fail result. Simple, right?

Hardware design is different. And the differences matter.

## Why Hardware Benchmarks Are Hard

### The Specification Problem

In [Part 1](/blog/2024/11/12/eda-fundamentals-code-to-silicon/), we saw that RTL design involves translating architectural intent into precise hardware descriptions. But what constitutes a "correct" specification?

Consider this simple request: "Design a FIFO buffer."

The questions each discipline asks reveal how different the problem spaces are:

| **Software Engineer Asks** | **Hardware Engineer Asks** |
|---------------------------|---------------------------|
| What's the interface? | Which clock domain? |
| What should happen on overflow? | What's the reset behavior (sync vs async)? |
| What's the expected throughput? | Are we optimizing for area or speed? |
| | What's the power budget? |
| | Which standard cell library? |
| | What's the target frequency? |

The same natural language description can map to dozens of valid but fundamentally different hardware implementations. This is the **specification ambiguity problem**.

### The Correctness Problem

In software, you can usually test correctness by running the code. In hardware:

1. **Synthesis might fail**: The RTL might be syntactically correct but unimplementable
2. **Timing might not close**: The design might work functionally but be too slow
3. **Area might explode**: The design might be correct but use 10x more gates than necessary
4. **Power might be excessive**: The design might meet timing but draw too much current
5. **Testbench coverage matters**: Your tests might not exercise critical corner cases

You need to evaluate not just functional correctness, but also **implementability** and **quality of results (QoR)**.

### The Feedback Loop Problem

Remember from last week: chip design has an irrevocability constraint. You can't patch hardware after fabrication. This means the verification process is fundamentally different from software.

<div class="mermaid">
graph TD
    subgraph "Software Debugging Loop"
    A1[Write Code] --> A2[Run]
    A2 --> A3{Error?}
    A3 -->|Yes| A4[Fix]
    A4 --> A1
    A3 -->|No| A5[Done]
    end
    
    subgraph "Hardware Verification Loop"
    B1[Write RTL] --> B2[Synthesize]
    B2 --> B3[Check Timing]
    B3 --> B4[Simulate]
    B4 --> B5[Check Coverage]
    B5 --> B6[Place & Route]
    B6 --> B7[Physical Verify]
    B7 --> B8{Issue?}
    B8 -->|Yes| B9[Debug]
    B9 --> B1
    B8 -->|No| B10[Tape Out]
    end
    
    style A1 fill:#e8f5e9
    style A5 fill:#e8f5e9
    style B1 fill:#fff3e0
    style B10 fill:#A51C30,color:#fff
    style B8 fill:#ffebee
</div>

**Software cycle time: seconds to minutes**  
**Hardware cycle time: hours to days per iteration**

Any benchmark needs to capture this multi-stage feedback loop, not just "does it compile?"

## The Papers: Two Approaches to Benchmarking

This week's papers tackle different aspects of this evaluation challenge.

### Paper 1: Comprehensive Verilog Design Problems

*A Next-Generation Benchmark Dataset for Evaluating Large Language Models and Agents on RTL Design and Verification*

This paper addresses the **dataset quality problem**. Existing benchmarks like VerilogEval have serious limitations. Many problems are too simple, solvable through pattern matching alone. They have poor coverage, missing crucial tasks like verification, debugging, and optimization. The specifications are often ambiguous, mapping to multiple valid solutions without guidance on which to choose. And the feedback is binary - pass or fail - without any quality metrics to distinguish an elegant solution from a brute-force hack.

The key insight: **we need benchmarks that test the full spectrum of hardware design capabilities**, not just basic code generation.

What makes a good RTL benchmark problem?
1. **Realistic complexity**: Problems that mirror real design tasks
2. **Complete specifications**: Detailed enough to have unambiguous solutions
3. **Comprehensive test suites**: Coverage-driven verification
4. **Quality metrics**: Not just correctness, but PPA (Power, Performance, Area)
5. **Multi-step reasoning**: Tasks requiring design, verification, and debugging

Think back to [Week 7's discussion of tacit knowledge](/blog/2024/11/05/week-7-tacit-knowledge-architecture/). Many aspects of hardware design involve experience-based judgment. How do you encode that into a benchmark?

### Paper 2: Make Every Move Count - MCTS for RTL Generation

*LLM-based High-Quality RTL Code Generation Using Monte Carlo Tree Search*

This paper addresses the **search problem**. Even with good benchmarks, how do you generate high-quality RTL?

The key observation: **Hardware design is a search problem with delayed feedback**.

Monte Carlo Tree Search (MCTS) is a tree exploration algorithm originally developed for games like Go. It balances exploration of new design choices against exploitation of promising approaches, while maintaining lookahead to reason about future consequences. This makes it particularly relevant for RTL generation, where early decisions cascade through the entire design.

Why is MCTS relevant for RTL generation?

<div class="mermaid">
graph TD
    A[Natural Language<br/>Specification] --> B{Design<br/>Choice 1}
    B --> C[Register-based]
    B --> D[Combinational]
    C --> E{Design<br/>Choice 2}
    D --> F{Design<br/>Choice 2}
    E --> G[Synchronous Reset]
    E --> H[Asynchronous Reset]
    F --> I[Pipeline]
    F --> J[Non-pipeline]
    
    G --> K[Simulate &<br/>Synthesize]
    H --> K
    I --> K
    J --> K
    
    K --> L{Meets<br/>Constraints?}
    L -->|Yes| M[Valid Design]
    L -->|No| N[Backtrack]
    N -.-> B
    
    style A fill:#e9ecef
    style B fill:#A51C30,color:#fff
    style E fill:#A51C30,color:#fff
    style F fill:#A51C30,color:#fff
    style K fill:#fff3e0
    style M fill:#e8f5e9
    style N fill:#ffebee
</div>

At each node, you're making a design decision. But you don't know if it's good until you've completed the entire design and run synthesis. MCTS helps navigate this search space efficiently through a cycle of simulation (trying a design path), evaluation (scoring results based on PPA metrics), backpropagation (updating beliefs about which early decisions led to good outcomes), and selection (focusing future exploration on promising branches).

This is fundamentally different from greedy autoregressive generation (the standard LLM approach):

**Standard LLM approach:**
```
Generate token → Generate next token → Generate next token → ...
(no lookahead, no backtracking)
```

**MCTS approach:**
```
Explore multiple partial designs → Simulate outcomes → 
Learn which patterns work → Focus on promising directions
```

The MCTS approach explicitly models the fact that **early design decisions have far-reaching consequences** that aren't immediately apparent.

## The Deeper Tension: Benchmarks vs. Reality

Here's the uncomfortable truth: **good benchmarks might not reflect real design tasks**.

### The Training Data Contamination Problem

We discussed this back in [Week 3 with code generation](/blog/2024/09/17/week-3-code-optimization-paradox/). LLMs are trained on massive amounts of text from the internet: GitHub repositories with Verilog code, academic papers with RTL examples, documentation with common design patterns, Stack Overflow discussions about HDL quirks. All of this becomes part of the model's knowledge.

When you create a benchmark, how do you ensure it's testing true design capability rather than memorization?

For software, this is already a problem. For hardware, it's worse. There's less open-source HDL code available online since most professional designs are proprietary. The design space is more constrained - you can't just try random things and see what works. And verification is much harder to automate, making it difficult to validate novel approaches quickly.

### The Spec Quality Problem

In [Week 2](/blog/2024/09/08/week-2-fundamental-challenges/), we talked about the challenge of unclear specifications. Real-world design specs are often incomplete, missing critical corner cases. They're ambiguous, with multiple valid interpretations. They evolve as requirements change during the design process. And they're deeply context-dependent, relying on unwritten assumptions about the broader system.

But benchmark problems need clear, unambiguous specifications to enable automatic evaluation. This creates a fundamental gap:

| **Aspect** | **Benchmark Specs** | **Real-World Specs** |
|-----------|-------------------|-------------------|
| **Completeness** | Fully specified | Incomplete, missing corner cases |
| **Clarity** | Unambiguous | Multiple valid interpretations |
| **Stability** | Fixed and static | Evolving during design |
| **Context** | Self-contained | Deeply system-dependent |
| **Testability** | Verifiable automatically | Requires human judgment |

An AI that performs well on benchmarks might struggle with the messy reality of actual chip design.

### The Human-in-the-Loop Problem

Real hardware design is iterative and collaborative. Designers consult with verification engineers about corner cases. Architects provide feedback on microarchitecture choices. Physical design teams push back on unrealistic timing constraints. Customers clarify requirements as they better understand what's possible.

None of this appears in current benchmarks. We're testing **individual capability** when the real task requires **collaborative problem-solving**.

## Connecting to Our Course Themes

Let's revisit the three reasoning challenges we identified in Part 1:

### 1. Tacit Knowledge (Week 7)

Benchmarks can only test explicit knowledge. How do you benchmark "this design pattern usually causes timing issues in the place-and-route stage"?

The MCTS paper partially addresses this by incorporating synthesis feedback into the search process. But it still requires that knowledge to be learnable from the reward signal.

### 2. Co-design Reasoning (Week 8)

Remember the [circular dependencies in hardware-software co-design](/blog/2024/10/22/week-8-mapping-codesign/)? RTL design has similar circular dependencies:
- Clock frequency depends on critical path
- Critical path depends on implementation choices
- Implementation choices depend on timing constraints
- Timing constraints depend on target frequency

Good benchmarks need to test this co-design reasoning, not just isolated module generation.

### 3. Irrevocability Constraints

Software can be patched. Hardware cannot. This fundamentally changes the verification requirements.

In software testing, we often accept "good enough" coverage and fix bugs in production. In hardware, this isn't an option. How do benchmarks capture this higher bar for correctness?

## The Data Problem: Quality vs. Quantity

Mark Ren mentioned last week that EDA tools have detailed logs but limited data diversity. This creates a fundamental tension for benchmark creation.

You could go for quantity: scrape lots of open-source Verilog from GitHub. But quality varies wildly - many examples are incorrect or suboptimal. And you immediately face the training data contamination problem.

Or you could prioritize quality: carefully curate high-quality, verified designs. But this is expensive to create at scale, and you end up with limited diversity.

The comprehensive benchmark paper argues for quality, but then how do you get enough examples to train modern LLMs?

This is similar to the challenge we saw in [Week 10 with LLM serving](/blog/2024/11/05/optimizing-optimizers-llm-adaptation/). Systems need diverse, representative workloads to learn good policies. But hardware design workloads are inherently less diverse than software workloads because physical constraints limit the design space.

## The Meta-Question: What Are We Actually Measuring?

When we evaluate LLMs on RTL generation, what capability are we really testing?

**Pattern matching?**
"I've seen similar designs in training data, let me adapt them."

**Design understanding?**
"I understand the functional requirements and hardware constraints, let me create an appropriate implementation."

**Engineering judgment?**
"I know this approach will cause problems later, let me choose a different one."

Current benchmarks mostly test pattern matching. The MCTS paper moves toward design understanding by incorporating feedback. But engineering judgment remains elusive.

Consider this analogy from earlier on: 

A human chip designer looking at "design a FIFO" immediately asks contextual questions. What's this FIFO used for? That determines width and depth. What are the read/write patterns? That drives implementation choices. What's the timing budget? That affects pipelining decisions. What's the area budget? That determines memory style.

These questions come from experience and understanding of the broader system context. An AI that just pattern-matches on "FIFO" will miss this reasoning.

## Looking Forward: What Would Better Benchmarks Look Like?

At the start of this post, we noted that software benchmarks like HumanEval work by giving a model a problem description, running tests, and getting pass/fail results. Simple, binary, focused on functional correctness.

But everything we've discussed shows why that approach breaks down for hardware. The feedback loop diagram showed that hardware verification is multi-stage, not single-shot. The specification tables revealed that hardware problems are context-dependent and have multiple valid solutions. The papers demonstrated that quality (PPA metrics) matters as much as correctness.

So what would hardware benchmarks need to look like?

### 1. Multi-Stage Evaluation, Not Single-Shot Testing

**Software benchmarks**: Generate code → Run tests → Pass/fail

**Hardware needs**: Following our feedback loop, benchmarks should test specification clarification (can the AI ask the right questions like "which clock domain?"), initial RTL generation, testbench creation, debugging when synthesis reveals timing issues, and optimization for PPA. Each stage feeds information to the next, just like real chip design.

### 2. Quality Metrics, Not Just Correctness

**Software benchmarks**: Measure pass@k - how many attempts to get one working solution

**Hardware needs**: Remember the correctness problem from earlier? Synthesis might fail, timing might not close, area might explode. We need metrics for synthesis QoR (area, timing, power), verification coverage (did tests exercise corner cases?), and implementation quality (is it maintainable? reusable?).

### 3. Contextual Problems, Not Self-Contained Puzzles

**Software benchmarks**: Problems are typically self-contained with complete specifications

**Hardware needs**: Our benchmark vs real-world table showed that real specs are context-dependent. Problems should require understanding system-level constraints (this FIFO connects to a slow peripheral), making trade-offs (speed vs power), and reasoning about manufacturing (will this close timing at worst-case process corners?).

### 4. Handling Ambiguity, Not Assuming Clarity

**Software benchmarks**: Precise specifications with single correct answers

**Hardware needs**: As we saw with "design a FIFO," real hardware specs are incomplete and evolving. Benchmarks should test whether AI can identify missing information, ask clarifying questions, and adapt when requirements change mid-design.

### 5. Verification-Centric Evaluation

**Software benchmarks**: Tests are provided; just make code pass them

**Hardware needs**: The irrevocability constraint means verification is paramount. Benchmarks should test the ability to generate comprehensive testbenches, identify corner cases the spec didn't mention, create meaningful assertions, and debug systematically when issues arise.

## The Uncomfortable Reality

Here's what the papers don't say but we should acknowledge: **We might be quite far from AI systems that can meaningfully assist with RTL design.**

Not because the technical approaches are wrong. The MCTS paper shows genuine improvements. The comprehensive benchmark paper identifies real limitations.

But because the gap between "generate a module that passes tests" and "design a chip that works reliably in production" is enormous.

Remember from [Week 4](/blog/2024/09/24/week-4-production-reality/) the difference between proof-of-concept systems and production-ready systems? RTL generation faces an even higher bar. Hardware can't be patched post-deployment. Verification must be exhaustive, not probabilistic. Manufacturing costs make mistakes extremely expensive. And system integration requires deep contextual understanding that goes far beyond the module specification.

## Discussion Questions

**For everyone:** What would convince you that an AI-generated RTL design is production-ready? What level of verification would be sufficient?

**For those with hardware backgrounds:** What aspects of RTL design do current benchmarks fail to capture? What would a "realistic" benchmark problem look like?

**For those with ML backgrounds:** How do we address the training data contamination problem when the domain is small and most professional code is proprietary?

**The deeper question:** Are we trying to automate the wrong thing? Should we focus on AI assistants that help human designers, rather than autonomous AI designers?

## Synthesis

The papers this week highlight a crucial truth: **evaluation methodology shapes research direction**.

If our benchmarks only test simple pattern matching, we'll build systems that excel at pattern matching. If we want AI that can reason about design trade-offs, handle ambiguity, and verify correctness rigorously, we need benchmarks that test those capabilities.

The MCTS paper shows that incorporating richer feedback (synthesis results, not just functional tests) enables better search strategies. This suggests a path forward: **benchmarks that capture the full design flow, not just code generation**.

But we should also recognize the limits. Some aspects of chip design - the tacit knowledge, the engineering judgment, the system-level reasoning - might be fundamentally hard to benchmark because they require human interaction and contextual understanding.

Perhaps the goal shouldn't be "autonomous RTL generation" but rather "AI-assisted design exploration." Not replacing human designers, but augmenting their capabilities to explore larger design spaces and identify promising approaches faster.

That would require different benchmarks. Not "can the AI generate a correct module?" but "can the AI help a human designer explore options, identify problems, and make informed trade-offs?"

This is a much harder problem to benchmark. But it might be the right problem to solve.

---

*Next week: Physical Design and Layout - where the rubber meets the silicon. Guest speaker: Richard Ho from OpenAI on co-optimizing ML models and hardware.*

*For detailed readings, slides, and materials for this week, see [Week 11 in the course schedule]({{ site.baseurl }}/course/schedule/#week-11---rtl-design--logic-synthesis).*

