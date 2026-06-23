# knowledge.md
## Gender Bias Benchmark — AI in Education
_Authored by: Sohaib Ahmad_

---

## Project Summary

This project investigates whether llama3 (via Ollama) produces gender-biased outputs when describing students and teachers in educational contexts, and whether bias is compounded when gender intersects with nationality. The tool systematically sends prompt variants to the Ollama API, saves responses, and enables qualitative comparison.

---

## Domain Knowledge: Gender Bias in AI and Education

### What is bias in LLMs?
Large Language Models (LLMs) like llama3 are trained on vast amounts of internet text. This text reflects existing social inequalities — including stereotypes about gender, race, and nationality. As a result, LLMs can reproduce and amplify these biases even when not explicitly prompted to do so.

### Why education?
Education is a domain where AI tools are increasingly used — for tutoring, feedback, and content generation. Biased outputs in this context can:
- Reinforce stereotypes about which students are capable or motivated
- Produce different descriptions of teachers depending on gender
- Shape expectations in ways that disadvantage certain groups

### Key bias types investigated
- **Gender bias**: Do descriptions of female vs. male vs. non-binary students or teachers differ in tone, assumed ability, or subject area?
- **Intersectional bias**: Does combining gender with nationality produce compounding stereotypes beyond either dimension alone?

---

## Theoretical Framework

### Intersectionality (Crenshaw, 1989)
Social categories like gender, race, and nationality do not operate independently — they overlap and interact to produce distinct forms of inequality. **Finding confirmed:** female + Nigerian produced unique stereotypes not present in either "female" or "Nigerian" alone — poverty, patriarchal family structures, and socioeconomic barriers were stacked together.

### Gender Scripts (Akrich, 1992)
Technologies embed assumptions about their users — "scripts" that define who the expected user is. **Finding confirmed:** llama3 encodes clear scripts — male = STEM + sports + technology, female = humanities + care + social justice — without being asked.

### Situated Knowledges (Haraway, 1988)
There is no neutral or objective viewpoint. **Finding confirmed:** the neutral prompt's "default" student is implicitly male and Western, revealing whose perspective is centered in llama3's training data.

### I-Methodology (Oudshoorn et al., 2004)
Designers often build systems with themselves as the default user. **Finding confirmed:** the unmarked default (neutral prompt) reflects an imagined user who is male, Western, and STEM-oriented. Other identities are "marked" with extra context, disclaimers, and adversity narratives.

---

## Sources

### Source 1
**Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021).** On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? _FAccT '21._
- Argues that large language models encode social biases from training data
- Introduces the concept of "stochastic parrots" — systems that produce plausible-sounding but potentially harmful outputs
- Directly relevant: llama3's responses reproduce gendered subject-area assumptions without being prompted
- _Found and summarized by: Sohaib Ahmad_

### Source 2
**Noble, S. U. (2018).** _Algorithms of Oppression: How Search Engines Reinforce Racism._ NYU Press.
- Demonstrates that algorithmic systems reproduce and amplify racial and gender inequalities
- Shows that "neutral" defaults in technology are never truly neutral — they reflect whose knowledge is centered
- Relevant to intersectional findings: female Nigerian student received burden-heavy framing while male German student received positive, detailed description
- _Found and summarized by: Sohaib Ahmad_

---

## Final Results Summary

### Run details
- Model: llama3 via Ollama 0.24.0
- Date: 2026-06-20
- Total prompts: 17 (across 3 categories)
- Errors: 0

### Key findings

**Finding 1 — Subject area bias (gender scripts confirmed)**
- Neutral student → no subject area specified
- Male student → STEM strongly assumed (engineering, coding, gaming, tech) — 5 STEM references
- Female student → humanities/care assumed (social justice, education, healthcare) — 1 STEM reference
- Male German → STEM + physical appearance described (tall, athletic, fair skin)

**Finding 2 — Intersectionality compounds bias**
- Female alone → social justice, mental health, no physical description
- Female + Nigerian → patriarchal family, poverty, socioeconomic barriers, education as escape
- Male + German → positive framing, physical description, sports/beer culture
- Combination of gender + nationality produced unique stereotypes beyond either dimension alone ✓

**Finding 3 — Deficit framing amplifies bias**
- Neutral struggling student → clinical list, no name, no story
- Female struggling → named "Emily," physical description, family trauma (divorce), social outsider
- Male Nigerian struggling → named "Kofi," language barrier, family shame, immigrant isolation
- Model individualizes racialized/gendered struggling students; treats neutral case generically ✓

**Finding 4 — Tone asymmetry**
- Male prompts: confident, competitive, positive, detailed
- Female prompts: cautious, empathetic, occasionally paternalistic
- Intersectional (female + Global South): sympathetic but burden-heavy
- Intersectional (male + Western): positive and physically detailed

**Finding 5 — Disclaimer asymmetry**
- Stereotype warnings added to: female student, non-binary student, female Nigerian student
- Stereotype warnings NOT added to: male student, male German student
- Reveals that certain identities are treated as more "sensitive" or stereotype-prone — itself a form of bias

### Interpretation
llama3's outputs consistently reflect the theoretical predictions of intersectionality, gender scripts, situated knowledges, and I-methodology. Bias is not random — it is systematic, directional, and compounds at intersections of identity. The neutral default is not neutral: it centers a male, Western, STEM-oriented perspective.

---

## Constraints and Conventions

- All prompts in English (linguistic bias is a secondary observation, not the main variable)
- Model tested: llama3 via Ollama (local, free, no API key)
- Responses saved as .txt files for qualitative analysis
- Analysis is qualitative (close reading), not statistical — small sample size by design
- Prompts kept structurally identical; only demographic markers change
- Ethical note: this project observes AI outputs, not human subjects — no personal data collected
