# Glossary

Every discipline has a vocabulary, and half of software engineering's
difficulty is that its words already mean something in ordinary English.
*Architecture*, *requirement*, *model*, *state* and *test* are all words a
student met long before page 1, and every one of them means something
narrower here.

This glossary settles that. It holds the terms the chapters introduce as
**key terms**, together with the recurring proper names of the running case.
Each entry gives the term, its settled Chinese equivalent, a definition of
one or two sentences, and the section where the book develops it. Where two
chapters use a word, both sections are cited and the definition covers the
sense they share.

Two conventions, both deliberate.

- **One English term, one meaning, one Chinese equivalent.** Section 5.7
  argues that a specification carries a glossary precisely so that the same
  noun cannot mean two things in two sections. The same rule applies to this
  book. Where a word genuinely has two senses — *specification* is an
  activity in Chapter 4 and a document in Chapter 5 — the entry says so
  rather than pretending otherwise.
- **The Chinese equivalents are glosses, not a translation of the text.**
  They are here because the book is used in bilingual classrooms as well as
  in English-medium ones. The definition is the English one; the Chinese
  column settles the word.

A reference such as *§5.4* means Section 5.4, and promises that Section 5.4
is where the term is taught. Terms the chapters themselves mark as key terms
are listed here in the chapter's own words wherever the chapter gave a
Chinese equivalent, and given a standard equivalent where it did not.

A handful of entries cite a chapter — *Ch 6* — rather than a section. These
are terms the chapter introduces in **Before You Read** and then names in its
summary without ever using them again in the numbered text: *composition*,
*conceptual class*, *documented process*, *necessary non-value-adding*,
*process owner* and *value-adding*. Pointing at a section that does not
contain the word would be worse than pointing at the chapter, so the
reference says what is true. They are also a small to-do list for the second
edition, and the build reports them:

```bash
python3 build/make-backmatter.py --audit
```

That command checks every `§` reference in this glossary against the chapter
sources and fails if a citation points at a section that does not use the
term it is cited for. A glossary is the one part of a book that can be
checked mechanically, so it is checked.

---

## A

**acceptance criterion** 验收标准 — A statement of how a requirement will be
judged satisfied, written so that a tester who did not write the requirement
can apply it without asking. *§5.7*

**action** 动作 — Work performed inside a transition or an activity, as
opposed to a **state**, which is a condition the object is in. If you can ask
how long it lasted, it is not an action. *§9.4*

**activity diagram** 活动图 — A model of a workflow: what is done, in what
order and by whom. Chapter 6 uses it to model a business process across
swimlanes; Chapter 9 uses it to model a workflow that crosses both roles and
the system. *§6.3, §9.5*

**actor** 参与者 — A role outside the system boundary that interacts with the
system to reach a goal. Actors are roles — never people, never departments,
and never the system itself. *§7.2*

**actor goal** 参与者目标 — The goal an actor is pursuing in a use case, and
the organising principle of the use case list. Sorting by actor goal rather
than by feature is what makes a hole visible. *§7.7*

**aggregation** 聚合 — A whole–part association in which the part may outlive
the whole. Weaker than composition, and in a domain model usually not worth
the extra notation. *§8.5*

**Agile Manifesto** 敏捷宣言 — The four values and twelve principles published
in 2001. Each value prefers something *over* its counterpart — individuals
and interactions over processes and tools — rather than rejecting it. *§3.2*

**agility** 敏捷性 — Rapid, flexible response to change, plus effective
communication, built on short cycles and continuous delivery. A context
decision, not a religion. *§3.4*

**alt fragment** 选择片段 — The sequence-diagram frame that draws a branch: a
box labelled `alt` with a guard on each compartment, exactly one of which
runs. *§9.3*

**alternative flow** 备选流程 — Any path through a use case other than the
main flow: a failure, a recovery, a variation. The alternative flows are
where the requirements live. *§7.4*

**analysis** 分析 — The work that turns elicited statements into a decided,
bounded, prioritised requirement set. Elicitation finds; analysis decides.
*§5.1*

