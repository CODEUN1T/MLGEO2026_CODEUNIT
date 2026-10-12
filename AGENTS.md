# AGENTS.md for MLGEO2026_CODEUNIT

## Project
Course repository for ESS 469/569, Autumn 2026: homeworks and the final project.
Every number and figure here must be regenerated from a fresh clone using
the commands in README.md.

## Environment and compute
- Run all code through `pixi run`; add packages only with `pixi add`, and
  commit pixi.toml and pixi.lock together.
- Do not install packages with pip or conda outside pixi.
- Before running `pixi add` or any command that modifies pixi.toml or pixi.lock, tell the user the package and version and wait for approval. After it runs, show `git diff --stat pixi.toml pixi.lock`. 


## Data and provenance
- Fetch values that a provider publishes (station coordinates, velocities,
  catalogs) and cite the URL and retrieval date; do not recompute or retype them.
- Download data with a script in this repository, not by hand, and record the
  dataset DOI or URL, version, and retrieval date in README.md.
- Never modify raw data files; write processed data to a separate folder.

## Code and workflow
- Use paths relative to the repository root; no absolute paths such as /Users/...
- Every notebook must run top to bottom after Restart Kernel and Run All Cells.
- Every reported number and figure comes from a command listed in README.md.
- Before creating, editing, renaming, or deleting any file, show a diff (or the full contents for a new file) and wait for user approval. Do not apply changes until the user says yes. This applies for every file, including notebooks, scripts, pixi.toml, and README.md.
- Set a fixed random seed in every script or notebook that uses randomness (splits, initialization, sampling) and record the seed value in README.md.
- Commit after each completed step, one logical change per commit. Before committing, show the commit message and the output of `git diff --staged --stat`, and wait for user approval. Do not run `git push` until the user approves.

## Reporting and credit
- State the reference frame, units, and time window of every number.
- Mark AI-drafted commits: "AI-assisted: <tool>, <what it drafted>".
- For every AI session, remind the user to save a log in `AI_logs/` named
  `YYYY-MM-DD_tool_task.md` and add a row to `AI_logs/README.md`.
  Log structure (retrieved 2026-10-11):
  https://geo-smart.github.io/mlgeo-book/workbench-setup-hw1/#ai-logs-keep-them-from-the-first-step
  Disclosure norms: https://geo-smart.github.io/mlgeo-book/disclosure-and-norms
- Do not write in the "What I did with it" section of log files; this is left for the user to fill in. 

## Verification
- Run `pixi run smoke` before reporting any result, and show its last line.
- Report the exact commands you ran and the commit hash they ran on.
- If a check fails or a value cannot be fetched, say so; do not substitute an estimate.
- Before reporting, run `git log --grep "AI-assisted" --oneline` and confirm each commit listed has a file in `AI_logs/` and a row in `AI_logs/README.md`. List any that are missing.
- Before committing anything in `AI_logs/`, run `grep -n -i "token\|password\|ghp_" AI_logs/*.md` and show the output.
