# Note on Technical Issues

## Problem Running Jupyter with venv

Had issues running Jupyter Notebook with venv active in VS Code. Jupyter is installed and the Jupyter extension is installed in VS Code, but the kernel would hang when trying to interrupt and wouldn't stop running even though the code already finished executing.

**What happened:**
- Code ran fine and showed correct output
- Hitting stop/interrupt wouldn't work - just hung forever
- Had to force close VS Code

**Solution:**
Closed everything, deactivated venv, ran Jupyter without venv active. Worked fine after that.

Not sure if this is a VS Code bug, Jupyter issue, or something with how venv interacts with the Jupyter kernel, but running outside venv fixed it for this assignment.

---

**Environment:**
- Windows
- Python 3.14
- VS Code with Jupyter extension (installed)
- Jupyter (installed via pip)
- venv for virtual environment

The code itself works perfectly - just the Jupyter kernel interaction was broken when venv was active.