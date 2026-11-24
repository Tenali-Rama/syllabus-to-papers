---
syllabus: intro-ai-machine-learning
run: run-001_2026-11-24
difficulty: medium
paper_number: 2
marks: 100
duration_hours: 3
modules_covered: 8
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "81/90"
---

# Introduction to AI & Machine Learning — End-Semester Exam (Medium Paper)

**Total marks: 100 | Duration: 3 hours**
Answer all questions. Every question carries a tag `(Mn, marks, Sk)` = module, marks, blueprint sub-topic IDs. Unless a question states otherwise, use log base 2 for entropy and round final numerical answers to 3 decimal places.

## Section A — Modules 1 & 2: ML Basics and Classification Algorithms (10 questions, 22 marks)

**Q1.** A retailer wants to predict next month's **sales revenue** (in rupees) from advertising spend and seasonality data. Identify the learning task type and justify in one sentence.
*(M1, 2 marks, S1)*

**Q2.** Which of these is **supervised learning**?
(A) Grouping customers into segments with no labels
(B) Learning spam / not-spam from emails labeled by human reviewers
(C) An agent learning to stack blocks from trial, reward, and error
(D) Compressing images into smaller representations
*(M1, 2 marks, S1)*

**Q3.** During a churn-prediction project the team discovers duplicate customer rows and missing age values. To which workflow stage does fixing this belong, and why must it happen **before** training?
*(M1, 2 marks, S2)*

**Q4.** A fraud model reports **98% accuracy on its training set** and **71% on a held-out validation set**. Diagnose the behaviour and state one appropriate response.
*(M1, 2 marks, S3)*

**Q5.** A tree is being built for disease diagnosis. The algorithm evaluates two candidate splits and picks the one whose child nodes have the **lower total impurity**. The quantity it is implicitly maximizing is:
(A) The number of samples per child
(B) Information gain (parent impurity minus weighted child impurity)
(C) The tree's total depth
(D) The average of the numeric feature values
*(M2, 2 marks, S4)*

**Q6.** A node with class distribution 50/50 has **higher entropy** than a node with 90/10 because:
(A) Its samples are more numerous
(B) Its class distribution is more uniform, so class membership is more uncertain
(C) 50/50 nodes are always leaves
(D) Entropy only applies to numeric attributes
*(M2, 2 marks, S4)*

**Q7.** A fraud-detection tree has depth 40 and 2,000 leaves, and its validation accuracy has started **falling** as it grows deeper. The most appropriate action is:
(A) Keep growing until every leaf is pure
(B) Apply pruning / a depth or leaf-size limit, since validation performance indicates the tree is fitting noise
(C) Add more attributes so splits are finer
(D) Switch the target variable
*(M2, 2 marks, S6)*

**Q8.** Setting a **minimum samples-per-leaf** rule of 20 in a decision tree primarily helps by:
(A) Speeding up data collection
(B) Preventing leaves that summarize very few samples, which often encode noise
(C) Increasing tree depth
(D) Removing the need for a test set
*(M2, 2 marks, S6)*

**Q9.** State the core assumption naive Bayes makes about features, and give one example from email classification where the assumption is clearly false yet the classifier still works.
*(M2, 3 marks, S7)*

**Q10.** A kNN classifier for house-type prediction switches its distance metric from Euclidean to one that weights "area in sq ft" 100× more than "number of balconies". Explain in 2–3 sentences what will happen to the neighbourhoods it finds and why.
*(M2, 3 marks, S7)*

## Section B — Module 3: Neural Networks and Deep Learning (6 questions, 16 marks)

**Q11.** A student builds a 5-layer network in which every "activation" is the identity function. State precisely what class of functions this network can compute and why it cannot learn curved decision boundaries.
*(M3, 2 marks, S9)*

**Q12.** The **sigmoid** activation σ(z) outputs values in the range:
(A) [−1, 1]  (B) [0, ∞)  (C) (0, 1)  (D) (−∞, ∞)
*(M3, 2 marks, S9)*

**Q13.** During training, **backpropagation** computes:
(A) New training examples
(B) Gradients of the loss with respect to each weight, propagated layer by layer from the output back toward the input
(C) The final class predictions
(D) The convolution filters by hand
*(M3, 2 marks, S10)*