**analysis model** 分析模型 — A model built during analysis that organises
what has been elicited around three views — data, function and behaviour. Its
output is *questions*, not diagrams. *§5.2*

**as-is model** 现状模型 — A model of the process as it actually runs today.
It is evidence, and Chapter 6 requires it to be produced before the to-be
model. *§6.2*

**association** 关联 — A structural relationship between two concepts, or
between an actor and a use case, meaning that they are linked in the domain
or that the actor participates in the goal. *§7.3, §8.5*

**association class** 关联类 — A class that holds facts about a *link* rather
than about either of its ends, such as the care assignment between a caregiver
and a resident. *§8.6*

**association end name** 关联端名 — The name read along one direction of an
association. Its job is to let you say the sentence aloud in both directions
before you choose a multiplicity. *§8.5*

**attribute** 属性 — A fact about exactly one concept, decided by the three
tests: an attribute has no identity of its own, no independent life, and is
not shared. *§8.3*

## B

**behavioural model** 行为模型 — A model that answers what is true at a given
moment and what happens next — the question a use case and a domain model
cannot answer. *§9.1*

**bounded metric** 有界度量 — A measurable quantity with a range that makes
the requirement checkable, such as "within 60 s at p95". A non-functional
requirement with no bounded metric is a wish. *§5.6*

**boundary list** 边界清单 — The written list of what the system is *not*
responsible for, kept beside the model so that obligations handed to named
humans stay outside it. *§8.4*

**burndown chart** 燃尽图 — A plot of work remaining against time inside a
Sprint, used to see progress rather than to predict it. *§3.11*

**business process** 业务流程 — A set of activities that produces something a
customer values. A system participates in a business process; it is not the
process. *§6.1*

## C

**classification** 分类 — Operation 2 of the five analysis operations:
deciding whether each candidate is a functional requirement, a non-functional
requirement, a domain constraint, a design decision or a wish. *§5.3*

**composition** 组合 — A whole–part association in which the part cannot
outlive the whole. The strong form of aggregation. *Ch 8*

**compound requirement** 复合需求 — One requirement hiding two, joined by "and"
or "or" — a defect, because the two halves will be tested and scheduled
separately. *§5.6*

**concept** 概念 — A thing in the problem domain that the model claims exists,
named in the vocabulary of the people whose world it describes. *§8.3*

**concept inventory** 概念清单 — The table of every surviving concept with its
definition, its evidence and its verdict. The discard list is as much a
deliverable as the survivors. *§8.7*

**conceptual class** 概念类 — A synonym for **concept** when the emphasis is
on its being a class in the model rather than an object in the world. *Ch 8*

**concurrent model** 并发模型 — A process model in which several activities
proceed in parallel with defined synchronisation points, rather than in
sequence. *§2.10*

**conflict** 冲突 — A disagreement between stakeholders about what the system
must do. Conflicts are factual, goal or resource, and each kind has exactly
one owner. *§5.4*

**consolidation** 归并 — Operation 1 of the five: merging statements that
describe the same need into one row while keeping the union of their
evidence. Every removal is a duplicate, never a decision. *§5.3*

**corrective / adaptive / perfective / preventive maintenance**
修正性 / 适应性 / 完善性 / 预防性维护 — The four kinds of change software
undergoes: fixing faults, adapting to a changed environment, improving
quality, and forestalling future faults. *§1.5*

**coverage check** 覆盖检查 — Comparing one artefact against another to find
what is missing — the use case list against the feature list, the domain model
against the use case list. *§7.8*

**cycle time** 周期时间 — Elapsed time from the start of a process to its end,
for one case. CareLink's alarm call is 112 minutes. *§6.5*

## D

**data / function / behaviour view** 数据 / 功能 / 行为视图 — The three
complementary views of the analysis model. Each one exposes a class of gap
the other two hide. *§5.2*

**Daily Scrum** 每日站会 — The fifteen-minute daily inspection of progress
toward the Sprint Goal. *§3.10*

**decision node** 判定节点 — The diamond in an activity diagram whose
outgoing edges carry exhaustive guards. *§6.3*

