# Security Policy

## Supported versions

This repository is currently pre-1.0. Security fixes are handled on the default branch.

## Reporting a vulnerability

If you find a vulnerability or unsafe automation behavior, please open a private GitHub security advisory when available, or contact the maintainer through the repository profile.

Please include:

- affected file or workflow
- steps to reproduce
- expected impact
- suggested fix, if known

## Scope

Security-sensitive areas include:

- scripts that write files
- instructions that could trigger unsafe shell or GUI automation
- documentation that encourages risky Logic Pro automation assumptions
- handling of user-provided paths or project names

Do not publish exploit details publicly before the maintainer has had a reasonable chance to respond.
