import json
from pathlib import Path

corpus_path = Path("final_verified_corpus.json")
output_path = Path("generated_gams_report.md")

with open(corpus_path, "r") as f:
    corpus = json.load(f)

with open(output_path, "w", encoding="utf-8") as f:
    f.write("# Generated GAMS CoT Corpus Report\n\n")
    f.write(f"Total Problems: {len(corpus)}\n\n")

    for p in corpus:
        f.write(f"## Problem {p['id']} — {p['problem_type'].title()}\n\n")
        f.write(f"**Description:** {p['text_description']}\n\n")

        f.write("**Supplementary Tables:**\n")
        for name, table in p["tables"].items():
            f.write(f"- {name}:\n")
            if isinstance(table, dict):
                for k, v in table.items():
                    f.write(f"    - {k}: {v}\n")
            f.write("\n")

        f.write("**Chain-of-Thought Reasoning:**\n\n")
        f.write("```\n" + p["reasoning"] + "\n```\n\n")

        f.write("**Generated GAMS Program:**\n\n")
        f.write("```GAMS\n" + p["gams_code"] + "\n```\n\n")

        v = p["verification"]
        f.write(f"**Verification:** static_valid={v['static_valid']}, "
                f"solver_success={v['solver_success']}, "
                f"objective={v['objective_value']}\n\n")
        f.write("---\n\n")

print(f"Markdown report exported to: {output_path}")