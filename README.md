# Search Algorithm Benchmark Tool

A comprehensive Python tool for benchmarking various search algorithms against text datasets.

## :dart: Features

- Benchmark 10 different search algorithms:
  1. Linear Search
  2. Binary Search
  3. Jump Search
  4. Interpolation Search
  5. Exponential Search
  6. Ternary Search
  7. Sentinel Linear Search
  8. Meta Binary Search
  9. Ubiquitous Binary Search
  10. Fibonacci Search
- Rich terminal output with:
  - Progress bars showing real-time search progress
  - Color-coded results
  - Performance comparison tables
- Detailed performance metrics:
  - Best case execution time
  - Worst case execution time
  - Average execution time
  - Median execution time
- Automatic time unit conversions (nanoseconds to seconds)
- Multi-run benchmarking for statistically significant results
- Full comparison mode to find the most efficient algorithm for your data

## :hammer_and_wrench: Installation

1. Clone this repository: 

```bash
git clone https://github.com/thealper2/search-algorithm-benchmark.git
cd search-algorithm-benchmark
```

2. Install the required dependencies:

```bash
pip install rich
```

## :joystick: Usage

Basic usage:

```bash
python benchmark.py --target "SearchTerm" --file data.txt
```

### Command-line Arguments

| Argument | Short | Description | Default |
| -------- | ----- | ----------- | ------- |
| `--file` | `-f` | Path to the data file | `data.txt` |
| `--algorithm` | `-a` | Search algorithm to use | `all` |
| `--target` | `-t` | Target string to serach for | (Required) |
| `--runs` | `-r` | Number of runs for each algorithm | `5` |

## :warning: Algorithm Notes

**Sorted Data Requirements** : Binary, Jump, Interpolation, Exponential, Ternary, Meta Binary, Ubiquitous Binary, and Fibonacci search algorithms require sorted data. The tool automatically sorts the dataset when needed. Algorithm Characteristics:

- **Linear Search**: O(n) - Simple but inefficient for large datasets
- **Binary Search**: O(log n) - Efficient for sorted datasets
- **Jump Search**: O(sqrt(n)) - Balance between linear and binary search
- **Interpolation Search**: O(log log n) - Excellent for uniformly distributed data
- **Exponential Search**: O(log n) - Good for unbounded or infinite lists
- **Ternary Search**: O(log3 n) - Divides the array into three parts
- **Sentinel Linear Search**: O(n) - Optimized linear search
- **Meta Binary Search**: O(log n) - One-sided binary search variant
- **Ubiquitous Binary Search**: O(log n) - More robust binary search implementation 
- **Fibonacci Search**: O(log n) - Uses Fibonacci numbers for division

## :clipboard: Example Output

When running all algorithms, you'll see a comparison table like this:

```bash
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Rank ┃ Algorithm          ┃ Result ┃ Avg Time  ┃ Median Time ┃ Best Time ┃ Worst Time ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 1    │ binary             │ Found  │ 5.20 μs   │ 5.10 μs     │ 4.95 μs   │ 5.70 μs    │
│ 2    │ ubiquitous_binary  │ Found  │ 6.15 μs   │ 6.10 μs     │ 5.85 μs   │ 6.70 μs    │
│ 3    │ interpolation      │ Found  │ 8.35 μs   │ 8.20 μs     │ 7.95 μs   │ 9.10 μs    │
│ 4    │ meta_binary        │ Found  │ 8.65 μs   │ 8.50 μs     │ 8.30 μs   │ 9.50 μs    │
│ 5    │ ternary            │ Found  │ 9.40 μs   │ 9.30 μs     │ 9.15 μs   │ 9.90 μs    │
│ 6    │ exponential        │ Found  │ 10.25 μs  │ 10.10 μs    │ 9.85 μs   │ 11.20 μs   │
│ 7    │ fibonacci          │ Found  │ 12.15 μs  │ 12.05 μs    │ 11.90 μs  │ 12.70 μs   │
│ 8    │ jump               │ Found  │ 14.80 μs  │ 14.70 μs    │ 14.30 μs  │ 15.60 μs   │
│ 9    │ sentinel           │ Found  │ 18.35 μs  │ 18.20 μs    │ 17.90 μs  │ 19.30 μs   │
│ 10   │ linear             │ Found  │ 22.70 μs  │ 22.50 μs    │ 22.20 μs  │ 23.80 μs   │
└──────┴────────────────────┴────────┴───────────┴─────────────┴───────────┴────────────┘
```

## :scroll: License

MIT License