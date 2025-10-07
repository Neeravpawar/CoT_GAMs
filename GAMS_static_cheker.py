# The Static checker performs the pre-Gams validator or responsible to check sytactically correct 

from __future__ import annotations
from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass
import re

@dataclass
class StaticCheckResult:
    """Result of static GAMS code analysis"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    suggestions: List[str]
    symbol_table: Dict[str, str]
    undeclared_symbols: Set[str]
    unused_symbols: Set[str]

class GAMSStaticChecker:
    """
    Production-ready static analyzer for GAMS code
    """
    
    def __init__(self):
        self.gams_keywords = {
            'sets', 'parameters', 'variables', 'equations', 'model', 'solve',
            'scalars', 'tables', 'binary', 'integer', 'positive', 'free',
            'sum', 'prod', 'smin', 'smax', 'min', 'max', 'if', 'else',
            'loop', 'while', 'for', 'display', 'option', 'file', 'put',
            'using', 'minimizing', 'maximizing', 'all'
        }
        
    def check_gams_code(self, gams_code: str) -> StaticCheckResult:
        """
        Perform comprehensive static analysis on GAMS code
        """
        errors = []
        warnings = []
        suggestions = []
        
        # Parse the code
        lines = self._preprocess_code(gams_code)
        symbol_table = self._build_symbol_table(lines)
        
        # Run checks
        self._check_syntax_errors(lines, errors)
        undeclared_symbols = self._find_undeclared_symbols(lines, symbol_table)
        unused_symbols = self._find_unused_symbols(lines, symbol_table)
        
        # Filter results
        filtered_undeclared = self._filter_undeclared_symbols(undeclared_symbols, lines)
        filtered_unused = self._filter_unused_symbols(unused_symbols, symbol_table, lines)
        
        # Generate suggestions
        if filtered_undeclared:
            suggestions.append(f"Check these symbols: {', '.join(sorted(filtered_undeclared))}")
        if filtered_unused:
            warnings.append(f"Unused symbols: {', '.join(sorted(filtered_unused))}")
        if not errors:
            suggestions.append(" Code is syntactically valid")
        if not errors and not filtered_undeclared:
            suggestions.append(" Ready for solver execution")
        
        is_valid = len(errors) == 0
        
        return StaticCheckResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
            suggestions=suggestions,
            symbol_table=symbol_table,
            undeclared_symbols=filtered_undeclared,
            unused_symbols=filtered_unused
        )
    
    def _preprocess_code(self, code: str) -> List[Tuple[int, str]]:
        """Clean and prepare code for analysis"""
        lines = []
        
        for i, line in enumerate(code.split('\n'), 1):
            line = line.rstrip()  # Keep original for accurate analysis
            if line.strip() and not line.strip().startswith('*'):
                lines.append((i, line))
        
        return lines
    
    def _build_symbol_table(self, lines: List[Tuple[int, str]]) -> Dict[str, str]:
        """Extract all declared symbols and their types"""
        symbol_table = {}
        current_section = None
        
        for line_num, line in lines:
            clean_line = line.split('$')[0].strip() if '$' in line else line.strip()
            
            # Detect section headers
            if re.match(r'^sets\b', clean_line, re.IGNORECASE):
                current_section = 'set'
                continue
            elif re.match(r'^parameters?\b', clean_line, re.IGNORECASE):
                current_section = 'parameter'
                continue
            elif re.match(r'^variables?\b', clean_line, re.IGNORECASE):
                current_section = 'variable'
                continue
            elif re.match(r'^equations?\b', clean_line, re.IGNORECASE):
                current_section = 'equation'
                continue
            elif re.match(r'^scalars?\b', clean_line, re.IGNORECASE):
                current_section = 'scalar'
                continue
            elif re.match(r'^model\b', clean_line, re.IGNORECASE):
                current_section = 'model'
                # Extract model name
                match = re.match(r'model\s+([a-zA-Z_][a-zA-Z0-9_]*)', clean_line, re.IGNORECASE)
                if match:
                    symbol_table[match.group(1)] = 'model'
                continue
            elif re.match(r'^table\b', clean_line, re.IGNORECASE):
                current_section = 'table'
                # Extract table name
                match = re.match(r'table\s+([a-zA-Z_][a-zA-Z0-9_]*)', clean_line, re.IGNORECASE)
                if match:
                    symbol_table[match.group(1)] = 'table'
                continue
            
            # End of section
            if clean_line == ';':
                current_section = None
                continue
            
            # Extract symbols from current section
            if current_section:
                symbols = self._extract_symbols_from_line(clean_line, current_section)
                for symbol in symbols:
                    if symbol and symbol not in self.gams_keywords:
                        symbol_table[symbol] = current_section
        
        return symbol_table
    
    def _extract_symbols_from_line(self, line: str, symbol_type: str) -> List[str]:
        """Extract symbol names from a declaration line"""
        symbols = []
        
        if symbol_type in ['set', 'parameter', 'variable', 'equation', 'scalar']:
            # Remove everything after / (data) or ; 
            clean_line = re.split(r'[/;]', line)[0].strip()
            
            # Extract the first word as symbol name
            match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)', clean_line)
            if match:
                symbol = match.group(1)
                symbols.append(symbol)
        
        return symbols
    
    def _check_syntax_errors(self, lines: List[Tuple[int, str]], errors: List[str]):
        """Check for real syntax errors"""
        brace_count = 0
        
        for line_num, line in lines:
            clean_line = line.split('$')[0] if '$' in line else line
            
            # Check for unbalanced parentheses in sum statements
            if 'sum(' in clean_line:
                brace_count += clean_line.count('(') - clean_line.count(')')
            
            # Check for incomplete equations
            if '..' in clean_line and not any(op in clean_line for op in ['=e=', '=l=', '=g=', '=n=']):
                errors.append(f"Line {line_num}: Equation missing relation operator")
        
        if brace_count > 0:
            errors.append(f"Unclosed parentheses in sum statements: {brace_count} missing ')'")
        elif brace_count < 0:
            errors.append(f"Extra closing parentheses: {-brace_count} extra ')'")
    
    def _find_undeclared_symbols(self, lines: List[Tuple[int, str]], symbol_table: Dict[str, str]) -> Set[str]:
        """Find symbols used but not declared"""
        used_symbols = set()
        
        for line_num, line in lines:
            # Skip declaration lines
            if any(re.match(r'^' + sec, line.lower()) for sec in 
                  ['sets', 'parameters', 'variables', 'equations', 'scalars', 'model', 'table']):
                continue
            
            clean_line = line.split('$')[0] if '$' in line else line
            
            # Find symbol usage patterns: symbol( or symbol[ or symbol.
            matches = re.finditer(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*[\(\[\.]', clean_line)
            for match in matches:
                symbol = match.group(1)
                if (symbol not in self.gams_keywords and 
                    symbol not in symbol_table and 
                    not symbol.isdigit()):
                    used_symbols.add(symbol)
        
        return used_symbols
    
    def _filter_undeclared_symbols(self, undeclared: Set[str], lines: List[Tuple[int, str]]) -> Set[str]:
        """Filter out false positives from undeclared symbols"""
        # These are common equation relation operators, not symbols
        equation_ops = {'e', 'l', 'g', 'n'}
        
        set_elements = set()
        for line_num, line in lines:
            found_matches = re.findall(r'/\s*([^/]+)\s*/', line)
            for match in found_matches:
                elements = [elem.strip() for elem in match.split(',')]
                set_elements.update(elements)
                
        filtered = set()
        for symbol in undeclared:
            if symbol.lower() not in equation_ops:
                filtered.add(symbol)
        
        return filtered
    
    def _find_unused_symbols(self, lines: List[Tuple[int, str]], symbol_table: Dict[str, str]) -> Set[str]:
        """Find symbols declared but not used"""
        declared_symbols = set(symbol_table.keys())
        used_symbols = set()
        
        for line_num, line in lines:
            clean_line = line.split('$')[0] if '$' in line else line
            
            # Skip declaration lines
            if any(re.match(r'^' + sec, clean_line.lower()) for sec in 
                  ['sets', 'parameters', 'variables', 'equations', 'scalars', 'model', 'table']):
                continue
            
            # Check for symbol usage in equations and assignments
            for symbol in declared_symbols:
                # Look for symbol used in equations: symbol.. or = symbol or symbol(
                if (f"{symbol}.." in clean_line or 
                    re.search(r'[=\s]' + re.escape(symbol) + r'[\s\(\)]', clean_line)):
                    used_symbols.add(symbol)
        
        return declared_symbols - used_symbols
    
    def _filter_unused_symbols(self, unused: Set[str], symbol_table: Dict[str, str], lines: List[Tuple[int, str]]) -> Set[str]:
        """Filter unused symbols to remove false positives"""
        filtered = set()
        
        for symbol in unused:
            symbol_type = symbol_table.get(symbol)
            # Keep variables and equations that are truly unused
            if symbol_type in ['variable', 'equation']:
                # Double check if they're actually used
                truly_unused = True
                for line_num, line in lines:
                    if (f"{symbol}(" in line or f".{symbol}" in line or 
                        f" {symbol} " in line and not line.strip().startswith(symbol)):
                        truly_unused = False
                        break
                if truly_unused:
                    filtered.add(symbol)
        
        return filtered


def test_final_checker():
    """Test the final GAMS static checker"""
    
    valid_transport = """
