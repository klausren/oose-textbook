# The CareLink Running Case — Setting Document (v1.0)

> This document is the single source of truth for the CareLink case study.
> Every chapter of the textbook draws its case material from here.
> Version: 1.0 · 2026-08-29 · Owner: textbook author

## 1. What Is CareLink?

**CareLink** is a community-based home-care platform that helps elderly people
live safely and independently in their own homes. It watches over their daily
well-being through lightweight sensors, alerts family members and a community
care center when something looks wrong, and responds to emergencies in
escalating levels of urgency.

CareLink is the *running case* of this textbook. It appears in every chapter.
Requirements gathered in Part II become the models of Part III, the designs of
Part IV, and the plans of Part V. By the end of the book, the reader has walked
a complete, coherent software engineering project from first interview to final
delivery.

**Why elder care?** The domain is genuinely meaningful, is growing fast in
every aging society, and — crucially for teaching — naturally contains
everything a software engineering case needs: hardware/software boundaries,
multiple user roles, real-time constraints, privacy concerns, safety-critical
alerting, and human-in-the-loop processes.

## 2. Stakeholders

| Stakeholder | Role in the system |
|---|---|
| **Elder (primary user)** | Lives alone; wears a smart wristband; interacts through an oversized-button simple interface |
| **Family member** | Uses the CareLink mobile app; receives notifications; configures alert thresholds |
| **Care center operator** | Staffs the 24/7 console; triages automatic alerts; escalates emergencies |
| **Community doctor / emergency service** | Third-party responder contacted through escalation |
| **Property/community manager** | Provides sensor installation and door-access integration |
| **CareLink development team** | The "we" of the textbook — a small Scrum team of 6 |

## 3. System Snapshot (level of detail: Chapter 1)

- **Sensing**: wristband (heart rate, fall detection, button), room sensors
  (motion, temperature), smart plug (kettle/oven usage as daily-activity signal)
- **Modes**: *Home mode*, *Night mode*, *Outing mode* — different alert rules
- **Alerting**: three levels —
  L1 *gentle* (reminder to the elder), L2 *family* (push to app),
  L3 *urgent* (care center call chain → doctor/ambulance)
- **Daily report**: activity summary pushed to family app each evening
- **Privacy**: sensor data stays local by default; video is off; family access
  is permission-scoped

## 4. Mapping from SafeHome (for course-material migration)

Existing slide material built around Pressman's SafeHome transfers directly:

| SafeHome element | CareLink counterpart | Modeling value |
|---|---|---|
| Door/window/motion sensors | Wristband + room sensors + smart plug | Sensor abstraction, hardware boundaries |
| Homeowner app | Elder interface + family app (two user classes) | Richer roles, UI design for distinct users |
| Monitoring center | Community care center console | Human-in-the-loop, state machines |
| Police dispatch | L3 escalation to doctor/ambulance | Use-case extensions, exception flows |
| Arm/disarm | Home/Night/Outing modes | Strategy selection, configuration design |
| SafeHome SRS artifacts | CareLink SRS (Appendix A) | Full documentation set |

## 5. What Each Part of the Book Does with CareLink

| Book part | CareLink artifact produced |
|---|---|
| I Foundations | The project vision, the team, the problem statement |
| II Requirements | Interview notes → user stories → use cases → domain model → analysis classes → SRS |
| III Design | Architecture alternatives → component design → UI design |
| IV Implementation & Quality | Coding standards, review records, test plan and test cases |
| V Management & Evolution | Estimates, schedule, risk register, a v2.0 evolution scenario |

## 6. Student Project Parallels

Course teams should not build CareLink itself — they build a **parallel case**
with the same shape but a different domain (suggested: pet-home monitoring,
dormitory safety, shared-bicycle management, clinic queueing). The textbook's
CareLink artifacts then serve as worked references the students can compare
their own work against. This keeps the challenge honest while guaranteeing
worked answers exist for every technique.

## 7. Maintenance of This Document

- Any chapter that introduces new CareLink facts must update this file in the
  same commit (appendix A collects the final artifacts).
- Fact discipline: the elder is called "Grandma Lin" in narratives; the family
  app user is her son "Wei"; the care-center operator is "Operator Yan".
  Keep names, numbers, and thresholds consistent across all chapters.
