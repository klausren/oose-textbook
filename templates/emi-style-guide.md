# EMI Style Guide · 面向非母语读者的写作规范

> Scope 适用范围：全书 20 章 + 附录 | Version 1.0（2026-09-05）
> This guide is what makes the book different. Read it before writing any chapter.
> 本规范是本书差异化的核心。动笔前必读。

---

## 0. 为什么需要这份规范

Pressman 和 Sommerville 都由母语者写给母语者。在英语授课（EMI）的大学里——中国、东南亚、
中东欧、海湾地区、拉美——学生翻开这些教材时，**卡住的往往不是工程，而是英语**：

- 一句 45 词的从句套从句，专业概念其实早就会了，句子没读懂
- 同一概念在不同章节换了三种说法（*use case* / *use-case* / *usage scenario*），学生以为是两个东西
- 没有背景知识支撑，读到 *stakeholder*、*trade-off*、*scope creep* 这类行话就断片

**本书的定位不是"更简单的英语"，而是可控英语（Controlled English）**——与航空维修领域的
ASD Simplified Technical English 同一思路：牺牲一点文采，换取零歧义和低阅读负荷。

---

## 1. 五条硬规则 | Five Hard Rules

### 规则 1 · 句长中位数 ≤ 20 词

- 每段只讲一个观点
- 一个句子只承载一个主张；需要并列就用两个句子
- 允许少量短句（8–12 词）调节节奏，但**不得**出现 35 词以上的句子

**改前 / 改后对照**

> ❌ *Notwithstanding the aforementioned considerations, it is incumbent upon the requirements engineer to ensure that the elicited requirements are sufficiently unambiguous so as to preclude the possibility of divergent interpretations by disparate stakeholders.*（38 词）
>
> ✅ *Two stakeholders can read the same requirement and understand different things. That is the risk you must remove. A requirement is unambiguous when only one reading is possible.*（31 词，三句，最长 14 词）

### 规则 2 · 一词一义（Terminology Consistency）

- 全书 150 个核心术语，**每个概念只用一种说法**，禁止同义词轮换
- 首次出现：**加粗** + 中文对照，例：**stakeholder（利益相关者）**
- 同一术语的重音与大小写全书统一：`use case`（名词）/ `use-case`（仅作形容词）
- 禁止使用的同义轮换：*use case / usage scenario / user story* 混用；*class / type / kind* 指同一抽象时混用

> 维护方式：每个学期末跑一次一致性检查（见 `build/`），比对术语表与正文用词。

### 规则 3 · 每章术语预热（Before You Read）

每章开头一个术语框，**6–10 条**，每条一行、不超过 15 词，给中文对照：

```markdown
> **Before you read 术语预热**
> - **stakeholder（利益相关者）** — anyone affected by the system
> - **elicitation（需求获取）** — the act of drawing requirements out of people
> - **ambiguity（二义性）** — when one sentence allows two readings
```

> 为什么有效：非母语读者的阅读中断，70% 发生在"这个词我不认识"。预热把中断提前到阅读之前。

### 规则 4 · 章末 Language Focus（学术英语句型）

每章末尾一个**固定小节**，讲本章写作真正需要的 3–5 个句型。不是通用英语课，是"这一章的作业怎么写"。

结构固定为三步：**句型 → 例句 → 3 题练习**。

示例（第 8 章 用例规约）：

| 你在写什么 | 用这个句型 |
|---|---|
| 正常行为 | *The system shall \<verb\> \<object\> when \<trigger\>.* |
| 事件触发 | *Upon \<event\>, the system shall …* |
| 分支 | *If \<condition\>, the system shall …; otherwise, …* |
| 前置条件 | *\<Actor\> has \<state\>.* |
| 后置条件 | *\<Object\> is in \<state\>.* |

**练习**：把下面这句模糊需求改写为可测试的规约 —— *"The system should respond quickly."*

> 这一节是本书最容易被模仿、也最容易被低估的部分。**它是教师决定是否采用的隐性理由之一**：
> 学生的英文作业质量会因此明显提升，而这正是 EMI 课堂教师的痛点。

### 规则 5 · 图表自足（Self-Contained Figures）

- 每幅图有编号与**自足式图注**：不看正文也能看懂
- 图中所有文字使用与正文一致的术语
- 图注用一句完整的句子，不用名词短语

> ❌ `Fig 8-3 Use case diagram`
> ✅ `Fig 8-3 The five actors of CampusGuard and the use cases each one starts.`

---

## 2. 每章固定九段式（EMI 增强版）

在原有八段式基础上，新增**术语预热**与 **Language Focus** 两段：

```
1. Learning Objectives        学习目标（4–6 条，Bloom 动词）
2. Before You Read            术语预热（6–10 条，含中文对照）        ← 新增
3. Opening Scenario           CareLink 情境导入（1 页，以案例困境开篇）
4. Core Concepts              核心概念讲解（8–12 页，短句、每节配图）
5. CareLink in Action         案例实战（3–5 页）
6. Common Pitfalls            常见误区（1–2 页，来自真实课堂的高频错误）
7. Guided Lab                 导引实践（2–3 页，可作课堂练习）
8. Language Focus             本章学术英语句型 + 3 题练习              ← 新增
9. Summary & Key Terms        小结 + 术语框（中英对照）
10. Exercises                 习题（5–8 题：概念 / 分析 / 项目任务三档）
    + Running Project Task    本周项目任务（CampusGuard 进度同步）
```

> 注：新增两段共约 1.5 页，每章总量从 20 页增至约 21–22 页；全书 420 → 约 440 页，仍在 64 学时可讲完的范围内。

---

## 3. 多语术语表 | Multilingual Glossary

附录 B 的三栏结构：

| English | 中文 | Русский（可选） |
|---|---|---|
| stakeholder | 利益相关者 | заинтересованная сторона |
| use case | 用例 | вариант использования |

- **EN + 中文为必填**（主读者群体）
- **俄文列为可选项** —— 2026–2027 学年的授课班级为俄语母语者，收录俄文对中东欧市场是杀手锏，
  但需请俄语母语者核对后再定稿；若无人核对，宁可留空（错误的术语表比没有更糟）

---

## 4. 动笔前自检清单 | Pre-Submission Checklist

写完一章后逐条打勾：

- ☐ 随机抽 10 个句子，没有一句超过 30 词
- ☐ 本章出现的所有核心术语都在术语预热框里
- ☐ 全文未出现术语表之外的同义轮换
- ☐ 每幅图的图注是完整句子，且不依赖正文
- ☐ Language Focus 的句型在**本周作业中真的用得上**
- ☐ 章末 Key Terms 与附录 B 术语表逐条一致
- ☐ 中文对照部分由中文母语者确认（作者本人即可）
- ☐ 通读一遍，把所有 *notwithstanding / aforementioned / hereby* 删掉

---

## 5. 常见误区 | What This Guide Does Not Mean

| 误区 | 正解 |
|---|---|
| "可控英语 = 内容降级的教材" | 概念深度不变，只降低语言负荷。本书仍覆盖 ISO/IEEE 29148 与 25010 的完整术语体系 |
| "短句就是好英语" | 短句是手段，**零歧义**才是目标。为准确而稍长的句子可以保留，但不超过 30 词 |
| "加中文对照就够了" | 只加中文是翻译思维；本书的做法是**控制英文本身** + 术语预热 + 句型支架 |
| "Language Focus 是英语课内容" | 它讲的是**本章作业怎么写**，是专业写作，不是通用英语 |
