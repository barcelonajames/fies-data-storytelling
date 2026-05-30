"""
Filipino Family Income and Expenditure Survey (FIES)
Uncovering Stories from Data — Analysis Code

Extracted from group presentation slides.
Team: Euie, James, JB, John, Matt
Bootcamp: Uplift Code Camp — Python for Data and AI (2026)

Dataset: Family Income and Expenditure Survey (FIES) — Philippines (PSA)
Source: https://psa.gov.ph/statistics/income-expenditure/fies

Usage:
    Place the FIES CSV in the project root as:
        Family_Income_and_Expenditure_edited.csv
    Then run sections individually or in sequence.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load Dataset ──────────────────────────────────────────────────────────────

df = pd.read_csv('Family_Income_and_Expenditure_edited.csv')
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])


# =============================================================================
# THEME 1: Urban vs. Rural Differences
# By: James
# Question: How do household incomes and expenditures differ between
#           urban and rural households?
# Insight: NCR shows a consumption-driven pattern; Eastern Visayas reflects
#          restrained spending and higher savings margins.
# =============================================================================

# -- Table: Urban (NCR) average income and expenditure by bracket --
bins = [0, 132_000, 264_000, 528_000, 924_000, 1_572_000, 2_628_000, float('inf')]
labels = ['Poor', 'Low Income', 'Lower Middle', 'Middle Income',
          'Upper Middle', 'Upper Middle not Rich', 'Rich']

urban_df = df[df['Region'] == 'NCR']
urban_df['Income Bracket'] = pd.cut(urban_df['Annual Household Income'],
                                     bins=bins, labels=labels)
summary_df = (
    urban_df.groupby('Income Bracket')[['Annual Household Income', 'Total Expenditure']]
    .mean()
    .round(2)
    .reset_index()
)
print(summary_df)

# -- Scatter: Urban (NCR) Income vs. Expenditure --
urban_df = df[df['Region'] == 'NCR']
plt.scatter(urban_df['Annual Household Income'],
            urban_df['Total Expenditure'],
            alpha=0.6)
plt.xlabel('Annual Household Income')
plt.ylabel('Total Expenditure')
plt.title('Urban - NCR')
plt.show()


# =============================================================================
# THEME 2: Impact of Education on Income
# By: Euie
# Question: Do household heads with higher education levels earn more?
# Insight: Higher education strongly linked to better income opportunities.
# =============================================================================

# -- Top 5 and Bottom 5 education levels by average monthly income --
top5_high = (df[['Household Head Highest Grade Completed', 'Monthly Income']]
             .sort_values(by='Monthly Income', ascending=False)
             .head(5))

top5_high_mean_income = (
    df[df['Household Head Highest Grade Completed']
       .isin(top5_high['Household Head Highest Grade Completed'])]
    .groupby('Household Head Highest Grade Completed')['Monthly Income']
    .mean()
    .round(2)
)

bottom5 = (df[['Household Head Highest Grade Completed', 'Monthly Income']]
           .sort_values(by='Monthly Income', ascending=False)
           .tail(5))

bottom5_low_mean_income = (
    df[df['Household Head Highest Grade Completed']
       .isin(bottom5['Household Head Highest Grade Completed'])]
    .groupby('Household Head Highest Grade Completed')['Monthly Income']
    .mean()
    .round(2)
)

high = top5_high_mean_income.sort_values(ascending=False)
low = bottom5_low_mean_income.sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(16.6, 6))
y_high = np.arange(len(high.values))
y_low = np.arange(len(low.values)) + len(high.values) + 1

ax.barh(y_high, high.values, color='green', label='Top 4 Average Income')
ax.barh(y_low, low.values, color='gray', label='Bottom 4 Average Income')
ax.set_yticks(list(y_high) + list(y_low))
ax.set_yticklabels(list(high.index) + list(low.index))
ax.set_xlabel('Average Monthly Income')
ax.set_title('Top 4 vs Bottom 4 Education Levels and Average Monthly Incomes')
ax.invert_yaxis()
ax.legend()
plt.tight_layout()
plt.show()


# =============================================================================
# THEME 3: Household Size and Spending
# By: John
# Question: Do larger families spend more on food or education?
# Insight: Large families spend more overall, but the proportion of income
#          spent does not increase significantly with family size.
# =============================================================================

# -- Categorize family size --
df['Family Size Category'] = pd.cut(
    df['Total Number of Family members'],
    bins=[0, 4, 10, 30],
    labels=['Small', 'Medium', 'Large']
)

# -- Bar charts: Monthly food and education expenditure by family size --
filt_food = df['Total Food Expenditure'] / 12
filt_edu = df['Education Expenditure'] / 12

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.barplot(data=df, x='Family Size Category', y=filt_food, ax=axes[0])
axes[0].set_ylabel('Monthly Food Expenditure')
axes[0].set_xlabel('Family Size Category')
axes[0].set_title('Average Monthly Food Expenditure by Family Size')

sns.barplot(data=df, x='Family Size Category', y=filt_edu, ax=axes[1])
axes[1].set_ylabel('Monthly Education Expenditure')
axes[1].set_xlabel('Family Size Category')
axes[1].set_title('Average Monthly Education Expenditure by Family Size')

plt.show()

# -- Regression plots: Expense ratio vs. family size --
df['food expense ratio'] = ((df['Total Food Expenditure'] / 12) / df['Monthly Income']).round(2)
df['education expense ratio'] = ((df['Education Expenditure'] / 12) / df['Monthly Income']).round(2)

sns.regplot(data=df, x='Total Number of Family members', y='food expense ratio')
plt.title('Correlation Between Household Size and Food Expense Ratio')
plt.show()

sns.regplot(data=df, x='Total Number of Family members', y='education expense ratio')
plt.title('Correlation Between Household Size and Education Expense Ratio')
plt.show()


# =============================================================================
# THEME 4: Gender Differences in Household Economics
# By: Matt
# Question: Is there a difference in spending patterns based on the sex
#           of the household head?
# Insight: Female-headed households spend more on family/welfare categories;
#          male-headed households spend more on staples and vices.
# =============================================================================

exp_cols = [
    'Bread and Cereals Expenditure', 'Total Rice Expenditure', 'Meat Expenditure',
    'Total Fish and  marine products Expenditure', 'Fruit Expenditure',
    'Vegetables Expenditure', 'Restaurant and hotels Expenditure',
    'Alcoholic Beverages Expenditure', 'Tobacco Expenditure',
    'Clothing, Footwear and Other Wear Expenditure', 'Housing and water Expenditure',
    'Medical Care Expenditure', 'Transportation Expenditure', 'Communication Expenditure',
    'Education Expenditure', 'Miscellaneous Goods and Services Expenditure',
    'Special Occasions Expenditure', 'Crop Farming and Gardening expenses'
]

avg_exp = df.groupby('Household Head Sex')[exp_cols].mean().T
avg_exp['Total'] = avg_exp.mean(axis=1)
avg_exp = avg_exp.sort_values('Total', ascending=True)
avg_exp = avg_exp.drop(columns='Total')

plt.figure(figsize=(10, 7))
y = range(len(avg_exp))
plt.barh(y, avg_exp['Female'], height=0.4, label='Female')
plt.barh([i + 0.4 for i in y], avg_exp['Male'], height=0.4, label='Male')
plt.yticks([i + 0.2 for i in y], avg_exp.index)
plt.xlabel('Average Spending')
plt.ylabel('Expenditure Category')
plt.title('Average Expenditure by Category and Gender')
plt.legend(title='Household Head Sex')
plt.show()


# =============================================================================
# THEME 5: Regional Spending Patterns
# By: JB
# Question: Which regions spend the most on education, transportation, and food?
# Insight: Spending highest in urban regions (NCR); lowest in rural areas
#          like ARMM and Northern Mindanao.
# =============================================================================

regional_spending = df.groupby('Region')[
    ['Education Expenditure', 'Transportation Expenditure', 'Total Food Expenditure']
].mean().reset_index()

regional_spending = regional_spending.sort_values('Total Food Expenditure', ascending=False)
df_regional_spending = regional_spending.melt(
    id_vars='Region', var_name='Category', value_name='Expenditure'
)

plt.figure(figsize=(10, 8))
sns.barplot(data=df_regional_spending, x='Expenditure', y='Region', hue='Category')
plt.title('Average Household Spending by Region')
plt.xlabel('Average Expenditure')
plt.ylabel('Region')
plt.legend(title='Category')
plt.show()


# =============================================================================
# THEME 6: Personal Exploration — Impact of Lifestyle on Cost of Living
# =============================================================================

# -- 6a. Special Occasions Expenditure (by JB) --
# Insight: Most households spend very little; relationship with cost of
#          living is weak with some high-spend outliers.

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Special Occasions Expenditure', y='Total Expenditure')
plt.title('Impact of Special Occasions Expenditure on Household Cost of Living')
plt.xlabel('Annual Special Occasions Expenditure')
plt.ylabel('Annual Total Household Expenditure')
plt.show()


# -- 6b. Vehicle Ownership by Social Class (by Matt) --
# Insight: Vehicle ownership rises sharply with income; rich households
#          average ~2 vehicles. Poor households rarely own any.

bins = [0, 132000, 264000, 528000, 924000, 1572000, 2628000, 9999999999999]
labels = ['Poor', 'Low Income', 'Lower Middle', 'Middle Income',
          'Upper Middle', 'Upper Middle not Rich', 'Rich']

df['Social Class'] = pd.cut(df['Total Household Income'], bins=bins, labels=labels)
car_by_class = (df.groupby('Social Class', observed=False)['Number of Car, Jeep, Van']
                .mean()
                .reset_index()
                .sort_values('Number of Car, Jeep, Van', ascending=False))

sns.barplot(data=car_by_class, y='Social Class', x='Number of Car, Jeep, Van',
            order=car_by_class['Social Class'])
plt.title('Average Vehicle Ownership by Social Class')
plt.xlabel('Average Number of Cars/Jeep/Vans')
plt.ylabel('Social Class')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()


# -- 6c. Tenure Status by Income Bracket (by John) --
# Insight: Housing security improves with income. Higher-income households
#          more likely to fully own their homes.

df = df[df['Tenure Status'] != 'Not Applicable']
tenure_map = {
    'Own or owner-like possession of house and lot': 'Full Ownership',
    'Rent-free house and lot with consent of owner': 'Allowed to Stay',
    'Own house, rent-free lot with consent of owner': 'Landowner Permitted',
    'Own house, rent lot': 'Legally Renting Lot',
    'Rent house/room including lot': 'Formal Rental',
    'Own house, rent-free lot without consent of owner': 'Own House, Unauthorized Lot',
    'Rent-free house and lot without consent of owner': 'Informal Settlers'
}
df['Clear Tenure Status'] = df['Tenure Status'].map(tenure_map)

income_order = ['Poor', 'Low-income', 'Lower Middle Income', 'Middle Income',
                'Upper Middle Income', 'Upper Middle not Rich', 'Rich']
legend_order = ['Full Ownership', 'Formal Rental', 'Allowed to Stay',
                'Landowner Permitted', 'Legally Renting Lot',
                'Own House, Unauthorized Lot', 'Informal Settlers']

tenure_income = pd.crosstab(df['Income Brackets'], df['Clear Tenure Status'])
tenure_income = tenure_income.div(tenure_income.sum(axis=1), axis=0)
tenure_income = tenure_income[legend_order]
tenure_income.loc[income_order].plot(kind='barh', stacked=True, figsize=(15, 6))
plt.legend(title='Tenure Status', bbox_to_anchor=(1, 1), loc='upper left')
plt.title('Tenure Status Distribution by Income Bracket')
plt.ylabel('Income Brackets')
plt.xlabel('Proportion of Households')
plt.show()


# -- 6d. Clothing Expenditure by Income Bracket (by James) --
# Insight: Middle brackets peak on clothing as share of expenditure (~2.5-2.6%).
#          Rich households spend more in absolute terms but proportionally less.

bins = [0, 132_000, 264_000, 528_000, 924_000, 1_572_000, 2_628_000, float('inf')]
labels = ['Poor', 'Low Income', 'Lower Middle', 'Middle Income',
          'Upper Middle', 'Upper Middle not Rich', 'Rich']

clothing_df = df.copy()
clothing_df['Income Brackets'] = pd.cut(
    clothing_df['Annual Household Income'], bins=bins, labels=labels
)

summary_df = (
    clothing_df.groupby('Income Brackets')[
        ['Annual Household Income', 'Total Expenditure',
         'Clothing, Footwear and Other Wear Expenditure']
    ]
    .mean()
    .round(2)
    .reset_index()
)
print(summary_df)

clothing_summary = (
    df.groupby('Income Brackets')['Clothing, Footwear and Other Wear Expenditure']
    .mean()
    .round(2)
    .reset_index()
)

plt.figure(figsize=(10, 6))
plt.barh(clothing_summary['Income Brackets'],
         clothing_summary['Clothing, Footwear and Other Wear Expenditure'],
         color='red')
plt.xlabel('Average Clothing, Footwear and Other Wear Expenditure (Annual)')
plt.ylabel('Income Brackets')
plt.title('Clothing Expenditure by Income Bracket')
plt.tight_layout()
plt.show()


# -- 6e. Tobacco and Alcohol Expenditure by Social Class (by Euie) --
# Insight: Upper-middle spends most; poor spend least. Tobacco more accessible
#          than alcohol due to price and packaging. Sin Tax (RA 10351) is a
#          key factor limiting alcohol access in lower brackets.

bins = [0, 132_000, 264_000, 528_000, 924_000, 1_572_000, 2_628_000, float('inf')]
labels = ['Poor', 'Low Income', 'Lower Middle', 'Middle Income',
          'Upper Middle', 'Upper Middle not Rich', 'Rich']

vices_df = df.copy()
vices_df['Income Bracket'] = pd.cut(
    vices_df['Annual Household Income'], bins=bins, labels=labels
)

summary_df = (
    vices_df.groupby('Income Bracket')[
        ['Tobacco Expenditure', 'Alcoholic Beverages Expenditure']
    ]
    .mean()
    .round(2)
    .reset_index()
)

summary_df['Income Bracket'] = pd.Categorical(
    summary_df['Income Bracket'], categories=labels, ordered=True
)
summary_df = summary_df.sort_values('Income Bracket')

plot_df = summary_df.melt(
    id_vars='Income Bracket',
    value_vars=['Tobacco Expenditure', 'Alcoholic Beverages Expenditure'],
    var_name='Expenditure Type',
    value_name='Average Expenditure'
)

plt.figure(figsize=(15, 6))
sns.barplot(data=plot_df, x='Income Bracket', y='Average Expenditure',
            hue='Expenditure Type')
plt.title('Average Tobacco and Alcohol Expenditures of Social Classes', fontsize=16)
plt.xlabel('Social Classes', fontsize=15)
plt.ylabel('Average Expenditure of Alcohol and Tobacco', fontsize=13.5)
plt.xticks(rotation=30)
plt.grid(visible=True, axis='y', linestyle='--', color='black', alpha=0.4)
plt.tight_layout()
plt.show()
