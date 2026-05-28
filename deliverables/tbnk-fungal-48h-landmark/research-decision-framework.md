# ICU患者48小时内TBNK指标预测14天肺部真菌感染风险研究框架

研究主题：基于ICU入院后48小时内TBNK检测及临床信息，预测随后14天内肺部真菌PCR阳性风险

交付类型：预交付研究决策框架

日期：2026-05-28

版本：v0.1 草稿

说明：本框架基于当前口头信息生成。正式分析前仍需确认数据字段、结局编码、PCR检测机制、死亡/出院处理和48小时内已阳性病例处理规则。

## Table of Contents

## 一、研究概览

1. 研究问题：在ICU患者中，入院后48小时内TBNK细胞亚群及临床变量能否预测随后14天内肺部真菌PCR阳性风险。
2. 目标人群：ICU入院患者，预计样本量约300例。
3. 研究类型与模型用途：48小时landmark风险预测模型；用于早期识别未来14天内肺部真菌感染高风险患者。
4. 临床场景与决策时间点：预测起点为ICU入院后48小时。模型只能使用48小时内可获得的信息。
5. 结局定义与预测时间窗：预测起点后14天内肺部真菌PCR阳性。PCR为临床怀疑后检测，存在结局验证偏倚风险。
6. 候选预测变量：CD3、CD4、CD8、NK、B细胞、CD4/CD8比值、年龄、性别、48小时内抗菌药物使用、48小时内机械通气等。
7. 当前数据条件：约300例，阳性事件约45例，缺失值约5%，无外部验证数据，存在死亡和出院导致结局NA的情况。
8. 本研究能回答与不能回答的问题：可回答基于48小时内信息的探索性风险预测问题；不能证明TBNK与真菌感染的因果关系，也不能直接声称模型已可临床部署。

## 二、数据可行性与研究定位

1. 样本量与事件数：总样本量约300例，阳性事件约45例。事件数支持简化预测模型开发，但不支持高复杂度机器学习作为主要结论。
2. 候选变量与候选参数数：TBNK含6个指标，临床变量至少包括年龄、性别、抗菌药物、机械通气。若全部纳入普通logistic模型，候选参数数偏多；若再加入非线性、交互项或多模型比较，过拟合风险升高。
3. 缺失、类别不平衡与数据泄漏风险：缺失约5%，总体可处理。阳性比例约15%，存在类别不平衡。住院过程变量仅可使用48小时内信息；48小时后变量不得进入主模型。
4. 验证条件：无外部验证数据。建议采用bootstrap内部验证或重复交叉验证，避免单次随机拆分造成阳性事件过少。
5. 可行性判断：适合探索性模型开发或简化模型开发。
6. 推荐研究定位：建议定位为“48小时landmark探索性预测模型开发”，强调内部验证、校准和偏倚风险，不建议宣称临床实用模型已经建立。

## 三、分析方法设计

### 1. 结局与时间结构

推荐：采用48小时landmark设计。仅纳入达到48小时landmark且在landmark时尚未发生肺部真菌PCR阳性的患者。预测窗定义为landmark后14天内PCR阳性。

原因：抗菌药物和机械通气属于住院过程变量，如果模型仍定义为入院即刻预测，则可能发生信息泄漏。改为48小时landmark后，这些变量可作为预测起点前信息。

可选方案：若研究者希望严格使用入院即刻信息，则应排除48小时内发生的抗菌药物、机械通气等后续变量，仅保留入院时已知变量。

适用与不适用：48小时landmark适用于早期ICU风险分层；不适用于解释入院当刻的即时预测能力。

### 2. 预测变量与特征工程

推荐：按基础临床变量、TBNK核心变量和48小时内治疗/支持变量分组。TBNK连续指标优先保留连续形式，检查分布、极端值、单位、检测平台和参考区间。

原因：TBNK指标之间可能存在明显生物学相关性，机械二分类会损失信息并增加不稳定性。

可选方案：对强偏态指标考虑log转换；对关键连续指标在样本量允许时探索限制性立方样条；对TBNK作为整体模块进行增量价值评估。

适用与不适用：样本量和事件数有限时，不宜大量构造比值、交互项或复杂非线性项。

### 3. 缺失值处理

推荐：先报告各变量缺失比例和缺失模式。缺失约5%时，可比较完整病例分析与多重插补分析；若采用多重插补，应在重采样流程内控制信息泄漏。

原因：即使总体缺失较低，若TBNK或结局相关变量存在选择性缺失，也可能影响模型稳定性。

可选方案：缺失极少且随机时可进行完整病例主分析；若关键预测变量缺失非随机，应做敏感性分析。

适用与不适用：不建议简单删除大量样本后直接建模；不建议在全数据上先插补再做内部验证。

### 4. 变量筛选

候选变量池：年龄、性别、CD3、CD4、CD8、NK、B细胞、CD4/CD8比值、48小时内抗菌药物、48小时内机械通气等。

