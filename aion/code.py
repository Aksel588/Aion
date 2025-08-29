#!/usr/bin/env python3
"""
LinkAI-Aion Code Analysis Module
===============================

Advanced code analysis and understanding utilities for AI/ML projects.
"""

import re
import ast
from typing import List, Dict, Any, Optional, Tuple
from collections import Counter


def explain_code(code: str) -> str:
    """
    Provide a detailed explanation of code structure and patterns.
    
    Args:
        code: Source code to analyze
        
    Returns:
        Detailed explanation of the code
    """
    explanations = []
    
    # Check for various patterns
    if re.search(r'\bfor\b.*\bin\b', code):
        explanations.append("Contains for-in loops for iteration")
    
    if re.search(r'\bwhile\b', code):
        explanations.append("Contains while loops")
        
    if re.search(r'\bdef\s+\w+\s*\(', code):
        functions = extract_functions(code)
        explanations.append(f"Defines {len(functions)} function(s): {', '.join(functions)}")
    
    if re.search(r'\bclass\s+\w+', code):
        classes = extract_classes(code)
        explanations.append(f"Defines {len(classes)} class(es): {', '.join(classes)}")
    
    if re.search(r'\bimport\b|\bfrom\b.*\bimport\b', code):
        imports = extract_imports(code)
        explanations.append(f"Imports {len(imports)} module(s)/library(s)")
    
    if re.search(r'\bif\b.*:', code):
        explanations.append("Contains conditional statements")
    
    if re.search(r'\btry\b.*\bexcept\b', code):
        explanations.append("Contains error handling (try-except)")
    
    if re.search(r'\bwith\b.*:', code):
        explanations.append("Uses context managers (with statements)")
    
    # Analyze complexity
    lines = [line.strip() for line in code.splitlines() if line.strip()]
    explanations.append(f"Contains {len(lines)} non-empty lines")
    
    if not explanations:
        return "Simple code without complex patterns detected."
    
    return ". ".join(explanations) + "."


def extract_functions(code: str) -> List[str]:
    """
    Extract function names from code.
    
    Args:
        code: Source code to analyze
        
    Returns:
        List of function names
    """
    return re.findall(r'def\s+(\w+)\s*\(', code)


def extract_classes(code: str) -> List[str]:
    """
    Extract class names from code.
    
    Args:
        code: Source code to analyze
        
    Returns:
        List of class names
    """
    return re.findall(r'class\s+(\w+)', code)


def extract_imports(code: str) -> List[str]:
    """
    Extract import statements from code.
    
    Args:
        code: Source code to analyze
        
    Returns:
        List of imported modules
    """
    imports = []
    
    # Standard imports: import module
    imports.extend(re.findall(r'^\s*import\s+([^\s,]+)', code, re.MULTILINE))
    
    # From imports: from module import ...
    from_imports = re.findall(r'^\s*from\s+([^\s]+)\s+import', code, re.MULTILINE)
    imports.extend(from_imports)
    
    return list(set(imports))  # Remove duplicates


def strip_comments(code: str) -> str:
    """
    Remove comments from code.
    
    Args:
        code: Source code with comments
        
    Returns:
        Code without comments
    """
    lines = []
    for line in code.splitlines():
        # Remove inline comments but preserve strings
        stripped = line
        if '#' in line:
            # Simple approach - doesn't handle # in strings perfectly
            comment_pos = line.find('#')
            stripped = line[:comment_pos].rstrip()
        
        if stripped:  # Only add non-empty lines
            lines.append(stripped)
    
    return "\n".join(lines)


def analyze_complexity(code: str) -> Dict[str, Any]:
    """
    Analyze code complexity metrics.
    
    Args:
        code: Source code to analyze
        
    Returns:
        Dictionary with complexity metrics
    """
    lines = code.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    
    # Count various constructs
    functions = len(extract_functions(code))
    classes = len(extract_classes(code))
    imports = len(extract_imports(code))
    
    # Count control flow statements
    if_count = len(re.findall(r'\bif\b', code))
    for_count = len(re.findall(r'\bfor\b', code))
    while_count = len(re.findall(r'\bwhile\b', code))
    try_count = len(re.findall(r'\btry\b', code))
    
    # Calculate cyclomatic complexity (simplified)
    complexity = 1 + if_count + for_count + while_count + try_count
    
    return {
        'total_lines': len(lines),
        'code_lines': len(non_empty_lines),
        'functions': functions,
        'classes': classes,
        'imports': imports,
        'if_statements': if_count,
        'loops': for_count + while_count,
        'try_blocks': try_count,
        'cyclomatic_complexity': complexity
    }


def extract_docstrings(code: str) -> List[str]:
    """
    Extract docstrings from Python code.
    
    Args:
        code: Python source code
        
    Returns:
        List of docstrings found in the code
    """
    docstrings = []
    
    # Find triple-quoted strings that are likely docstrings
    docstring_pattern = r'"""(.*?)"""|\'\'\'(.*?)\'\'\''
    matches = re.findall(docstring_pattern, code, re.DOTALL)
    
    for match in matches:
        docstring = match[0] if match[0] else match[1]
        if docstring.strip():
            docstrings.append(docstring.strip())
    
    return docstrings


def count_operators(code: str) -> Dict[str, int]:
    """
    Count different types of operators in code.
    
    Args:
        code: Source code to analyze
        
    Returns:
        Dictionary with operator counts
    """
    operators = {
        'arithmetic': ['+', '-', '*', '/', '//', '%', '**'],
        'comparison': ['==', '!=', '<', '>', '<=', '>='],
        'logical': ['and', 'or', 'not'],
        'assignment': ['=', '+=', '-=', '*=', '/='],
        'bitwise': ['&', '|', '^', '~', '<<', '>>']
    }
    
    counts = {}
    for category, ops in operators.items():
        count = 0
        for op in ops:
            if op.isalpha():
                count += len(re.findall(r'\b' + op + r'\b', code))
            else:
                count += code.count(op)
        counts[category] = count
    
    return counts


def find_code_smells(code: str) -> List[str]:
    """
    Identify potential code smells and issues.
    
    Args:
        code: Source code to analyze
        
    Returns:
        List of identified code smells
    """
    smells = []
    
    # Long functions (>50 lines)
    functions = re.findall(r'def\s+\w+.*?(?=def|\Z)', code, re.DOTALL)
    for func in functions:
        if len(func.splitlines()) > 50:
            smells.append("Long function detected (>50 lines)")
    
    # Deep nesting (>4 levels of indentation)
    lines = code.splitlines()
    for line in lines:
        if len(line) - len(line.lstrip()) > 16:  # 4 levels * 4 spaces
            smells.append("Deep nesting detected (>4 levels)")
            break
    
    # Magic numbers
    magic_numbers = re.findall(r'\b\d{2,}\b', code)
    if len(magic_numbers) > 5:
        smells.append("Many magic numbers detected")
    
    # Long lines (>100 characters)
    long_lines = [line for line in lines if len(line) > 100]
    if long_lines:
        smells.append(f"{len(long_lines)} long lines detected (>100 chars)")
    
    # TODO comments
    todos = re.findall(r'#.*TODO|#.*FIXME|#.*HACK', code, re.IGNORECASE)
    if todos:
        smells.append(f"{len(todos)} TODO/FIXME/HACK comments found")
    
    return list(set(smells))  # Remove duplicates