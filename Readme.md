# 🚀 Automation Framework — Playwright

![CI](https://github.com/PrasadHelaskar/automation-framework-playwright/actions/workflows/regression-evening-run.yml/badge.svg)
![Playwright Framework](https://img.shields.io/badge/Playwright-Framework-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
---

## 📌 About

A scalable, maintainable, and modular **Playwright Automation Framework** built using **Python + Pytest** for modern Web UI end-to-end testing.

This repository represents a **production-style automation framework**, developed incrementally using a **continuous, phased engineering approach** rather than a one-time demo implementation.

The framework is designed with long-term maintainability, clarity, and scalability in mind — closely mirroring how automation systems evolve in real-world QA teams.

---

## 🧠 Design Philosophy (Why This Framework Looks This Way)

This is my first Playwright automation framework, built after ~2.4 years of experience designing and maintaining Selenium-based test frameworks.

Rather than focusing only on Playwright syntax, I intentionally approached this project from a framework and scalability perspective, reflecting how automation is built in real-world teams.

Key Design Choices

Framework-first structure (BasePage, utilities, fixtures, logging) to keep tests clean, consistent, and maintainable as the project scales.

Centralized locator handling to enforce consistency and simplify future refactoring, inspired by large Selenium-based automation systems.

Pytest-driven lifecycle management using fixtures and conftest.py for clean setup/teardown and extensibility.

Logging support to improve debugging and CI/CD failure analysis.

Playwright-Specific Considerations

Playwright encourages powerful, readable locators (get_by_role, get_by_test_id, etc.), which are used throughout the project.
This framework balances Playwright-native capabilities with proven automation design principles.

Future iterations will reduce unnecessary abstraction and lean further into idiomatic Playwright patterns as the framework evolves.

### Intent

This project is intentionally treated as Version 1 and represents my transition from Selenium-heavy automation to Playwright, with a focus on clarity, scalability, and long-term maintainability rather than demo-style scripts.

---

## ✨ Key Features

✔ Playwright-based UI automation using Python </br>
✔ Page Object Model (POM) architecture </br>
✔ Centralized locator management </br>
✔ Pytest fixtures and configuration </br>
✔ Reusable utilities and base classes </br>
✔ CLI-driven test execution </br>
✔ Framework designed for CI/CD readiness </br>

---

## 📁 Project Structure

```
.
├── locatores/            # Centralized UI locators
├── pages/                # Page Object Models
├── tests/                # Test cases grouped by feature
├── utils/                # Common utilities (logger, helpers, base logic)
├── conftest.py           # Pytest fixtures and setup/teardown
├── pytest.ini            # Pytest configuration & markers
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🛠 Prerequisites

* Python 3.8+
* Node.js (required for Playwright browsers)
* pip

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Run with verbose logs:

```bash
pytest -v
```

Run a specific test or folder:

```bash
pytest tests/
pytest tests/login/test_login.py
```

---

## 🔄 Continuous Development (Phased Approach)

This framework follows a **phased continuous development strategy**, ensuring that each stage delivers stable and usable automation while allowing controlled growth.

### 🟠 Phase 1 — Foundation (Current)

✔ Project structure finalized </br>
✔ Playwright + Pytest integration </br>
✔ Page Object Model (POM) </br>
✔ Centralized locator strategy </br>
✔ BasePage abstraction for UI interactions </br>
✔ Reusable utilities </br>

🎯 **Objective:** Establish a clean, maintainable automation baseline.

---

### 🔵 Phase 2 — Stabilization & Coverage (Planned)

⬜ Test data management </br>
⬜ Assertion helpers </br>
⬜ HTML / Allure reporting </br>
⬜ Enhanced logging & failure analysis </br>
⬜ Smoke vs Regression tagging </br>

🎯 **Objective:** Improve reliability, diagnostics, and test visibility.

---

### 🟢 Phase 3 — CI/CD & Scalability (Upcoming)

⬜ GitHub Actions CI pipeline </br>
⬜ Parallel execution </br>
⬜ Cross-browser execution strategy </br>
⬜ Environment-based execution (test / staging / prod) </br>

🎯 **Objective:** Make the framework CI-ready and production-scalable.

---

### 🔮 Phase 4 — Advanced Automation (Future)

⬜ Self-healing locators </br>
⬜ Flaky test detection </br>
⬜ Visual regression testing </br>
⬜ API + UI hybrid automation flows </br>

🎯 **Objective:** Transition from automation execution to automation intelligence.

---

## 🧠 Engineering Philosophy

* Built as a **living framework**, not a one-time implementation
* Each phase adds value without breaking existing tests
* Emphasis on readability, maintainability, and scalability
* Mirrors real-world SDET automation practices

---

## 📈 Framework Versioning

**Current Version:** `v1.0`

* Foundation phase completed
* Stable baseline for further enhancements

Future versions will increment as each phase is completed.

---

## 🤝 Contributions

Suggestions, issues, and improvements are welcome.

This framework is intentionally designed to evolve — contributions that align with the phased roadmap are encouraged.

---

## 👤 Author

Prasad Helaskar
Senior QA / SDET (Automation) </br>
🔗 GitHub: https://github.com/PrasadHelaskar

> 📢 *This repository reflects how real automation frameworks are built, evolved, and maintained in professional QA organizations.*
