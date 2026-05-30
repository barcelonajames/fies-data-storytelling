# Filipino Family Income and Expenditure Survey
### Uncovering Stories from Data — Group Data Storytelling Project

A collaborative data storytelling project analyzing the 2021 Philippine Family Income and Expenditure Survey (FIES) dataset. Six analytical themes were developed across five team members, pairing Python visualizations with narrative insights presented as a structured slide deck.

---

## The Project

Rather than a single pipeline, this project is a **data storytelling exercise** — each theme poses a real question about Philippine household economics, answers it with code and charts, and frames the finding as a human-readable insight. The presentation format mirrors how data analysis is communicated to non-technical stakeholders in professional settings.

## Project Deliverables

[View Presentation (Google Slides)](https://docs.google.com/presentation/d/1o4Nu46gm-Edse7zSldJBIzAIdaftHODWul7Sf_wc7U8/edit?usp=drive_link)  
[View Analysis Notebook (Google Drive)](https://drive.google.com/file/d/1dTrizfzilhBTgG0HC3Ojg0oa-1nCicDk/view?usp=sharing)

---

## Team

| Member | Theme |
|---|---|
| James | Urban vs. Rural Differences · Clothing Expenditure |
| Euie | Impact of Education on Income · Tobacco & Alcohol |
| John | Household Size and Spending · Tenure Status |
| Matt | Gender Differences in Household Economics · Vehicle Ownership |
| JB | Regional Spending Patterns · Special Occasions Expenditure |

---

## Dataset

**Source:** [Philippine Statistics Authority — Family Income and Expenditure Survey (FIES)](https://psa.gov.ph/statistics/income-expenditure/fies)

| Detail | Value |
|---|---|
| Rows | 41,544 households |
| Columns | 64 features |
| Coverage | All regions of the Philippines |

> **Note:** The dataset is not included in this repository. Download the FIES 2021 dataset from the PSA website and save it as `Family_Income_and_Expenditure_edited.csv` in the project root.

---

## Analysis Themes

**Theme 1 — Urban vs. Rural Differences** *(James)*
> NCR shows a consumption-driven pattern where low-income households overspend relative to income. Eastern Visayas reflects restrained spending — households consistently spend below income, especially at higher brackets.

**Theme 2 — Impact of Education on Income** *(Euie)*
> Household heads with higher education levels earn significantly more. Education is the strongest individual-level predictor of income mobility in the dataset.

**Theme 3 — Household Size and Spending** *(John)*
> Large families spend more on food and education in absolute terms, but the proportion of income allocated to these categories does not increase significantly with family size — expenses are shared across members.

**Theme 4 — Gender Differences in Household Economics** *(Matt)*
> Female-headed households allocate more to housing, medical care, education, and communication. Male-headed households spend more on staple foods, agricultural expenses, tobacco, and alcohol.

**Theme 5 — Regional Spending Patterns** *(JB)*
> Household spending is highest in NCR across all three categories (food, education, transport). Spending is lowest in rural regions like ARMM and Northern Mindanao.

**Theme 6 — Impact of Lifestyle on Household Cost of Living** *(All members)*
- **Special Occasions** — spending is highly concentrated near zero; weak relationship with cost of living
- **Vehicle Ownership** — rises sharply with income; rich households average ~2 vehicles
- **Tenure Status** — housing security improves with income; higher brackets more likely to own outright
- **Clothing** — middle brackets peak at ~2.5–2.6% of expenditure; rich spend more in absolute terms but proportionally less
- **Tobacco & Alcohol** — upper-middle spends most; tobacco more accessible than alcohol due to Sin Tax (RA 10351) pricing

---

## Repository Structure

```
fies-data-storytelling/
├── slides/
│   └── fies_storytelling.pptx     ← Full presentation deck (44 slides)
├── analysis_snippets.py            ← All analysis code, organized by theme
├── requirements.txt                ← Python dependencies
├── .gitignore                      ← Dataset excluded
├── LICENSE                         ← MIT
└── README.md
```

---

## How to Run the Code

### 1. Clone the repository
```bash
git clone https://github.com/barcelonajames/fies-data-storytelling.git
cd fies-data-storytelling
```

### 2. Set up the environment
```bash
conda activate fies-analysis
pip install -r requirements.txt
```

### 3. Add the dataset
Download from the [PSA website](https://psa.gov.ph/statistics/income-expenditure/fies) and place in the project root:
```
fies-data-storytelling/
└── Family_Income_and_Expenditure_edited.csv   ← place here
```

### 4. Run the analysis
```bash
python analysis_snippets.py
```
Or open individual sections in a Jupyter notebook — each theme is self-contained with clear section headers.

---

## Tools & Libraries

| Category | Libraries |
|---|---|
| Data handling | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Environment | Python 3.11, conda |

---

## Context

Built as part of the **Uplift Code Camp Python for Data and AI Bootcamp** (2026) — Activity 2: Uncovering Stories from Data. This project emphasizes communicating analytical findings to a non-technical audience through structured narrative and visualization, complementing the technical ML pipeline work in the other bootcamp projects.

---

*James Aleister Barcelona — Visual Designer & Data Analyst | Davao, Philippines*