**Definition of Done** 完成的定义 — The team's written agreement on what
"done" means for an Increment. Without one, velocity measures attendance.
*§3.11*

**derived attribute** 派生属性 — An attribute that could be computed from
others. In a domain model it is usually better left out, because drawing it
invites the reader to argue about arithmetic instead of about the world. *§8.5*

**disagreement log** 分歧记录 — The running record of conflicts raised, their
kind, their owner and how they were settled — kept so that a decided conflict
is not re-argued in the next meeting. *§5.4*

**documented process** 文件化流程 — What the manual says happens. The point of
Section 6.5: the documented process is precisely the one you must not model.
*Ch 6*

**documentation** 文档 — The third part of software, beside instructions and
data structures. All three are the product. *§1.1*

**domain constraint** 领域约束 — A requirement that is not negotiable because
the world sets it, such as health data that may not leave the province. *§5.3*

**domain model** 领域模型 — A model of the **problem**: the things in the
user's world, their attributes and their relationships, in the user's
vocabulary. Not a design class diagram and not a database schema. *§8.1*

## E

**elaboration** 精化 — The requirements activity that expands an elicited need
into a structured, detailed statement, and that produces the analysis model.
One of the six requirements activities. *§4.2*

**elicitation** 需求获取 — The activity of getting requirements out of people:
interviews, observation, workshops, document study. Elicitation is a cycle,
and its **confirm** step is what turns notes into evidence. *§4.6*

**elicitation record** 需求获取记录 — The artefact elicitation produces, built
in four steps: separate, classify, test, number and attribute. *§4.9*

**eliminate / simplify / parallelise / automate** 消除 / 简化 / 并行 / 自动化 —
The four process improvements, attempted in that order. Automation applied to
a step that should not exist produces a faster mistake with a maintenance
contract. *§6.6*

**empirical process control** 经验性过程控制 — The position that in complex
work, progress is discovered by short cycles of observation and adjustment
rather than planned in full up front. *§3.7*

**entry / exit criteria** 进入 / 退出准则 — The conditions that must hold
before a process activity may start and when it is considered complete. *§2.5*

**event** 事件 — Something that happens and that an object can react to. In a
state machine, an event with no matching transition is ignored unless a
transition says otherwise. *§9.4*

**evidence** 证据 — The source that supports a concept or a requirement.
Supported, inferred and unsupported are three different verdicts, and only
the last one is a verdict about deletion. *§8.7*

**evidence label** 证据标签 — The one-letter mark carried by every element of
a process model: `[O]` observed, `[S]` stated, `[D]` documented, `[A]`
assumed. *§6.7*

**extend** 扩展 — The use case relationship for behaviour that runs only under
a condition; the source use case is complete without it. *§7.6*

## F

**factual / goal / resource conflict** 事实性 / 目标性 / 资源性冲突 — The three
kinds of disagreement: about what is true, about what is wanted, and about who
gets a limited thing. Check a factual conflict before you negotiate it. *§5.4*

**framework activity** 框架活动 — One of the five process activities:
communication, planning, modeling, construction, deployment. *§2.3*

**functional requirement** 功能需求 — A requirement on what the system does —
the behaviour it must exhibit. *§5.3*

## G

**gap** 差距 — The difference between the as-is and the to-be process. The gap
is what gets funded. *§6.2*

**generalisation** 泛化 — The relationship in which one concept is a
specialisation of another. Generalise when concepts share identity and differ
by role; do not generalise when they differ by state. *§7.3, §8.5*

**goal level** 目标层次 — The altitude at which a use case is written.
Summary-level ambitions and subfunction-level steps both fail, for opposite
reasons. *§7.1*

**goal test** 目标测试 — The test "〈actor〉 is trying to 〈name〉", applied to
every candidate use case. A name that fails it is a function, not a goal.
*§7.1*

**guard** 守卫条件 — The condition attached to a transition or to a decision
edge. Guards on a decision must be exhaustive; in Chapter 9, a case with no
exit is a finding rather than an oversight. *§6.3, §9.4*

