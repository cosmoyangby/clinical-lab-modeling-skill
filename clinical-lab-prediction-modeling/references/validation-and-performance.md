# Validation and Performance

Use this guide to plan validation and model performance reporting.

## 1. Separate Performance Levels

Always distinguish:

- apparent performance
- internally validated performance
- test-set performance
- external validation performance

Do not present apparent performance as final model performance.

## 2. Internal Validation

Use internal validation to estimate optimism and overfitting.

Preferred options:

- bootstrap validation
- repeated cross-validation
- nested cross-validation when tuning models

Keep feature selection, preprocessing, and hyperparameter tuning inside the resampling loop.

## 3. External Validation

Use external validation when an independent cohort exists.

External validation may be:

- temporal
- geographic
- center-based
- platform-based
- population-based

Do not use external validation data for feature selection, threshold tuning, or hyperparameter tuning.

If a held-out test set is created from the same source population and time period, describe it as test-set validation rather than external validation.

## 4. Discrimination

Report:

- AUC or C-statistic
- confidence interval
- PR-AUC when class imbalance is important

Do not rely on AUC alone.

## 5. Calibration

Report calibration for prediction and prognostic models, and for diagnostic models when probabilities are used.

Useful outputs:

- calibration plot
- calibration intercept
- calibration slope
- Brier score
- calibration by risk group when appropriate

Poor calibration can make a model unsuitable even when AUC is high.

## 6. Diagnostic Threshold Performance

For diagnostic models, report threshold-specific performance:

- sensitivity
- specificity
- PPV
- NPV
- LR+
- LR-
- Youden index when appropriate

Prefer clinically meaningful thresholds over purely data-optimized thresholds.

## 7. Prediction and Prognostic Thresholds

For prediction or prognostic models, thresholds should map to clinical decisions.

Report:

- absolute risk categories
- threshold probability
- sensitivity and specificity at selected thresholds
- consequences of false positives and false negatives

## 8. Clinical Utility

Use decision curve analysis when the model is intended to guide decisions.

Report:

- threshold probability range
- net benefit
- comparison with treat-all and treat-none
- comparison with existing practice when available

## 9. Class Imbalance

When classes are imbalanced, add:

- PR-AUC
- balanced accuracy
- sensitivity at fixed specificity
- specificity at fixed sensitivity
- confusion matrix at clinically relevant thresholds

Avoid judging imbalanced models by accuracy alone.

## 10. Final Performance Summary

The final report should state:

- validation type
- discrimination
- calibration
- threshold performance
- clinical utility
- limitations
- whether the model is exploratory or clinically ready
