# Study Starter — Introduction to AI & Machine Learning

**Read this before the Easy paper. Revisit after each attempt.**

## How to use this file
1. Read each module's sub-topics here, working through the mini-examples by hand.
2. Attempt the Easy paper, then diagnose every mistake against the relevant S# here (an AI study partner helps).
3. Restudy the weak spots, then climb Medium → Hard, repeating the diagnose-and-restudy loop each time.

*Sub-topic tags: [G] = named in the syllabus, [D] = standard intro-course content added by the blueprint.*

---

## Module 1 — Introduction to Machine Learning

### S1 — Supervised learning: classification vs regression [G]
- **What it is:** supervised learning fits a function from labeled examples; **classification** predicts a discrete category (e.g. fruit type: apple/mango/pear) while **regression** predicts a continuous number (e.g. a flat's monthly rent).
- **Worked mini-example:** 40 photos each tagged "ripe" or "unripe" → classification (label output). The same 40 fruits with grams-of-sugar measured per fruit → regression (numeric output). Same data, different target type, different task.
- **Pitfall:** the topic (fruit, medical, photos) does not determine the task — the **target's type** does. A medical dataset is classification if it predicts disease/no-disease but regression if it predicts blood-pressure value.
- **Self-check:** Predicting tomorrow's electricity demand in megawatts — classification or regression?
  <details><summary>reveal answer</summary>Regression — the target is a continuous numeric quantity.</details>

### S2 — The ML workflow [G]
- **What it is:** the standard pipeline: collect data → clean/prepare → split (train/validation/test) → train → evaluate on held-out data → deploy and monitor. Splitting must happen **before** tuning, never after seeing results.
- **Worked mini-example:** a bakery collects 90 days of sales records, removes duplicated rows and fixes mis-entered dates (cleaning), sets aside 20% of the days as a test set, trains a demand model on the other 80%, and only at the end checks error on the held-out 20%.
- **Pitfall:** evaluating on the training data itself, or defining the test set after the model has been tuned on everything, produces an inflated score that says nothing about new data (data leakage).
- **Self-check:** A team trains on all 600 rows, then reports 99% accuracy on those same rows. What is wrong?
  <details><summary>reveal answer</summary>No held-out evaluation — the score measures memorization of the training rows, not generalization to unseen data.</details>

### S3 — Overfitting, underfitting, and generalization [D]
- **What it is:** **overfitting** = great training performance, poor new-data performance (the model memorized noise); **underfitting** = poor performance everywhere (model too simple); **generalization** = performance on unseen data.
- **Worked mini-example:** a model fit to 80 training days of bus-ridership gets train error near zero but validation error four times larger — overfit. A straight line forced through clearly seasonal data misses both train and validation — underfit.
- **Pitfall:** high training accuracy is **not** evidence of a good model; the train–validation gap is the overfitting signal, and the fix (simpler model, more data, regularization/pruning) trades training accuracy for generalization.
- **Self-check:** Train accuracy 97%, validation accuracy 62%. Name the problem and one fix.
  <details><summary>reveal answer</summary>Overfitting; fixes include simplifying/regularizing the model, pruning, or gathering more training data.</details>

---

## Module 2 — Decision Trees and Classification Algorithms

### S4 — Tree structure, Gini impurity, entropy [D]
- **What it is:** a tree tests attributes at internal nodes and outputs a class at leaves. Impurity measures how mixed a node's classes are: $\text{Gini} = 1 - \sum_c p_c^2$; entropy $H = -\sum_c p_c \log_2 p_c$ (both peak at a uniform mix, both reach $0$ at purity).
- **Worked mini-example:** a node holds 8 customers: 6 bought (B), 2 did not (N). $p_B = 0.75$, $p_N = 0.25$. Gini $= 1 - (0.75^2 + 0.25^2) = 1 - (0.5625 + 0.0625) = 0.375$.
- **Pitfall:** Gini is the probability of mislabeling a randomly drawn item, **not** the fraction of majority-class items and **not** an accuracy. Also, Gini and entropy almost always pick the **same** best split — they are not rival answers.
- **Self-check:** A node is 6 of one class and 6 of another. What is its Gini impurity?
  <details><summary>reveal answer</summary>$1 - (0.5^2 + 0.5^2) = 0.5$ — the maximum, i.e. a coin-flip node.</details>

### S5 — Information gain [D]
- **What it is:** the impurity drop from splitting a node on an attribute: $IG = H_{parent} - \sum_v \frac{\lvert v\rvert}{\lvert \text{parent}\rvert} H(v)$. The tree picks the attribute with the largest gain.
- **Worked mini-example:** 15 pet-adoption records: 8 adopted (A), 7 not (N). Parent: $H = -(0.533\log_2 0.533 + 0.467\log_2 0.467) \approx 0.997$ (given $\log_2 0.533 \approx -0.907$, $\log_2 0.467 \approx -1.100$). Split on "age $< 3$ years": **Yes → 9 rows (7A, 2N)**: $H = 0.778 \cdot 0.363 + 0.222 \cdot 2.170 \approx 0.764$; **No → 6 rows (1A, 5N)**: $H = 0.833 \cdot 0.263 + 0.167 \cdot 2.585 \approx 0.650$. Weighted child entropy $= \frac{9}{15}(0.764) + \frac{6}{15}(0.650) \approx 0.718$. $IG \approx 0.997 - 0.718 = 0.279$.
- **Pitfall:** $IG = 0$ does not mean the attribute is "wrong" — it means the split leaves the classes exactly as mixed as before, so the attribute carries no classification information here. And comparing candidate splits always uses the **weighted** child entropy, not the raw sum or the best child alone.
- **Self-check:** After a split, one child is pure and the other has entropy $0.9$. Could the gain still be small?
  <details><summary>reveal answer</summary>Yes — if the pure child holds very few rows, the weighted average stays close to the parent entropy, so the gain is small. Weights matter.</details>

### S6 — Overfitting in trees, pruning, capacity controls [D]
- **What it is:** a tree grown until every leaf is pure has memorized the sample. **Pruning** removes branches; depth caps and minimum-leaf-size limit how finely the tree can fit.
- **Worked mini-example:** a loan tree grown to purity splits on trivia like "application number is even"; capping it at depth 3 keeps only broad rules ("income band", "years employed") and validation accuracy rises even though training accuracy falls.
- **Pitfall:** pure leaves are a red flag, not a goal — a perfectly fitting tree generalizes worst. The right depth is chosen on a **validation** set, and it is usually where validation accuracy peaks, not where training accuracy peaks.
- **Self-check:** Training accuracy rises every time depth grows, but validation accuracy peaked at depth 3 and now falls. What do you deploy and why?
  <details><summary>reveal answer</summary>The depth-3 tree — beyond the validation peak the tree trades generalization for training memorization (overfitting).</details>

### S7 — k-nearest neighbours and naive Bayes [D]
- **What it is:** **kNN** classifies a point by majority vote of its $k$ closest training points (so it stores all data and is lazy). **Naive Bayes** applies Bayes' rule assuming features are independent given the class.
- **Worked mini-example:** kNN with $k = 3$ on flats: a query flat's three nearest labeled neighbours have prices labeled {high, high, low} → predict "high". If the "flat area" feature is measured in thousands while "number of balconies" is 0–3, area dominates the distance — that is why features must be scaled.
- **Pitfall:** naive Bayes' independence assumption is usually false (e.g. "free" and "winner" co-occur in scam mail), yet it still ranks well because correlated evidence points the same way. And in kNN, a badly scaled feature makes points near-duplicates on the scaled dimension, effectively ignoring the others.
- **Self-check:** Why does naive Bayes still work when its independence assumption is violated?
  <details><summary>reveal answer</summary>Because classification needs only the argmax of the posterior — correlated features push the same posterior up, so the ranking survives even if the probability values are miscalibrated.</details>

---

## Module 3 — Neural Networks and Deep Learning

### S8 — The perceptron [G]
- **What it is:** computes a weighted sum $net = \sum_i w_i x_i + b$ and outputs $1$ if $net > 0$, else $0$ (step activation). On a mistake it updates: $w \leftarrow w + \eta\, y\, x$, $b \leftarrow b + \eta\, y$, where $\eta$ is the learning rate.
- **Worked mini-example:** weights $w = (3, -1)$, bias $1$, input $x = (2, 2)$: $net = 3(2) + (-1)(2) + 1 = 5 > 0$ → output $1$. If the true label were $-1$, update with $\eta = 0.2$: $w \leftarrow (3, -1) + 0.2(-1)(2,2) = (2.6, -1.4)$, $b \leftarrow 1 - 0.2 = 0.8$.
- **Pitfall:** $\eta$ scales **each** update — a huge $\eta$ makes one mistake throw the weights far away and training oscillates or diverges; unscaled features make the largest-magnitude feature dominate the sum.
- **Self-check:** With $w = (3,-1)$, $b = 1$ above, what is the output for $x = (1, 4)$?
  <details><summary>reveal answer</summary>$net = 3 - 4 + 1 = 0$, which is not $> 0$, so the output is $0$.</details>

### S9 — Activation functions: step, sigmoid, ReLU [D]
- **What it is:** activations add non-linearity. Step: $\{0,1\}$ threshold. Sigmoid: $\sigma(z) = \frac{1}{1+e^{-z}} \in (0,1)$. ReLU: $\max(0, z)$. Without them, stacked linear layers collapse into a single linear map.
- **Worked mini-example:** $\sigma(1) = \frac{1}{1+e^{-1}} \approx 0.731$; $\text{ReLU}(-4) = 0$; $\text{ReLU}(6) = 6$. A network of pure linear layers, no matter how deep, can only draw straight decision boundaries.
- **Pitfall:** sigmoid's range is the **open** interval $(0,1)$ — it never outputs exactly $0$ or $1$ (and $[-1,1]$ is tanh's range, not sigmoid's). ReLU outputs $0$ for every negative input, which also means its gradient is exactly $0$ there.
- **Self-check:** Why can't a deep stack of purely linear layers learn a curved boundary?
  <details><summary>reveal answer</summary>The composition of linear maps is itself linear, so the whole network equals one linear map regardless of depth — non-linear activations are what let it bend.</details>

### S10 — Multi-layer perceptrons and backpropagation [D]
- **What it is:** an MLP stacks layers of weighted sums + activations; hidden layers compose intermediate features. **Backpropagation** sends the loss gradient backward via the chain rule, so each weight's update is proportional to its influence on the error.
- **Worked mini-example:** for a loss that depends on output $o$ via $L = (o - t)^2$ with $o = 2h$ and $h = 3z$, the chain rule gives $\frac{dL}{dz} = \frac{dL}{do}\cdot\frac{do}{dh}\cdot\frac{dh}{dz} = 2(o-t)\cdot 2 \cdot 3$ — each layer multiplies in its own local derivative.
- **Pitfall:** backprop is the chain-rule gradient flow, not a data generator and not a prediction algorithm; hidden layers do not guarantee zero error nor remove the need for labeled data.
- **Self-check:** In one sentence, what does backpropagation compute for each weight?
  <details><summary>reveal answer</summary>The partial derivative of the loss with respect to that weight, obtained by multiplying local derivatives layer by layer from output back to input.</details>

### S11 — CNN overview: convolution, pooling, feature maps [G]
- **What it is:** convolution slides small kernels over the image producing **feature maps** (local patterns, shared weights → far fewer parameters than dense layers); **pooling** downsamples maps for translation robustness and cheaper compute. Used for image classification, detection, segmentation.
- **Worked mini-example:** a $5\times5$ kernel that responds to dark-to-bright horizontal edges, slid over a skin-photo, produces a feature map that lights up along lesion borders; a $2\times2$ max-pool then keeps only the strongest response in each block, so a slightly shifted lesion still fires the same pooled unit.
- **Pitfall:** pooling does **not** learn filters and does not reduce channel count — kernels are learned in convolutional layers, and pooling only shrinks each map's height/width.
- **Self-check:** Why does a CNN typically need far less data than a dense net on the same image?
  <details><summary>reveal answer</summary>Weight sharing: one small kernel is reused across every location, giving far fewer parameters than connecting every pixel to every neuron.</details>

### S12 — CNN output-dimension arithmetic [D]
- **What it is:** output size after a convolution/pool layer: $O = \lfloor (W + 2P - K)/S \rfloor + 1$, with input width $W$, kernel $K$, padding $P$, stride $S$. Channels come from the number of filters. Chain the formula layer by layer.
- **Worked mini-example:** input $40 \times 40 \times 3$; conv with kernel $5\times5$, $8$ filters, stride $2$, padding $1$: $O = \lfloor (40 + 2 - 5)/2 \rfloor + 1 = \lfloor 18.5 \rfloor + 1 = 19$ → $19 \times 19 \times 8$. Then $2\times2$ max-pool, stride $2$: $O = \lfloor (19-2)/2 \rfloor + 1 = 9$ → $9 \times 9 \times 8$ (channels unchanged). Kernel weights for the conv layer: $5 \cdot 5 \cdot 3 \cdot 8 = 600$, plus $8$ biases.
- **Pitfall:** three classic slips — forgetting the $+1$, forgetting that pooling changes height/width but **not** channel count, and forgetting that conv weights count input channels too ($K \cdot K \cdot C_{in} \cdot C_{out}$, biases added separately).
- **Self-check:** Pooling a $19 \times 19 \times 8$ map with $2\times2$, stride $2$ gives what shape?
  <details><summary>reveal answer</summary>$9 \times 9 \times 8$: $\lfloor(19-2)/2\rfloor + 1 = 9$ per side, channels still $8$.</details>

---

## Module 4 — Reinforcement Learning

### S13 — Reward-based learning and the RL loop [G]
- **What it is:** an **agent** acts in an **environment**: state → action → reward + next state. The **policy** maps states to actions and is what learning improves, using scalar **rewards** as the only feedback.
- **Worked mini-example:** a warehouse robot gets $+10$ for reaching the loading bay and $-1$ for every step taken; over trials it learns the shorter route because the per-step penalty makes long routes lower-value. The robot is the agent; the floor layout is the environment; the route rule it converges to is the policy.
- **Pitfall:** the reward is scalar feedback from the environment — not a model parameter, not a label; and the designer controls the policy directly, while environment behaviour (how states respond to actions) must be learned from feedback.
- **Self-check:** In the robot example, which element is the policy?
  <details><summary>reveal answer</summary>The learned mapping from locations (states) to moves (actions) — the route rule itself.</details>

### S14 — Exploration vs exploitation, reward design, sparse rewards [D]
- **What it is:** **exploitation** uses the currently known-best action; **exploration** tries alternatives to discover better ones (e.g. $\epsilon$-greedy: explore with probability $\epsilon$). **Sparse rewards** give feedback only at the end, leaving intermediate actions uncredited.
- **Worked mini-example:** a news app shows articles with $\epsilon = 0.15$: 85% of impressions go to the current best article, 15% to others — $\epsilon$ is the fraction of traffic spent exploring. A maze agent rewarded only at the exit of a 260-step task cannot tell which of its many turns mattered (the credit-assignment problem); a small per-step progress reward fixes that.
- **Pitfall:** too much exploration wastes interactions the user dislikes, and pure exploitation risks missing better options forever. And a poorly designed reward invites **reward hacking** — optimizing the metric instead of the intent (fix the reward's anchoring, not just one loophole).
- **Self-check:** An agent gets reward only when the full 260-step task ends. Why does it learn so slowly?
  <details><summary>reveal answer</summary>Sparse reward: almost no action receives a credit signal, so the agent cannot tell which moves contributed to the final outcome; shaping or return-estimation remedies this.</details>

---

## Module 5 — NLP and Large Language Models

### S15 — Tokenization and text representation [D]
- **What it is:** tokenization splits text into model-ready units (words or sub-words); tokens are then mapped to numeric vectors. The same word can differ in meaning by context, so tokenization alone does not resolve sense.
- **Worked mini-example:** "unhappiness" might split into the sub-words `un` + `happi` + `ness` — three tokens; the bank of a river vs. a savings bank tokenize identically but need surrounding context to be told apart.
- **Pitfall:** tokenization is splitting into units, not translation, encryption, or understanding; and a context-free representation of polysemous words will pick one meaning and err.
- **Self-check:** Why can sub-word tokenization change the cost of a request?
  <details><summary>reveal answer</summary>Punctuation, underscores, or rare words fragment differently, changing the total token count — and cost is billed per token, not per word or per output line.</details>

### S16 — Prompt engineering [G]
- **What it is:** steering behaviour through the prompt: explicit **task** statement, output **format**, **context**, **role framing**, and **few-shot** worked examples inside the prompt. None of this changes the model's weights.
- **Worked mini-example:** "Summarise this refund policy as exactly 4 bullet points for a call-centre agent" beats "tell me about refunds" because it names the task, a countable format, and the audience; two worked input→output examples turn it into a few-shot prompt.
- **Pitfall:** in-context examples steer only that request — they are not fine-tuning and do not guarantee factual correctness. Also, role framing ("you are a tax advisor") sets register and defaults, but still touches no weights.
- **Self-check:** Name three things a strong prompt specifies beyond the bare topic.
  <details><summary>reveal answer</summary>Any three: the task, the output format, the length, the audience, the role, worked examples, what to exclude.</details>

### S17 — LLMs: training, generation, token/cost arithmetic [G]
- **What it is:** LLMs are trained on large text corpora and generate **token by token**, each token predicting the next. Cost = (input tokens × input rate) + (output tokens × output rate); rates are per million tokens.
- **Worked mini-example:** a call with 4,000 input tokens and 1,000 output tokens at $\$0.60$ and $\$0.90$ per million: input $4{,}000 \times \$0.60/10^6 = \$0.0024$; output $1{,}000 \times \$0.90/10^6 = \$0.0009$; per-call $\$0.0033$; 250 calls $\rightarrow \$0.825$.
- **Pitfall:** generation is next-token prediction, not retrieval from a database; and output length alone does not set cost — input tokens and the per-token rates matter too.
- **Self-check:** Doubling only the output tokens of the mini-example changes the per-call cost to what?
  <details><summary>reveal answer</summary>Output doubles to $2{,}000 \times \$0.90/10^6 = \$0.0018$; per-call $= \$0.0024 + \$0.0018 = \$0.0042$.</details>

### S18 — LLM limitations: hallucination, cutoff, prompt sensitivity [D]
- **What it is:** **hallucination** = fluent but fabricated content; **knowledge cutoff** = training data ends at a date, so later events are unknown; **prompt sensitivity** = small wording changes can change the answer.
- **Worked mini-example:** asked about a statute amended last month, a model may confidently describe the pre-amendment rule; asked for a citation, it may invent a plausible-looking case number. Both look exactly as trustworthy as a correct answer.
- **Pitfall:** fluency is not evidence of truth — confident fake citations are dangerous precisely because they are hard to doubt. Mitigations target the failure: grounding in retrieved verified documents, publishing the cutoff date, routing to humans where freshness matters.
- **Self-check:** Which limitation does retrieval-augmented generation (grounding) directly target?
  <details><summary>reveal answer</summary>Hallucination — answers are anchored to retrieved verified documents instead of generated from memory alone.</details>

---

## Module 6 — Computer Vision

### S19 — Image classification pipeline [G]
- **What it is:** classification assigns **one label per image**. Supervised training needs image–label pairs; the pipeline is collect labeled images → train → evaluate per class → deploy.
- **Worked mini-example:** 3,000 photos of leaves, each tagged by a botanist as "healthy", "fungal", or "nitrogen-deficient" — three image–label pairs per photo? No: one pair per photo, three possible labels.
- **Pitfall:** boxes belong to detection, not classification; and accuracy alone hides class-level failures — a dataset that is 95% "healthy" can be "predicted" by a model that never detects disease at all.
- **Self-check:** Why is raw accuracy a poor metric on that 95/5 leaf dataset?
  <details><summary>reveal answer</summary>Always predicting "healthy" scores 95% while catching zero diseased leaves; per-class precision/recall expose the failure accuracy hides.</details>

### S20 — Object detection: localization and bounding boxes [G]
- **What it is:** detection outputs a **bounding box plus class per object** — classification for each object plus localization of where it is. Coordinates define the box (e.g. leftmost column to rightmost column).
- **Worked mini-example:** a box given as columns 15–65 and rows 25–55 spans width $65-15 = 50$ columns and height $55-25 = 30$ rows; the box starts **at** column 15, it does not extend to column 65 + 15.
- **Pitfall:** "width" is $x_{right} - x_{left}$, not the right coordinate itself; and a model can classify correctly yet localize badly — a real failure mode for any system that uses box position.
- **Self-check:** A box is recorded as columns 30–70. What is its width?
  <details><summary>reveal answer</summary>$70 - 30 = 40$ columns.</details>

### S21 — Confusion-matrix metrics and IoU [D]
- **What it is:** from TP/FP/FN/TN: $\text{Precision} = TP/(TP+FP)$ (of predicted positives, how many were right), $\text{Recall} = TP/(TP+FN)$ (of actual positives, how many were found), $F_1 = 2PR/(P+R)$. For boxes: $\text{IoU} = \frac{\lvert A \cap B\rvert}{\lvert A \cup B\rvert}$, accepted if above a threshold.
- **Worked mini-example:** a defect detector on 30 parts: TP $= 5$, FP $= 3$, FN $= 4$, TN $= 18$. Precision $= 5/8 = 0.625$; Recall $= 5/9 \approx 0.556$; $F_1 = 2(0.625)(0.556)/(0.625 + 0.556) \approx 0.695/1.181 \approx 0.588$. Boxes: ground truth spans columns 10–42, rows 20–52 ($32\times32$); prediction spans columns 26–58, rows 36–68 ($32\times32$). Intersection $= 16\times16 = 256$; union $= 1024 + 1024 - 256 = 1792$; IoU $= 256/1792 = 0.143$ → below a $0.5$ threshold → **rejected**.
- **Pitfall:** precision and recall answer different questions — a screening system that must not miss cases cares about recall, one where false alarms are costly cares about precision; accuracy conflates both. For IoU, intersection is computed on **both** axes and union subtracts the intersection once (don't add the areas twice).
- **Self-check:** A detector finds all 10 defects but also flags 30 good parts. Is precision or recall the problem?
  <details><summary>reveal answer</summary>Precision: recall is 1.0, but precision is $10/40 = 0.25$ — three quarters of the positive calls are false alarms.</details>

---

## Module 7 — Responsible AI, Ethics, Bias and AI Governance

### S22 — Fairness metrics [D]
- **What it is:** **demographic parity** = similar positive-decision rates across groups; **equalized odds** = similar true-positive **and** false-positive rates conditional on the true outcome; **disparate impact (DI) ratio** = $\frac{\text{rate}_{min}}{\text{rate}_{max}}$, with the four-fifths rule flagging DI $< 0.80$.
- **Worked mini-example:** group X: 36 of 50 applicants approved → $0.720$; group Y: 15 of 50 approved → $0.300$. DI $= 0.300/0.720 \approx 0.417 < 0.80$ → adverse impact. Demographic parity is already violated by the raw rates alone.
- **Pitfall:** parity looks only at decision **rates**; equalized odds additionally conditions on the true outcome, so it catches systems whose overall rates match but whose errors fall unevenly. The question being asked determines which metric applies — don't swap them.
- **Self-check:** Model approval rates are equal across groups, but its false-positive rate is triple for one group. Which metric does demographic parity miss here?
  <details><summary>reveal answer</summary>Equalized odds — parity constrains only decision rates and is blind to unequal error types.</details>

### S23 — Sources of bias [D]
- **What it is:** bias enters as **historical** bias (past decisions encode past exclusion and become training labels), **sampling** bias (training data under-represents a population), **label** bias (the label reflects subjective judgement, not ground truth), **measurement/proxy** bias (a feature stands in for a protected attribute).
- **Worked mini-example:** a hiring model trained on ten years of past invite decisions learns those invite patterns as its target — historical bias; if all training recordings came from one city's accent, that's sampling bias; if "fit" was scored by one recruiter's gut feeling, that's label bias; if postcode stands in for community, that's proxy bias.
- **Pitfall:** bias is systemic, not a random bug — and unrelated to the numeric **bias term** in a model's equations, which is just an offset. The dangerous case is subjective labels: the model faithfully reproduces the annotator's prejudice as if it were ground truth.
- **Self-check:** A loan model uses postcode and replicates a community's historical exclusion. Name the bias source(s).
  <details><summary>reveal answer</summary>Both historical bias (past decisions as labels) and proxy bias (postcode as a stand-in for the protected attribute).</details>

### S24 — AI governance: documentation, audits, oversight [D]
- **What it is:** governance = documented intended use and limits (**model cards**, data lineage), routine **disparity audits**, **human oversight** (review before consequential actions, appeal channels), and regulatory frameworks requiring transparency and accountability.
- **Worked mini-example:** before a screening tool ships, the team publishes a model card (data summary, per-group performance, known failure modes), runs a per-group error audit each quarter, requires a human caseworker to confirm every automated denial, and offers an appeal route — each control produces a checkable artefact.
- **Pitfall:** oversight means a human reviews **individual decisions**, not just aggregate accuracy dashboards; and documentation is not paperwork-for-its-own-sake — it is what lets stakeholders judge whether the tool suits their population.
- **Self-check:** Give one governance control that catches a biased denial **before** harm, and one that works **after**.
  <details><summary>reveal answer</summary>Before: mandatory human review of each denial before it is sent. After: an appeal channel that routes the case to a human for re-examination.</details>

---

## Module 8 — AI Applications

### S25 — AI in healthcare and finance [D]
- **What it is:** healthcare: image- or record-based diagnosis/triage (retinal screening, triage prioritization) with constraints like hardware, connectivity, clinician review, and severe costs of misses. Finance: fraud detection, credit approval on transaction/application records, with strict fairness and explainability requirements.
- **Worked mini-example:** labeled fraud/not-fraud transaction history → supervised classification scoring each new transaction; deployment constraint: a flagged card freezes instantly, so a low-precision model locks out too many genuine customers — the threshold must balance missed fraud against frozen accounts.
- **Pitfall:** matching the task matters — labeled outcome history → supervised classification; a screening context prioritizes **recall** (missed cases are the costly error), a freeze-the-card context also needs precision. And every high-stakes deployment needs a named human-override path.
- **Self-check:** A hospital builds an AI triage score. What is the highest-risk failure mode, and one control?
  <details><summary>reveal answer</summary>Systematically under-triaging a subgroup (missed emergencies); control: clinician override on every AI priority, plus a re-triage channel.</details>

### S26 — AI in transport, agriculture, education, retail [D]
- **What it is:** match technique to problem: labeled outcomes → supervised; no labels but a computable feedback signal → unsupervised or reinforcement learning; grouping → clustering.
- **Worked mini-example:** a delivery firm has fuel cost per route (computable, no "optimal route" labels) → route optimization / RL over historical traces; a farm has years of field photos labeled with outbreak/no-outbreak → supervised classification for alerts; an education platform wants study groups without labels → clustering.
- **Pitfall:** the feedback signal defines the method — fuel cost is a computable signal needing no labels, while disease alerts need historical labeled outcomes; deploying a human-facing flag (student risk, loan denial) always requires a human-review safeguard, never automatic penalty.
- **Self-check:** Historical outbreak records exist per field. Which learning type fits predicting next season's outbreaks, and why?
  <details><summary>reveal answer</summary>Supervised classification — labeled historical outcomes exist and a discrete per-field alert is the usable output.</details>

---

## Formula sheet

| Concept | Formula | Notes |
|---|---|---|
| Gini impurity | $1 - \sum_c p_c^2$ | $0$ at purity, max at uniform mix |
| Entropy | $H = -\sum_c p_c \log_2 p_c$ | same shape as Gini; log base 2 |
| Information gain | $IG = H_{parent} - \sum_v \frac{\lvert v\rvert}{\lvert \text{parent}\rvert}H(v)$ | weighted child entropy |
| Perceptron net | $net = \sum_i w_i x_i + b$ | output 1 if $net > 0$ else 0 |
| Perceptron update | $w \leftarrow w + \eta\,y\,x$ | on mistakes; $\eta$ = learning rate |
| Sigmoid | $\sigma(z) = \frac{1}{1+e^{-z}}$ | range $(0,1)$, open interval |
| ReLU | $\max(0, z)$ | $0$ for all $z \le 0$ |
| Conv/pool output size | $O = \lfloor (W + 2P - K)/S \rfloor + 1$ | chain per layer; pooling keeps channels |
| Conv weights | $K \cdot K \cdot C_{in} \cdot C_{out}$ | biases: $+C_{out}$ |
| Precision | $TP/(TP+FP)$ | of predicted positives |
| Recall | $TP/(TP+FN)$ | of actual positives |
| $F_1$ | $2PR/(P+R)$ | harmonic mean |
| IoU | $\frac{\lvert A \cap B\rvert}{\lvert A \cup B\rvert}$ | union subtracts intersection once |
| Disparate impact | $\text{rate}_{min}/\text{rate}_{max}$ | four-fifths rule: $< 0.80$ flags impact |
| LLM cost | $(in \cdot r_{in} + out \cdot r_{out})$ | rates per million tokens; $\times$ calls |
| Train/test split | $n_{train} = n \cdot f$, $n_{test} = n(1-f)$ | define split before tuning |

## Misconception checklist

1. **Topic ≠ task type.** The target's type (label vs number) decides classification vs regression — never the domain.
2. **Training accuracy ≠ good model.** The train–validation gap is the overfitting signal; the held-out set is the only honest score.
3. **Pure leaves are a red flag.** A fully grown tree memorizes noise; deploy the depth where validation peaks.
4. **IG = 0 means "no information here", not "wrong attribute"** — and candidate splits compare on *weighted* child entropy.
5. **Gini vs entropy is a false dilemma** — they almost always pick the same split.
6. **Stacked linear layers stay linear.** Depth without non-linear activations adds nothing.
7. **Sigmoid never outputs exactly 0 or 1** — its range is the open interval $(0,1)$; $[-1,1]$ is tanh.
8. **Pooling doesn't learn or change channels** — kernels are learned in convolution; pooling only shrinks height/width.
9. **$\eta$ scales each update** — a huge learning rate oscillates; unscaled features let the biggest feature dominate.
10. **Accuracy hides class failures** — the 95%-negative dataset "predictable" by an all-negative model needs per-class precision/recall.
11. **Fluency ≠ truth.** Confident hallucinated citations are dangerous precisely because they look reliable; grounding targets this directly.
12. **Demographic parity ≠ equalized odds** — parity checks decision rates; equalized odds checks both error types against true outcomes.
13. **Label bias is the silent one.** A subjective human judgement used as ground truth teaches the model the annotator's prejudice.
14. **In-context examples ≠ fine-tuning** — prompts steer one request; weights never move.
15. **Historical decisions as labels reproduce historical exclusion** — the model learns the past pattern, bias included.
