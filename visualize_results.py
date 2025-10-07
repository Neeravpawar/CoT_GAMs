import json
import os
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ensure non-interactive backend
import matplotlib
matplotlib.use("Agg")

sns.set(style="whitegrid")

# === Load Corpus ===
corpus_path = Path("final_verified_corpus.json")
if not corpus_path.exists():
    print("Error: final_verified_corpus.json not found.")
    exit(1)

with open(corpus_path, "r") as f:
    corpus = json.load(f)

print(f"Loaded {len(corpus)} problems from {corpus_path.name}")

# === Convert Corpus to DataFrame ===
records = []
for p in corpus:
    verification = p.get("verification", {})
    records.append({
        "id": p["id"],
        "problem_type": p["problem_type"],
        "static_valid": verification.get("static_valid", False),
        "solver_success": verification.get("solver_success", False),
        "fully_verified": verification.get("fully_verified", False),
        "objective_value": verification.get("objective_value", None),
        "reasoning_length": len(p.get("reasoning", "")),
    })

df = pd.DataFrame(records)
os.makedirs("results", exist_ok=True)

# === 1. Problem Type Distribution ===
plt.figure(figsize=(8, 5))
sns.countplot(
    x="problem_type", 
    data=df, 
    palette="Set2", 
    order=sorted(df["problem_type"].unique())
)
plt.title("Problem Type Distribution")
plt.xlabel("Problem Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("results/fig_problem_distribution.png")
plt.close()

# === 2. Verification Success Rates ===
stats = {
    "static_valid": df["static_valid"].mean() * 100,
    "solver_success": df["solver_success"].mean() * 100,
    "fully_verified": df["fully_verified"].mean() * 100
}

plt.figure(figsize=(6, 4))
sns.barplot(x=list(stats.keys()), y=list(stats.values()), palette="Set1")
plt.title("Verification Success Rates (%)")
plt.ylabel("Percentage (%)")
plt.ylim(0, 105)
plt.tight_layout()
plt.savefig("results/fig_verification_success.png")
plt.close()

# === 3. Reasoning Length by Problem Type ===
plt.figure(figsize=(8, 5))
sns.boxplot(
    x="problem_type", 
    y="reasoning_length", 
    data=df, 
    palette="Set3",
    order=sorted(df["problem_type"].unique())
)
plt.title("Reasoning Length Distribution by Problem Type")
plt.xlabel("Problem Type")
plt.ylabel("Reasoning Length (characters)")
plt.tight_layout()
plt.savefig("results/fig_reasoning_length.png")
plt.close()

# === 4. Scatter Plot: Reasoning Length vs Objective Value ===
plt.figure(figsize=(8, 6))
scatter_df = df.dropna(subset=["objective_value"])
scatter_df = scatter_df[scatter_df["objective_value"].apply(lambda x: isinstance(x, (int, float)))]

if not scatter_df.empty:
    sns.scatterplot(
        data=scatter_df,
        x="reasoning_length",
        y="objective_value",
        hue="problem_type",
        palette="husl",
        s=80,
        alpha=0.8
    )
    plt.title("Reasoning Length vs Objective Value by Problem Type")
    plt.xlabel("Reasoning Length (characters)")
    plt.ylabel("Objective Value")
    plt.legend(title="Problem Type", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig("results/fig_reasoning_vs_objective_scatter.png")
    plt.close()

# === 5. Correlation Heatmap ===
numeric_df = df[["reasoning_length", "objective_value"]].copy()
numeric_df["objective_value"] = pd.to_numeric(numeric_df["objective_value"], errors="coerce")
corr = numeric_df.corr()

plt.figure(figsize=(5, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap: Reasoning vs Objective")
plt.tight_layout()
plt.savefig("results/fig_success_heatmap.png")
plt.close()

print("\nSaved visualizations:")
print(" - fig_problem_distribution.png")
print(" - fig_verification_success.png")
print(" - fig_reasoning_length.png")
print(" - fig_reasoning_vs_objective_scatter.png")
print(" - fig_success_heatmap.png")