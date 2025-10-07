# CoT_GAMs: Chain-of-Thought Reasoning for Automated GAMS Program Generation and Validation

## Project Overview
This repository implements a **Chain-of-Thought (CoT) driven reasoning system** for automated generation, validation, and verification of **GAMS (General Algebraic Modeling System)** programs.  
The system translates **textual optimization problem descriptions and Markdown-based data tables** into **structured GAMS models**, verifies them for correctness, and solves them using the **SCIP optimization solver**. The Project identifies 5 types of optimizations problems namely 
- transport
- assignment
- knapsack
- facility_location
- generic_lp

and generates a verified Training corpus using template based reasoning with a minimal LLM wrapper (Phi-3 model) due to memory and availability.

The project integrates:
- LLM-guided CoT reasoning for structured mathematical formulation.
- Automated corpus generation across multiple optimization domains.
- Static validation, solver execution, and result verification.
- Visual analytics for reasoning trace complexity and model performance.

---

## Objectives
- Automatically generate optimization problems: transportation, assignment, knapsack, facility location, and generic LP.
- Use Chain-of-Thought reasoning to produce interpretable reasoning traces and GAMS code.
- Validate model correctness through a **GAMS static checker** and solve using **SCIP**.
- Compile a corpus of verified problems with reasoning and solver metadata.
- Visualize statistics, solver performance, and reasoning length distributions.

---

## Data and Corpus Overview

**Corpus Components**
- Textual problem description  
- Supplementary Markdown-style data tables  
- Chain-of-Thought reasoning trace  
- Generated GAMS code  
- Verification metadata (static validity, solver success, objective value)

**Corpus Summary**
| Metric | Value |
|---------|--------|
| Total Problems | 200 |
| Problem Types | transport, assignment, knapsack, facility_location, generic_lp |
| Static Valid | 100% |
| Solver Success | 94% |
| Fully Verified | 94% |
| Avg. Reasoning Length | ~1050 characters |

### Corpus Analysis Summary

After running `analyze_corpus.py`, the verified corpus (`final_verified_corpus.json`) produced the following results:

| Metric | Value |
|---------|-------|
| Total Problems | 200 |
| Problem Types | transport (50), assignment (50), knapsack (40), facility_location (40), generic_lp (20) |
| Static Valid (%) | 100.0 |
| Solver Success (%) | 94.0 |
| Fully Verified (%) | 94.0 |
| Average Reasoning Length | 1056.85 characters |

All corresponding visualizations are saved in the `results/` folder:
- `problem_type_distribution.png`
- `verification_success_rates.png`
- `reasoning_length_distribution.png`
- `reasoning_vs_objective_scatter.png`


## Methodology

The system follows a five-stage pipeline that automatically generates, validates, and verifies optimization problems written in GAMS. Each stage plays a specific role in producing a consistent and solvable corpus of optimization tasks. The pipeline begins with text-based problem generation, proceeds through static and mathematical validation, and ends with full solver verification.

### 1. Problem Generation
The process starts with the `CorpusGenerator` , which creates optimization problems from structured seed templates.
Each problem type such as transport, assignment, knapsack, facility location, and linear programming is built using pre-defined tables of parameters. The generator varies these parameters randomly to create diversity while keeping the underlying mathematical structure intact.

For example, in transport problems, supply and demand values are adjusted by up to thirty percent from their base values to simulate real-world variability. This ensures that no two problems are identical while remaining valid and balanced.

Each generated problem contains a textual description, structured tables, and metadata fields that describe problem type, dimensionality, and variable characteristics

### 2. Chain-of-Thought Reasoning
Once the data and tables are generated, the `GAMSGenerator`  module uses a reasoning process to explain and translate the problem into executable GAMS code. This stage produces what we call a chain of thought trace, where the system explains each modeling step before writing code.

The generator reasons through several layers: identifying sets and parameters, defining variables, formulating equations, and writing the objective function.
Each reasoning trace includes descriptions like “supply nodes represent factories” or “demand nodes represent customer regions.”
This trace helps verify that the logic behind the model matches the structure of the final GAMS code.

The generator then writes full GAMS programs that include all major sections: Sets, Parameters, Variables, Equations, Model, and Solve statements.
A reasoning completeness score is assigned internally. Models that include all sections and pass integrity checks are marked as valid.

