import random
import sys


def run_network_audit():
    # 1. The Global Architecture (The List)
    dashboard = ["London", "USA", "China"]

    print("=" * 40)
    print("CORE SECURITY AUDIT: INITIALIZING...")
    print("=" * 40)

    # OUTER LOOP: The Architect moves between regions
    for region in dashboard:
        print(f"\n[>] ENTERING REGION: {region.upper()}")
        print("-" * 30)

        # INNER LOOP: The Mason pings 4 devices per region
        # range(1, 5) creates the IDs for Devices 1, 2, 3, and 4
        for device_id in range(1, 5):

            # THE PROBABILITY GATE: 1-in-5 chance of a critical failure
            audit_roll = random.randint(1, 5)

            if audit_roll == 1:
                print(f"Device {device_id}: [!] STATUS: OFFLINE (CRITICAL VULNERABILITY)")
            else:
                print(f"Device {device_id}: [ok] STATUS: ONLINE (SECURE)")

    print("\n" + "=" * 40)
    print("GLOBAL AUDIT COMPLETE. NO BREACHES DETECTED.")
    print("=" * 40)


if __name__ == "__main__":
    try:
        run_network_audit()
    except KeyboardInterrupt:
        print("\n\n[!] USER ABORT DETECTED. EMERGENCY SHUTDOWN.")
        sys.exit()