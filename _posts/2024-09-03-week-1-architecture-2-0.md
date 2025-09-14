---
layout: post
title: "Week 1: The End of an Era, The Dawn of Architecture 2.0"
date: 2024-09-03
categories: architecture
---

We kicked off CS249r with a provocative question: *"Ask not what you can do for AI—ask what AI can do for you."* And honestly, after seeing AI generate everything from Warhol-style astronauts to working code, the question isn't whether AI can help us design computer systems—it's whether we can afford not to use it.

## The End of an Era

For decades, computer systems innovation followed a predictable playbook I call **TAO**: Technology innovation (thank you, Moore's Law), Architecture innovation (hello, parallelism), and Optimization (compiler tricks and hardware-software co-design). This worked beautifully when design spaces were manageable and human intuition could guide us toward good solutions.

But here's the thing—that era is over.

Moore's Law is sputtering. Dennard scaling is dead. We're dealing with dark silicon and diminishing returns from traditional approaches. Meanwhile, as Hennessy and Patterson famously declared, we've entered the age of domain-specific computing. Every application needs its own specialized solution, and the design spaces have exploded beyond anything a human can reasonably navigate.

## Welcome to Architecture 2.0

This brings us to **TAOS**—the same TAO, but with a crucial fourth pillar: **Specialization**. And this is where things get wild.

We're not talking about tweaking a few parameters anymore. Modern design spaces contain somewhere between 10^14 and 10^2300 possible configurations. To put that in perspective, that's more combinations than there are atoms in the observable universe. No human—no matter how brilliant—can systematically explore spaces like that.

This is why we need AI agents that can navigate these exponentially complex design spaces automatically. It's not about replacing human expertise; it's about augmenting it with systems that can explore solution spaces too vast for manual analysis.

## The North Star

Imagine being able to say: *"Act like an architect—design me a custom 64-bit RISC-V processor with full vector extension support and optimize it for less than 3 Watt TDP in a 7nm LP process node using the TSMC plugin library."* 

That's not science fiction. That's where we're heading.

## What's Next?

Next week, I will continue to cover some introductory material. And soon we'll start our class journey through the computing stack, beginning with AI for software. Code generation is the most accessible entry point as it's where we can clearly see both the incredible promise and the current limitations of AI in systems design. We'll explore what it really takes to move from "impressive demos" to "production-ready tools."

The slides are posted below, and I'm curious to hear your thoughts on the research challenges we outlined: datasets, algorithms, best practices, workforce training, and infrastructure. Which of these do you think will be the biggest bottleneck?

## Resources

**Materials**: [Slides](https://github.com/harvard-edge/cs249r_fall2025/releases/download/sep-3/CS249r_.Architecture.2.0.-.Part.1.pdf) • [All materials](https://github.com/harvard-edge/cs249r_fall2025/releases/tag/sep-3)