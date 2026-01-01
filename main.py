#!/usr/bin/env python3
"""
Cosmological Question Engine
Author: Pranay M.

AI dedicated to formulating testable hypotheses about fundamental
cosmological questions.
"""

import ollama
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt
import json
import sys

console = Console()

BANNER = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║              🌌 COSMOLOGICAL QUESTION ENGINE 🌌                                ║
║                    Fundamental Universe Hypothesis Generator                   ║
║                           Author: Pranay M.                                    ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

MODULES = {
    "1": ("Question Formulator", "question", "Formulate fundamental cosmological questions"),
    "2": ("Hypothesis Generator", "hypothesis", "Generate testable hypotheses"),
    "3": ("Observable Predictor", "observable", "Predict observable consequences"),
    "4": ("Experiment Designer", "experiment", "Design cosmological experiments"),
    "5": ("Theory Comparator", "theory", "Compare cosmological theories"),
    "6": ("Data Analyzer", "data", "Analyze cosmological data"),
    "7": ("Anomaly Investigator", "anomaly", "Investigate cosmological anomalies"),
    "8": ("Scale Bridger", "scale", "Bridge micro and macro scales"),
    "9": ("Paradigm Explorer", "paradigm", "Explore new paradigms"),
    "10": ("Cosmology Dashboard", "dashboard", "View cosmological research dashboard")
}

SYSTEM_PROMPTS = {
    "question": """You are an expert cosmologist and philosopher of science.

For each cosmological question formulation, develop:

1. **Question Statement**: Clear articulation of fundamental question
2. **Historical Context**: How this question emerged
3. **Current Understanding**: What we know and don't know
4. **Significance**: Why this question matters
5. **Related Questions**: Connected fundamental questions
6. **Testability Assessment**: Can we hope to answer it?

Questions to explore: origin of universe, nature of dark matter/energy,
fine-tuning, multiverse, arrow of time, fate of universe, etc.

Formulate fundamental cosmological questions rigorously.""",

    "hypothesis": """You are an expert in cosmological theory and hypothesis formation.

For each hypothesis generation, develop:

1. **Hypothesis Statement**: Clear, testable proposition
2. **Theoretical Basis**: Underlying physics and assumptions
3. **Predictions**: What the hypothesis predicts
4. **Distinguishing Features**: How it differs from alternatives
5. **Testability Analysis**: How to test it
6. **Falsification Criteria**: What would disprove it

Generate rigorous, testable cosmological hypotheses.""",

    "observable": """You are an expert in observational cosmology and prediction.

For each observable prediction, identify:

1. **Predicted Phenomena**: What should be observed
2. **Quantitative Predictions**: Specific numbers, ranges
3. **Observable Signatures**: How it would appear in data
4. **Measurement Requirements**: Precision needed
5. **Confounding Factors**: What might obscure signal
6. **Observation Strategy**: How to detect it

Predict observable consequences of cosmological theories.""",

    "experiment": """You are an expert in experimental cosmology and instrumentation.

For each experiment design, specify:

1. **Experimental Objective**: What to measure
2. **Methodology**: How to measure it
3. **Instrumentation**: Equipment and technology needed
4. **Sensitivity Analysis**: Required precision
5. **Systematic Errors**: Potential biases
6. **Feasibility Assessment**: Can it be done?

Design cosmological experiments and observations.""",

    "theory": """You are an expert in theoretical cosmology and physics.

For each theory comparison, analyze:

1. **Theory Overview**: Core claims of each theory
2. **Mathematical Framework**: Underlying formalism
3. **Predictions Comparison**: Different predictions
4. **Evidence Assessment**: Support for each
5. **Open Problems**: Unresolved issues
6. **Decision Framework**: How to choose between them

Compare cosmological theories systematically.""",

    "data": """You are an expert in cosmological data analysis.

For each data analysis, provide:

1. **Data Description**: What data exists
2. **Analysis Methods**: Statistical approaches
3. **Signal Extraction**: How to find signals
4. **Uncertainty Quantification**: Error analysis
5. **Interpretation**: What data tells us
6. **Limitations**: What we can't conclude

Analyze cosmological data rigorously.""",

    "anomaly": """You are an expert in cosmological anomalies and puzzles.

For each anomaly investigation, examine:

1. **Anomaly Description**: What's unexpected
2. **Data Quality**: Is it a real effect?
3. **Conventional Explanations**: Standard physics explanations
4. **Novel Explanations**: New physics possibilities
5. **Further Tests**: How to investigate more
6. **Implications**: What it might mean

Investigate cosmological anomalies thoroughly.""",

    "scale": """You are an expert in multi-scale physics and cosmology.

For each scale-bridging analysis, connect:

1. **Micro Scale**: Quantum and particle physics
2. **Macro Scale**: Cosmological phenomena
3. **Connection Mechanisms**: How scales relate
4. **Emergence Patterns**: What emerges at different scales
5. **Unified Frameworks**: Theories spanning scales
6. **Research Frontiers**: Where connections are unclear

Bridge micro and macro cosmological scales.""",

    "paradigm": """You are an expert in scientific paradigms and cosmological theory.

For each paradigm exploration, develop:

1. **Current Paradigm**: Standard cosmological model
2. **Limitations**: Where current paradigm struggles
3. **Alternative Paradigms**: Different frameworks
4. **Paradigm Comparison**: Strengths and weaknesses
5. **Paradigm Shifts**: What might trigger change
6. **Future Directions**: Where field might go

Explore new cosmological paradigms.""",

    "dashboard": """You are an expert in cosmological research synthesis.

For each dashboard, generate:

1. **Big Questions**: Fundamental questions being addressed
2. **Active Hypotheses**: Current testable proposals
3. **Observational Status**: What data exists
4. **Theory Status**: Competing theories
5. **Anomaly Alerts**: Unexplained observations
6. **Research Priorities**: Where to focus

View cosmological research dashboard."""
}

