<h1>8-Puzzle Search Algorithms</h1>

<p>
This project implements classical search algorithms for solving the <b>8-puzzle problem</b>, based on <i>Artificial Intelligence: A Modern Approach</i> by Russell &amp; Norvig.<br>
It supports both uninformed and informed search methods and provides detailed trace logs for analysis.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li><b>Search Algorithms Implemented</b>
    <ul>
      <li>Breadth-First Search (BFS)</li>
      <li>Uniform-Cost Search (UCS)</li>
      <li>Depth-First Search (DFS)</li>
      <li>Depth-Limited Search (DLS)</li>
      <li>Iterative Deepening Search (IDS)</li>
      <li>Greedy Best-First Search</li>
      <li>A* Search</li>
    </ul>
  </li>
  <li><b>Trace Logging</b>
    <ul>
      <li>Generates a <code>trace-YYYY-MM-DD-HH-MM-SS.txt</code> file when run with the <code>-d/--dump</code> flag</li>
      <li>Trace includes:
        <ul>
          <li>Command-line arguments</li>
          <li>Closed set and fringe contents at each step</li>
          <li>Nodes popped, expanded, generated</li>
          <li>Maximum fringe size</li>
          <li>Final solution path</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><b>Puzzle Solvability Check</b>
    <ul>
      <li>Ensures the given puzzle state is solvable before running search</li>
    </ul>
  </li>
</ul>

<hr>

<h2>Project Structure</h2>
<pre>
project/
│
├── expense_8_puzzle.py      # Main driver (CLI entry point)
├── eight_puzzle.py          # Node, EightPuzzle class, heuristics
├── search_algorithms.py     # BFS, UCS, DFS, DLS, IDS, Greedy, A*
├── utils.py                 # Logger, formatting, solution printing
├── start.txt                # Example start state
└── goal.txt                 # Example goal state
</pre>

<hr>

<h2>Requirements</h2>
<ul>
  <li>Python 3.8+</li>
  <li>Standard libraries only (<code>heapq</code>, <code>datetime</code>, <code>argparse</code>, etc.) — no external dependencies</li>
</ul>

<hr>

<h2>Input Format</h2>
<p>Puzzle states are stored as plain text files, formatted as a 3×3 grid of integers.<br>
The digit <code>0</code> represents the blank tile.</p>

<p>Example <code>start.txt</code>:</p>
<pre>
2 3 6
1 0 7
4 8 5
</pre>

<p>Example <code>goal.txt</code>:</p>
<pre>
1 2 3
4 5 6
7 8 0
</pre>

<hr>

<h2>Usage</h2>

<h3>Command Format</h3>
<pre>
python expense_8_puzzle.py &lt;start-file&gt; &lt;goal-file&gt; &lt;method&gt; [-d]
</pre>

<h3>Arguments</h3>
<ul>
  <li><code>&lt;start-file&gt;</code> : path to the initial puzzle state file</li>
  <li><code>&lt;goal-file&gt;</code>  : path to the goal puzzle state file</li>
  <li><code>&lt;method&gt;</code>     : one of the following
    <ul>
      <li><code>bfs</code> → Breadth-First Search</li>
      <li><code>ucs</code> → Uniform-Cost Search</li>
      <li><code>dfs</code> → Depth-First Search</li>
      <li><code>dls</code> → Depth-Limited Search (prompts for depth)</li>
      <li><code>ids</code> → Iterative Deepening Search</li>
      <li><code>greedy</code> → Greedy Best-First Search</li>
      <li><code>a*</code> → A* Search (default if omitted)</li>
    </ul>
  </li>
  <li><code>-d</code> / <code>--dump</code> : optional, generate trace log file</li>
</ul>

<hr>

<h2>Example Runs</h2>

<p>Breadth-First Search:</p>
<pre>
python expense_8_puzzle.py start.txt goal.txt bfs
</pre>

<p>A* Search with trace logging:</p>
<pre>
python expense_8_puzzle.py start.txt goal.txt a* -d
</pre>

<hr>

<h2>Sample Console Output</h2>
<pre>
Nodes Popped: 97
Nodes Expanded: 64
Nodes Generated: 173
Max Fringe Size: 77
Solution Found at depth 12 with cost of 63.
Steps:
        Move 7 Left
        Move 5 Up
        Move 8 Right
        Move 7 Down
        Move 5 Left
        Move 6 Down
        Move 3 Right
        Move 2 Right
        Move 1 Up
        Move 4 Up
        Move 7 Left
        Move 8 Left
</pre>

<hr>

<h2>Sample Trace File</h2>
<p>Example <code>trace-2025-09-15-14-55-12.txt</code>:</p>
<pre>
Command-Line Arguments : ['start.txt', 'goal.txt', 'a*', 'true']
After Initialization
    Closed: []
    Fringe: [
        &lt; state = [[2, 3, 6], [1, 0, 7], [4, 8, 5]], action = {Start} g(n) = 0, d = 0, f(n) = 47, Parent = Pointer to {None} &gt;]
    Nodes Popped: 0
    Nodes Expanded: 0
    Nodes Generated: 1
    Max Fringe Size: 1
Running a*
...
=== Final Solution ===
Nodes Popped: 97
Nodes Expanded: 64
Nodes Generated: 173
Max Fringe Size: 77
Solution Found at depth 12 with cost of 63.
Steps:
        Move 7 Left
        Move 5 Up
        ...
</pre>

<hr>

<h2>Testing</h2>

<h3>Manual Testing</h3>
<pre>
python expense_8_puzzle.py start.txt goal.txt bfs -d
python expense_8_puzzle.py start.txt goal.txt ucs -d
python expense_8_puzzle.py start.txt goal.txt dfs -d
python expense_8_puzzle.py start.txt goal.txt dls -d   # prompts for depth
python expense_8_puzzle.py start.txt goal.txt ids -d
python expense_8_puzzle.py start.txt goal.txt greedy -d
python expense_8_puzzle.py start.txt goal.txt a* -d
</pre>

<h3>Automated Testing</h3>
<p>You can run all algorithms in sequence with a shell script:</p>

<p><code>run_tests.sh</code></p>
<pre>
#!/bin/bash

methods=("bfs" "ucs" "dfs" "ids" "greedy" "a*")

for m in "${methods[@]}"; do
    echo "Running $m..."
    python expense_8_puzzle.py start.txt goal.txt $m -d
done

echo "Running dls (depth=10)..."
python expense_8_puzzle.py start.txt goal.txt dls -d <<EOF
10
EOF
</pre>

<p>Run it:</p>

<pre>
chmod +x run_tests.sh
./run_tests.sh
</pre>

<hr>

<h2>References</h2>
<ul>
  <li>Stuart Russell &amp; Peter Norvig, <i>Artificial Intelligence: A Modern Approach</i></li>
  <li>Classic AI search algorithms: BFS, DFS, UCS, IDS, Greedy, A*</li>
</ul>
