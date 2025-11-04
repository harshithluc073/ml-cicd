# ML CI/CD Pipeline using GitHub Actions

This project implements a fully automated **Continuous Integration and Continuous Deployment (CI/CD)** pipeline tailored for **machine learning workflows**.
It uses **GitHub Actions** to automate every stage of the ML lifecycle — from code validation and data integrity checks to model training, evaluation, versioning, and release generation.

---

## **Key Features**

* **Automated CI/CD Workflow**

  * Runs on every push or pull request.
  * Includes linting (`flake8`, `black`, `ruff`), testing (`pytest`), and model training.
* **End-to-End ML Automation**

  * Validates dataset structure and quality.
  * Trains and evaluates ML models automatically.
* **Performance-Gated Model Promotion**

  * New models are only released if they outperform the previous version.
* **Artifact Management**

  * Automatically uploads the trained model and performance report as build artifacts.
* **Automated GitHub Releases**

  * Generates versioned releases with attached model files and reports.
* **Performance Dashboard**

  * Tracks historical accuracy and version data in a simple Markdown dashboard.
* **Containerized Environment**

  * Docker support ensures reproducibility across systems and CI runners.

---

## **Pipeline Overview**

### **1. Trigger**

The workflow runs automatically on:

* Every push to the `main` branch
* Every pull request targeting `main`

### **2. Stages**

| Stage                | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| **Linting**          | Runs `flake8`, `black`, and `ruff` to enforce clean code.                   |
| **Testing**          | Executes `pytest` unit tests to verify logic and data validation.           |
| **Training**         | Trains a model using dummy or uploaded data.                                |
| **Evaluation**       | Compares accuracy against previous model performance.                       |
| **Artifact Upload**  | Uploads the trained model and performance report.                           |
| **Release Creation** | Creates a GitHub release with model artifacts if accuracy improved.         |
| **Dashboard Update** | Appends the latest accuracy and version info to `dashboard/performance.md`. |

---

## **Repository Structure**

```
ml-cicd/
├── .github/
│   └── workflows/
│       └── ci.yml                # Main CI/CD workflow
├── src/
│   ├── data_validation.py        # Checks data integrity and schema
│   ├── train.py                  # Handles model training and saving
│   ├── evaluate.py               # Evaluates model performance and compares with previous versions
│   └── dashboard.py              # Updates Markdown performance dashboard
├── tests/
│   └── test_pipeline.py          # Unit tests for validation and core logic
├── models/                       # Stored trained models (ignored by Git)
├── reports/                      # Stores performance reports
├── dashboard/                    # Performance tracking file
├── Dockerfile                    # Reproducible container for pipeline
├── .dockerignore                 # Excludes unnecessary files from Docker image
├── requirements.txt              # Python dependencies
├── .flake8                       # Lint configuration
├── .pre-commit-config.yaml       # Pre-commit hooks for lint/test
├── README.md                     # Project documentation
└── .gitignore                    # Ignored files
```

---

## **Getting Started**

### **1. Clone the Repository**

```bash
git clone https://github.com/<your-username>/ml-cicd.git
cd ml-cicd
```

### **2. Create and Activate Virtual Environment**

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # For PowerShell
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run Linting and Tests Locally**

```bash
flake8 src
pytest
```

### **5. Run the Pipeline via Docker**

```bash
docker build -t ml-cicd-pipeline .
docker run --rm ml-cicd-pipeline
```

---

## **GitHub Actions Workflow**

The workflow file is located at:

```
.github/workflows/ci.yml
```

It executes the entire ML pipeline in the following order:

1. Code Quality Checks
2. Unit Tests
3. Data Validation
4. Model Training
5. Model Evaluation
6. Model Version Comparison
7. Artifact Upload & Release
8. Dashboard Update

You can view detailed logs under your repo’s **Actions** tab on GitHub.

---

## **Pre-Commit Hooks**

Before each commit, pre-commit automatically checks:

* Formatting (`black`)
* Linting (`flake8`, `ruff`)
* Code style compliance

To install hooks:

```bash
pre-commit install
```

Run manually anytime:

```bash
pre-commit run --all-files
```

---

## **Example Output**

When the pipeline runs successfully, you’ll see logs like:

```
✅ Model trained successfully.
📁 Saved model at: models/model_v1.joblib
Model evaluation metrics: {'accuracy': 0.95}
🎉 Release created: v5
```

---

## **Future Enhancements**

* Add cloud artifact upload (AWS S3 / GCS)
* Integrate model registry (MLflow / DVC)
* Include experiment tracking and visualization
* Expand dataset handling and retraining triggers

---

## **License**

This project is licensed under the MIT License — feel free to modify and use it for your own MLOps workflows.