## H

**handoff** 交接 — The point in a process where a case passes from one actor to
another. Handoffs are where queueing, lost context and travel time live.
*§6.4*

## I

**identity** 标识 — The first of the three concept-or-attribute tests: can two
instances of this thing be told apart, and must they be? *§8.3*

**include** 包含 — The use case relationship for behaviour that always runs as
part of the source and that has shared meaning. Extract for meaning, never for
repeated text. *§7.6*

**inception** 起始 — The first of the six requirements activities: agreeing on
what the project is and who cares about it. *§4.2*

**Increment** 增量 — The sum of the completed work of one Sprint, usable as a
whole. The third Scrum artefact. *§3.9*

**incremental model** 增量模型 — A process model that delivers planned slices
of the product in sequence, each slice adding working functionality. *§2.8*

**initial state** 初始状态 — The filled circle that marks where a state machine
begins. *§9.4*

## K

**Kano model** 卡诺模型 — A way of sorting features by their effect on
satisfaction: must-be, performance and attractive. Used in Section 5.5 to
resist the habit of promoting everything to Must. *§5.5*

## L

**legacy software** 遗留软件 — Software still in use that was written for an
earlier environment, and whose change is the expensive kind. *§1.5*

**lifeline** 生命线 — The vertical line under a participant in a sequence
diagram, representing that participant's life during the interaction. *§9.3*

## M

**main flow** 主流程 — The shortest **complete** path through a use case that
ends in success — not the typical path. Any recovery inside it means the happy
path was not written. *§7.4*

**merge node** 合并节点 — The diamond that joins alternative paths back
together in an activity diagram. *§6.3*

**message** 消息 — A unit of communication in a sequence diagram: an event in
the users' vocabulary, never a screen and never a click. *§9.3*

**method** 方法 — The technical how-to of software engineering: procedures,
notations and techniques. One of the three essentials, with process and
tools. *§1.8*

**MoSCoW** 必做 / 应做 / 可做 / 本期不做 — A prioritisation scheme with four
levels: Must, Should, Could, Won't. It works only with a test — "release 1
fails without this" — and a cap on how many items may be Must. *§5.5*

**multiplicity** 多重度 — The number of objects that may participate at one
end of an association. Multiplicity is read out of a sentence, not chosen.
*§8.5*

## N

**necessary non-value-adding** 必要非增值 — Work that adds no value the
customer wants but that physics, law or safety requires — a car journey, a
signature, a waiting period. To be acknowledged honestly, not eliminated.
*Ch 6*

**need** 需要 — A problem or a desire in the user's world. A need is not a
requirement and not a solution; keep the three in separate columns. *§4.1*

**negotiation** 协商 — The activity in which stakeholders with conflicting
wants reach a decision. Also Operation 3 of the five analysis operations.
*§4.2, §5.4*

**non-functional requirement** 非功能需求 — A requirement on *how well* the
system does something: performance, reliability, usability. Each one needs a
named measurement method or it is a wish. *§5.3*

## O

**obligation** 义务 — Something the project owes that is not anybody's goal:
escalation, retention, archiving. It belongs in the requirements and in the
alternative flow of the use case that failed — not as an oval of its own.
*§7.9*

**open / leading / closed question** 开放式 / 诱导式 / 封闭式问题 — The three
shapes a question can take. Ask open questions; leading questions feel
productive and produce nothing. *§4.8*

**open question** 待决问题 — An unresolved item in a specification, listed
with an owner and a date. The honest section of the document. *§5.7*

**ordering guarantee** 时序保证 — What a sequence diagram asserts: which
message precedes which. The ordering *is* the whole content of the model.
*§9.3*

**over-specification** 过度规格化 — Constraining *how* something is done when
only *what* has been agreed. It forecloses alternatives before anyone has
measured them. *§5.6*

**owner** 归属人 — In Chapter 9, the person responsible for an object at a
given moment. A fact about a relationship, not a state of the object. *§9.5, §9.8*

## P

