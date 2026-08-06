#!/usr/bin/env bash
# Publish the site to the gh-pages branch.
#
# GitHub Pages' Actions-based deploy kept sitting in deployment_queued and
# timing out, so the site publishes from a branch instead. Run this after any
# change to index.html or the frames:
#
#   ./publish.sh
#
set -euo pipefail
cd "$(dirname "$0")"

BRANCH="gh-pages"
WT=".gh-pages-wt"

# First run: create the branch from an empty tree using plumbing, so the
# working tree and the current branch are never touched.
if ! git show-ref --verify --quiet "refs/heads/$BRANCH"; then
  if git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
    git fetch -q origin "$BRANCH:$BRANCH"
  else
    empty_tree=$(git hash-object -t tree /dev/null)
    root=$(git commit-tree "$empty_tree" -m "Start gh-pages")
    git branch "$BRANCH" "$root"
  fi
fi

rm -rf "$WT"; git worktree prune
git worktree add -q "$WT" "$BRANCH"

# only what the live site serves
find "$WT" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp index.html pearldrop-logo.png "$WT"/
cp -r frames-v2b "$WT"/
touch "$WT/.nojekyll"          # skip Jekyll processing

( cd "$WT"
  git add -A
  if git diff --cached --quiet; then
    echo "nothing changed"
  else
    git -c user.name="Claude" -c user.email="noreply@anthropic.com" \
        commit -q -m "Publish site $(date -u +%Y-%m-%dT%H:%MZ)"
  fi
  for i in 1 2 3 4; do git push -q origin "$BRANCH" && break || sleep $((2**i)); done
)
git worktree remove --force "$WT"
echo "published $(git rev-parse --short $BRANCH) to $BRANCH"