建模前排除变量：48小时后才出现的治疗、检测、临床状态变量；结局定义组成部分；PCR检测触发后的信息；48小时内已PCR阳性的病例应从预测模型开发集中排除或单独处理。

强制纳入变量：建议强制纳入年龄、性别。TBNK为研究核心模块，应以预设方式纳入或作为模块评估。

推荐筛选路线：基础临床模型作为基线；TBNK模块通过临床预设少量指标、ridge/elastic net或block-wise方式评估增量价值。若TBNK指标高度相关，elastic net或ridge优于普通全变量logistic。

不推荐作为主策略的方法：不建议仅按单因素P值筛选；不建议按表观AUC最大化选择变量；不建议把全部TBNK指标、全部临床变量和多个派生指标直接放入普通logistic作为主模型。

稳定性或敏感性分析：建议报告bootstrap或重复交叉验证中的变量选择稳定性；比较基础临床模型与基础临床+TBNK模块的性能和校准变化。

### 5. 建模方法

推荐：以logistic回归或惩罚logistic回归作为主模型。优先考虑ridge或elastic net以控制过拟合和共线性。

原因：阳性事件约45例，复杂模型不稳定。惩罚回归可在保留临床解释性的同时降低系数波动。

可选方案：可将随机森林、XGBoost等作为探索性比较模型，但必须使用嵌套或严格重采样流程，并与回归基线公平比较。

适用与不适用：机器学习不宜作为主要结论，除非后续获得更大样本或外部验证数据。

### 6. 验证策略

推荐：采用bootstrap内部验证估计乐观偏倚，并报告校正后的性能。若进行调参或变量选择，应将预处理、插补、变量筛选和调参放入重采样内部。

原因：300例、45个事件时，单次训练/测试拆分会导致开发集和测试集事件数不足，性能估计不稳定。

可选方案：重复交叉验证可作为替代；若未来获得独立时间段、中心或平台数据，可进行外部验证。

适用与不适用：当前无外部验证，不应声称模型具有外部泛化能力或临床可用性。

### 7. 性能评价

推荐：报告AUC及置信区间、校准曲线、校准截距和斜率、Brier score、敏感度、特异度、PPV、NPV、PR-AUC，以及临床阈值下的风险分层表现。

原因：阳性比例约15%，仅报告AUC不足以评价模型。风险预测模型必须关注校准，临床应用还需阈值和决策价值。

可选方案：若临床需要决策支持，可报告决策曲线分析，并明确阈值概率范围。

适用与不适用：不建议用单一最优cutoff作为主要结论；cutoff需结合临床使用场景。

### 8. 临床实用性评价

推荐：以“辅助风险分层”而非“诊断真菌感染”作为主要用途。若提出阈值，应说明高风险患者可能进入进一步真菌检测、早期影像复核或临床评估流程。

原因：PCR为怀疑后检测，模型预测的更接近“未来被怀疑并PCR阳性”的风险，而不一定等于真实感染发生风险。

可选方案：可与仅包含年龄、性别和临床变量的基础模型比较，评估TBNK模块是否带来增量价值。

适用与不适用：在没有外部验证和明确干预策略前，不宜建议模型直接指导抗真菌治疗。

### 9. 报告与偏倚控制

推荐：按TRIPOD/TRIPOD+AI和BMJ预测模型开发指南报告。偏倚风险重点写明landmark设计、PCR验证偏倚、死亡/出院导致结局NA、无外部验证和样本量限制。

原因：PCR不是系统检测，死亡/出院会改变结局观察机会，均可能影响模型解释。

可选方案：可做多种结局编码敏感性分析，并在附录中报告。

适用与不适用：不宜把本研究表述为诊断准确性研究；更适合表述为探索性风险预测模型开发。

## 四、推荐分析流程

1. 数据检查：确认入组标准、48小时landmark、PCR检测时间、死亡/出院时间、变量测量时间。
2. 结局构建：排除landmark前PCR阳性者；构建landmark后14天PCR阳性结局；明确死亡/出院和未检测PCR的编码规则。
3. 变量处理：仅保留48小时内可获得变量；检查TBNK单位、平台、异常值和缺失。
4. 特征工程：连续TBNK优先保留连续形式，必要时转换；减少派生变量数量。
5. 变量筛选：建立基础临床模型，再评估TBNK模块；优先使用临床预设、ridge或elastic net。
6. 模型开发：以简化logistic或惩罚logistic为主模型；机器学习仅作探索性比较。
7. 模型验证：bootstrap内部验证；所有预处理和筛选嵌入重采样。
8. 结果报告：报告区分度、校准度、Brier score、PR-AUC、阈值表现、决策曲线和主要偏倚风险。

## 五、报告规范与偏倚风险

