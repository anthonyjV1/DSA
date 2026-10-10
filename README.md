# DSA practice — Blind 75

75 unsolved Python problems, grouped by topic. No packages to install; use Python 3.10 or newer.

## Start here

1. Open [the progress tracker](PROGRESS.md) and follow the LeetCode link for Two Sum.
2. Write your solution in [problems/arrays/two_sum.py](problems/arrays/two_sum.py).
3. From the repo root, run:

   ```sh
   python3 -m unittest tests.test_two_sum -v
   ```

4. Add your own edge cases in [tests/test_two_sum.py](tests/test_two_sum.py), then submit on LeetCode.
5. Fill in the notes at the top of your solution. Change `[ ]` to `[x]` in `PROGRESS.md` when you can explain and solve it independently, and record a review date.

The starter tests intentionally report `NotImplementedError` until you implement Two Sum. All 75 solution files are blank stubs; only Two Sum has starter tests. Local tests are practice checks, not a replacement for the LeetCode judge.

## Daily workflow

- Read the problem and clarify inputs, outputs, and constraints.
- Work through a small example, then write down an initial approach.
- Try implementing it yourself. If stuck, take one hint and try again.
- Test normal inputs and edge cases. Explain time and space complexity.
- Revisit difficult problems after a few days with your previous solution hidden.

Start with arrays and strings, then move through linked lists, matrices, trees, graphs, intervals, heaps, bit manipulation, and dynamic programming. Move around when you want to focus on a particular topic.

## Add tests for your next problem

Copy the template and update the import, method call, and assertions:

```sh
cp templates/test_problem.py.template tests/test_contains_duplicate.py
python3 -m unittest tests.test_contains_duplicate -v
```

Name test files `test_*.py` and test methods `test_*`. Use a separate test file for each problem. For outputs with arbitrary order, compare sets or use `assertCountEqual`; for in-place problems, check the input after the method call.

Run every test you've added:

```sh
python3 -m unittest discover -s tests -v
```

Check Python syntax without running your solutions:

```sh
python3 -m compileall -q problems tests
```

## Layout

```text
problems/<topic>/<problem>.py   Solution stub and approach/complexity notes
problems/structures.py         ListNode, TreeNode, and graph Node for local use
tests/                        Your local test cases
templates/                    Copyable test starter
PROGRESS.md                   All 75 links, completion, and review dates
```

Files use LeetCode-style class and method names. When submitting, copy the solution and any standard-library imports it needs; omit `from problems.structures import ...` because LeetCode supplies its node classes. Locally, import those classes in tests to construct inputs. Run tests from the repo root so imports resolve.

The list is based on [Yangshun Tay's original Blind post](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU). Merge k Sorted Lists appears under both linked lists and heaps there; it is included once here. This repo uses Combination Sum IV (#377), the original linked problem; some Blind 75 versions use Combination Sum (#39). Problems marked † in the tracker were listed as Premium in the source. Read full problem statements through the linked pages.
