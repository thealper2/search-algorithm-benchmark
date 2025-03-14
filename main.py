#!/usr/bin/env python3
"""
Search Algorithm Benchmark Tool

This script benchmarks various search algorithms on a given dataset and
provides performance metrics for comparison.
"""

import time
import argparse
import statistics
from typing import List, Dict, Tuple, Union, Callable
from pathlib import Path

from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn
from rich.table import Table

# Import search algorithms
from search.linear import linear_search, sentinel_linear_search
from search.binary import binary_search, ubiquitous_binary, meta_binary_search
from search.jump import jump_search
from search.interpolation import interpolation_search
from search.exponential import exponential_search
from search.ternary import ternary_search
from search.fibonacci import fibonacci_search

# Initialize console
console = Console()

# Define algorithm mapping
ALGORITHMS = {
    "linear": linear_search,
    "binary": binary_search,
    "jump": jump_search,
    "interpolation": interpolation_search,
    "exponential": exponential_search,
    "ternary": ternary_search,
    "sentinel": sentinel_linear_search,
    "meta_binary": meta_binary_search,
    "ubiquitous_binary": ubiquitous_binary,
    "fibonacci": fibonacci_search,
    "all": None,
}


def format_time(seconds: float) -> str:
    """
    Format execution time into appropriate units.

    Args:
        seconds: Time in seconds

    Returns:
        Formatted time string with appropriate unit
    """
    if seconds < 1e-6:  # Less than 1 microsecond
        return f"{seconds * 1e9:.2f} ns"
    elif seconds < 1e-3:  # Less than 1 millisecond
        return f"{seconds * 1e6:.2f} μs"
    elif seconds < 1:  # Less than 1 second
        return f"{seconds * 1e3:.2f} ms"
    elif seconds < 60:  # Less than 1 minute
        return f"{seconds:.2f} s"
    else:  # Minutes or more
        return f"{seconds / 60:.2f} min"