**p95** 第 95 百分位 — The value below which 95 % of observations fall. A
bounded metric that resists an average's habit of hiding the bad cases. *§5.6*

**Planning Poker** 计划扑克 — The estimation technique in which the team
reveals story-point estimates simultaneously, so that disagreement surfaces
fast instead of being averaged away. *§3.11*

**postcondition** 后置条件 — What must be true once a use case has completed
successfully. *§7.4*

**precondition** 前置条件 — What must be true before a use case can start. A
false precondition is one of the six alternative-flow families. *§7.4*

**primary actor** 主参与者 — The actor whose goal the use case exists to
satisfy. A use case has exactly one. *§7.4*

**prioritisation** 优先级排序 — Operation 4 of the five: ordering the
requirement set by value. Decided by the Product Owner, informed by the
team's cost. *§5.5*

**process** 过程 — The set of activities by which software is built. One of
the three essentials, with methods and tools. *§1.8*

**process frame** 过程框架 — The skeleton of framework activities, actions and
tasks that any process fills in with its own detail. *§2.5*

**process model** 过程模型 — A description of how the framework activities are
ordered and repeated: waterfall, V, incremental, prototyping, spiral,
concurrent, RUP. *§2.5*

**process owner** 流程负责人 — The person accountable for the result a process
produces, as distinct from the people who work inside it. *Ch 6*

**Product Backlog** 产品待办列表 — The ordered list of everything that might
be built, owned by the Product Owner and the single source of work. *§3.9*

**Product Owner** 产品负责人 — The Scrum role accountable for the value the
Increment delivers, and the only person who orders the Product Backlog. *§3.8*

**prototyping** 原型法 — An evolutionary process model that builds a version of
the product to answer a question the team cannot answer on paper. *§2.9*

## Q

**queue** 排队 — Work waiting for a resource. Queue time is waiting time, and
in CareLink it is the largest single part of the cycle. *§6.5*

## R

**reachability** 可达性 — The check that every state of a state machine can be
entered from the initial state. An unreachable state is a modelling error, not
an unneeded one. *§9.4*

**real-world identifier** 现实标识 — An identifier that exists in the world,
such as a wristband serial number. It belongs in the domain model, where a
surrogate key does not, because it is a fact about the world. *§8.1*

**requirement** 需求 — A checkable statement of what the system must do, or of
how well it must do it. Not a need, and not a solution. *§4.1*

**residual** 不可压缩余量 — The part of a cycle time that no software change
can reach. Forty-two of CareLink's 112 minutes are a car, and reporting that
is what makes the rest of the claim credible. *§6.5*

**Retrospective** 回顾会 — The Sprint-closing event in which the team inspects
how it worked and chooses one thing to change. *§3.10*

**rework** 返工 — Work redone because the first attempt was wrong or
incomplete. A form of waste that a process model makes visible. *§6.5*

**role** 角色 — What an actor, or a person, is *as* in a given relationship.
Actors are roles; concepts that share identity but differ by role are the ones
worth generalising. *§8.5*

**RUP** 统一过程 — The Rational Unified Process: a phase-based, iterative
process model designed for large projects, with defined disciplines and
milestones. *§2.10*

## S

**scenario** 场景 — One concrete path through a use case, carrying names and
values: one beginning, one path, one ending. *§9.2*

**Scrum Master** 敏捷教练 — The Scrum role accountable for the team's use of
Scrum. A servant-leader who removes obstacles, not a project manager. *§3.8*

**self-message** 自消息 — A message an object sends to itself in a sequence
diagram, drawn as an arrow returning to its own lifeline. *§9.3*

**sequence diagram** 顺序图 — A model of who talks to whom, in what order, for
one scenario. *§9.3*

**software** 软件 — Instructions, data structures and documentation together.
All three are the product. *§1.1*

**software crisis** 软件危机 — The recognition, from the late 1960s onward,
that projects were routinely late, over budget and unreliable. The origin
story of the discipline. *§1.6*

**software engineering** 软件工程 — The systematic, disciplined and quantifiable
approach to developing, operating and maintaining software. *§1.6*

