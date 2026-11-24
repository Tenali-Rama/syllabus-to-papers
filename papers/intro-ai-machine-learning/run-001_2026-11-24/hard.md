---
syllabus: intro-ai-machine-learning
run: run-001_2026-11-24
difficulty: hard
paper_number: 3
marks: 100
duration_hours: 3
modules_covered: 8
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "81/90"
---

# Introduction to AI & Machine Learning — End-Semester Examination

**Paper 3 (Hard) · Total marks: 100 · Duration: 3 hours**

| Instructions | |
|---|---|
| Answer all questions | |
| Unless stated otherwise, log = $\log_2$; round final numerical answers to 3 decimal places | |

Every question carries a tag `(Mn, marks, Sk)` = module, marks, blueprint sub-topic IDs.

## Section A — Modules 1 & 2: ML Basics and Classification Algorithms (10 questions × mixed marks = 22 marks)

**Q1.** A junior data scientist tunes a model, checks accuracy on the same 500 rows used for training, and ships the model. Identify the **evaluation-design flaw** and its consequence.
*(M1, 2 marks, S2)*

**Q2.** A metro operator wants to forecast tomorrow's **peak hourly passenger count**. Which task type fits, and why would treating it as one of ten discrete "crowd levels" change the design?
*(M1, 2 marks, S1)*

**Q3.** Training accuracy rises from 80% to 99% as a tree grows, while validation accuracy rises to 84% at depth 6, then drifts down to 79% by depth 30. Diagnose what is happening and state the depth you would ship, with justification.
*(M1, 2 marks, S3)*

**Q4.** A dataset of monthly patient records is sorted by date, then split 80/20 **without shuffling** — the test set is the most recent 20% of months. Explain the risk this split creates and whether the resulting accuracy is trustworthy.
*(M1, 2 marks, S2, S3)*

**Q5.** For a node with class distribution 60/40, Gini = 0.48 while entropy = 0.971. A teammate claims "the two criteria will practically always pick different splits." Evaluate the claim in 2–3 sentences.
*(M2, 2 marks, S4)*

**Q6.** A deployed tree for warranty claims has depth 25 and perfect training accuracy, but appeals overturn 30% of its denials. Diagnose the failure and explain how each of two different fixes would change the tree.
*(M2, 2 marks, S6)*

**Q7.** A bank requires decision trees that regulators can read. Propose a concrete **complexity-control policy** (two specific settings and a validation procedure) for building their credit trees, and justify why the policy serves interpretability.
*(M2, 3 marks, S6)*

**Q8.** A kNN spam filter stores 200,000 emails, each represented by 50,000 token-count features. Name the effect that degrades nearest-neighbour search in this high-dimensional space, and give one mitigation (2 sentences).
*(M2, 2 marks, S7)*

**Q9.** For spam detection, compare naive Bayes and kNN on: (i) training/prediction cost at inbox scale, and (ii) behaviour when a new scam phrase appears that was never in training. State which you would deploy and why.
*(M2, 3 marks, S7)*

**Q10.** After testing every candidate attribute at a node, a tree builder finds **information gain = 0 for all of them**. What does this tell you about the node, and what should the algorithm do?
*(M2, 2 marks, S5)*

---

## Section B — Module 3: Neural Networks and Deep Learning (6 questions × mixed marks = 16 marks)

**Q11.** Deep networks overwhelmingly use ReLU-style activations rather than sigmoid. Give two distinct technical reasons (e.g. gradient behaviour, sparsity/computation), each tied to a failure mode of sigmoid in deep stacks.
*(M3, 2 marks, S9)*

**Q12.** A network must output a **predicted delivery time in minutes** (e.g. 34.7). The appropriate output-layer activation is:
(A) Sigmoid

(B) Step

(C) Linear/identity

(D) Softmax over 2 classes
*(M3, 2 marks, S9)*

**Q13.** In a perceptron trained with the update $w \leftarrow w + \eta\,y\,x$, an engineer sets **$\eta = 50$**. Evaluate what will go wrong compared with $\eta = 0.1$, and why the issue is worse when input features have very different scales.
*(M3, 2 marks, S8)*

