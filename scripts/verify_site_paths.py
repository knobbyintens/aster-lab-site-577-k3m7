"""Verify that generated site URLs use the intended origin and path prefix.

The values below are read from the deployment workflow environment and are
compared with this module's expectations before publishing.
"""

import argparse
import sys

# Expected deployment target for the published site.
EXPECTED_ORIGIN = ""
EXPECTED_BASEURL = ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--origin", default="")
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()

    ok = True
    if args.origin.rstrip("/") != EXPECTED_ORIGIN.rstrip("/"):
        print(f"origin mismatch: got {args.origin!r}, expected {EXPECTED_ORIGIN!r}")
        ok = False
    if args.baseurl.rstrip("/") != EXPECTED_BASEURL.rstrip("/"):
        print(f"baseurl mismatch: got {args.baseurl!r}, expected {EXPECTED_BASEURL!r}")
        ok = False

    if not ok:
        sys.exit(1)
    print("Site paths verified.")


if __name__ == "__main__":
    main()
