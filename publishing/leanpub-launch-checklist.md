# Leanpub 占坑操作清单 — 5 步上线（含自检与排错）

> 状态：仓库侧配置**已全部就绪**（见下方「已就位」），剩下 5 步需要您的 Leanpub 账号登录，我无法代做。
> 预计耗时：**首次 30–45 分钟**，此后每次更新 = `git push` 即可（Leanpub 自动重建）。
> 相关文件：文件清单 `manuscript/Book.txt` · 样章 `manuscript/Sample.txt` · 书目文案 `publishing/leanpub-book-description.md`

---

## ✅ 仓库侧已就位（无需您操作）

| 项 | 路径 | 说明 |
|---|---|---|
| 章节清单 | `manuscript/Book.txt` | 按顺序列出全书 20 章 + 3 个后置文件；**Ch1–9 已启用**，Ch10–20 仍用 `#` 注释，写好一章就取消注释 |
| 后置内容 | `manuscript/appendix-a-carelink-models.md` `glossary.md`（手写）+ `index.md`（**生成物**） | 排在全书最后，顺序 = 附录 → 术语表 → 索引 |
| 后置内容自检 | `build/make-backmatter.py` | `--check` 术语双向覆盖、`--audit` 核验每条 § 引用；**改章后必跑** |
| 免费样章 | `manuscript/Sample.txt` | 列 Ch1–3 → Leanpub 自动生成免费样书 |
| 书名 | `manuscript/title.txt` | `Object-Oriented Software Engineering` |
| 副标题 | `manuscript/subtitle.txt` | 含 EMI + AI Companion 卖点 |
| 作者 | `manuscript/author.txt` | `Ren Zheng` |
| 插图 | `manuscript/images/` | **81 幅 PNG**（Leanpub 只读此目录）；`manuscript/resources` 软链兼容 Markua 处理器 |
| 插图同步 | `build/sync-figures.sh` | `figures/`（开源 CC BY）→ `manuscript/images/` 一键同步 |
| 书目文案 | `publishing/leanpub-book-description.md` | 书名/简介/长描述/适合谁读/定价，**逐段复制粘贴即可** |

> ⚠️ 图片路径已统一为 `images/xxx.png`（相对 `manuscript/`）。**不要改回 `../figures/...`** ——
> pandoc 会拒绝逃逸出资源根的路径，Leanpub 也看不到 `manuscript/` 以外的文件。

---

## 第 1 步 · 注册 Leanpub（5 分钟）

1. 打开 https://leanpub.com/signup
2. **用 GitHub 账号注册**（最快，且后续授权少一步）
3. 到 `Settings` 填作者署名：`Ren Zheng`，简介可填：
   > Teaches software engineering to international and bilingual classes; writes for students who read English as a second language.

> 💡 Leanpub 是 **0 元开店 + 分成制**：无月费，售出后平台抽 20% 再扣支付手续费，
> 净收益约 70%。不需要预付任何费用。

---

## 第 2 步 · 创建书目并连仓库（10 分钟）

1. 打开 https://leanpub.com/create/book
2. 填写：

| 字段 | 填什么 |
|---|---|
| **Book URL** | `oose-textbook` → 最终地址 `leanpub.com/oose-textbook`（与 GitHub 仓库同名，便于管理） |
| **Title** | 从 `manuscript/title.txt` 复制 |
| **Subtitle** | 从 `manuscript/subtitle.txt` 复制 |
| **Author** | `Ren Zheng` |
| **"Where do you want to write?"** | 选 **"On GitHub"**（不要选 "On your computer"，那是付费功能） |
| **Repository** | `klausren/oose-textbook` |

> ⚠️ **仓库必须是 public**（当前已是 public ✅）。Leanpub 需要读权限。

---

## 第 3 步 · 授权 Leanpub 读取仓库（5 分钟）

创建后 Leanpub 会跳到 **Getting Started** 页，按提示做两件事：

1. **加协作者（必做）**：把 Leanpub 的机器账号（形如 `leanpub`）加为 GitHub 仓库 collaborator。
   GitHub 路径：仓库 → `Settings` → `Collaborators` → `Add people`
2. **加 webhook（强烈建议）**：让每次 `git push` 自动触发重建。
   GitHub 路径：`Settings` → `Webhooks` → `Add webhook`（URL 由 Leanpub 提供）

> 不做 webhook 也能用，但要每次手动点 "Create Preview"。

---

## 第 4 步 · 填书目页并设价（10 分钟）

1. 进 `Author → Books → Object-Oriented Software Engineering → Settings`
2. **Book Description**：打开 `publishing/leanpub-book-description.md`，
   把 `Book description` 代码块里的 Markdown 整段粘进去；`Short description` 粘到对应短描述字段
3. **Pricing**：

| 字段 | 建议值 |
|---|---|
| Minimum price | `$19.99` |
| Suggested price | `$24.99` |
| Free sample | 已由 `Sample.txt` 自动提供（Ch1–3） |

4. **Categories**：`Computers & Technology → Software Engineering`
5. **封面**（可选，但强烈建议）：上传 1600×2560 px 竖版封面

> ⚠️ 定价说明：Leanpub 的 "minimum price" 不能设 0 后再靠打包卖书。
> 前 3 章已在 GitHub 永久免费，这里用 $19.99 门槛筛出真实读者，是合理的做法。

---

## 第 5 步 · 预览 → 上架（10 分钟）

