param(
  [Parameter(Mandatory = $true)]
  [string]$TargetPath,

  [Parameter(Mandatory = $true)]
  [string]$SkillName,

  [string]$DisplayName,
  [string]$DomainSummary = "the exact job this skill should own",
  [string]$ShortDescription,
  [string]$DefaultPrompt
)

$ErrorActionPreference = "Stop"

if ($SkillName -notmatch '^[a-z0-9-]+$') {
  throw "SkillName must use lowercase letters, digits, and hyphens only."
}

if (-not $DisplayName) {
  $DisplayName = (($SkillName -split "-") | ForEach-Object {
      if ($_.Length -gt 0) {
        $_.Substring(0,1).ToUpper() + $_.Substring(1)
      }
    }) -join " "
}

if (-not $ShortDescription) {
  $ShortDescription = "Reusable Codex skill for $DomainSummary"
}

if (-not $DefaultPrompt) {
  $DefaultPrompt = "Use `$$SkillName to help me with $DomainSummary."
}

if (Test-Path -LiteralPath $TargetPath) {
  $existing = Get-ChildItem -Force -LiteralPath $TargetPath
  if ($existing.Count -gt 0) {
    throw "TargetPath already exists and is not empty: $TargetPath"
  }
} else {
  New-Item -ItemType Directory -Path $TargetPath | Out-Null
}