**software process** 软件过程 — The framework of activities, actions and tasks
used to build software. See **process**. *§2.2*

**specification** 规格说明 — Two senses, and the book keeps them apart. In
Chapter 4 it is the **activity** of writing requirements down; in Chapter 5 it
is the **document** that results. *§4.2, §5.7*

**spiral model** 螺旋模型 — An evolutionary process model whose cycles are
driven by risk, each loop closing with a review. *§2.9*

**Sprint Backlog** 冲刺待办列表 — The subset of the Product Backlog the team
takes into one Sprint, together with the plan for delivering it. *§3.9*

**Sprint Goal** 冲刺目标 — The single purpose a Sprint serves, which is what
makes the Sprint Backlog a coherent whole rather than a list. *§3.9*

**Sprint Review** 冲刺评审 — The Sprint-closing event in which the Increment is
inspected with stakeholders and the Product Backlog is adjusted. *§3.10*

**stakeholder** 利益相关者 — Anyone who cares about the outcome of the
project. Sorted by influence and interest before you book their time. *§4.4*

**state** 状态 — A condition an object is in over an interval. If you can ask
how long, it is a state; if you can only say what is happening, it is an
action. *§9.4*

**state machine** 状态机 — A model of what can happen to one object over its
whole life: its states, its events and its transitions. *§9.4*

**state-event table** 状态-事件表 — The check that asks about every state and
event pair. CareLink's has thirty-six cells: seven move the object, two
refuse, one changes the owner, twenty-six ignore. Thirty-six cells are
thirty-six tests waiting to be written. *§9.8*

**story point** 故事点 — A relative unit of size for estimating work.
Meaningful only inside one team, and never comparable across teams. *§3.11*

**supporting actor** 支持参与者 — An actor that participates in a use case to
provide a service, but does not want the goal for itself. *§7.2*

**surrogate key** 代理键 — A computed identifier introduced for storage. It
belongs in the schema, not in the domain model. *§8.1*

**swimlane** 泳道 — The partition of an activity diagram by actor, whose whole
value is making handoffs visible. *§6.4, §9.5*

**system boundary** 系统边界 — The rectangle that separates what the project is
responsible for from what is somebody else's job. It is a decision, and every
element outside it becomes a named human's obligation. *§7.3*

## T

**tacit knowledge** 隐性知识 — What an expert knows and cannot easily say. The
main reason elicitation is hard, and why watching beats asking. *§4.10*

**terminal state** 终态 — A state an object never leaves. In a state machine it
is drawn as a bullseye. *§9.4*

**timebox** 时间盒 — A fixed, non-extendable period within which work must
finish. Scrum and XP use it to force a scope decision rather than a schedule
slip. *§3.10*

**to-be model** 目标模型 — The model of the process as the project intends it
to run. A design, not evidence. *§6.2*

**tool** 工具 — The automation that supports a process and its methods. One of
the three essentials, with process and methods. *§1.8*

**touch time** 作业时间 — The part of a cycle during which somebody is
actually working on the case. CareLink's alarm call spends 21 of its 112
minutes in touch time. *§6.5*

**traceability** 可追溯性 — The maintained link from a requirement to the
design element that satisfies it and to the test that verifies it. It buys
change impact analysis, visible coverage and evidence. *§5.8*

**transition** 迁移 — The move from one state to another on an event, possibly
guarded and possibly carrying an action. *§9.4*

**transparency / inspection / adaptation** 透明 / 检视 / 调整 — The three
pillars of empirical process control: everyone can see the true state, it is
inspected often, and it is changed when it is wrong. *§3.7*

**transport time** 转运时间 — The part of a cycle spent moving the case
between actors or places. CareLink's alarm call spends 45 minutes in transit.
*§6.5*

**trap state** 陷阱状态 — A state with no exit, entered by an event the model
does not handle. A trap state is a missing requirement, not a missing arrow.
*§9.4*

**trigger** 触发器 — The event that starts a use case. *§7.4*

## U

