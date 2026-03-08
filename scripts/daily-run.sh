#!/usr/bin/env bash
# Horizon daily run + deploy to GitHub Pages
# Usage: ./scripts/daily-run.sh
# Cron:  0 8 * * * /path/to/horizon/scripts/daily-run.sh >> /path/to/horizon/logs/cron.log 2>&1

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')]"

cd "$PROJECT_DIR"

echo "$LOG_PREFIX Starting Horizon daily run..."

# 1. Pull latest code
git pull --quiet origin main 2>/dev/null || true

# 2. Install/update dependencies
uv sync --quiet

# 3. Run Horizon
uv run horizon --hours 24

# 4. Deploy docs to gh-pages
echo "$LOG_PREFIX Deploying to gh-pages..."

# Use a temporary worktree to update gh-pages without switching branches
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

# Ensure gh-pages branch exists locally
if ! git show-ref --verify --quiet refs/heads/gh-pages; then
    # Local gh-pages doesn't exist, try to fetch from remote
    if git show-ref --verify --quiet refs/remotes/origin/gh-pages; then
        git branch gh-pages origin/gh-pages
    else
        # Create orphan branch if remote doesn't exist either
        git checkout --orphan gh-pages
        git rm -rf . 2>/dev/null || true
        git commit --allow-empty -m "Initial gh-pages"
        git checkout -
    fi
fi

git worktree add "$TMPDIR" gh-pages
cp -r docs/* "$TMPDIR/"

cd "$TMPDIR"
git add -A
git commit -m "Daily Summary: $(date '+%Y-%m-%d')" || { echo "$LOG_PREFIX Nothing to commit."; exit 0; }
git push origin gh-pages

cd "$PROJECT_DIR"
git worktree remove "$TMPDIR"

echo "$LOG_PREFIX Done."
