# Output Contract

Use this file to keep final deliverables standardized and concise.

Write the main deliverable in Chinese unless the user requests another language.

Write the manuscript methods draft in both Chinese and English.

For formal delivery, create files instead of only returning a long chat response:

- research decision framework: `.docx`
- downstream R agent prompt: `.md`
- optional brief summary: chat response with file links

## Full Research Decision Framework

Generate the full framework only after core intake is complete, the uploaded dataset has been reviewed, or the user explicitly asks for a preliminary draft.

If information is incomplete, output an intake-only response instead of the full framework.

Return these sections:

1. Title page
2. Table of contents
3. 研究概览
4. 数据可行性与研究定位
5. 分析方法设计
6. 推荐分析流程
7. 报告规范与偏倚风险
8. 论文方法学草稿
9. R Agent Prompt 文件说明
10. 实用注意事项

The deliverable must use broad sections and clear nested structure. Fold feature engineering, missing data, predictor selection, modeling, validation, and performance evaluation into the "分析方法设计" section. Avoid one large method-selection table as the main structure.

## Deliverable Files

When creating formal deliverables, produce:

1. `research-decision-framework.docx`
2. `r-agent-prompt.md`

Use user-provided naming or output paths when available. If the user does not specify paths, choose clear filenames based on the study topic.

The Word document should contain the full research decision framework, including the bilingual manuscript methods draft.

The Markdown prompt file should contain only the downstream agent prompt and any execution notes needed by that agent.

Use bundled scripts for deterministic file rendering:

- `scripts/render_deliverable_docx.py <framework.md> <research-decision-framework.docx>`
- `scripts/write_agent_prompt_md.py <prompt.txt> <r-agent-prompt.md>`

The scripts only render prepared content. They do not decide study design, select models, or interpret data.

`render_deliverable_docx.py` requires `python-docx`. In Codex Desktop, prefer the bundled Python runtime for document rendering when available; do not assume the macOS system Python has this package installed.

## Research Boundary

State:

- model type
- target population
- intended clinical setting
- intended use
- index or baseline time
- outcome
- prediction horizon or reference standard
- whether the task is diagnostic, prediction, prognostic, screening, or risk stratification

## Data Feasibility

State:

- sample size
- event or positive-case count
- candidate predictor count
- candidate parameter count if estimable
- missingness concerns
- class imbalance concerns
- validation availability
- overfitting risk
- whether the study is development, validation, model updating, or exploratory

If feasibility is weak, recommend a simpler or exploratory route.

## Method Choice Structure

Inside each methods subsection, include concise inline content for:

- 推荐
- 原因
- 可选方案
- 适用与不适用

Do not turn these labels into excessive heading levels.

For predictor selection, state the candidate predictor pool, pre-model exclusions, forced-in clinical variables, main selection route, and leakage-control plan.

The Word framework must include a compact statistical-methods summary table. Recommended methods should be explicit for collinearity assessment, nonlinearity assessment, missing data, predictor selection, final modeling, validation, calibration, threshold analysis, nomogram or risk score presentation, and decision curve analysis.

## R Agent Prompt

Generate the R agent prompt as conditional or draft until the user confirms key choices.

Include:

- dataset path
- outcome variable
- candidate predictors
- model type
- intended use and prediction horizon or reference standard
- validation structure
- required preprocessing
- candidate models
- required performance metrics
- required outputs
- code style rules
- leakage-control rules

## Cautions

End with short cautions tailored to the task.

Examples:

- The study is exploratory if no external validation is available.
- AUC should not be interpreted without calibration.
- Cutoffs should be justified by clinical decision context.
- Uncertain outcome definitions should be documented before modeling.
- External validation requires a locked model and independent setting, time, platform, or population.
