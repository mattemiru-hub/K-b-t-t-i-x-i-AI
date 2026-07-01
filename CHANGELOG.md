# Changelog

All notable changes to this skill package will be tracked here.

## Unreleased

### Added

- `scripts/init_standard_skill_repo.ps1` to bootstrap a new repo from a built-in reusable template

### Changed

- updated repo documentation to explain the reusable template workflow

## v1.0.1 - 2026-06-30

### Added

- `references/clarification-rules-vi.md` to force clarification-first behavior before field guessing
- `references/repo-packaging-playbook-vi.md` to document how to build a complete repo like this in one pass

### Changed

- updated `SKILL.md` with a clarification gate, required question style, and do-not-guess rules
- updated `README.md` and `README_vi.md` to explain the clarification-first behavior

## v1.0.0 - 2026-06-30

First public-ready release.

### Added

- `LICENSE` for public sharing
- `CHANGELOG.md` for version history
- preview image asset in `assets/golden-reference-preview.png`
- Vietnamese repository overview in `README_vi.md`
- real-world prompt examples in `examples/README.md`
- sample deliverable notes in `sample-output/README.md`

### Changed

- renamed the skill and repo to `excel-dashboard-ai-skill`
- synced `SKILL.md`, `agents/openai.yaml`, and `README.md` to the new identity
- synced the latest dashboard styling script from the local working version
- added quick start, one-prompt usage, and public repo metadata improvements
