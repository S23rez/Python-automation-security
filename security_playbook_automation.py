import time
import random

# --- CONFIGURATION (The "Policy" layer of your Playbook) ---
MAX_FAILED_ATTEMPTS = 5  # The threshold for detection
TARGET_IP = "192.168.1.42"
LOG_FILE = "security_audit.log"


def log_event(message):
    """Writes security events to a local log file (Mock SIEM Log)."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[*] {message}")


def check_siem_alerts():
    """Simulates the 'Detection' phase of the incident response lifecycle."""
    print("\n--- [PHASE 1: DETECTION] SIEM MONITORING ACTIVE ---")

    # Simulating a sudden burst of failed logins
    failed_logins = random.randint(1, 10)
    log_event(f"SIEM Check: {failed_logins} failed login attempts detected from {TARGET_IP}.")

    if failed_logins >= MAX_FAILED_ATTEMPTS:
        log_event("ALERT: Critical threshold exceeded! Potential Brute Force Attack.")
        execute_containment_playbook(TARGET_IP)
    else:
        log_event("Status: Normal activity. No playbook required.")


def execute_containment_playbook(attacker_ip):
    """The 'Containment' phase as outlined in a standard IR Playbook."""
    print("\n--- [PHASE 2: CONTAINMENT] EXECUTING PLAYBOOK ---")

    steps = [
        f"Verifying IP Reputation for {attacker_ip}...",
        f"Quarantining IP {attacker_ip} at the Firewall...",
        "Locking target user accounts to prevent takeover...",
        "Notifying SOC Lead via Incident Report..."
    ]

    for step in steps:
        time.sleep(1.5)  # Simulating the time it takes to run these commands
        log_event(f"PLAYBOOK ACTION: {step}")

    print("\n--- [PHASE 3: RECOVERY] THREAT NEUTRALIZED ---")
    log_event("Incident Closed. System remains in hardened state.")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    try:
        # Simulate a 3-cycle monitoring loop
        for i in range(3):
            check_siem_alerts()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[!] Monitoring stopped by analyst.")