**Q14.** In the perceptron update rule, the **learning rate** controls:
(A) How many training points exist
(B) The step size of each weight change, i.e. how strongly one mistake moves the weights
(C) The threshold function shape
(D) The number of input features
*(M3, 2 marks, S8)*

**Q15.** A team must classify 50,000 labeled X-ray images into "normal" / "abnormal". Give two reasons a CNN is a better architectural choice than a plain MLP on raw pixels in this setting.
*(M3, 3 marks, S11)*

**Q16.** *(Numerical — perceptron update)* A perceptron uses the convention y ∈ {+1, −1} and the update rule **w ← w + η·y·x, b ← b + η·y** on each mistake, with learning rate **η = 0.1**. Initial weights: **w = (0.5, −0.3), b = 0.2**. Step activation outputs sign(net), net = w·x + b. Training points, processed in order:
- Point 1: x = (1, 2), true label y = **+1**
- Point 2: x = (2, 1), true label y = **−1**

For each point in order: compute net, decide whether an update occurs, and if so apply it. Report the **final weights and bias** after both points are processed, showing every intermediate value.
*(M3, 5 marks, S8)*

## Section C — Modules 4 & 5: Reinforcement Learning; NLP & Large Language Models (8 questions, 18 marks)

**Q17.** In an ad-placement system that learns from click feedback, the **policy** is best described as:
(A) The click-through rate
(B) The rule mapping each user/context state to the action of which ad to show
(C) The set of ads available
(D) The revenue report
*(M4, 2 marks, S13)*

**Q18.** A warehouse robot receives **+1 for each package delivered** and **−2 for each collision**. Identify the reward signal's role and explain in one sentence why the −2 term changes the agent's learned behaviour.
*(M4, 2 marks, S13)*

**Q19.** A game agent receives its first reward only after 200 moves when the level is finally cleared (a **sparse reward**). Explain in 2–3 sentences why learning is slow in this setting and name one standard remedy.
*(M4, 3 marks, S14)*

**Q20.** The sentence "The bank was steep" is tokenized and passed to a model. Which issue does this illustrate for a model that treats each word independently?
(A) Tokenization loss
(B) Word-sense ambiguity — "bank" has two meanings (river edge vs financial institution) that require context
(C) Knowledge cutoff
(D) Overfitting
*(M5, 2 marks, S15)*

**Q21.** Including **three labeled examples** of complaint → category pairs inside a prompt, before the complaint to classify, primarily:
(A) Retrains the model permanently
(B) Shows the model the desired input–output pattern, improving format and label consistency for this request
(C) Reduces the model's token limit
(D) Removes hallucinations entirely
*(M5, 2 marks, S16)*

**Q22.** A prompt that begins "You are a claims adjuster for an Indian insurer. Given the repair invoice below, ..." is using which prompt-engineering technique, and what does it contribute?
(A) Fine-tuning; it changes model weights
(B) Role framing; it narrows the register, vocabulary, and defaults the answer should follow
(C) Tokenization; it shortens the input
(D) Caching; it stores prior answers
*(M5, 2 marks, S16)*

**Q23.** A medical-chatbot team finds the model invents plausible-looking but nonexistent drug interactions. The most appropriate first mitigation among these is:
(A) Raise the temperature setting
(B) Ground the model's answers in a retrieved, verified drug-interaction database and require citations
(C) Train on fewer examples
(D) Shorten all prompts
*(M5, 2 marks, S18)*

**Q24.** *(Numerical — token cost)* An LLM API charges **$0.50 per 1 million input tokens** and **$1.50 per 1 million output tokens**. A document-QA service sends a **350-token prompt** each call and caps the response at **150 tokens**. Compute the cost of **1,000 calls**, showing the per-call cost as an intermediate step.
*(M5, 3 marks, S17)*

## Section D — Modules 6 & 7: Computer Vision; Responsible AI (8 questions, 19 marks)

**Q25.** To train a factory camera system to classify bottles as "cracked" or "intact", describe the labeled dataset you need (one sentence: images plus what labels).
*(M6, 2 marks, S19)*

