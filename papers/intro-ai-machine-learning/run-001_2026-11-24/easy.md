---
syllabus: intro-ai-machine-learning
run: run-001_2026-11-24
difficulty: easy
paper_number: 1
marks: 100
duration_hours: 3
modules_covered: 8
question_types: [MCQ, short-answer, numerical, long-answer]
qa_verdict: ACCEPTED
reviewer_score: "81/90"
---

# Introduction to AI & Machine Learning — End-Semester Examination

**Paper 1 (Easy) · Total marks: 100 · Duration: 3 hours**

| Instructions | |
|---|---|
| Answer all questions | |

Every question carries a tag `(Mn, marks, Sk)` = module, marks, blueprint sub-topic IDs.

## Section A — Modules 1 & 2: ML Basics and Classification Algorithms (10 questions × mixed marks = 22 marks)

**Q1.** Which statement correctly distinguishes classification from regression?
(A) Classification predicts continuous values; regression predicts categories
(B) Classification predicts a discrete category label; regression predicts a continuous numeric value
(C) Classification is unsupervised; regression is supervised
(D) Classification requires images; regression requires tables
*(M1, 2 marks, S1)*

**Q2.** A hospital model predicts a patient's blood pressure reading from age, weight, and activity data. This is an example of:
(A) Classification, because the output is a medical quantity
(B) Clustering, because there are several inputs
(C) Regression, because the output is a continuous numeric value
(D) Reinforcement learning, because the model improves with feedback
*(M1, 2 marks, S1)*

**Q3.** Put these ML workflow steps in the correct order: (i) model training, (ii) data collection, (iii) evaluation on held-out data, (iv) data cleaning.
(A) ii → i → iii → iv  (B) ii → iv → i → iii  (C) ii → iv → iii → i  (D) iv → ii → i → iii
*(M1, 2 marks, S2)*

**Q4.** *(Numerical)* An inbox provider has **1,200 labeled emails** and splits them **70% train / 30% test**. State the number of emails in each set, and name the problem that training accuracy alone cannot detect.
*(M1, 2 marks, S2, S3)*

**Q5.** In a decision tree for loan approval, a **leaf node** represents:
(A) A question about one attribute  (B) A final predicted decision (class)  (C) The root of the tree  (D) A measurement error
*(M2, 2 marks, S4)*

**Q6.** The **Gini impurity** of a node measures:
(A) The depth of the tree below that node
(B) How often a randomly chosen sample would be mislabeled if labeled according to the node's class distribution
(C) The number of samples in the node
(D) The correlation between the tree's attributes
*(M2, 2 marks, S4)*

**Q7.** *(Numerical)* A node in an email-filter tree contains **8 spam and 2 non-spam** emails. Compute its Gini impurity, showing the substitution into the formula. (Round to 2 decimal places.)
*(M2, 3 marks, S4)*

**Q8.** When a decision-tree algorithm splits a node, it prefers the attribute that:
(A) Produces the most balanced number of samples only
(B) Is alphabetically first
(C) Produces the largest increase in purity (largest information gain)
(D) Has the largest numeric range
*(M2, 2 marks, S5)*

**Q9.** Explain in 2–3 sentences what **pruning** a decision tree does, and why a tree whose every leaf is pure can still predict poorly on new data.
*(M2, 3 marks, S6)*

**Q10.** With **k = 1** nearest neighbours, a new point is classified as:
(A) The majority class of all training points
(B) The class of the single closest training point
(C) The average of the numeric labels
(D) Randomly, since no neighbors are used
*(M2, 2 marks, S7)*

---

## Section B — Module 3: Neural Networks and Deep Learning (6 questions × mixed marks = 16 marks)

**Q11.** A **perceptron** makes its decision by:
(A) Averaging the inputs
(B) Computing a weighted sum of inputs plus a bias, then applying a step threshold
(C) Comparing inputs to all stored training examples
(D) Backpropagating the error first
*(M3, 2 marks, S8)*

