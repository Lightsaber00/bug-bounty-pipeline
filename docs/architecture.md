# Architecture

## Objective

The bug bounty pipeline is intended to help a researcher move from recon to scan results, validation, and report creation in one structured workflow.

The system is designed to support:
- faster target understanding,
- better scan organization,
- reproducible validation,
- and cleaner reporting.

## High-level view

The project is composed of four main parts:

- Presentation layer.
- Orchestration layer.
- Analysis layer.
- Data layer.

## Layer overview

### 1. Presentation layer
The frontend is the researcher workspace.

Main goals:
- Show target scope.
- Present recon and scan results.
- Display findings and report drafts.
- Surface evidence and notes.

### 2. Orchestration layer
The orchestrator coordinates the pipeline.

Main goals:
- Accept a target or scope item.
- Determine which stage runs next.
- Route output to the right module.
- Combine outputs into one case view.

### 3. Analysis layer
This layer performs the research logic.

Main goals:
- Enumerate and enrich targets.
- Detect interesting services.
- Validate findings.
- Draft report content.

### 4. Data layer
The data layer stores operational context.

Main goals:
- Store targets.
- Store results.
- Store evidence.
- Preserve report history.

## Example workflow

1. A target is added.
2. Recon modules gather scope and asset data.
3. Scan modules probe services and technologies.
4. Validation checks confirm the issue.
5. The system drafts a report.
6. The researcher reviews and finalizes it.

## Future extensions

- Tool output import.
- Case management.
- Screenshot and evidence vault.
- Report templates.
- Export to Markdown, PDF, or JSON.

## Design principles

- Keep the workflow explainable.
- Prefer modular components over one large script.
- Make validation steps visible.
- Preserve human review.
- Support future hardening and integration.
