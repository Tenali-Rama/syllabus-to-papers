# Blueprint — intro-ai-machine-learning, run-001_2026-11-24

Source: `syllabi/intro-ai-machine-learning.md`. Sub-topic tags are marked **[G]** (syllabus-derived: a syllabus bullet explicitly names the topic) or **[D]** (analyzer-derived: the syllabus module/section is sparse, so the sub-topic was decomposed into standard intro-course content).

## 1. Sub-topic inventory (coverage contract — 26 sub-topics)

### Module 1 — Introduction to Machine Learning
- **S1** [G] Supervised learning: classification vs regression — definitions, output types, examples
- **S2** [G] The ML workflow: data collection → cleaning → train/validation/test split → training → evaluation → deployment
- **S3** [D] Overfitting, underfitting, and train/test split logic; generalization

### Module 2 — Decision Trees and Classification Algorithms
- **S4** [D] Decision tree structure and splitting criteria: Gini impurity, entropy (definitions and single-node computation)
- **S5** [D] Information gain: computing entropy of splits and choosing the best attribute
- **S6** [D] Overfitting in trees, pruning, and depth/leaf-size controls
- **S7** [D] Instance-based and probabilistic classifiers: k-nearest neighbours and naive Bayes intuition

### Module 3 — Neural Networks and Deep Learning
- **S8** [G] The perceptron: weighted sum, step activation, the perceptron update rule
- **S9** [D] Activation functions: step, sigmoid, ReLU — why non-linearity is needed
- **S10** [D] Multi-layer perceptrons and backpropagation intuition (forward pass, error backpropagation)
- **S11** [G] Convolutional Neural Networks overview: convolution, pooling, feature maps, typical uses
- **S12** [D] CNN layer-output dimension arithmetic (kernel size, stride, padding, pooling chains)

### Module 4 — Reinforcement Learning
- **S13** [G] Reward-based learning: agent, environment, state, action, reward, policy
- **S14** [D] Exploration vs exploitation; reward design and sparse-reward problems

### Module 5 — NLP and Large Language Models
- **S15** [D] Basic NLP: tokenization, text representation for models
- **S16** [G] Prompt engineering: instruction clarity, context, few-shot examples, role/task framing
- **S17** [G] Large Language Models: training on text, token-based generation, token/cost arithmetic
- **S18** [D] LLM limitations: hallucination, knowledge cutoff, prompt sensitivity

### Module 6 — Computer Vision
- **S19** [G] Image classification: pipeline, labeled data, typical datasets/domains
- **S20** [G] Object detection: localization, bounding boxes, detection vs classification
- **S21** [D] Vision evaluation: confusion matrix metrics (precision/recall/F1) and IoU for boxes

### Module 7 — Responsible AI, Ethics, Bias and AI Governance
- **S22** [D] Fairness metrics: demographic parity, equalized odds, disparate impact ratio
- **S23** [D] Sources of bias: historical/sampling/label/measurement bias and how they enter pipelines
- **S24** [D] AI governance: documentation, audits, human oversight, regulatory frameworks

### Module 8 — AI Applications
- **S25** [D] AI in healthcare and finance: example systems, data types, deployment constraints
- **S26** [D] AI in other domains: transport, agriculture, education, retail — matching technique to domain problem

## 2. Exam scheme (verbatim from syllabus)
End-semester exam: **100 marks, 3 hours**. Mix of MCQ, short answer (2–5 marks), numerical problems, and long answer (≤ 10 marks). All three papers use this scheme.

## 3. Coverage map: sub-topic × paper

Question→sub-topic tags in the paper files are the authoritative map (every question carries `(Mn, marks, Sk)` tags); `verify.py` recomputes coverage from those tags. Machine-checked results:

| Paper | Sub-topics covered | Coverage % | Missing |
|---|---|---|---|
| easy.md | 25/26 | 96.2% | S12 (CNN dimension arithmetic — a hard-only template, TF9) |
| medium.md | 25/26 | 96.2% | S12 (same reason) |
| hard.md | 26/26 | 100.0% | — |

All papers ≥ 85%; the run covers 100% of the inventory.

## 4. Section structure (identical in all three papers; sections are stated logical groupings of modules — every section ≥ 10 marks; questions appear in module-progressive order)

| Section | Modules | Questions | Marks |
|---|---|---|---|
| A | M1 + M2 | 10 | 22 |
| B | M3 | 6 | 16 |
| C | M4 + M5 | 8 | 18 |
| D | M6 + M7 | 8 | 19 |
| E | M8 + integrative longs | 5 | 25 |
| **Total** | | **37** | **100** |

(Small single-bullet modules M4 and M8 fall below the 10-mark section floor on their own, so they are grouped per the pipeline's "stated logical grouping" allowance; every section carries counts and totals and all sections are ≥ 10 marks.)

Marks band check per paper: 27×2 + 6×3 + 2×5 + 1×8 + 1×10 = 54+18+10+18 = 100 ✓. Majority of questions in the 2–5 band (33/37); exactly two long answers (≤3 ten-mark rule satisfied; the 8-mark long also enumerates sub-parts).

## 5. Three-axis difficulty rubric
- **Cognitive level**: easy = recall/definition/single-step computation; medium = application, trace-through, small design; hard = evaluation, diagnosis, multi-concept synthesis, trade-off analysis.
- **Concepts combined**: easy = 1 concept; medium = 2 linked concepts (e.g., entropy + attribute choice); hard = ≥3 (e.g., metrics + bias + governance in one scenario).
- **Numerical complexity**: easy = one formula, one substitution; medium = 2–4 step computation with intermediate values; hard = chained computations (multi-layer dimension math, metric tables across groups) plus interpretation of the result.

## 6. Uniqueness constraints (template families, ≤1 use across the whole run)
- TF1 Gini impurity of a single node (easy §B)
- TF2 Entropy + information gain over candidate splits (medium §B)
- TF3 Train/test split sizing (easy §A)
- TF4 Single-layer perceptron forward pass (easy §C)
- TF5 Perceptron update trace over epochs (medium §C)
- TF6 Confusion-matrix precision/recall/F1 (medium §F)
- TF7 IoU of two boxes with threshold decision (hard §F)
- TF8 Token-count / cost arithmetic for an LLM prompt (medium §E)
- TF9 CNN single-layer output dims (hard §C, part a) and pooled chain (part b) — one family in one question
- TF10 Fairness metric table computation across demographic groups (hard §G)
- TF11 Dataset-size arithmetic for a vision data plan (medium §F)

No numerical template family repeats across papers; conceptual question families are also non-repeating (e.g., only one question per paper asks for a definition of overfitting, phrased differently per paper with different framings).