**Q12.** An **activation function** in a neural network is needed to:
(A) Introduce non-linearity so the network can learn non-linear patterns
(B) Normalize the pixel values
(C) Reduce the number of training samples
(D) Choose the optimizer
*(M3, 2 marks, S9)*

**Q13.** Using the **ReLU** activation, the output for an input of **−3.5** is:
(A) −3.5  (B) 0  (C) 1  (D) 3.5
*(M3, 2 marks, S9)*

**Q14.** Hidden layers in a multi-layer perceptron allow the network to:
(A) Store the raw training data
(B) Build intermediate feature combinations of the inputs, enabling more complex decision boundaries than a single layer
(C) Guarantee zero training error
(D) Remove the need for labeled data
*(M3, 2 marks, S10)*

**Q15.** In a CNN, a **pooling layer** typically:
(A) Learns new filters by gradient descent
(B) Downsamples a feature map (e.g. taking the max in each 2×2 region), reducing its size while keeping strong activations
(C) Converts images to text
(D) Adds labeled examples to the dataset
*(M3, 3 marks, S11)*

**Q16.** *(Numerical)* A perceptron has weights **w₁ = 0.4, w₂ = −0.6**, bias **b = 0.1**, and step activation with threshold 0 (output 1 if net ≥ 0, else 0). For the input **x₁ = 1, x₂ = 1**, compute the net input and the perceptron's output, showing the substitution.
*(M3, 5 marks, S8)*

---

## Section C — Modules 4 & 5: Reinforcement Learning; NLP & Large Language Models (8 questions × mixed marks = 18 marks)

**Q17.** In reinforcement learning, a **reward** is:
(A) The model's parameters
(B) A scalar feedback signal the agent receives from the environment after an action
(C) The number of training epochs
(D) A label attached to each input
*(M4, 2 marks, S13)*

**Q18.** In a game-playing agent, the **agent** and the **environment** are respectively:
(A) The game program and the programmer
(B) The learning/decision-making program and everything it interacts with (the game board and rules)
(C) The reward and the state
(D) The training data and the test data
*(M4, 2 marks, S13)*

**Q19.** Explain in 2–3 sentences what the **exploration vs exploitation** trade-off means for a delivery-route robot that has already found a good route, and why always exploiting can be harmful.
*(M4, 3 marks, S14)*

**Q20.** **Tokenization** in NLP is:
(A) Encrypting the text
(B) Splitting text into smaller units (words or sub-words) that the model processes
(C) Translating the text to another language
(D) Deleting punctuation only
*(M5, 2 marks, S15)*

**Q21.** Which prompt is most likely to get a useful, correctly formatted answer from an LLM?
(A) "Write me something about birds that I would want to read."
(B) "Write a 5-bullet summary of how migration helps Arctic terns, for a grade-8 reader."
(C) "Write about birds, and make the answer as good as you can."
(D) "Write quickly about the bird topic we discussed last time."
*(M5, 2 marks, S16)*

**Q22.** Giving an LLM **two worked examples** inside the prompt before asking it to solve a new case is called:
(A) Fine-tuning  (B) Few-shot prompting  (C) Reinforcement learning  (D) Data augmentation
*(M5, 2 marks, S16)*

**Q23.** At its core, a generative LLM produces text by:
(A) Looking up the answer in a stored database of facts
(B) Predicting the next token repeatedly, given the tokens so far
(C) Running a decision tree on the prompt
(D) Summarizing every web page in real time
*(M5, 2 marks, S17)*

**Q24.** Explain in 2–3 sentences what a **knowledge cutoff** is, and name one situation where it could cause an LLM to give an outdated answer.
*(M5, 3 marks, S18)*

---

## Section D — Modules 6 & 7: Computer Vision; Responsible AI (8 questions × mixed marks = 19 marks)

**Q25.** **Image classification** takes an image as input and outputs:
(A) A bounding box per object
(B) A single category label for the image
(C) A caption sentence
(D) The image's resolution
*(M6, 2 marks, S19)*

