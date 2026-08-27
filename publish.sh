#!/usr/bin/env bash
# Build the site and publish it to the gh-pages branch.
#
# What gets published is site/ — the generated preview, whose URLs are the real
# WordPress slugs. The homepage is at /, the drone page at
# /services/aerial-drone-video-production/, and so on. What we look at is what
# pearldrop.com will be, addresses included.
#
#   ./publish.sh
#
# GitHub Pages' Actions-based deploy kept sitting in deployment_queued and
# timing out, so the site publishes from a branch instead. Do not run this twice
# in quick succession: a new deploy cancels the one in flight.
set -euo pipefail
cd "$(dirname "$0")"

BRANCH="gh-pages"
WT=".gh-pages-wt"

python3 build/build.py
python3 build/urls.py

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

# only what the live site serves. -L follows the symlinks build.py leaves for
# the frame sequence and the menu thumbnails, so the branch carries real files.
find "$WT" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -rL site/. "$WT"/
cp -r design "$WT"/          # the design explorations, for review
touch "$WT/.nojekyll"        # skip Jekyll processing

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
