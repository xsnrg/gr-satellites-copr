# AGENTS.md

This is a CopR packaging repo for [gr-satellites](https://github.com/daniestevez/gr-satellites)
(GNU Radio 3.10 out-of-tree module with Amateur satellite telemetry decoders, CMake).
The only artifact is `gr-satellites.spec` — there is no application source, tests, CI,
or build system in this repo.

## Spec conventions
- `Source0` is a URL to the upstream GitHub release tarball (`archive/refs/tags/v<version>`).
  No local tarball, no `sources` file.
- Upstream releases for GNU Radio 3.10 come from the v5.x.y series (maint-3.10 branch).
  The v4.x.y series (GNU Radio 3.9) was frozen 2025-07-31; do not package it.
- Upstream update: bump `Version`, reset `Release` to `1%{?dist}`, add `%changelog` entry.
  Re-release of same upstream: bump `Release` only, add `%changelog` entry.
- `%changelog` is Fedora format:
  `* <Day Mon DD YYYY> Jim Howard <xsnrg@users.noreply.github.com> - <version>-<release>`
  followed by `- ` bullets.
- `License` is `GPL-3.0-or-later` (upstream LICENSE).
- Runtime Python deps that the RPM cannot auto-detect: python3-construct, python3-pyzmq,
  python3-pyyaml, python3-requests, python3-websocket-client. Keep them listed in `Requires`.
- Installed layout: `libgnuradio-satellites.so*`, `include/satellites/`,
  Python package at `%{python3_sitelib}/satellites/` (includes bundled `satyaml/` satellite
  definitions), GRC blocks `satellites_*.block.yml` in `%%{_datadir}/gnuradio/grc/blocks`,
  commands `gr_satellites`, `gr_satellites_ssdv`, `smog_p_spectrum`, and three man pages
  (bzip2-compressed at build time, so `bzip2` is a BuildRequires).
- Upstream ships no tests suitable for `%check`; QA tests need a full runtime graph.

## Verification
- The real build is CopR: pushing to master triggers an automatic build.
- Locally, only on a Fedora/RHEL environment with RPM tooling:
  - `rpmlint gr-satellites.spec`
  - `rpmbuild -ba gr-satellites.spec` (put the upstream tarball in `~/rpmbuild/SOURCES`
    first, or use `rpmdev-rpmbuild` / `mock`).
- No test suite exists in this repo.

## Workflow
- Commit directly to master; commit style is lowercase, e.g. `fix spec: <description>`.
- Don't commit build artifacts or tarballs. `.opencode/` is gitignored (root `.gitignore`).