**Q26.** A model outputs, for one street photo: box(120, 40, 300, 180) = "bus", box(400, 60, 520, 150) = "car". This output format is characteristic of:
(A) Image classification  (B) Object detection  (C) Text extraction  (D) Image super-resolution
*(M6, 2 marks, S20)*

**Q27.** In the box format (x_left, y_top, width, height), the box (120, 40, 300, 180) spans pixel columns:
(A) 120 to 300  (B) 120 to 420  (C) 40 to 180  (D) 300 to 480
*(M6, 2 marks, S20)*

**Q28.** *(Numerical — labeling throughput)* A training set needs **10,000 labeled drone images** for a crop-monitoring classifier. Each annotator labels **120 images/hour**; a team of **4 annotators** works **6 hours/day**. Compute how many working days the labeling takes (round up to a whole day), showing the images-per-day intermediate.
*(M6, 3 marks, S19)*

**Q29.** A speech-recognition product was trained mostly on urban, native-accent recordings and performs far worse for rural accents. The dominant **source of bias** here is:
(A) Sampling/coverage bias in the training data
(B) A hardware defect
(C) Label noise on the accent attribute
(D) Random seed variation
*(M7, 2 marks, S23)*

**Q30.** For a loan model, the legal team asks: "are approval rates equal across gender groups, irrespective of genuine need?" The fairness concept being requested is closest to:
(A) Equalized odds / group-conditioned error parity
(B) Demographic parity of approval rates
(C) Perplexity
(D) Top-1 accuracy
*(M7, 2 marks, S22)*

**Q31.** Explain in 3–4 sentences what a **model card** documents for a deployed ML system, and name two decisions it helps a non-technical stakeholder make.
*(M7, 3 marks, S24)*

**Q32.** A "default risk" label was recorded by a loan officer's subjective judgement rather than observed repayment outcomes. Explain in 2–3 sentences how this **label/measurement bias** propagates into the trained model.
*(M7, 3 marks, S23)*

## Section E — Module 8 and Integrative Long Answers (5 questions, 25 marks)

**Q33.** An eye hospital deploys retinal-photo screening for diabetic retinopathy. State the task type and one **deployment constraint** (e.g. hardware, connectivity, or human-review requirement) the hospital must plan for.
*(M8, 2 marks, S25)*

**Q34.** A lender uses a credit-scoring model trained on historical approvals. Name one concrete fairness risk specific to this application and one practical check against it.
*(M8, 2 marks, S25)*

**Q35.** A school district wants to flag students at risk of dropping out using attendance, grades, and assignment submissions. Propose the AI task type and data source, and justify the choice in 2–3 sentences, noting one safeguard.
*(M8, 3 marks, S26)*

**Q36.** *(Numerical — evaluation metrics)* A tumor-screening model on an illustrative test set of 1,000 scans produces: **TP = 45, FN = 15, FP = 30, TN = 910**.
(a) Compute precision. *(2 marks)*
(b) Compute recall. *(2 marks)*
(c) Compute F1. *(2 marks)*
(d) A radiologist says "recall matters more than precision here." Interpret both metrics for this screening use case and say why the radiologist's claim is defensible. *(2 marks)*
*(M6, 8 marks, S21)*

**Q37.** *(Numerical — decision-tree construction)* A bank has an illustrative training set of **10 loan applicants**: 6 approved (Y), 4 denied (N).
Candidate split A — "credit history": Good → 5 applicants (5 Y, 0 N); Bad → 5 applicants (1 Y, 4 N).
Candidate split B — "income > ₹40k": Yes → 6 applicants (4 Y, 2 N); No → 4 applicants (2 Y, 2 N).
Given: log₂0.6 = −0.737, log₂0.4 = −1.322, log₂0.2 = −2.322, log₂0.8 = −0.322, log₂(2/3) = −0.585, log₂(1/3) = −1.585.
(a) Compute the parent entropy. *(2 marks)*
(b) Compute the weighted child entropy for split A and its information gain. *(3 marks)*
(c) Compute the information gain for split B. *(2 marks)*
(d) Which attribute becomes the root, and what does the size of the difference tell you? *(3 marks)*
*(M2, 10 marks, S4, S5)*

---

## Answer Key — Medium Paper (with mark splits)