**先跑一遍机器自检（30 秒，不能跳）。** 索引与术语表是**生成物**：改过任何一章都可能让它们与正文脱节，
而脱节的参考章节比没有更糟——读者会照着错引用去翻，然后不再信任书的任何一处交叉引用。

```bash
PY=~/.workbuddy/binaries/python/envs/default/bin/python
$PY build/make-backmatter.py --check --strict   # 术语表 ↔ 各章 Key terms 双向对齐
$PY build/make-backmatter.py --audit --strict   # 每条 § 引用都指向真实使用该术语的节
$PY build/make-backmatter.py                    # 有改动就重生成索引，并一并提交
```

一条非零退出就是一条待修的问题，别带着它上架。

1. 进 `Versions` 页 → 点 **Create Preview**
2. 等进度条跑完，**下载 PDF 逐页检查**（这是唯一能发现排版问题的方式）。

> **先对清单。** `manuscript/Book.txt` 决定**完整版**，`manuscript/Sample.txt` 决定**免费样章**，两者不同：
> 当前完整版 = **Ch1–9 + 附录 A + 术语表 + 索引（12 个文件）**；免费样章 = **Ch1–3**。
> 每加一章，这两处预期都要跟着改，否则"看到的内容比预期多/少"会被误判成构建事故。

- [ ] **完整版**目录含 9 章 + 3 个后置文件（Appendix A / Glossary / Index），且三者排在**全书最后**
- [ ] **免费样章**只含 Ch1–3
- [ ] 书名页 / 副标题正确
- [ ] **9 幅图全部显示**，不是空白框、不是"missing image"
- [ ] **附录 A 的 14 幅图全部显示**（这是全书图最密的一处，最容易漏）
- [ ] 术语表按字母分节，中文对照没有变成乱码或方框
- [ ] 索引条目引用的是**节号**（`5.4`）而不是页码，加粗项可读
- [ ] 图题（caption）在图的**下方**、居中
- [ ] 表格没有溢出页面（附录 A 有 3 张宽表，重点看）
- [ ] `> **In this chapter:**` 引用块渲染正常
- [ ] 代码/术语的内联格式正常

3. 检查通过后点 **Publish**，填版本说明（建议）：

```
Early Access v0.2 — Chapters 1–9 complete, plus back matter.

Part I (Foundations) and Part II (Requirements Engineering, Ch 4–9) are
final-draft quality: twelve-part chapter structure, 81 figures, an AI
Companion with a verification checklist in every chapter, and four-tier
exercises. Back matter is in: Appendix A collects the CareLink artefact
set, and the glossary and index are generated from the chapter sources
and checked mechanically.

Coming next: Chapter 10 closes Part II, then Part III (Design) from
2027 Q1. Buy once, get every future revision.
```

4. 上架后把链接回填到两个地方：
   - GitHub `README.md` 的 "Commercial Edition" 段（有 `<!-- EARLY ACCESS LINK -->` 占位）
   - 课程前言 / 课件末页（可选）

---

## 🔧 排错速查

| 症状 | 原因 | 处理 |
|---|---|---|
| 预览里图片全是空白框 | 图片不在 `manuscript/images/` | 跑 `./build/sync-figures.sh` 后重新 push |
| 预览报 `could not find image` | 章节里用了 `../figures/...` | 改回 `images/xxx.png` |
| 只出现 1 章，其余丢失 | `Book.txt` 里文件名写错或缺扩展名 | 确认每行是 `ch01.md` 这样的完整文件名 |
| 免费样书是整本书 | `Sample.txt` 没生效 | 确认文件名为 `Sample.txt`（大写 S）且在 `manuscript/` 内 |
| 章节标题层级乱 | 章内出现两个 `#` 一级标题 | 一节只能用 `##`；`#` 只用于章标题 |
| `{width=15cm}` 原样显示为文字 | 处理器对属性语法解析差异 | 见下方「备选方案」 |

### 备选方案：Markua 模式

如果 Leanpub 用 Markua 处理器（对 `.md` 文件有可能会），图片属性语法从
pandoc 风格 `{width=15cm}` 变为 `{width: 15cm}`，图片目录从 `images/` 变为
`resources/images/`（已用软链预先兼容）。
**处理顺序**：先看预览结果 → 只有确实报错才改，不要提前改。

---

## 📌 暂不做、但迟早要做（写在这里防止遗忘）

| 事项 | 何时 | 说明 |
|---|---|---|
| **申请 ISBN** | 上架后 1 个月内 | 电子 + 纸质各 1 个。国内可向中国 ISBN 中心申请，或走 Leanpub 的免费 ISBN（仅电子，且会显示 Leanpub 为出版方）。**机构采购必须有 ISBN** |
| **Amazon KDP 纸质版** | Ch10 完成后 | 内页黑白控制成本；彩图版另开高价版 |
| **IngramSpark** | 同上 | 进图书馆 / 馆配，机构背书 |
| **教师资源包（$199/年）** | 2027 Q2 | 含 PPT、题库、答案、SVG 图包；Gumroad 或 Payhip 单独上架（费率仅 ~5%） |
| **俄语 / 西语翻译授权** | 2027 Q3 | 学生来源市场匹配度最高；许可中已保留翻译权 |
| **CC BY 图库单独打包** | 随时 | 免费发放，反哺销量（教师课堂复用 → 学生买书） |

---

## 一句话总结

**您要做的只有 5 步：注册 → 建书连仓库 → 授权 → 贴文案设价 → 预览上架。**
仓库这一侧我已经全部备好，任何一步卡住，把报错发我，我直接改仓库文件。
