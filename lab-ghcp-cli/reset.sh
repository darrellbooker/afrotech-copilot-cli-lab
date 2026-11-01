#!/bin/bash
# Resets the GitHub Copilot CLI lab to its original state.
# Manual only. Run from the repo root: bash lab-ghcp-cli/reset.sh
# This erases docstrings, tests, and fixes made during the lab.

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
git rev-parse --verify HEAD >/dev/null 2>&1 || { echo "❌ No commits yet. Commit the lab before resetting."; exit 1; }

echo "🔄 Resetting GitHub Copilot CLI lab..."
git checkout -- lab-ghcp-cli/
git clean -fd lab-ghcp-cli/
echo "✅ GitHub Copilot CLI lab ready!"
