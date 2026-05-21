# Standard Deliverable Template

Use this template when core intake information is available and the user asks for a complete research framework.

Write the main deliverable in Chinese unless the user requests another language. Write the manuscript methods draft in both Chinese and English.

For formal delivery, write this template into a Word document. Write the downstream R agent prompt into a separate Markdown file. Do not treat a long chat response as the final deliverable unless the user explicitly asks for inline output.

The Word document should use broad sections and concise nested content. Avoid a large method-selection table. Avoid excessive headings where short inline labels are enough.

## Title Page

Include:

- document title
- study topic
- deliverable type
- date
- version if available

## Table of Contents

Include a simple manual table of contents for the major sections.

## 一、研究概览

Include:

1. 研究问题
2. 目标人群
3. 研究类型与模型用途
4. 结局定义
5. 候选预测变量
6. 当前数据条件
7. 本研究能回答与不能回答的问题

Keep this section factual and concise.

## 二、数据可行性与研究定位

Include:

1. 样本量与事件数
2. 变量数量与缺失情况
3. 验证条件
4. 可行性判断
5. 推荐研究定位

Use one of these feasibility labels:

- 适合模型开发
- 适合探索性模型开发
- 更适合关联分析
- 需要简化设计或补充数据

Explain the feasibility judgment in a short paragraph.

## 三、分析方法设计

Organize methods under these subsections:

1. 结局与时间结构
2. 预测变量与特征工程
3. 缺失值处理
4. 变量筛选
5. 建模方法
6. 验证策略
7. 性能评价
8. 临床实用性评价

For each subsection, use concise inline labels:

- 推荐：
- 原因：
- 可选方案：
- 适用与不适用：

Do not turn these labels into many additional heading levels.

## 四、推荐分析流程

Provide an ordered plan:

1. 数据检查
2. 变量处理
3. 特征工程
4. 变量筛选
5. 模型开发
6. 模型验证
7. 结果报告

This section should summarize the selected route only. Do not re-list all alternatives.

## 五、报告规范与偏倚风险

Include:

1. 学术表述
2. TRIPOD / TRIPOD+AI
3. PROBAST / PROBAST+AI
4. 主要偏倚风险
5. 适用性限制

Keep the focus on reporting quality and interpretive boundaries.

## 六、论文方法学草稿

Include:

1. 中文版本
2. English Version

Both versions should match the recommended route.

Cover:

- study type
- data source
- outcome and predictors
- preprocessing
- predictor selection
- model development
- validation
- performance metrics
- software

## 七、R Agent Prompt 文件说明

Include:

1. 文件用途
2. 使用前提
3. 文件路径

State that the full downstream prompt is saved as a separate Markdown file.

## 八、实用注意事项

Include concise cautions tailored to the study.

Mention only relevant cautions, such as:

- 样本量或事件数有限
- 类别不平衡
- 结局定义不确定
- 缺少外部验证
- 信息泄漏风险
- 过拟合风险
- 校准不足
- 模型复杂度过高
- 诊断、预测或预后表述不当
