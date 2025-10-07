import json
from pathlib import Path
import textwrap

corpus_path = Path("final_verified_corpus.json")

if not corpus_path.exists():
    print("Error: final_verified_corpus.json not found. Run main.py first.")
    exit(1)

with open(corpus_path, "r") as f:
    corpus = json.load(f)

print("=" * 70)
print("GENERATED GAMS CoT REASONING AND PROGRAMS")
print("=" * 70)
print(f"Total problems: {len(corpus)}\n")

# Display first few generated problems
for i, p in enumerate(corpus[:5]):  # show first 5
    print(f"\nProblem ID: {p['id']}")
    print(f"Type: {p['problem_type']}")
    print(f"Static Valid: {p['verification']['static_valid']}")
    print(f"Solver Success: {p['verification']['solver_success']}")
    print(f"Objective Value: {p['verification']['objective_value']}")
    print("\nTEXTUAL DESCRIPTION:")
    print(textwrap.fill(p["text_description"], width=100))
    
    print("\nSUPPLEMENTARY MARKDOWN TABLES:")
    for name, table in p["tables"].items():
        print(f"\n  **{name.upper()}**")
        if isinstance(table, dict):
            for key, val in table.items():
                print(f"    {key:15} : {val}")
    
    print("\nCHAIN-OF-THOUGHT REASONING (first 20 lines):")
    reasoning_preview = "\n".join(p["reasoning"].splitlines()[:20])
    print(textwrap.indent(reasoning_preview, "    "))

    print("\nGENERATED GAMS PROGRAM (first 20 lines):")
    gams_preview = "\n".join(p["gams_code"].splitlines()[:20])
    print(textwrap.indent(gams_preview, "    "))

    print("-" * 70)

print("\nEnd of preview.")
print("Full data available in final_verified_corpus.json")