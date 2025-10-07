import json
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean
import os

# Use non-interactive backend to avoid hanging on plt.show()
import matplotlib
matplotlib.use("Agg")

sns.set(style="whitegrid")

# --- Load corpus ---
corpus_path = Path("final_verified_corpus.json")

if not corpus_path.exists():
    print("Error: final_verified_corpus.json not found. Run main.py first.")
    exit(1)

with open(corpus_path, "r") as f:
    corpus = json.load(f)

print(f"Loaded {len(corpus)} problems from {corpus_path.name}")

# --- Convert to DataFrame ---
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

# --- Corpus Summary ---
print("\n=== CORPUS SUMMARY ===")
print(df["problem_type"].value_counts())

# --- Verification Statistics ---
stats = {
    "static_valid": df["static_valid"].mean() * 100,
    "solver_success": df["solver_success"].mean() * 100,
    "fully_verified": df["fully_verified"].mean() * 100
}
print("\n=== VERIFICATION STATISTICS ===")
print(pd.Series(stats).round(1))
print(f"\nAverage reasoning length: {df['reasoning_length'].mean():.2f} characters")

# --- Create results directory ---
os.makedirs("results", exist_ok=True)

# --- Plot 1: Problem Type Distribution ---
plt.figure(figsize=(8, 5))
sns.countplot(x="problem_type", data=df, hue="problem_type", legend=False, palette="Set2",
              order=sorted(df["problem_type"].unique()))
plt.title("Problem Type Distribution")
plt.xlabel("Problem Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("results/problem_type_distribution.png")
plt.close()

# --- Plot 2: Verification Success Rates ---
plt.figure(figsize=(6, 4))
sns.barplot(x=list(stats.keys()), y=list(stats.values()), palette="Set1")
plt.title("Verification Success Rates (%)")
plt.ylim(0, 105)
plt.ylabel("Percentage (%)")
plt.tight_layout()
plt.savefig("results/verification_success_rates.png")
plt.close()

# --- Plot 3: Reasoning Length by Type ---
plt.figure(figsize=(8, 5))
sns.boxplot(x="problem_type", y="reasoning_length", data=df, palette="Set3",
            order=sorted(df["problem_type"].unique()))
plt.title("Reasoning Length Distribution by Problem Type")
plt.xlabel("Problem Type")
plt.ylabel("Reasoning Length (characters)")
plt.tight_layout()
plt.savefig("results/reasoning_length_distribution.png")
plt.close()

# --- Plot 4: Scatter Plot (Reasoning Length vs Objective Value) ---
plt.figure(figsize=(8, 6))

# Keep only rows with numeric objective values
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
    plt.savefig("results/reasoning_vs_objective_scatter.png")
    plt.close()
    print(" - reasoning_vs_objective_scatter.png")
else:
    print("No valid objective values available for scatter plot.")

print("\nAll visualizations saved to 'results/' folder:")
print(" - problem_type_distribution.png")
print(" - verification_success_rates.png")
print(" - reasoning_length_distribution.png")
print(" - reasoning_vs_objective_scatter.png")