def load_data(filepath: Union[str, Path]) -> List[str]:
    """
    Load data from a text file.

    Args:
        filepath: Path to the data file

    Returns:
        List of strings from the file

    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an issue reading the file
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            # Read lines and strip whitespace
            data = [line.strip() for line in file if line.strip()]
        return data
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/] File {filepath} not found.")
        raise
    except IOError as e:
        console.print(f"[bold red]Error:[/] Could not read file {filepath}: {e}")
        raise


def run_single_search(
    algorithm: Callable, data: List[str], target: str, runs: int = 1
) -> Tuple[bool, List[float]]:
    """
    Run a single search algorithm and measure execution time.

    Args:
        algorithm: Search algorithm function
        data: Dataset to search in
        target: Item to search for
        runs: Number of times to run the algorithm for averaging

    Returns:
        Tuple containing (found_status, execution_times)
    """
    execution_times = []
    found = False

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task(f"Running {algorithm.__name__}", total=runs)

        for _ in range(runs):
            start_time = time.perf_counter()
            result = algorithm(data, target)
            end_time = time.perf_counter()

            execution_time = end_time - start_time
            execution_times.append(execution_time)

            if result != -1:
                found = True

            progress.update(task, advance=1)

    return found, execution_times


def benchmark_algorithm(
    algorithm_name: str,
    algorithm: Callable,
    data: List[str],
    target: str,
    runs: int = 10,
    run_all: bool = False,
) -> Dict:
    """
    Benchmark a single algorithm and return performance metrics.

    Args:
        algorithm_name: Name of the algorithm
        algorithm: Algorithm function
        data: Dataset to search in
        target: Item to search for
        runs: Number of times to run the algorithm

    Returns:
        Dictionary with benchmark results
    """
    console.print(f"\n[bold blue]Running benchmark for {algorithm_name}[/]")

    found, execution_times = run_single_search(algorithm, data, target, runs)

    # Calculate statistics
    avg_time = statistics.mean(execution_times)
    median_time = statistics.median(execution_times)
    min_time = min(execution_times)
    max_time = max(execution_times)

    # Print results
    if not run_all:
        console.print(f"\n[bold green]Results for {algorithm_name}:[/]")
        console.print(f"Target '{target}' {'found' if found else 'not found'}")
        console.print(f"Average time: {format_time(avg_time)}")
        console.print(f"Median time: {format_time(median_time)}")
        console.print(f"Best time: {format_time(min_time)}")
        console.print(f"Worst time: {format_time(max_time)}")

    return {
        "algorithm": algorithm_name,
        "found": found,
        "avg_time": avg_time,
        "median_time": median_time,
        "min_time": min_time,
        "max_time": max_time,
    }


def run_all_algorithms(data: List[str], target: str, runs: int = 5) -> List[Dict]:
    """
    Run all search algorithms and compare their performance.

    Args:
        data: Dataset to search in
        target: Item to search for
        runs: Number of times to run each algorithm

    Returns:
        List of dictionaries with benchmark results for each algorithm
    """
    results = []

    # Make sure data is sorted for algorithms that require sorted input
    sorted_data = sorted(data)

    # Define which algorithms need sorted data
    need_sorted = [
        "binary",
        "interpolation",
        "exponential",
        "ternary",
        "meta_binary",
        "ubiquitous_binary",
        "fibonacci",
        "jump",
    ]

    for name, func in ALGORITHMS.items():
        if name == "all":
            continue

        # Use sorted data for algorithms that need it
        current_data = sorted_data if name in need_sorted else data

        if func:
            try:
                result = benchmark_algorithm(name, func, current_data, target, runs)
                results.append(result)
            except Exception as e:
                console.print(f"[bold red]Error running {name}:[/] {str(e)}")

    return results


def display_comparison_table(results: List[Dict]) -> None:
    """
    Display a comparison table of all algorithm results.

    Args:
        results: List of benchmark results
    """
    # Sort results by average execution time
    sorted_results = sorted(results, key=lambda x: x["avg_time"])

    table = Table(title="Search Algorithm Performance Comparison")

    table.add_column("Rank", style="cyan")
    table.add_column("Algorithm", style="green")
    table.add_column("Result", style="yellow")
    table.add_column("Avg Time", style="magenta")
    table.add_column("Median Time", style="blue")
    table.add_column("Best Time", style="green")
    table.add_column("Worst Time", style="red")

    for i, result in enumerate(sorted_results, 1):
        table.add_row(
            str(i),
            result["algorithm"],
            "Found" if result["found"] else "Not Found",
            format_time(result["avg_time"]),
            format_time(result["median_time"]),
            format_time(result["min_time"]),
            format_time(result["max_time"]),
        )

    console.print(table)


def main() -> None:
    """
    Main function to parse arguments and run the benchmark.
    """
    parser = argparse.ArgumentParser(
        description="Benchmark search algorithms on text data"
    )

    parser.add_argument(
        "-f",
        "--file",
        type=str,
        default="data.txt",
        help="Path to the data file (default: data.txt)",
    )
    parser.add_argument(
        "-a",
        "--algorithm",
        type=str,
        default="all",
        choices=ALGORITHMS.keys(),
        help="Search algorithm to use (default: all)",
    )
    parser.add_argument(
        "-t", "--target", type=str, required=True, help="Target string to search for"
    )
    parser.add_argument(
        "-r",
        "--runs",
        type=int,
        default=5,
        help="Number of runs for each algorithm (default: 5)",
    )

    args = parser.parse_args()

    # Display banner
    console.print("[bold cyan]=======================================")
    console.print("[bold cyan]    SEARCH ALGORITHM BENCHMARK TOOL")
    console.print("[bold cyan]=======================================")

    try:
        # Load data
        console.print(f"\n[bold]Loading data from {args.file}...[/]")
        data = load_data(args.file)
        console.print(f"[green]Loaded {len(data)} items.[/]")

        # Run benchmark
        if args.algorithm == "all":
            console.print("\n[bold yellow]Running all search algorithms...[/]")
            results = run_all_algorithms(data, args.target, args.runs)
            display_comparison_table(results)
        else:
            algorithm = ALGORITHMS[args.algorithm]

            # Check if algorithm needs sorted data
            if args.algorithm in [
                "binary",
                "interpolation",
                "exponential",
                "ternary",
                "meta_binary",
                "ubiquitous_binary",
                "fibonacci",
                "jump",
            ]:
                console.print(
                    "[yellow]This algorithm requires sorted data. Sorting...[/]"
                )
                data = sorted(data)

            benchmark_algorithm(args.algorithm, algorithm, data, args.target, args.runs)

    except Exception as e:
        console.print(f"[bold red]An error occurred:[/] {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