def get_multiline_input(prompt_text):
    console.print(f"\n[cyan]{prompt_text}[/cyan]")
    console.print("[dim](Type 'END' on a new line when finished)[/dim]\n")
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        except EOFError:
            break
    return '\n'.join(lines)

def query_llama(system_prompt, user_input):
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input}
        ])
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}\n\nMake sure Ollama is running."

def display_menu():
    console.print(BANNER, style="bold blue")
    table = Table(title="🌌 Cosmology Modules", show_header=True, header_style="bold magenta")
    table.add_column("Option", style="cyan", width=8)
    table.add_column("Module", style="green", width=28)
    table.add_column("Description", style="white", width=42)
    for key, (name, _, desc) in MODULES.items():
        table.add_row(key, name, desc)
    table.add_row("0", "Exit", "Exit the application")
    console.print(table)

def run_module(module_key):
    name, key, desc = MODULES[module_key]
    console.print(Panel(f"🌌 {name}", style="bold green"))
    user_input = get_multiline_input(f"Describe your {name.lower()} request:")
    with console.status(f"[bold green]Processing {name}..."):
        response = query_llama(SYSTEM_PROMPTS[key], user_input)
    console.print(Panel(Markdown(response), title=f"🌌 {name} Results", border_style="green"))

def main():
    while True:
        display_menu()
        choice = Prompt.ask("\nSelect a module", choices=["0","1","2","3","4","5","6","7","8","9","10"])
        if choice == "0":
            console.print("\n[yellow]Thank you for using the Cosmological Question Engine![/yellow]")
            console.print("[dim]Exploring the fundamental nature of the universe.[/dim]")
            console.print("[dim]Author: Pranay M.[/dim]\n")
            break
        try:
            run_module(choice)
        except KeyboardInterrupt:
            console.print("\n[yellow]Operation cancelled.[/yellow]")
        except Exception as e:
            console.print(f"\n[red]Error: {str(e)}[/red]")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
