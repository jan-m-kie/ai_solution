# 🤖 AI Solution Stack with CrewAI

This repository defines a **cloud-native AI automation stack** using [CrewAI](https://docs.crewai.com/). It leverages multiple agents to handle development, testing, security auditing, and DevOps automation — fully orchestrated through GitHub Actions, with no local execution required.

---

## 🚀 Project Structure

- `crewai.yaml` – Defines CrewAI agents, tasks, memory, and LLMs.
- `pyproject.toml` – Minimal config required for CrewAI CLI.
- `.env.example` – Placeholder for API keys and service URLs.
- `.github/workflows/run-crewai.yaml` – GitHub Actions workflow to run CrewAI in the cloud.

---

## 🧠 Agents & Responsibilities

| Agent         | Role                | Description                                                       | Tools                       | Expected Input                                      | Output                                                  |
|---------------|---------------------|-------------------------------------------------------------------|-----------------------------|----------------------------------------------------|----------------------------------------------------------|
| `DevAgent`    | Code Generator       | Writes application code based on task prompts                    | `codeium`, `gpt-4o`         | Description of the service to build                 | Python scripts, app code, logic                          |
| `TestAgent`   | Quality Assurance    | Develops tests for generated code                                | `testim`                    | Source code or spec                                 | Unit/integration test scripts                            |
| `SecAgent`    | Security Auditor     | Audits the code for vulnerabilities and recommends fixes         | `synk`                      | Application code                                    | Security report, CVE findings, suggestions               |
| `DevOpsAgent` | Infra Automation     | Builds infrastructure-as-code for deployment (K8s, Terraform)    | `KubeAI`, `TerraformAI`     | Codebase or system requirements                     | YAML manifests, `.tf` files for infrastructure setup     |

---

## 💾 Memory & LLMs

- **Memory:**
  - `qdrant` (vector store) — configurable via API key + URL
  - `chromadb` (optional)
- **LLMs:**
  - `openai` — uses GPT-4o via API key

---

## 🔑 Environment Configuration

Copy `.env.example` to `.env` and fill in your secrets:

```env
OPENAI_API_KEY=your-key-here
QDRANT_API_KEY=your-key-here
QDRANT_URL=https://your-qdrant-instance
CHROMADB_URL=https://your-chromadb-instance
```

Secrets must also be added to **GitHub > Repo Settings > Secrets and variables** for workflows to function.

---

## 🧪 How to Use (No Local Scripts)

1. Push any changes to `master`
2. Visit the **Actions** tab in GitHub
3. Select **“CrewAI Automation”**
4. Click **“Run workflow”**

The agents will run their tasks directly in the cloud.

---

## 🌱 Roadmap Ideas

- [ ] Slack or Discord notification integration
- [ ] Deploy CrewAI outputs with auto `kubectl` or `terraform apply`
- [ ] UI dashboard for triggering agent tasks
- [ ] Auto versioning and artifact upload

---

## 🧩 Workflow Structure
This project separates workflows into two categories:

**1. full-automation.yaml (Generic)**
Location: .github/workflows/full-automation.yaml

Runs when: Changes occur in crewai.yaml, src/**, or terraform/**

Purpose: Runs CrewAI to generate/update Terraform infrastructure as code.

Use case: Shared automation across all apps; no app-specific logic here.

**2. deploy-<app>.yaml (Per App)**
Location: .github/workflows/deploy-predictive-maintenance.yaml (example)

Runs when: Changes occur in app/**, terraform/**, or the workflow file itself

Purpose: Deploys a specific app (e.g., Predictive Maintenance) to Kubernetes using Terraform + Docker.

Use case: Isolated deployments with app-specific steps.



## 🛡 Disclaimer

This project is for experimentation and prototyping. Outputs from AI agents should be reviewed before use in production environments.

---
