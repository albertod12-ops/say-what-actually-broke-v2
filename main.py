#!/usr/bin/env python3
"""Say What Actually Broke — v2 (deep ATM).

Writes one line of software error copy to /output/entry.txt:
the login code that went to a phone number the user changed years
ago. Field analysis (200 judged entries, 24 Nov 2026): disk-full
(55), database-down (38) and deploy-on-Friday (20) saturate the
field; the 2FA/login-code cluster has only code-expiry lines, and
no entry names the code going to a number the user no longer owns.
This line takes that empty slot: real failure in plain words, an
explicit next step, and a twist a reader repeats out loud. The
line is 171 characters, one line, no padding, shippable as-is in
a real product error dialog.
Stdlib only, deterministic: the same bytes on every run, no
network, no clock, no randomness.
"""
import os

LINE = "We sent your login code to the number you changed in 2022. It will never arrive — update your number and ask for a new code; the old one died on a phone you no longer own."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
