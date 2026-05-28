# Analysis Decision Tree

Use this decision tree to choose an analysis route based on study type and data characteristics.

Use `bmj-methodology-anchor.md` as the scientific anchor for formal frameworks and publication-oriented recommendations.

## 1. First Decide the Research Boundary

Start with intended use:

- who will use the model
- at what clinical decision time
- for what decision or risk communication
- in which target population and setting

If the outcome is current disease or current clinical state:

- use a diagnostic model route
- require a reference standard
- report diagnostic accuracy and threshold performance

If the outcome is future risk:

- use a prediction or prognostic model route
- require baseline time and prediction horizon
- report calibration and clinical utility

If the outcome is time-to-event:

- use survival modeling route
- account for censoring and follow-up time

## 2. Then Judge Data Feasibility

If event count is low:

- reduce predictor count
- prefer clinical pre-specification
- prefer logistic or Cox regression
- avoid broad machine learning comparison
- avoid many nonlinear terms, interactions, and derived ratios

If predictors are many relative to events:

- use penalized regression
- reduce derived features
- avoid univariable-only screening
- keep selection inside resampling
- count parameters, not just named variables

If external validation exists:

- lock the development workflow before validation
- use external data only for validation
- report applicability and performance shift
- check population, prevalence, assay platform, and care-process differences

If no external validation exists:

- emphasize internal validation
- avoid claiming clinical readiness
- frame results as model development or exploratory evidence

## 3. Choose Feature Engineering Route

If predictors are mostly continuous laboratory indicators:

- inspect skewness and outliers
- avoid arbitrary dichotomization
- consider transformations or splines
- preserve clinical interpretability

If predictors are highly correlated:

- inspect correlation and VIF
- choose clinically representative predictors
- consider penalized regression or composite scores

If repeated measurements exist:

- define index time
- define measurement window
- choose one repeated-measurement summary rule
- avoid future information leakage
- ensure summary windows are clinically available at the intended decision time

If derived ratios are requested:

- allow only clinically meaningful ratios
- document formulas
- limit the number of derived features when event count is small

## 4. Choose Predictor Selection Route

If variables are few and clinically justified:

- use prespecified full model
- consider shrinkage or penalization if overfitting risk remains

If variables are many or correlated:

- use LASSO or elastic net

If robustness is important:

- use bootstrap stability or repeated resampling

If predictors belong to clinical groups:

- use block-wise comparison

Avoid choosing predictors only by univariable P value.

Avoid selecting thresholds, transformations, or predictors using the final validation data.

## 5. Choose Model Route

If sample size is small or interpretability is critical:

- use logistic regression, Cox regression, or penalized regression

If nonlinear effects are expected and sample size is adequate:

- consider splines or tree-based models

If machine learning is requested:

- check sample size
- check event count
- check class balance
- check validation strength
- check whether calibration and model updating can be handled
- compare with a regression baseline

If these checks fail, explain why machine learning is not recommended as the main model.

## 6. Choose Validation Route

If only one dataset exists:

- use bootstrap or cross-validation
- avoid overinterpreting test-set performance from small splits
- report internally validated performance, not only apparent performance

If hyperparameters are tuned:

- use nested cross-validation or a locked validation strategy

If an independent cohort exists:

- use it only for final external validation
- report external validation as a separate evaluation of a locked model

If the external cohort is too small:

- use it cautiously as exploratory validation
- report uncertainty with confidence intervals
- avoid strong claims about transportability

## 7. Choose Performance Route

For diagnostic models:

- report AUC
- report sensitivity and specificity
- report PPV and NPV
- report likelihood ratios
- justify thresholds clinically

For prediction or prognostic models:

- report discrimination
- report calibration
- report Brier score
- report decision curve analysis when decisions are involved
- report absolute risk performance when the model outputs risk

For imbalanced outcomes:

- add PR-AUC
- add balanced accuracy
- add fixed-sensitivity or fixed-specificity results

## 8. Final Recommendation Rule

End by recommending one clear analysis route:

- conservative interpretable route
- penalized regression route
- machine learning comparison route
- external validation route
- exploratory feasibility route

State why the route matches the dataset and research goal.