### 3. Static Validation
The `GAMSStaticChecker` validates each generated program before solving it. This step does not run the program but checks that it is syntactically correct.
It detects unbalanced brackets, invalid equation symbols, and undefined variables. It also builds a symbol table to ensure that all declared variables are used properly.

For each model, a static validity score is computed. This score reflects the number of syntax errors, warnings, and symbol mismatches relative to total code length. A perfect static score is one point zero, which means that the program can run directly in a solver without manual correction.

The system also ensures that all essential parts of the GAMS program are present. A model fails static validation if any of the following sections are missing: variable declaration, objective function, or constraints.

### 4. Mathematical Validation
After the code passes static checks, the `MathematicalOptimizationValidator` examines the mathematical structure of the model. This component analyzes the relationships between sets, parameters, and equations to confirm that the model corresponds to a known optimization category.

For example:
- If the model defines two sets with balanced flow equations, it is recognized as an assignment or transport problem.
- If it defines one set with binary selection variables and a capacity constraint, it is classified as a knapsack problem.
- If it contains both binary and continuous variables with facility capacity constraints, it is labeled as a facility location model.

The validator measures structural consistency using simple quantitative rules. The most important are the balance of supply and demand, the presence of a clear objective, and the correctness of variable types.
A problem passes this stage only when its structure matches a valid mathematical signature such as “balanced bipartite flow” or “binary selection with capacity bound.”

### 4. Solver or Verification
Once a model passes static and mathematical checks, it is sent to the `SCIPSolver`  for numerical verification.
The solver converts the GAMS model to LP or MPS format and attempts to find an optimal solution.
Each solution record includes the solver status, the objective value, and the residuals of equality and inequality constraints.

A model is marked as feasible if the solver returns the status “optimal” and all constraint residuals are smaller than one times ten to the power of negative six.
Solver performance is also measured by runtime and optimality gap.
The target runtime is less than two seconds for linear problems and less than ten seconds for mixed integer problems.
A successful solution produces an objective gap smaller than 0.001 and a constraint residual smaller than one times ten to the power of negative six.
### 5. Corpus Compilation
After validation, all verified problems are stored in a JSON corpus with metadata and reasoning traces. The final dataset typically includes one hundred to two hundred problems distributed across all supported types.

The corpus generation process ensures diversity in both numerical values and textual form.
Diversity is measured through entity variety, constraint structure, and lexical difference. The generator aims for at least seventy five percent textual diversity and ninety percent structural validity across the corpus.

## Confidence Score 

Each model receives a confidence score that combines its static validity and parameter integrity scores.
The formula is
C = 0.6 × StaticScore + 0.4 × ParameterIntegrity

A model with C greater than 0.9 is considered reliable for inclusion in the verified corpus.

## Validation Results

| Problem Type       | Average Confidence | Static Score | Structure Signature                      | Feasibility |
|--------------------|--------------------|---------------|------------------------------------------|--------------|
| Transport          | 0.92               | 0.98          | Balanced bipartite flow                  | Pass         |
| Assignment         | 0.95               | 0.99          | Bipartite flow with equality constraints | Pass         |
| Knapsack           | 0.90               | 0.97          | Binary selection with capacity bound     | Pass         |
| Facility Location  | 0.88               | 0.95          | Binary facility opening with flow        | Pass         |
| Generic LP         | 0.93               | 0.99          | Linear resource allocation               | Pass         |

=== VERIFICATION STATISTICS ===
static_valid      100.0
solver_success     94.0
fully_verified     94.0


## Future Work

1. Extend the current GAMS-based corpus to integrate reinforcement learning for accuracy enhancement using verifiable optimization tasks.  
2. Implement a small-scale replication of the “DeepSeek-trick” by combining RL with fine-tuning on DSL-specific datasets.  
3. Develop an automated fine-tuning pipeline for generating domain-specialized corpora in less-studied DSLs beyond GAMS.  
4. Integrate SCIP-driven reward signals to evaluate and refine generated programs during the RL loop.  
5. Explore generalization of the framework to other well-documented, industrially relevant DSLs for broader verification and testing.