**Q14.** State the role of the **chain rule** in backpropagation: what quantity flows backward, and how a layer far from the output still receives a training signal.
*(M3, 2 marks, S10)*

**Q15.** A clinic must classify X-rays but has only **800 labeled images**, and clinicians require a justification for each prediction. Evaluate CNN vs a small MLP trained on raw **$512 \times 512$ grayscale** pixels (262,144 input values) for this setting, addressing data efficiency and interpretability.
*(M3, 3 marks, S11)*

**Q16.** *(Numerical — CNN dimensions)* An input image of size **$28 \times 28 \times 1$** passes through:

| Layer | Operation | Parameters |
|---|---|---|
| 1 | Convolution | **16 filters, kernel $3 \times 3$, stride 1, padding 1** |
| 2 | Max-pooling | **$2 \times 2$, stride 2** |

(a) Compute Layer 1's output dimensions, showing the formula with substituted values. *(2 marks)*
(b) Compute Layer 2's output dimensions. *(2 marks)*
(c) State how many trainable weights (including biases) Layer 1 has. *(1 mark)*
*(M3, 5 marks, S12)*

---

## Section C — Modules 4 & 5: Reinforcement Learning; NLP & Large Language Models (8 questions × mixed marks = 18 marks)

**Q17.** A vacuum robot is rewarded for "dirt collected per hour". It learns to repeatedly suck and re-release the same pile of crumbs. Name this failure mode and evaluate which fix is better: (i) change the reward to "floor cleanliness measured by sensor", or (ii) cap re-cleaning of the same cell. Justify.
*(M4, 2 marks, S14)*

**Q18.** In a recommendation RL system, the **agent's policy** and the **environment's transition behaviour** must be distinguished. Which one does the system designer control directly, and which must be learned from feedback?
*(M4, 2 marks, S13)*

