#!/usr/bin/env python3
"""Open/close the relay on BCM 17. Active-HIGH board: HIGH=closed, LOW=open."""
import sys

import RPi.GPIO as GPIO

PIN = 17


def usage() -> None:
    print(f"usage: {sys.argv[0]} open|close", file=sys.stderr)
    sys.exit(2)


def main() -> None:
    if len(sys.argv) != 2:
        usage()

    action = sys.argv[1].lower()
    if action not in ("open", "close"):
        usage()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, GPIO.LOW if action == "open" else GPIO.HIGH)
    level = "LOW" if action == "open" else "HIGH"
    print(f"relay {action} (GPIO {PIN} = {level})")


if __name__ == "__main__":
    main()