**Q26.** A traffic system must output **where each car is** (a box) **and** what it is. The required task is:
(A) Image classification  (B) Object detection  (C) Image generation  (D) Semantic segmentation only
*(M6, 2 marks, S20)*

**Q27.** To train an image classifier of crop diseases, the training data must be:
(A) Unlabeled images
(B) Images paired with correct labels (e.g. "healthy", "leaf-rust")
(C) Only images taken at night
(D) Text descriptions of diseases
*(M6, 2 marks, S19)*

**Q28.** A tumor-screening dataset has 95% healthy and 5% tumor images. A model that predicts "healthy" for every image still gets 95% accuracy. Explain in 2–3 sentences why accuracy alone is a misleading way to judge this model.
*(M6, 3 marks, S21)*

**Q29.** **Algorithmic bias** refers to:
(A) Random bugs in the code
(B) Systematic errors that treat certain groups or cases unfairly, often inherited from data or design choices
(C) Any model with accuracy below 100%
(D) The bias term in a perceptron
*(M7, 2 marks, S23)*

**Q30.** A hiring model is trained on 10 years of past hiring decisions in which most engineers hired were men. The most likely consequence is:
(A) The model becomes more accurate for all groups
(B) The model may learn to favour male applicants, repeating the historical pattern
(C) The model ignores gender automatically
(D) The model cannot be trained at all
*(M7, 2 marks, S23)*

**Q31.** Explain in 2–3 sentences what **demographic parity** asks of a model's decisions, using a loan-approval example.
*(M7, 3 marks, S22)*

**Q32.** A city uses an AI system to screen housing-benefit applications; at present, denials go out automatically with no explanation and no route to contest them. From this labeled list, choose the **two** oversight mechanisms that best fit this deployment, and give one sentence on why each helps:
(i) periodically re-measuring the model's overall accuracy;
(ii) human review of each denial, with a stated-reason requirement, before it is sent;
(iii) collecting a larger training set for the next model version;
(iv) an appeal channel where an applicant can have the decision re-examined by a human caseworker.
*(M7, 3 marks, S24)*

---

## Section E — Module 8 and Integrative Long Answers (5 questions × mixed marks = 25 marks)

**Q33.** Name one real AI application in **healthcare** and state what data it uses.
*(M8, 2 marks, S25)*

**Q34.** A bank flags credit-card transactions as fraudulent in real time. This system is best described as:
(A) Unsupervised image segmentation
(B) A supervised classification system operating on transaction features
(C) A CNN trained on receipts
(D) A reinforcement-learning agent that sets the prices
*(M8, 2 marks, S25)*

**Q35.** A farmer wants early warning of pest outbreaks from field photos and weather readings. Propose an AI approach (task type + one data source) and justify the choice in 2–3 sentences.
*(M8, 3 marks, S26)*

**Q36.** A hospital wants a model that predicts whether a discharged patient will be **readmitted within 30 days**. An early prototype scores 89% on the rows it was trained on. A nurse reviewing it notices one input feature: *the number of follow-up appointments booked after discharge* — a value that can only be known once the 30-day window has already closed.
(a) Arrange the main ML workflow stages for this project in order, with one sentence each. *(4 marks)*
(b) Design the evaluation split for this data and name the problem a held-out set protects against. *(2 marks)*
(c) State whether the appointment-booking feature should be used in the shipped model, and why. *(2 marks)*
*(M1, 8 marks, S1, S2, S3)*

**Q37.** A gym's membership team builds a decision tree to predict churn. From **8 members** in an illustrative sample, **4 churned (Y)** and **4 stayed (N)**. Candidate split — "visits per week < 1": Yes → 4 members (**3 Y, 1 N**); No → 4 members (**1 Y, 3 N**). Given: log₂0.75 = −0.415, log₂0.25 = −2.000.
(a) Name the parts of a decision tree and what a leaf represents here. *(2 marks)*
(b) Using the log values provided, calculate the parent entropy, the weighted child entropy for this split, and its information gain. *(4 marks)*
(c) The tree was then grown until every leaf was pure, after which its accuracy on new members dropped sharply. Name the problem and recommend one fix, with a sentence of justification. *(4 marks)*
*(M2, 10 marks, S4, S5, S6)*

