# Security Policy

## Scope
stalker2-repack-zone operates entirely on local files from the S.T.A.L.K.E.R. 2:
Heart of Chornobyl repack. It never phones home, and plugins must not perform
network I/O.

## Reporting
Open a private security advisory on GitHub if you find a path traversal, unsafe
pak parsing, or plugin loader issue. Do not file public issues for those.

## Supported versions
| Version | Supported |
|---------|-----------|
| 0.9.x   | ✅        |
| < 0.9   | ❌        |

Disclaimers: This tool is community-made and unaffiliated with GSC Game World.
Use at your own risk; always back up your repack before running the installer.