1. 学术表述：本研究应称为48小时landmark风险预测模型开发。避免称为诊断模型或诊断准确性研究。
2. TRIPOD / TRIPOD+AI：报告目标人群、预测起点、预测窗、候选预测变量、缺失处理、变量筛选、模型开发、内部验证、性能指标和局限性。
3. PROBAST / PROBAST+AI：重点评估参与者选择、预测变量测量、结局验证、样本量、缺失数据、模型开发和验证偏倚。
4. BMJ预测模型开发与验证要点：从 intended use 和 decision time 出发；区分表观性能、内部验证性能和外部验证性能；不以单一AUC作为结论。
5. 主要偏倚风险：PCR为怀疑后检测导致验证偏倚；死亡/出院导致结局缺失或截断；住院过程变量存在时间泄漏风险；无外部验证；阳性事件数有限。
6. 适用性限制：模型仅适用于相似ICU环境、类似TBNK检测平台和相似PCR检测策略下的患者。

## 六、论文方法学草稿

### 中文版本

本研究拟开发一个基于ICU入院后48小时内可获得信息的14天肺部真菌感染风险预测模型。研究对象为ICU入院患者，预测起点设定为入院后48小时。候选预测变量包括年龄、性别、48小时内TBNK细胞亚群指标（CD3、CD4、CD8、NK、B细胞及CD4/CD8比值）以及48小时内抗菌药物使用和机械通气等临床变量。研究结局定义为预测起点后14天内临床怀疑后进行肺部真菌PCR检测并呈阳性。

模型开发前将检查变量测量时间、缺失值、异常值、TBNK指标相关性和潜在信息泄漏。考虑到阳性事件数约45例，主模型拟采用简化logistic回归或惩罚logistic回归，并优先考虑ridge或elastic net以降低过拟合和共线性影响。年龄和性别将作为基础临床变量优先纳入，TBNK指标将作为核心实验室模块进行评估。变量筛选和预处理将在内部验证流程中完成，以避免信息泄漏。

模型性能将通过bootstrap内部验证进行评估，并报告校正后的区分度、校准度、Brier score、PR-AUC、阈值相关指标和决策曲线分析。由于本研究暂无外部验证数据，模型结果将定位为探索性模型开发。研究报告将遵循TRIPOD/TRIPOD+AI、PROBAST/PROBAST+AI和BMJ预测模型开发与验证指南，并重点讨论PCR非系统检测、死亡/出院导致结局缺失、样本量有限和外部验证缺失带来的偏倚风险。

### English Version

This study aims to develop a 48-hour landmark prediction model for 14-day pulmonary fungal infection risk among ICU patients. The landmark time will be set at 48 hours after ICU admission. Candidate predictors will include age, sex, TBNK lymphocyte subset measurements obtained within the first 48 hours (CD3, CD4, CD8, NK cells, B cells, and the CD4/CD8 ratio), and clinical variables available within the same time window, such as antimicrobial exposure and mechanical ventilation. The outcome will be defined as pulmonary fungal PCR positivity within 14 days after the landmark time among patients tested because of clinical suspicion.

Before model development, predictor timing, missingness, implausible values, correlations among TBNK markers, and potential information leakage will be assessed. Given approximately 45 positive events, the primary model will use a parsimonious logistic regression or penalized logistic regression approach, with ridge regression or elastic net considered to reduce overfitting and collinearity. Age and sex will be considered core clinical predictors, and TBNK markers will be evaluated as the main laboratory predictor module. Predictor selection and preprocessing will be embedded within the internal validation procedure to avoid data leakage.

Model performance will be assessed using bootstrap internal validation. Optimism-corrected discrimination, calibration, Brier score, PR-AUC, threshold-specific performance, and decision curve analysis will be reported. As no external validation dataset is currently available, the study will be interpreted as exploratory model development. Reporting will be aligned with TRIPOD/TRIPOD+AI, PROBAST/PROBAST+AI, and BMJ guidance on prediction model development and validation, with explicit discussion of verification bias from clinically triggered PCR testing, outcome missingness due to death or discharge, limited event count, and lack of external validation.

## 七、R Agent Prompt 文件说明

1. 文件用途：`r-agent-prompt.md`用于交给R代码agent执行标准化数据检查、模型开发、内部验证和结果输出。
2. 使用前提：正式运行前需补充数据路径、变量名、PCR检测时间字段、死亡/出院时间字段、48小时内已阳性病例处理规则和结局编码方案。
3. 文件路径：`deliverables/tbnk-fungal-48h-landmark/r-agent-prompt.md`

## 八、实用注意事项

- 当前文档为预交付草稿，不是最终统计分析方案。
- PCR为临床怀疑后检测，结局存在验证偏倚，必须在论文中明确。
- 死亡/出院导致结局NA不能简单当作普通缺失，应进行敏感性分析。
- 48小时后出现的变量不得进入主模型。
- 阳性事件约45例，模型复杂度必须控制。
- 无外部验证，不能声称模型已具备临床可用性。
- AUC不能单独作为模型有效的证据，必须同时报告校准和临床实用性。