---

## Answer Key

### Section A — Modules 1 & 2 (22 marks)
- Q1 (2): **B**. Classification outputs discrete labels, regression outputs continuous values; A swaps the two, C confuses supervised/unsupervised.
- Q2 (2): **C**. Blood pressure is continuous → regression. Distractor A is the trap of equating "medical" with classification.
- Q3 (2): **B**. Collect → clean → train → evaluate. C and D also place data before training, but C evaluates before any model is trained and D cleans before any data is collected; A trains before cleaning and evaluates before cleaning completes. Only B trains on cleaned data and then evaluates on held-out data.
- Q4 (2): Train = 1,200 × 0.70 = **840**, Test = 1,200 × 0.30 = **360** *(1 mark)*; overfitting — strong training accuracy can hide failure on unseen data *(1 mark)*.

*(Module 2 questions.)*

- Q5 (2): **B**. A leaf holds the final class decision; internal nodes ask questions.
- Q6 (2): **B**. Gini = mislabeling probability under the node's class distribution.
- Q7 (3): Gini = 1 − p_spam² − p_non² with p_spam = 8/10 = 0.8, p_non = 0.2 → 1 − (0.64 + 0.04) = **0.32**. *(1 mark setup, 1 mark substitution, 1 mark result.)*
- Q8 (2): **C**. Splits maximize purity gain; balanced counts are not the criterion.
- Q9 (3): Pruning removes branches that fit noise in the training emails, simplifying the tree *(1–2)*; fully pure leaves encode accidental patterns of the training sample, so they fail to generalize to new mail *(1–2)*. *(Split: 1 mark what pruning does, 2 marks why purity ≠ generalization.)*
- Q10 (2): **B**. k = 1 uses exactly the nearest neighbor's class.

### Section B — Module 3 (16 marks)
- Q11 (2): **B**. Perceptron = weighted sum + bias → step threshold.
- Q12 (2): **A**. Without non-linear activations, stacked layers collapse to one linear map.
- Q13 (2): **B**. ReLU(x) = max(0, x) → max(0, −3.5) = 0.
- Q14 (2): **B**. Hidden layers compose intermediate features; they do not guarantee zero error (C) or remove the need for labels (D).
- Q15 (3): **B**. Pooling downsamples feature maps, keeping strong activations and cutting computation; filter learning happens in convolutional layers, not pooling.
- Q16 (5): net = w₁x₁ + w₂x₂ + b = 0.4(1) + (−0.6)(1) + 0.1 = **−0.1** *(3 marks: formula + correct arithmetic)*; −0.1 < 0 → output **0** *(2 marks)*.

### Section C — Modules 4 & 5 (18 marks)

*(Module 4 questions.)*

- Q17 (2): **B**. A reward is scalar feedback from the environment, not a parameter or a label.
- Q18 (2): **B**. The agent is the decision-making program; the environment is the game it acts within.
- Q19 (3): Exploration = trying new routes to discover possibly better ones; exploitation = using the known good route *(1)*. Always exploiting risks missing better routes that are discovered only by trying alternatives *(2)*.

*(Module 5 questions.)*

- Q20 (2): **B**. Tokenization splits text into model-ready units; it does not encrypt or translate.
- Q21 (2): **B**. All four options are full sentences with similar openings, so only content decides: B alone states the task (summary), the output format (5 bullets), the length, and the audience; A, C and D give a topic but no format or audience.
- Q22 (2): **B**. Worked examples inside the prompt = few-shot prompting; fine-tuning changes weights, not the prompt.
- Q23 (2): **B**. LLMs generate token-by-token via next-token prediction; A describes retrieval, not generation.
- Q24 (3): Cutoff = training data ends at a date, so later events are unknown *(2)*; e.g. asking about a product released or a law passed after the cutoff gives stale answers *(1)*.

### Section D — Modules 6 & 7 (19 marks)

*(Module 6 questions.)*

