# Main intigrated pipeline of the system
from generator import GAMSGenerator
from GAMS_static_cheker import GAMSStaticChecker
from scip_solver import SCIPSolver
from corpus_generator import CorpusGenerator, CorpusProblem
from typing import Optional, List, Dict, Any
import json

class UnifiedPipeline:
    def __init__(self):
        self.generator = GAMSGenerator()
        self.static_checker = GAMSStaticChecker()
        self.solver = SCIPSolver()
        self.corpus_gen = CorpusGenerator()
    
    def run_complete_pipeline(self, num_problems: int = 20):
        """Complete pipeline: Generate → Check → Solve → Verify"""
        print(" STARTING UNIFIED GAMS CoT PIPELINE")
        
        #  Generate corpus
        corpus = self.corpus_gen.generate_corpus(num_problems)
        
        #  Verify each problem
        verified_problems = []
        for problem in corpus:
            result = self.verify_problem(problem)
            verified_problems.append(result)
        
        #  Save results
        self.save_results(verified_problems, "final_verified_corpus.json")
        
        return verified_problems
    
    def verify_problem(self, problem: CorpusProblem) -> Dict[str, Any]:
        """Verify a single problem through the pipeline"""
        print(f" Verifying {problem.id} - {problem.problem_type}")
        
        # Static validation
        static_result = self.static_checker.check_gams_code(problem.gams_code)
        
        # Solver verification (only if static passes)
        if static_result.is_valid:
            solver_result = self.solver.solve_gams(problem.gams_code)
        else:
            solver_result = None
        
        # Combine results
        return {
            **problem.__dict__,
            "verification": {
                "static_valid": static_result.is_valid,
                "solver_success": solver_result.success if solver_result else False,
                "solver_status": solver_result.status if solver_result else "not_attempted",
                "objective_value": solver_result.objective_value if solver_result else None,
                "fully_verified": static_result.is_valid and (solver_result.success if solver_result else False)
            }
        }
    
    def save_results(self, problems: List[Dict], filename: str):
        """Save final verified corpus"""
        with open(filename, 'w') as f:
            json.dump(problems, f, indent=2)
        print(f" Results saved to {filename}")

# Run the complete system
if __name__ == "__main__":
    pipeline = UnifiedPipeline()
    results = pipeline.run_complete_pipeline(200)
    print(f" Pipeline complete: {len(results)} problems processed")