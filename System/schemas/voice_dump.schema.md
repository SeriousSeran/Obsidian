# Voice Dump Schema

## Required Frontmatter

```yaml
type: voice_dump
source_file:
needs_transcription: true
processed: false
review_needed: true
```

## Required Headings

- `# Title`
- `## Raw Source`
- `## Transcript`

## Optional Headings

- `## Context`
- `## Immediate Actions`

## Example

```markdown
---
type: voice_dump
source_file: Recording.m4a
needs_transcription: true
processed: false
review_needed: true
---
# Recording

## Raw Source

Audio file link.

## Transcript

Not transcribed yet.
```