- Q25 (2): **B**. Classification = one label per image; boxes belong to detection.
- Q26 (2): **B**. Boxes + classes per object = detection.
- Q27 (2): **B**. Supervised image classification needs image–label pairs.
- Q28 (3): The all-"healthy" model misses every tumor, and those 5% of cases are exactly the clinically critical errors that accuracy does not expose *(2)*; per-class precision/recall are needed *(1)*.

*(Module 7 questions.)*

- Q29 (2): **B**. Systematic unfair treatment, distinct from random bugs; D confuses it with the numeric bias term.
- Q30 (2): **B**. The model reproduces the historical hiring pattern it was trained on.
- Q31 (3): Demographic parity asks the positive-decision (approval) rate to be similar across demographic groups *(2)*, e.g. applicants from each neighbourhood approved at roughly the same rate regardless of group *(1)*.
- Q32 (3): Correct pair: (ii) and (iv) *(1 each)*. Third mark — why each helps *(1)*: (ii) human review of each denial before it is sent catches erroneous or biased automatic denials before harm occurs, and the stated-reason requirement makes every decision checkable; (iv) the appeal channel lets wrongly denied applicants get the decision re-examined by a human caseworker after the fact. (i) re-measures accuracy but is model maintenance, not oversight of individual decisions; (iii) is a data-quality step, not oversight.

### Section E — Module 8 and long answers (25 marks)

*(Module 8 questions.)*

- Q33 (2): e.g. diabetic-retinopathy screening using retinal photographs; or triage from symptom text / EHR records *(1 application + 1 matching data type)*.
- Q34 (2): **B**. Labeled fraud/not-fraud history → supervised classification on transaction features.
- Q35 (3): Supervised classification (or detection) over field photos plus weather history to predict outbreak risk *(1)*; justified because labeled historical outbreak records exist and a per-field alert is a usable, discrete output *(2)*.

*(Integrative long answers.)*

- Q36 (8): (a) Four stages × 1 mark, in order: collect labeled discharge records (30-day outcomes per patient); clean/normalize the records; train on the training split; evaluate on held-out data, then deploy with monitoring. *(Judgment note: the split must be defined before tuning begins, not after seeing results.)* (b) Hold out a test set of discharge records set aside **before** any model building or tuning (e.g. a 70/30 split by patient) *(1)*; the held-out set estimates performance on future discharges and exposes overfitting to the training rows *(1)*. (c) Exclude the appointment-booking feature *(1)* — its value leaks the outcome, because whether/when appointments got booked is only known after the 30-day window closes, so it inflates training accuracy and is unavailable at prediction time; the 89% training score is exactly the kind of inflated number this leakage produces *(1)*.
- Q37 (10): (a) Root/internal nodes test attributes ("visits per week < 1"); leaves hold the final prediction — churn (Y) or stay (N) here *(2)*. (b) Parent entropy = −(0.5·log₂0.5 + 0.5·log₂0.5) = −(0.5·(−1) + 0.5·(−1)) = **1.000** *(1)*. Child entropies: yes child (3Y,1N) = −(0.75·(−0.415) + 0.25·(−2.000)) = 0.311 + 0.500 = **0.811**; no child (1Y,3N) = same by symmetry = **0.811** *(1)*. Weighted = 0.5(0.811) + 0.5(0.811) = **0.811** *(1)*. IG = 1.000 − 0.811 = **0.189** *(1)*. (c) Problem: overfitting — a tree grown until every leaf is pure has memorized this sample of 8 members, including noise, so it fails on new members *(2)*. Fix: prune / cap depth / set a minimum leaf size *(1)*, because a smaller tree keeps only the splits that generalize (here, IG 0.189 is modest, so little splitting is justified at all) *(1)*.

**Mark split summary:** 2-mark × 25 = 50; 3-mark × 9 = 27; 5-mark × 1 = 5; 8-mark × 1 = 8; 10-mark × 1 = 10 → **37 questions, 100 marks**. Long answers: one 8-mark, one 10-mark (≤ 3 ten-mark longs ✓).