$fileMap = [ordered]@{
  ".gitignore" = @'
.DS_Store
Thumbs.db
__pycache__/
.pytest_cache/
.idea/
.vscode/
*.pyc
*.pyo
*.tmp
'@
  "SKILL.md" = @'
---
name: {{SKILL_NAME}}
description: Help Codex with {{DOMAIN_SUMMARY}}. Use when the user needs a reusable workflow, domain rules, validation, or bundled assets for this specific job and you want the AI to ask before guessing business-critical mappings.
---

# {{DISPLAY_NAME}}

## Quick Start

- Inspect the user request and source artifacts first.
- Read `references/clarification-rules-vi.md` before mapping important fields or making structural changes.
- Read `references/domain-contract-vi.md` before building the main output.
- Read `references/qa-checklist-vi.md` before final delivery.
- Read `references/prompt-template-vi.md` only when the user asks for a reusable prompt.

## Workflow

1. Inspect the input files, current state, schema, and expected deliverable.
2. Run the clarification gate before mapping any critical fields or changing structure.
3. Map inputs to business roles instead of assuming fixed names.
4. Execute the domain workflow defined in `references/domain-contract-vi.md`.
5. Validate the output using `references/qa-checklist-vi.md`.
6. Save a stable final result and summarize any compromises clearly.

## Clarification Gate

Before doing the main build, decide whether the task can be executed with high confidence.

Ask the user before proceeding if any of these are unclear:

- the main source file or sheet
- the key business fields or control inputs
- the expected final deliverable format
- whether to preserve an existing output or rebuild from scratch
- whether a required KPI, metric, or business rule exists in the source data

Do not guess low-confidence business-critical mappings.
If confidence is below high confidence, stop and ask.

## Required Question Style

Ask only the minimum short concrete questions required to continue.

Preferred style:

1. Nguồn dữ liệu chính là file hoặc sheet nào?
2. Trường hoặc cột nào là input chính cho logic này?
3. Bạn muốn giữ bản hiện tại để polish hay rebuild lại từ đầu?

Do not ask broad open-ended questions when a short targeted question will unblock the work.

## Non-Negotiables

- Preserve the approved user-facing experience, not a rough draft.
- Do not replace a validated structured workflow with a shortcut unless the user asks.
- Keep colors, labels, wording, and logic stable and meaningful.
- Validate the output before final delivery.

## Deliverables

- Final working artifact
- Short summary of what was built
- Short clarification summary when important mappings were confirmed by the user
- List of any unresolved limitations
'@
  "README.md" = @'
# {{DISPLAY_NAME}}

GitHub-ready Codex skill repo for {{DOMAIN_SUMMARY}}.

## What this repo gives you

- a reusable `SKILL.md` entrypoint
- clarification-first behavior to reduce low-confidence guessing
- domain references under `references/`
- starter examples and sample-output notes
- install and bootstrap scripts

## Quick start

1. Copy this repo into your local Codex skills folder with `scripts/install_local_skill.ps1`.
2. Call `${{SKILL_NAME}}` in Codex.
3. Point Codex to the real files or artifacts for the task.
4. Let the skill inspect, ask the necessary clarification questions, and then execute the workflow.

## Folder structure

```text
.
├── SKILL.md
├── README_vi.md
├── agents/
│   └── openai.yaml
├── examples/
│   └── README.md
├── references/
│   ├── clarification-rules-vi.md
│   ├── domain-contract-vi.md
│   ├── prompt-template-vi.md
│   └── qa-checklist-vi.md
├── sample-output/
│   └── README.md
├── scripts/
│   └── install_local_skill.ps1
├── CHANGELOG.md
└── LICENSE
```

## Install for Codex

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install_local_skill.ps1
```

## Notes

- Replace the placeholders in this generated repo with your real domain rules.
- Tighten `references/domain-contract-vi.md` as soon as the workflow becomes concrete.
- Keep the clarification rules strict enough that the AI asks before guessing critical mappings.
'@
  "README_vi.md" = @'
# {{DISPLAY_NAME}} - Bản Tiếng Việt

Đây là repo skill mẫu cho Codex, dùng để xử lý: {{DOMAIN_SUMMARY}}.

## Repo này có gì

- `SKILL.md` để Codex biết khi nào phải dùng skill
- luật hỏi lại trước khi đoán
- tài liệu tham chiếu trong `references/`
- ví dụ dùng trong `examples/`
- ghi chú đầu ra mẫu trong `sample-output/`
- script cài nhanh vào thư mục skill local

## Cách dùng nhanh

1. Cài skill bằng `scripts/install_local_skill.ps1`
2. Gọi Codex với cú pháp `${{SKILL_NAME}}`
3. Trỏ Codex vào file hoặc artifact thật
4. Để skill tự inspect, tự hỏi lại các thông tin còn mơ hồ, rồi mới làm tiếp

## Cần chỉnh gì sau khi sinh repo này

- thay mô tả skill theo domain thật
- điền lại `references/domain-contract-vi.md`
- điền lại `references/prompt-template-vi.md`
- bổ sung checklist QA thật sự dùng được
- thay ví dụ và sample output bằng output thật của repo
'@
  "CHANGELOG.md" = @'
# Changelog

All notable changes to this skill package will be tracked here.

## v0.1.0 - YYYY-MM-DD

Initial scaffold release.
'@
  "LICENSE" = @'
MIT License

Copyright (c) YYYY Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'@
  "agents/openai.yaml" = @'
interface:
  display_name: "{{DISPLAY_NAME}}"
  short_description: "{{SHORT_DESCRIPTION}}"
  default_prompt: "{{DEFAULT_PROMPT}}"
'@
  "examples/README.md" = @'
# Examples

Use this folder to store example prompts, source artifacts, or before-after notes for `{{SKILL_NAME}}`.

Suggested examples:

- one simple example
- one ambiguous example that triggers clarification questions
- one production-like example
'@
  "sample-output/README.md" = @'
# Sample Output

Describe what a good final output from `{{SKILL_NAME}}` should look like.

Suggested contents:

- screenshot or preview image
- expected deliverable files
- summary of the quality bar
'@
  "references/clarification-rules-vi.md" = @'
# Quy Tắc Hỏi Lại Trước Khi Làm

Mục tiêu của file này là buộc AI hỏi lại đúng các câu cần thiết trước khi đoán các field hoặc logic quan trọng.

## Khi nào phải hỏi lại

AI phải dừng và hỏi lại nếu không rõ:

- nguồn dữ liệu chính là gì
- field hoặc input nào là cốt lõi cho workflow
- output cuối cùng phải ở định dạng nào
- nên giữ bản hiện tại hay rebuild lại

## Nguyên tắc hỏi

- chỉ hỏi những gì thực sự chặn việc làm tiếp
- hỏi ngắn, cụ thể, đúng trọng tâm
- không hỏi lan man khi chỉ thiếu một mapping
- nếu mapping quan trọng còn mơ hồ thì không được làm tiếp
'@
  "references/domain-contract-vi.md" = @'
# Domain Contract

Điền file này bằng luật domain thật của repo.

## Mục tiêu

- skill này phải tạo ra điều gì
- output cuối cùng trông như thế nào

## Workflow bắt buộc

1. bước 1
2. bước 2
3. bước 3

## Non-negotiables

- điều gì tuyệt đối không được phá
- điều gì phải luôn kiểm tra
- điều gì AI không được tự đoán
'@
  "references/prompt-template-vi.md" = @'
# Prompt Template Tiếng Việt

```text
Use ${{SKILL_NAME}} to help me with {{DOMAIN_SUMMARY}}.

Before doing the main work:
- inspect the source first
- ask short clarification questions if important mappings or inputs are ambiguous
- do not guess business-critical fields at low confidence

Deliverables:
- final working output
- short summary of what changed
- note any unresolved limitations
```
'@
  "references/qa-checklist-vi.md" = @'
# QA Checklist

Trước khi chốt đầu ra, kiểm tra:

- output chính có chạy hoặc mở được không
- không còn placeholder chưa thay
- wording rõ ràng, không mơ hồ
- logic chính khớp với domain contract
- nếu có field quan trọng, AI đã hỏi lại khi không chắc
'@
  "scripts/install_local_skill.ps1" = @'
param(
  [string]$TargetRoot = "$env:USERPROFILE\\.codex\\skills"
)

$ErrorActionPreference = "Stop"

$source = Split-Path -Parent $PSScriptRoot
$skillName = Split-Path -Leaf $source
$target = Join-Path $TargetRoot $skillName

if (-not (Test-Path -LiteralPath $TargetRoot)) {
  New-Item -ItemType Directory -Path $TargetRoot | Out-Null
}

robocopy $source $target /MIR /XD .git __pycache__ | Out-Null

Write-Output "Installed skill to: $target"
'@
}

$replacements = @{
  "{{SKILL_NAME}}" = $SkillName
  "{{DISPLAY_NAME}}" = $DisplayName
  "{{DOMAIN_SUMMARY}}" = $DomainSummary
  "{{SHORT_DESCRIPTION}}" = $ShortDescription
  "{{DEFAULT_PROMPT}}" = $DefaultPrompt
}

foreach ($entry in $fileMap.GetEnumerator()) {
  $outputPath = Join-Path $TargetPath $entry.Key
  $parent = Split-Path -Parent $outputPath
  if (-not (Test-Path -LiteralPath $parent)) {
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
  }

  $content = $entry.Value
  foreach ($replacement in $replacements.GetEnumerator()) {
    $content = $content.Replace($replacement.Key, $replacement.Value)
  }

  [System.IO.File]::WriteAllText($outputPath, $content, [System.Text.UTF8Encoding]::new($false))
}

Write-Output "Initialized standard skill repo at: $TargetPath"