Sets
    i   canning plants   / seattle, san-diego /
    j   markets          / new-york, chicago, topeka / ;

Parameters
    a(i)  capacity of plant i in cases
      / seattle     350
        san-diego   600  /
    b(j)  demand at market j in cases
      / new-york    325
        chicago     300
        topeka      275  / ;

Table d(i,j)  distance in thousands of miles
              new-york       chicago      topeka
    seattle          2.5           1.7          1.8
    san-diego        2.5           1.8          1.4  ;

Scalar f  freight in dollars per case per thousand miles  /90/ ;

Parameter c(i,j)  transport cost in thousands of dollars per case ;
c(i,j) = f * d(i,j) / 1000 ;

Variables
    x(i,j)  shipment quantities in cases
    z       total transportation costs in thousands of dollars ;

Positive Variable x ;

Equations
    cost        define objective function
    supply(i)   observe supply limit at plant i
    demand(j)   satisfy demand at market j ;

cost ..        z  =e=  sum((i,j), c(i,j)*x(i,j)) ;
supply(i) ..   sum(j, x(i,j))  =l=  a(i) ;
demand(j) ..   sum(i, x(i,j))  =g=  b(j) ;

Model transport /all/ ;
Solve transport using lp minimizing z ;
"""
    
    checker = GAMSStaticChecker()
    
    print("FINAL GAMS STATIC CHECKER - PRODUCTION READY")
    print("=" * 60)
    
    result = checker.check_gams_code(valid_transport)
    
    print(f"Valid: {result.is_valid}")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")
    print(f"Symbols declared: {len(result.symbol_table)}")
    
    print(f"\nDeclared symbols: {sorted(result.symbol_table.keys())}")
    
    if result.errors:
        print("\n ERRORS:")
        for error in result.errors:
            print(f"  {error}")
    
    if result.warnings:
        print("\n WARNINGS:")
        for warning in result.warnings:
            print(f"  {warning}")
    
    if result.suggestions:
        print("\n SUGGESTIONS:")
        for suggestion in result.suggestions:
            print(f"  {suggestion}")
    
    print(f"\nUndeclared symbols: {result.undeclared_symbols}")
    print(f"Unused symbols: {result.unused_symbols}")

if __name__ == "__main__":
    test_final_checker()