**ubiquitous language** 统一语言 — The shared, precise vocabulary a team uses
in conversation, in the model and in the code. A concept with no name in the
user's vocabulary is a sign the model has left the problem. *§8.2*

**umbrella activity** 贯穿性活动 — An activity such as review, risk management
or quality assurance that runs across the whole process rather than sitting in
one phase. *§1.8, §2.4*

**use case** 用例 — A goal an actor pursues with the system, together with the
flows by which it is reached. A use case is not a feature. *§7.1*

**use case description** 用例描述 — The structured text behind the oval: name,
actors, trigger, preconditions, main flow, alternative flows, postconditions,
and the requirements the flows produce. *§7.4*

**user story** 用户故事 — A short statement of value in the user's own words,
used to plan work. An input to requirements, not a substitute for one. *§3.9*

**user-goal level** 用户目标层 — The use case altitude at which an actor
achieves something worth a session. The level at which use cases are written.
*§7.1*

## V

**V model** V 模型 — A sequential process model that pairs each design level on
the left with the test level that verifies it on the right. *§2.7*

**validation** 验证 — Checking that what was written or built is the *right*
thing. Distinct from verification, which checks that it was built right.
*§4.2*

**value-adding** 增值的 — Work that changes something the customer is willing
to pay for. The first of three process verdicts, with necessary
non-value-adding and waste. *Ch 6*

**velocity** 速率 — The amount of work a team completes per Sprint, measured in
story points. A planning input, never a target. *§3.11*

**volatility** 易变性 — The rate at which requirements change. One of the five
reasons elicitation is hard, and an input to the choice of process model.
*§4.10*

## W

**waiting time** 等待时间 — The part of a cycle spent queued for the next
actor. CareLink's alarm call spends 46 of its 112 minutes waiting. *§6.5*

**waste** 浪费 — Work that changes nothing the customer values: rework,
queueing, moving things about. *§6.6*

**waterfall** 瀑布模型 — A sequential process model with distinct phases and a
single delivery at the end. *§2.6*

---

## Proper names of the running case

The chapters tell one story, and the people in it have to be the same people
from Chapter 1 to Chapter 20. These are the names, with the role each one
plays. Where a name appears in only part of the book, the chapter range is
given so that a reader who meets the name late can see where it came from.

| Name | Role | Appears |
|---|---|---|
| **CareLink** | The running case: a community home-care platform that watches over elderly people living alone, alerts the family and the care centre, and escalates emergencies | Ch 1–20 |
| **Grandma Lin** | The elder. Lives alone, wears a smart wristband, uses the oversized-button interface | Ch 1–9 |
| **Wei** | Grandma Lin's son, and the family-app user. Receives notifications and configures alert thresholds | Ch 1–9 |
| **Operator Yan** | The care-centre console operator. Triages automatic alerts and starts the escalation chain | Ch 2–3 |
| **Deng** | Care-centre supervisor. Owns the escalation policy, the caregiver roster and the care assignment — and is the person who shows why an actor must be a role and not a person | Ch 4–9 |
| **Piotr** | A developer on the CareLink team. He wants a database schema, which is how Chapter 8 separates the domain model from the schema | Ch 8–9 |

Two of these names earn their place beyond the narrative. **Deng** is the
chapter's standing counter-example: a supervisor who is also a family member
and also, sometimes, a caregiver — which is why the use case model promotes
the *role* and not the person. **Piotr** is the reader's temptation in the
flesh: he is the one who asks for a schema when the team has not yet agreed on
what the words mean.

---

## Maintaining this glossary

This glossary is generated from the chapters, not maintained by hand beside
them. Every chapter ends with a `**Key terms:**` line; the build script
`build/make-backmatter.py` reads those lines, compares them against the entries
above, and reports any term that a chapter introduces but this glossary does
not define, or defines but no chapter introduces. Run it before every release:

```bash
python3 build/make-backmatter.py --check
```

A term that appears in a chapter and not here is a defect of the same kind as
a figure that no caption points at. The rule the book applies to figures
applies to vocabulary too: **if the chapter uses it, the reference section
owes the reader a definition.**
