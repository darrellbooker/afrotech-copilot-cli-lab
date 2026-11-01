# Become the Detective: GitHub Copilot CLI Workshop

You've inherited a Python quiz game that seems to work fine. Play it, check your answers, and then use **GitHub Copilot CLI** to figure out what's wrong, prove it, and fix it.

**The flow:** Play → Answer Key → Understand → Investigate → Prove → Fix

---

## Before You Start (3 min)

Open a terminal and start a GitHub Copilot CLI session:

```bash
copilot
```

If prompted to **trust the files in this folder**, select `Yes`.

> 💡 You'll chat with Copilot in plain language. It may ask to use tools, like running shell commands or editing files. **Review and approve each one.**

### Choose a model

1. In the CLI, enter `/model`.
1. Select `Claude Haiku 4.5`.
1. Press **Enter**.

> 💡 Not every task needs the biggest model. Reading code, writing tests, and fixing a small bug are well within reach of a smaller, faster model. Knowing which model fits the job is part of working well with AI.

---

## Step 1: Play the Quiz (3 min)

Open a **second terminal** and keep Copilot running in the first one. Then run:

```bash
python lab-ghcp-cli/quiz.py
```

The quiz won't tell you if you're right until the end. **Write down your 5 answers**, then write down your final score.

When it asks `Play again?`, type `n`.

---

## Step 2: The Answer Key (2 min)

Your facilitator will reveal the answers on screen. **Write them down next to your own**, then count how many you actually got right.

Now start the quiz again in your second terminal with `python lab-ghcp-cli/quiz.py` and answer every question using the answer key. When it asks `Play again?`, type `n`.

> ❓ You got all 5 right. Did the quiz give you 5/5?

Something's off. Time to become the detective.

---

## 🕵🏾 Become the Detective

Good debugging follows the same order every time: understand the code, investigate the cause, prove it with a test, and only then fix it. You'll do all four with Copilot.

### 1. Understand (4 min)

Before you chase the bug, learn how the score gets calculated. In your Copilot terminal, submit:

```
Explain how @lab-ghcp-cli/quiz.py and @lab-ghcp-cli/utils.py work together to score the quiz. Then add docstrings to every function that's missing one.
```

> 💡 After typing `@`, start the file name and press **Tab** to pick it from the list.

Review the docstrings before approving. Do they match what you'd expect each function to do?

### 2. Investigate (5 min)

**Don't fix it yet.** Detectives gather evidence before they make an arrest.

First, make a prediction: which function do you think is responsible? Then submit:

```
I answered all 5 questions correctly, but my score was 4/5. Investigate why. Don't change any code. Tell me which function and which line cause the problem, and explain what's happening.
```

If Copilot offers to fix the code, say no. You'll get there.

> ❓ Was your prediction right? Does Copilot's explanation match what you saw when you played?

### 3. Prove (6 min)

A theory isn't proof. A failing test is. For this step, switch Copilot into **plan mode**.

1. Press **`Shift + Tab`** to switch to plan mode.
1. Submit:

    ```
    Create a pytest test suite in lab-ghcp-cli/test_quiz.py for check_answer, calculate_score, and display_score. Cover normal cases and edge cases. Include a test that reproduces the scoring bug we found. Don't fix the bug. That test should fail until we fix it.
    ```

1. Copilot may ask clarifying questions, then it will build a plan. **Read the plan carefully** before you approve it.
1. Accept the plan and let Copilot create the test file.
1. Run the tests:

    ```bash
    ! python -m pytest lab-ghcp-cli/test_quiz.py -v
    ```

    > 💡 Starting a command with `!` runs it directly in your shell, bypassing Copilot.

> ❓ Which test failed? Does the failure match what Copilot found when you investigated?

### 4. Fix (3 min)

1. Press **`Shift + Tab`** until you're back in standard mode.
1. Submit:

    ```
    Fix the bug in calculate_score so the failing test passes. Don't change the tests.
    ```

1. Run the tests again:

    ```bash
    ! python -m pytest lab-ghcp-cli/test_quiz.py -v
    ```

    All tests should pass. ✅

1. **Case closed?** Go to your second terminal, start the quiz again with `python lab-ghcp-cli/quiz.py`, and play once more with the answer key in hand.

> ❓ Did you get 5/5 this time?

---

## 🔍 Bonus: Did Copilot Find Anything Else?

The scoring bug isn't the only problem. At least two more edge cases are hiding in this code. If you have time, submit:

```
Look for edge cases in @lab-ghcp-cli/quiz.py and @lab-ghcp-cli/utils.py that could cause wrong results or crashes. Don't fix anything. Just list what you find.
```

Write down what you find. We'll compare notes in the debrief.

---

## Reflection

- One small slice in `calculate_score` made every perfect score come up one short, and you only caught it because you checked the answers yourself.
- There were no tests, so the bug shipped without anyone noticing.
- You didn't let Copilot jump straight to a fix. You understood the code, investigated the cause, proved it with a test, and then fixed it. That order is what keeps one fix from creating a new bug.

`Understand → Investigate → Prove → Fix` is the loop working developers use every day. Copilot helps you move through it faster.

---

## 🎉 Case Closed

Show your facilitator a 5/5 score and a passing test run. Then try this same loop on your own code this week.

---

## Start Over (Optional)

To return the lab to its starting state, run this in a regular terminal from the repo root:

```bash
bash lab-ghcp-cli/reset.sh
```

> ⚠️ This erases your docstrings, tests, and fixes. Only run it if you want a clean slate.