**Section A — Modules 1 & 2 (22 marks)**
- Q1 (2): Regression — revenue is a continuous numeric target *(1 task + 1 justification)*.
- Q2 (2): **B**. Human-assigned labels + discrete target = supervised classification; C is RL, A is clustering.
- Q3 (2): Data cleaning/preparation stage *(1)*; errors and duplicates distort the learned patterns, so they must be fixed before the model fits them *(1)*.
- Q4 (2): Overfitting — the 27-point train/validation gap shows memorization of training noise *(1)*; response: regularization/pruning, more data, or simpler model *(1)*.

*(Module 2 questions.)*

- Q5 (2): **B**. Lower weighted child impurity = larger information gain; sample counts (A) are not a purity measure.
- Q6 (2): **B**. Entropy measures distributional uncertainty; uniform 50/50 is maximally uncertain.
- Q7 (2): **B**. Falling validation accuracy during growth is the classic overfitting signature; pruning directly counters it.
- Q8 (2): **B**. Tiny leaves generalize poorly; a minimum leaf size is a standard capacity control.
- Q9 (3): Assumption: features are conditionally independent given the class *(1)*; example: "free" and "winner" co-occur in spam, violating independence *(1)*; yet the classifier still ranks spam highly because the correlated evidence points the same way *(1)*.
- Q10 (3): The weighted metric makes points differ almost only in area, so neighbours become near-duplicates in area while differing freely in balconies *(1.5)*; the classifier effectively ignores balconies, and any comparable-area house counts as a neighbour *(1.5)*.

**Section B — Module 3 (16 marks)**
- Q11 (2): Composition of linear maps is linear *(1)*, so the network can only represent linear boundaries regardless of depth and cannot bend them around clusters *(1)*.
- Q12 (2): **C** — sigmoid maps to the open interval (0, 1); [−1, 1] is tanh's range.
- Q13 (2): **B**. Backprop = chain-rule gradients flowing output→input; it does not create data or predictions.
- Q14 (2): **B**. η scales each weight update per mistake.
- Q15 (3): Any two, 1.5 marks each: convolutions exploit local spatial structure and share weights, so they need far less data/parameters than a dense net on 50k+ pixels; pooling gives translation robustness for lesion position; dense MLP on raw pixels overfits and ignores locality.
- Q16 (5): Point 1: net = 0.5(1) + (−0.3)(2) + 0.2 = 0.1 > 0 → predict +1 = true label → **no update** *(1)*. Point 2: net = 0.5(2) + (−0.3)(1) + 0.2 = 0.9 > 0 → predict +1, true −1 → mistake *(1)*. Update: w ← (0.5, −0.3) + 0.1·(−1)·(2, 1) = (0.5 − 0.2, −0.3 − 0.1) = **(0.3, −0.4)** *(1)*; b ← 0.2 + 0.1·(−1) = **0.1** *(1)*. Final: **w = (0.3, −0.4), b = 0.1** *(1: correct final statement)*.

**Section C — Modules 4 & 5 (18 marks)**

*(Module 4 questions.)*

- Q17 (2): **B**. Policy = state → action mapping; the CTR is feedback, not the policy.
- Q18 (2): Reward = scalar feedback shaping behaviour *(1)*; the −2 penalty makes collision-avoiding actions higher-value, so the agent learns safer paths *(1)*.
- Q19 (3): With reward only at the end, almost no action gets credit signal, so the agent cannot tell which of the 200 moves helped *(1.5)*; remedies: reward shaping (small intermediate rewards), or credit assignment methods like discounting/return estimation *(1.5, any one named remedy)*.

*(Module 5 questions.)*

- Q20 (2): **B**. Context determines word sense; a context-free treatment picks one meaning and errs.
- Q21 (2): **B**. In-context examples steer the output pattern for that request only; they do not retrain (A) or guarantee no hallucination (D).
- Q22 (2): **B**. Role framing sets domain-appropriate register and defaults; weights are untouched.
- Q23 (2): **B**. Grounding/citation in verified data targets the invented-content failure directly; higher temperature worsens it.
- Q24 (3): Per call: input 350 × $0.50/10⁶ = $0.000175; output 150 × $1.50/10⁶ = $0.000225 → per-call **$0.0004** *(2 marks)*; 1,000 calls → **$0.40** *(1 mark)*.

