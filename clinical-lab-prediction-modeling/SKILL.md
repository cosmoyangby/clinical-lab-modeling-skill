---
name: clinical-lab-prediction-modeling
description: Standardize clinical laboratory indicator-based diagnostic, predictive, and prognostic model studies. Use when Codex needs to help frame the research question, distinguish diagnostic versus prediction/prognostic boundaries, assess data feasibility, plan feature engineering and predictor selection, choose modeling approaches, evaluate validation and performance, prepare TRIPOD/PROBAST-aligned reporting, or draft downstream R agent prompts for clinical lab model development.
---

# Clinical Lab Prediction Modeling

Use this skill to standardize clinical laboratory indicator-based model development and review.

Focus on research framing, modeling workflow, validation, reporting quality, and downstream agent handoff prompts. Do not provide direct clinical diagnosis, treatment decisions, or patient-specific medical advice.

## Core Flow

1. Start with intake: summarize known information and identify missing information.
2. Ask focused follow-up questions when core design information is missing.
3. Classify the study as diagnostic, predictive, prognostic, screening, or risk stratification.
4. Define the clinical question, outcome, prediction horizon or reference standard, and intended use.
5. Check sample size, event count, class balance, missingness, and validation feasibility.
6. Choose feature engineering, predictor selection, modeling, validation, and performance strategies according to data characteristics.
7. Produce a full research decision framework only after intake is complete, a dataset is reviewed, or the user explicitly asks for a preliminary draft.
8. Label incomplete outputs as preliminary drafts and list required confirmations before downstream R agent work.

## What To Emphasize

- Distinguish diagnostic models from prediction/prognostic models in both method and language.
- Choose feature screening, collinearity handling, nonlinearity handling, and model type based on the dataset, not a fixed recipe.
- Treat machine learning as optional and conditional on sample size, event count, class balance, and validation design.
- Keep preprocessing, feature selection, threshold tuning, and hyperparameter tuning inside training or resampling.
- Use TRIPOD/TRIPOD+AI and PROBAST/PROBAST+AI concepts for reporting and bias review.
- Use BMJ prediction-model development and validation guidance as the methodological anchor.

## Preferred Outputs

When intake is complete or the user explicitly asks for a preliminary draft, produce:

1. A Word research framework with title page, table of contents, broad sections, and concise nested content.
2. A separate Markdown R agent prompt file.
3. A short chat summary with links to the created files.

For formal deliverables, write the research decision framework as a Word document and write the downstream R agent prompt as a separate Markdown file. In chat, provide a concise summary and links to the created files rather than pasting the full deliverable.

If core information is missing, produce only an intake summary, missing information list, and focused questions.

## Reference Files

Read the relevant files in `references/` for detailed rules on:

- `intake-checklist.md`
- `analysis-decision-tree.md`
- `feature-engineering.md`
- `model-selection.md`
- `diagnostic-vs-prognostic.md`
- `ml-suitability.md`
- `sample-size.md`
- `validation-and-performance.md`
- `reporting-and-bias.md`
- `do-dont.md`
- `output-contract.md`
- `standard-deliverable-template.md`
- `manuscript-methods-template.md`
- `r-agent-prompt.md`

## Scripts

Use `scripts/render_deliverable_docx.py` to render the prepared research framework Markdown into a Word document.

Use `scripts/write_agent_prompt_md.py` to write the prepared downstream R agent prompt into a standalone Markdown file.

## Style

Keep output practical, concise, and evidence-aware. Prefer clear sectioned frameworks and avoid unnecessary abstraction.
