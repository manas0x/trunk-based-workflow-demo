# Trunk-Based Workflow Demo

This public demo models trunk-based development for GitFlow Analyzer. It is a small workflow fixture, not a statistically representative team benchmark.

## Branch rules

- `main` is the single long-lived trunk and stays releasable.
- `feature/*` branches are short-lived and merge to `main` through small pull requests.
- There is no long-lived `develop` or release branch.
- Incomplete user-facing behavior should be isolated behind a feature flag.

## Automation

GitHub Actions runs the Python smoke test on every pull request to `main` and on each push to `main`. GitHub Pages deploys from `main` after a successful merge.
