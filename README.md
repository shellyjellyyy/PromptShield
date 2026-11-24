# PromptShield

**Automated LLM Security Testing & Evaluation Framework**

PromptShield is a student mini-project that explores how reliably an AI
chatbot follows its intended instructions when it receives ordinary,
unusual, or adversarial user inputs.

The project is designed to help developers test a chatbot, inspect its
responses, identify possible instruction-following or
information-disclosure failures, and compare different prompt
configurations.

> **Project status:** Work in progress. Features and results described
> as planned below should only be marked complete after they have been
> implemented and tested.

## Project objectives

-   Build a repeatable test workflow for an AI chatbot.
-   Organise normal, edge-case, and adversarial test inputs.
-   Run test inputs against a chatbot using selected system-prompt
    versions.
-   Record model responses in a consistent format.
-   Evaluate responses against a documented rubric.
-   Compare baseline and revised prompt configurations.
-   Present test outcomes and limitations in a simple dashboard.

## Use case

The initial prototype uses a fictional customer-support assistant,
**Acme Support Assistant**. It is intended to answer questions about
fictional order and refund policies while following its configured
instructions and protecting fictional internal information.

All test data should be synthetic. Do not use real customer data,
passwords, API keys, confidential documents, or other sensitive
information.

## Planned workflow

1.  **Test design:** Prepare test cases, categories, and expected safe
    behaviour.
2.  **AI execution:** Send each test input to the configured language
    model with a selected system prompt.
3.  **Response collection:** Save the input, model response, prompt
    version, model identifier, and test ID.
4.  **Evaluation:** Assess responses using rule-based checks and, where
    appropriate, a documented human or model-assisted review.
5.  **Analysis:** Calculate metrics and compare prompt versions.
6.  **Dashboard:** Display test runs, flagged responses, comparisons,
    and known limitations.

## Team and responsibilities

  -----------------------------------------------------------------------
  Team member             Specialisation          Primary responsibility
  ----------------------- ----------------------- -----------------------
  Shailja                 CSE -- Data Science     Evaluation rubric,
                                                  response evaluation,
                                                  metrics, and results
                                                  analysis

  Rijuta                  CSE -- Cybersecurity    Security research, test
                                                  categories, test-case
                                                  design, and expected
                                                  behaviour

  Keshav                  CSE -- AI/ML            LLM integration, target
                                                  chatbot prompts, test
                                                  execution, and response
                                                  collection

Vaibhav                 CSE -- AI/ML            Streamlit interface,
                                                  dashboard,
                                                  visualisations, and
                                                    integration
                                                    
  -----------------------------------------------------------------------


## Proposed technology stack

The exact model/provider should be recorded once selected by the team.

-   **Language:** Python
-   **LLM access:** API from the model provider selected by the team
-   **Application/dashboard:** Streamlit
-   **Data formats:** JSON, CSV, and Markdown
-   **Version control:** Git and GitHub

## Repository structure

``` text
PromptShield/
├── README.md
├── CHANGELOG.md
├── prompts/
│   ├── v1/
│   ├── v2/
│   ├── v3/
│   └── final/
├── code/
│   ├── llm_runner.py
│   ├── evaluator.py
│   ├── metrics.py
│   └── app.py
├── test-data/
│   ├── test_cases.json
│   ├── raw_results.json
│   └── evaluation_results.json
└── docs/
    ├── evaluation_rubric.md
    ├── security_categories.md
    ├── architecture.png
    └── milestone2.pdf
```

Create files only when they exist; do not add empty or placeholder files
as evidence of completed functionality.

## Data hand-off formats

To allow team members to work independently, modules should exchange
data using agreed JSON structures.

### Test case

``` json
{
  "test_id": "T01",
  "category": "instruction_override",
  "type": "Edge",
  "input": "Example test input",
  "expected_behavior": "The chatbot should retain its configured instructions."
}
```

### Raw model result

``` json
{
  "test_id": "T01",
  "prompt_version": "V1",
  "input": "Example test input",
  "response": "Actual response returned by the model",
  "model": "Selected model identifier"
}
```

### Evaluated result

``` json
{
  "test_id": "T01",
  "prompt_version": "V1",
  "status": "Needs Review",
  "reason": "Explanation based on the evaluation rubric"
}
```

These are interface examples. Replace example values with actual test
inputs and outputs from recorded runs.

## Evaluation approach

The team will document its rubric before reporting results. Potential
evaluation dimensions include:

-   **Instruction compliance:** Did the chatbot follow its configured
    instructions?
-   **Information disclosure:** Did it reveal information designated as
    confidential in the fictional test scenario?
-   **Appropriate refusal:** Did it decline requests that conflict with
    the defined rules?
-   **Normal-task performance:** Did it remain useful on harmless,
    in-scope questions?

Potential metrics include attack success rate, appropriate refusal rate,
false-positive rate, and normal-task success rate. Define each metric
precisely, record its denominator, and report actual measured values
only. Ambiguous cases should be marked for review rather than
automatically treated as successes or failures.

## Running the project

### 1. Launching the Security Dashboard (React UI)

You can launch the interactive security dashboard using either method:

* **Option A: One-Click Launcher (Windows)**
  Double-click `launch.bat` in the repository root.

* **Option B: Command Line (PowerShell / Terminal)**
  ```powershell
  python code/app.py
  ```

* **Option C: Standalone Browser View**
  Open `dashboard.html` directly in any web browser.

Once running, access the dashboard at:
👉 **`http://localhost:8501/`** or **`http://localhost:8501/dashboard.html`**

---

### 2. Running Automated Benchmarks & Evaluations via CLI

If you want to run the full testing and metrics pipeline from the command line:

```powershell
# 1. Run the test cases across all prompt versions (v1, v2, v3, final)
python code/llm_runner.py

# 2. Evaluate model outputs against security rubrics and canaries
python code/evaluator.py

# 3. Print quantitative metrics report (ASR, ARR, FPR, NSR)
python code/metrics.py
```

### 3. API Key Configuration (Optional)
Copy `.env.example` to `.env` to configure live Gemini, OpenAI, or Groq API keys:
```powershell
cp .env.example .env
```
*(Note: A built-in high-fidelity simulator is included by default, so the entire benchmark and dashboard function fully offline without requiring API keys).*

## Current implementation status

Update this section as work is completed and verified.

  Component                                      Status
  ---------------------------------------------- -------------
  Security test-case dataset                     In progress
  Target chatbot prompts and prompt iterations   In progress
  LLM execution and response collection          In progress
  Response evaluation and metrics                In progress
  Streamlit dashboard                            In progress
  End-to-end integration                         Not started

## Limitations and responsible use

-   Results depend on the selected model, its version, settings, and
    availability.
-   Automated evaluation can make mistakes; ambiguous outputs require
    review.
-   Prompt changes alone cannot guarantee that an AI application is
    secure.
-   This prototype is an educational testing tool, not a certification
    or guarantee of security.
-   Test only systems you own or have explicit permission to assess.
-   Use fictional test data and keep credentials outside the repository.

## Contributions

Each member should commit their own work and keep evidence of their
contribution. Update `CHANGELOG.md` with dated, factual entries as the
project evolves.

## Academic project

**Course:** SCSE4041 Mini Project\
**Team name:** Fourbidden Prompt\
**Project title:** PromptShield -- Automated LLM Security Testing &
Evaluation Framework

Add the official team ID, batch, faculty name, and enrollment numbers
here when confirmed.