**Section D — Modules 6 & 7 (19 marks)**

*(Module 6 questions.)*

- Q25 (2): Bottle images each paired with the inspector-verified label "cracked" or "intact" *(1 labels + 1 linkage to supervised training)*.
- Q26 (2): **B**. Per-object boxes + class labels = detection output format.
- Q27 (2): **B** — columns 120 to 120 + 300 = 420. Distractor A misreads width as x_right.
- Q28 (3): Throughput = 4 × 6 × 120 = **2,880 images/day** *(1.5)*; 10,000 / 2,880 = 3.47 → **4 working days** rounded up *(1.5)*.

*(Module 7 questions.)*

- Q29 (2): **A**. The training recordings under-represent rural accents — a coverage/sampling problem.
- Q30 (2): **B**. The question asks about approval **rates** by group — demographic parity; equalized odds conditions on true outcome, which was not asked.
- Q31 (3): A model card documents intended use, training data summary, performance (incl. per-group), limitations and known failure modes *(2)*; helps stakeholders decide e.g. whether the tool suits their population, and where human review is required *(1)*.
- Q32 (3): The model treats the officer's subjective judgement as ground truth *(1)*, so any consistent judgement pattern — leniency or prejudice toward certain groups or ages — becomes the target the model learns to reproduce *(1)*; observed repayments, not opinions, should define the label *(1)*.

**Section E — Module 8 and long answers (25 marks)**

*(Module 8 questions.)*

- Q33 (2): Supervised image classification (grading retinopathy severity) *(1)*; constraint: e.g. camera hardware at screening camps, offline connectivity, or mandatory ophthalmologist review of positives *(1)*.
- Q34 (2): Risk: historical approval disparities by gender/region get reproduced *(1)*; check: compute approval rates / error rates per group before deployment and investigate gaps *(1)*.
- Q35 (3): Supervised classification of at-risk vs on-track from attendance/grades/submission records *(1)*; justified: labeled historical outcomes exist and early flags enable intervention *(1)*; safeguard: flags must trigger human counsellor review, never automatic penalties *(1)*.

*(Integrative long answers.)*

- Q36 (8): (a) Precision = TP/(TP+FP) = 45/75 = **0.600** *(2: 1 formula+substitution, 1 value)*. (b) Recall = TP/(TP+FN) = 45/60 = **0.750** *(2)*. (c) F1 = 2PR/(P+R) = 2(0.60)(0.75)/1.35 = 0.900/1.35 = **0.667** *(2)*. (d) Precision 0.60: 40% of positive calls are false alarms → extra biopsies/anxiety; recall 0.75: 25% of tumors are missed *(1)*; in screening, missed tumors are far costlier than false alarms, so prioritizing recall is defensible *(1)*.
- Q37 (10): (a) Parent entropy = −(0.6·log₂0.6 + 0.4·log₂0.4) = 0.6(0.737) + 0.4(1.322) = 0.442 + 0.529 = **0.971** *(2)*. (b) Split A: good child pure → 0; bad child: −(0.2·log₂0.2 + 0.8·log₂0.8) = 0.2(2.322) + 0.8(0.322) = 0.464 + 0.258 = 0.722; weighted = 0.5(0) + 0.5(0.722) = 0.361; IG_A = 0.971 − 0.361 = **0.610** *(3: 1 child entropies, 1 weighting, 1 gain)*. (c) Split B: yes child: −((2/3)(−0.585) + (1/3)(−1.585)) = 0.390 + 0.528 = 0.918; no child: 1.000; weighted = 0.6(0.918) + 0.4(1.000) = 0.951; IG_B = 0.971 − 0.951 = **0.020** *(2)*. (d) **Split A (credit history)** — IG 0.610 ≫ 0.020 *(1)*; the gap shows credit history nearly purifies the classes (one child is pure), while income barely reduces uncertainty, so it carries almost no classification information here *(2)*.

**Mark split summary:** 2-mark × 25 = 50; 3-mark × 9 = 27; 5-mark × 1 = 5; 8-mark × 1 = 8; 10-mark × 1 = 10 → **37 questions, 100 marks**. Long answers: one 8-mark, one 10-mark (≤ 3 ten-mark longs ✓).