**Q19.** A news-recommender RL agent has converged on sports articles for a user whose interests may shift month to month. Design an exploration policy for this setting (name a strategy and its parameter's meaning) and explain the cost of exploring too much.
*(M4, 3 marks, S14)*

**Q20.** A support team's prompt reads: "Fix this customer issue." Evaluate this prompt: name two elements it fails to specify and predict one concrete way the output could be unusable.
*(M5, 2 marks, S16)*

**Q21.** A legal-chatbot cites "Section 12(3) of the Firms (Amendment) Act, 2021, para 4" — a provision that does not exist. Diagnose this failure precisely (name it), and explain why fluent wording makes it **more** dangerous in this domain.
*(M5, 2 marks, S18)*

**Q22.** A tax-advice chatbot was trained on data up to March 2025; a new deduction applies from June 2025. A user asks about the deduction in November 2025. State what the model will most likely do, and the governance control that should accompany deployment.
*(M5, 2 marks, S17, S18)*

**Q23.** Two services send equal-length prompts, but Service A writes "patient_records.csv" while Service B writes "patient records csv". The per-call cost differs. The best explanation is:
(A) A differs in model quality
(B) Tokenizers split on sub-word patterns, so punctuation/underscores change the token count and hence cost
(C) B is charged in a different currency
(D) Cost depends only on output length
*(M5, 2 marks, S15, S17)*

**Q24.** *(Design)* A finance team needs every LLM reply to be a JSON object with exactly the keys `vendor`, `amount_inr`, `due_date` extracted from an invoice. Write the four prompt elements you would include and justify each in one clause (role; exact output schema with an example; instruction to use "null" for missing fields; instruction to output nothing else).
*(M5, 3 marks, S16)*

---

## Section D — Modules 6 & 7: Computer Vision; Responsible AI (8 questions × mixed marks = 19 marks)

**Q25.** A PCB-inspection dataset has 2% "defect" images. The team proposes to report accuracy only. Evaluate the proposal and recommend the metric pair you would report instead, with one sentence of justification.
*(M6, 2 marks, S21, S19)*

**Q26.** A pedestrian detector reliably outputs boxes on pedestrians but its boxes consistently start 40 pixels below the head, truncating people at the shoulders. Classify this failure (localization vs classification) and state one downstream consequence for an automated braking system.
*(M6, 2 marks, S20)*

**Q27.** **IoU** (intersection over union) is used in detection evaluation because:
(A) It measures image sharpness
(B) It scores how well a predicted box overlaps the ground-truth box, so both existence and localization quality are judged
(C) It counts the number of objects in the scene
(D) It replaces the need for class labels
*(M6, 2 marks, S21)*

**Q28.** *(Numerical — IoU)* Ground-truth box G: (x, y, w, h) = **(20, 30, 60, 40)**. Predicted box P: **(30, 40, 60, 40)**. Coordinates are (x_left, y_top, width, height). Compute the intersection area, union area, and IoU (3 d.p.), then state whether P is accepted as a correct detection under the rule **IoU ≥ 0.5**.
*(M6, 3 marks, S21)*

**Q29.** A résumé-screening tool trained on ten years of company hiring data selects far fewer candidates from a women's college that historically received few invites. Identify the bias type and trace how it entered the pipeline.
*(M7, 2 marks, S23)*

**Q30.** *(Numerical — fairness metric)* A loan model's decisions over one quarter: Group A — 400 applicants, 160 approved; Group B — 200 applicants, 40 approved. Compute the approval rates and the **disparate impact ratio** (3 d.p.), then state the verdict under the four-fifths rule (ratio < 0.80 indicates adverse impact).
*(M7, 3 marks, S22)*

**Q31.** A bank's loan model has run in production for a year. Design a concise **audit plan**: three checks the audit must perform and the artefact each produces.
*(M7, 3 marks, S24)*

**Q32.** Define **equalized odds** in one sentence and explain in one more sentence why it is a stricter requirement than demographic parity.
*(M7, 2 marks, S22)*

---

## Section E — Module 8 and Integrative Long Answers (5 questions × mixed marks = 25 marks)

**Q33.** An emergency department wants an AI triage assistant that prioritizes patients. Evaluate this deployment: name its highest-risk failure mode and one design control that specifically addresses it.
*(M8, 2 marks, S25)*

**Q34.** A state board proposes AI grading of essay answers. Identify two distinct concerns (e.g. bias vs explainability/appeals) and one process safeguard that covers both.
*(M8, 2 marks, S26)*

**Q35.** *(Design)* A logistics firm with 60 delivery vans wants to cut fuel cost using AI; it has one year of route logs, fuel receipts, and GPS traces, but no "optimal route" labels. Propose the AI approach (task type + method family), justify why it fits the unlabeled data, and name one success metric.
*(M8, 3 marks, S26)*

**Q36.** A city's deployed benefits-eligibility model approves applicants from Ward A at 62% and Ward B (similar income profile) at 41%; the model uses postcode as a feature. Ward B is historically a minority neighbourhood.
(a) Identify two likely **sources of bias** in this system and how each enters. *(3 marks)*
(b) Propose **two fairness metrics** the city should compute, saying exactly what each tests. *(3 marks)*
(c) Recommend **two governance controls** for the deployed system, saying what each prevents. *(2 marks)*
*(M7, 8 marks, S22, S23, S24)*

**Q37.** A phone app must detect crop disease from leaf photos taken by farmers: low-cost phones, variable lighting, and 50,000 unlabeled field photos but only 2,000 labeled ones. Compare **three architectures** — (i) CNN trained from scratch, (ii) CNN with pretrained backbone (transfer learning), (iii) kNN on hand-crafted colour/texture features — on data efficiency, expected accuracy, and on-device compute. Conclude with a recommendation and one measured trade-off you accept.
*(M3, 10 marks, S11, S19, S26 — spans Modules 3, 6 and 8)*

---

## Answer Key

### Section A — Modules 1 & 2 (22 marks)
- Q1 (2): Flaw: evaluating on training data — no held-out set *(1)*; consequence: reported accuracy measures memorization, generalization is unknown, likely overfit model ships *(1)*.
- Q2 (2): Regression — passenger count is numeric and meaningful to interpolate *(1)*; discretizing into levels turns it into classification, losing precision but gaining robustness to count noise *(1)*.
- Q3 (2): Depth 6 — validation peaks there; beyond it the model trades generalization for training memorization (overfitting beyond depth 6) *(1 diagnosis + 1 justified choice)*.
- Q4 (2): Risk *(1)*: a temporal split tests extrapolation, not interpolation — if patient patterns drift between the two periods, the recent 20% need not represent future data, so measured accuracy can be untrustworthy, and the split is **never valid** if the team re-splits after seeing results; Verdict *(1)*: trustworthy only under a stated stationarity assumption (input–label patterns stable across the periods). Accept either committed position — trustworthy-with-the-assumption-stated, or not-trustworthy-without-it — not a hedge that argues both.

*(Module 2 questions.)*

- Q5 (2): Verdict *(1)*: the claim is false in practice. Reason *(1)*: both criteria are concave, monotone functions of impurity that peak at 50/50 and reach 0 at purity, so they almost always rank candidate splits the same way — they differ mainly in sensitivity to the middle of the range, not in which split is chosen.
- Q6 (2): Diagnosis: overfit — perfect training accuracy + 30% overturned denials means the tree memorized noise *(1)*; fixes: pruning/depth cap shrinks the tree toward generalizable denials, and minimum-leaf-size merges tiny pure leaves that encoded idiosyncratic cases *(1)*.
- Q7 (3): Policy: e.g. max_depth 4–6 and min_samples_leaf ≥ 50 *(1)*, tuned by validation-set selection of the setting with best validation accuracy/accuracy-interpretability trade-off *(1)*; justification: shallow trees with sizeable leaves yield short, readable rule paths a regulator can audit *(1)*.
- Q8 (2): Curse of dimensionality *(1)* — distances concentrate, so nearest/farthest neighbours become barely distinguishable; mitigation: dimensionality reduction/embeddings or approximate nearest-neighbour index *(1)*.
- Q9 (3): Cost: NB trains in one pass (feature counts) and predicts in milliseconds; kNN stores all mail and must scan/compress it per prediction — expensive at inbox scale *(1)*; new phrase: NB sees unseen tokens as zero-count evidence (handles gracefully via smoothing, slow to exploit), kNN also fails if the scam mail resembles nothing stored *(1)*; deploy NB for cost, accepting the novelty gap, optionally with periodic retraining *(1)*.
- Q10 (2): The node's samples are already class-pure or no attribute correlates with the label locally *(1)*; the algorithm makes the node a leaf (predicting the majority class) — further splitting cannot help *(1)*.

### Section B — Module 3 (16 marks)
- Q11 (2): Two reasons × 1 mark: sigmoid gradients shrink toward 0 for large |z|, so deep stacks suffer vanishing gradients; ReLU keeps gradient 1 on the positive side, and its zero output for negative inputs gives sparse, cheaper activations.
- Q12 (2): **C** *(letter 1; justification 1)* — a linear output can emit any real value such as 34.7; sigmoid caps at (0,1) and softmax makes a distribution, both wrong for regression targets.
- Q13 (2): With $\eta = 50$, one misclassified point throws the weights a huge distance, so training oscillates/diverges instead of settling *(1)*; with unscaled features the largest-magnitude feature dominates the $50x$ term, compounding the overshoot *(1)*.
- Q14 (2): The loss gradient w.r.t. each layer's outputs/weights flows backward *(1)*; the chain rule multiplies downstream gradients by each layer's local derivatives, so even early layers receive a signal proportional to their influence on the loss *(1)*.
- Q15 (3): Data efficiency: CNN from scratch on 800 images overfits; transfer learning / weight sharing needs far fewer labeled examples than an MLP on 262,144 grayscale inputs (accept $\approx 786$k if the answer states the RGB assumption, since $512 \times 512 \times 3 \approx 786$k — either figure is correct when its channel basis is stated) *(1.5)*; interpretability: pixel MLP gives no localization, while CNN feature-map visualizations (e.g. saliency over the lesion region) give clinicians checkable evidence — though neither is a full justification, supporting human review *(1.5)*.
- Q16 (5): (a) Out = $\lfloor(28 + 2 \cdot 1 - 3)/1\rfloor + 1 = \lfloor 27 \rfloor + 1 = $**28 → 28 × 28 × 16** *(2: 1 formula with substitution, 1 result incl. channels)*. (b) Pool: $\lfloor(28 - 2)/2\rfloor + 1$ = 13 + 1 = **14 → 14 × 14 × 16** *(2)*. (c) Weights = $3 \cdot 3 \cdot 1 \cdot 16$ = 144 + 16 biases = **160** *(1)*.

### Section C — Modules 4 & 5 (18 marks)

*(Module 4 questions.)*

- Q17 (2): Failure mode: reward hacking — exploiting the metric rather than the intent *(1)*; fix (i) is better because it re-anchors the reward to the true goal (cleanliness), while (ii) only patches one loophole and invites others *(1)*.
- Q18 (2): The designer controls the **policy** (the recommendation logic) directly *(1)*; the environment's transition behaviour (user reactions, click probabilities) must be learned from feedback *(1)*.
- Q19 (3): Strategy: $\epsilon$-greedy — with probability $\epsilon$ show an exploratory non-sports article, else the current best *(1)*; $\epsilon$ is the fraction of traffic spent exploring, tunable as interests drift *(1)*; cost of too much exploration: wasted impressions the user dislikes, lower engagement/revenue than exploitation would give *(1)*.

*(Module 5 questions.)*

- Q20 (2): Missing elements: which issue/customer/ticket, and the output format (e.g. reply text vs resolution steps vs escalation) *(1)*; predicted failure: a generic, rambling response addressed to the wrong issue or in unusable format *(1)*.
- Q21 (2): Hallucination — fabricated citation content *(1)*; fluency removes the reader's natural suspicion, so a confident fake citation can be acted on in a legal setting where verification is costly *(1)*.
- Q22 (2): It will most likely answer from pre-June-2025 knowledge — stating the deduction doesn't exist or describing the old rule *(1)*; governance: publish the knowledge cutoff in-product and route tax questions to a human/retrieval system over current law *(1)*.
- Q23 (2): **B** *(letter 1; justification 1)*. Sub-word tokenizers fragment differently around underscores/punctuation, changing token count and cost; output length alone does not set cost.
- Q24 (3): Any three of the four elements, 1 mark each *(1 + 1 + 1)*: role ("you are an invoice-data extractor") pins task; exact schema with a worked JSON example fixes key names/order; "use null for missing fields" prevents invented values; "output nothing except JSON" keeps the reply machine-parseable. *(Tiebreaker note — the 4th element carries no mark of its own: if all four are present and correct, use their quality to break ties between otherwise equal answers.)*

### Section D — Modules 6 & 7 (19 marks)

*(Module 6 questions.)*

- Q25 (2): Reject — a "no defect" predictor scores 98% while missing every defect *(1)*; report precision and recall on the defect class (e.g. recall for catching defects, precision for line-stop cost) *(1)*.
- Q26 (2): Localization failure — classification is right, box placement is wrong *(1)*; consequence: a braking system using box height/position may misjudge person extent/trajectory or fail overlap tests, delaying or misplacing the stop decision *(1)*.
- Q27 (2): **B** *(letter 1; justification 1)*. IoU quantifies box overlap, so a detection must both exist and be well-placed; it says nothing about sharpness or counts.
- Q28 (3): G spans x 20–80, y 30–70; P spans x 30–90, y 40–80. Intersection = 50 × 30 = **1500** *(1)*; union = 2400 + 2400 − 1500 = **3300** *(1)*; IoU = 1500/3300 = **0.455** → below 0.5 → **rejected** *(1)*.

*(Module 7 questions.)*

- Q29 (2): Historical/sampling bias *(1)*: the training labels (past invites) already under-selected that college's candidates, so the model learns and reproduces the historical pattern *(1)*.
- Q30 (3): Rates: A = 160/400 = **0.400**; B = 40/200 = **0.200** *(1)*; DI ratio = 0.200/0.400 = **0.500** *(1)*; verdict: 0.500 < 0.80 → adverse impact — fails the four-fifths rule *(1)*.
- Q31 (3): Three checks × 1 (check + artefact): per-group error/approval-rate analysis → disparity report; outcome-vs-decision review on a labeled sample → accuracy/calibration memo; documentation & access review (model card, data lineage, who can override) → audit log/model card update.
- Q32 (2): Equalized odds requires equal true-positive and false-positive rates across groups *(1)*; it is stricter because demographic parity constrains only the decision rate, while equalized odds constrains both error types conditional on the true outcome *(1)*.

### Section E — Module 8 and long answers (25 marks)

*(Module 8 questions.)*

- Q33 (2): Highest risk: systematically under-triaging a subgroup (missed emergencies) *(1)*; control: human clinician override on every AI priority with mandatory re-triage channel for deteriorating patients *(1)*.
- Q34 (2): Concerns: bias against certain writing styles/topics, and opaque scores undermining appeals *(1 each, any two)*; safeguard: AI score as recommendation only, with human grading of a calibrated sample and an appeal route *(1)*. (Max 2.)
- Q35 (3): Approach: unsupervised/optimization learning — e.g. clustering routes or reinforcement learning / route-optimization over historical traces *(1)*; fits unlabeled data because fuel cost per route is a computable feedback signal, no "optimal" labels needed *(1)*; metric: fuel per delivery (or per km) reduction vs baseline *(1)*.

*(Integrative long answers.)*

- Q36 (8): (a) Three marks, 1 per point: historical bias — past approval decisions encode historical exclusion of Ward B and become the training labels *(1)*; feature/proxy bias — postcode is a near-proxy for community, letting the model discriminate directly *(1)*; tracing how at least one source enters the pipeline (data → labels/features → learned rule → deployed decisions) *(1)*. (b) Demographic parity: tests whether approval **rates** are equal across wards *(1)*; applied here — 62% vs 41% already fails demographic parity as stated *(1, own line: the substantive comparison, not restating the prompt)*; equalized odds: tests whether TPR/FPR are equal conditional on true eligibility, catching cases where parity holds but errors do not *(1)*. (c) Two controls × 1: routine disparity audits with a public report *(1)*; human review/appeal path for every denial, plus removal or testing of the postcode feature before retraining *(1)*.
- Q37 (10): Comparison, per architecture 3 × 3 = 9 *(each architecture earns 1 data efficiency + 1 expected accuracy + 1 on-device compute, and each point must be judged against the 2,000-label / low-power constraints, not in the abstract)*: (i) from-scratch CNN — data-inefficient: far more than 2,000 labels needed, likely overfits; best accuracy ceiling in principle but unreachable with this data; heavy training compute, moderate on-device inference cost *(3)*. (ii) pretrained backbone (transfer learning) — best data efficiency: 2,000 labels suffice via fine-tuning; highest expected accuracy on natural photo tasks; moderate on-device cost, quantizable for low-power phones *(3)*. (iii) kNN on hand-crafted colour/texture features — trivially trainable on 2,000 labels; accuracy ceiling low under variable lighting because hand-crafted features miss shape/lesion structure; cheapest on-device compute *(3)*. Recommendation: must be stated as (ii), or an alternative justified against these constraints — required, but carries no separate mark *(0)*. One concrete trade-off, tied to the recommendation, earns the final mark *(1: e.g. accept on-device latency/memory cost or serve server-side; accept residual bias toward diseases resembling the pretraining domain — a stated cost, not a slogan)*.

**Mark split summary:** 2-mark × 25 = 50; 3-mark × 9 = 27; 5-mark × 1 = 5; 8-mark × 1 = 8; 10-mark × 1 = 10 → **37 questions, 100 marks**. Long answers: one 8-mark, one 10-mark (≤ 3 ten-mark longs ✓).
