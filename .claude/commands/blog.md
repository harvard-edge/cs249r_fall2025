---
name: blog
description: Launch the blog-writer agent to collect class notes or generate blog posts
---

## Usage

- `/blog` - Launches the blog-writer agent for note collection or post generation

## What it does

This command immediately launches the blog-writer agent, which will:

1. **Ask for date/week first**: "What date or week are these notes for?"
2. **Map to correct week**: Uses schedule.md to organize notes properly  
3. **Collect your thoughts**: Stores raw notes in `/blog/drafts/week-X/YYYY-MM-DD-notes.md`
4. **Or generate posts**: If you say "generate", creates polished blog post from accumulated notes

## Examples

```
/blog
> What date or week are these notes for?
September 15 (or "Week 3")
> Your thoughts?
Today we covered code generation with SWE-bench. Key insight: benchmarks are everything...
```

```  
/blog
> What date or week are these notes for?
generate week 3
> [Agent creates polished post from all Week 3 notes]
```

This provides a quick way to dump class thoughts throughout the week, then generate coherent blog posts when ready.