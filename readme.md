# CLAUSEBENCH: Enhancing Software License Analysis with Clause-Level Benchmarking

Welcome to the **CLAUSEBENCH** repository! This project introduces a comprehensive benchmarking framework for fine-grained clause-level analysis of open-source software (OSS) licenses. Our approach leverages state-of-the-art large language models (LLMs) to detect and interpret license clauses, offering enhanced accuracy for OSS compliance.

## Research Questions (RQs)

The main objectives of this study are captured in the following research questions and their corresponding solutions:

- **RQ1: Dataset Validity Verification**  
  *Solution*: To ensure high quality, accuracy, and consistency of the dataset, we constructed a fine-grained benchmark dataset with over 50 widely used open-source licenses annotated with 14 distinct clause categories. The dataset's validity was verified using inter-annotator agreement metrics and Cohen’s Kappa coefficient. We refined the dataset through a combination of LLM-based annotations and manual checks, achieving an inter-annotator agreement rate of 98.08% and a Cohen’s Kappa score of 0.896, indicating strong consistency.

- **RQ2: Accuracy of LLM Clause Recognition**  
  *Solution*: We evaluated the performance of multiple LLMs, including DeepSeek, Mistral-large, Qianwen, and Mixtral, on clause recognition tasks using our benchmark dataset. The models were assessed on their ability to accurately recognize and classify license clauses. The results showed that models like DeepSeek demonstrated the highest accuracy (up to 99.83%) with minimal hallucinations, confirming the effectiveness of our dataset and methodology for supporting LLM-based license analysis.

- **RQ3: Performance Improvement of CLAUSEBENCH**  
  *Solution*: CLAUSEBENCH significantly improved OSS license clause analysis by adopting a clause-level approach over traditional full-document scanning. This method enabled models to focus on individual clause-level features, resulting in enhanced precision and reduced hallucination rates. The clause-level approach improved model accuracy by approximately 50% in some cases and minimized hallucination rates to below 1% for certain models, demonstrating its effectiveness in refining LLM performance.

## Repository Structure

```
CLAUSEBENCH/
│
├── git_license/             # License raw data
│
├── license_extract/         # Scripts and extraction results for license clauses
│
├── license_info/            # License matching patterns, detailed term explanations, and SPDX classifications
│
├── license_json/            # Processed license text and related information
│
├── license_llm/
│   ├── evaluation/          # Scripts and results for clause-level benchmarking
│   ├── prompt/              # Prompt engineering files, including four types of prompts, test scripts, and results
│   └── term/                # Scripts and results for model-assisted annotation datasets
│
├── license_pre/             # License data preprocessing
│
├── license_scan/            # License deduplication and scan results
│
├── fine_grained.json        # Clause-level annotated dataset
└── README.md                # Project overview and usage information
```

## Key Features

- **Fine-Grained Benchmark Dataset**: Provides a comprehensive, clause-level annotated dataset for enhanced model training and evaluation.
- **Clause-Level Analysis**: Conducts detailed clause-specific recognition for more precise OSS compliance checks.
- **Multiple LLMs Supported**: Integrates with DeepSeek, Mistral-large, Qianwen, and Mixtral for comprehensive evaluation.
- **Prompt Engineering**: Here's the updated **Key Features** section with the four prompt engineering strategies and their respective hyperlinks:

---

## Key Features

- **Fine-Grained Benchmark Dataset**: Provides a comprehensive, clause-level annotated dataset for enhanced model training and evaluation.
- **Clause-Level Analysis**: Conducts detailed clause-specific recognition for more precise OSS compliance checks.
- **Multiple LLMs Supported**: Integrates with DeepSeek, Mistral-large, Qianwen, and Mixtral for comprehensive evaluation.
- **Prompt Engineering Strategies**:
  - [Basic Prompt](license_llm/prompt/prompt-basic.md)
  - [Few-Shot Prompt](license_llm/prompt/prompt-few.md)
  - [Contextual Prompt](license_llm/prompt/prompt-context.md)
  - [Full License Prompt](license_llm/prompt/prompt-full.md)


