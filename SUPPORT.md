# Concept Extraction from Competitive Exam Questions

Status: Not Started
Date Asked: June 8, 2025
Follow-up Required: No

<aside>
💡

**Objective**

Build a program that analyzes a **given set of questions from a competitive exam (e.g., UPSC Ancient History)** and identifies the **underlying concept** being tested in each question (e.g., "Indus Valley Civilization", "Gupta Period Literature", "Ashokan Edicts").

This tool will help in understanding the conceptual distribution of past questions and potentially aid in curriculum mapping or study analytics.

</aside>

<aside>

### **Problem Statement**

> Given a CSV file containing questions from a subject area (e.g., Ancient Indian History from UPSC), write a program (e.g. Python or any) that parses each question and outputs the associated historical concept(s) it is based on.
> 

You are not required to implement concept extraction using an LLM API (e.g., OpenAI, Anthropic etc) due to API costs. However, **design the program in such a way that an LLM call could be integrated easily later**. You must simulate/test the output by running questions manually through any LLM of your choice and include those results in your submission.

Improvise on the code or suggest methods such that it works across different domains or subjects 

</aside>

<aside>

### **Input Format**

The provided resources include four CSV files covering ancient history, economics, mathematics, and physics. You can begin with any subject and test your code across the others.

CSV file with the following structure:

```
Question Number,Question,Option A,Option B,Option C,Option D,Answer
1,Which of the following was a feature of the Harappan civilization?,City planning,Iron tools,Vedic rituals,Temple worship,A
```

</aside>

<aside>

### **Expected Output**

```bash
$ python concept_extractor.py --question path/to/questions.csv
```

```bash
Question 1: Harappan Civilization, Urban Planning
Question 2: Mauryan Empire, Kautilya's Arthashastra
...
```

Also write to an output file (`output_concepts.csv`) with this format:

```
Question Number,Question,Concepts
1,Which of the following was a feature of the Harappan civilization?,Harappan Civilization; Urban Planning
```

</aside>

<aside>

### **Resources**

You may use any resources to enrich the process (practical) including any of the following:

- A pre-built **concept keyword dictionary** (e.g., `harappan`: Harappan Civilization, `edict`: Mauryan Empire, `ashoka`: Ashokan Edicts)
- Basic NLP techniques (TF-IDF, Named Entity Recognition)
- Manually annotated examples (small test file)
</aside>

<aside>

### **Guidelines**

- Write a README with example LLM prompts and simulated output.
- Add the LLM prompt format used for testing:
    
    > "Given the question: <Question>, identify the historical concept(s) this question is based on."
    > 
- You are **not required to build a classifier**, but if you want to experiment with keyword or rule-based extraction, it's welcome.
- Keep your code modular and LLM-ready (e.g., with a `llm_interface.py` stub file).
</aside>

<aside>

### **Evaluation Criteria**

- Thought Process - creativity, depth
- Simulated output quality and relevance
- Ability to replicate the output (concept tagging) across multiple subject domains.
- Ability to scale with actual LLM integration.
</aside>

<aside>

### Starter Template

--- this repo.


</aside>

<aside>

### Deliverables

1. Share your GitHub repository with the user `edme-tutor`, including your roll number and a detailed README file.
2. Your previous project portfolio, if available. 
</aside>