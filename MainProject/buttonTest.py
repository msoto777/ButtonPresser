import time

from ButtonPresser import ButtonPresser


PULSE_INTERVAL_S = 0.1
GAP_BETWEEN_CYCLES_S = 1.0
CYCLES = 3


def double_pulse(presser: ButtonPresser) -> None:
    """Press-release twice with PULSE_INTERVAL_S between every transition."""
    for _ in range(2):
        presser.outputOn()
        time.sleep(PULSE_INTERVAL_S)
        presser.outputOff()
        time.sleep(PULSE_INTERVAL_S)


def main() -> None:
    presser = ButtonPresser()
    try:
        for cycle in range(1, CYCLES + 1):
            print(f"cycle {cycle}/{CYCLES}: double pulse")
            double_pulse(presser)
            if cycle < CYCLES:
                print(f"  waiting {GAP_BETWEEN_CYCLES_S}s before next cycle")
                time.sleep(GAP_BETWEEN_CYCLES_S)
        print("done; relay left open")
    finally:
        # Active-LOW board: HIGH on pin = relay open. Skip GPIO.cleanup()
        # so the pin doesn't briefly drop LOW (which would re-close the relay).
        presser.outputOff()


if __name__ == "__main__":
    main()
