def firewall_check(source_ip, protocol, destination_port):
    """
    Simulates the Cisco ACL First-Match logic for Router3.
    """
    # This represents your ordered ACL on the router
    acl_rules = [
        {"action": "PERMIT", "source": "192.168.60.3", "port": 22}, # Rule 1 (Admin PC)
        {"action": "DENY",   "source": "any",          "port": 22}, # Rule 2 (Block others)
        {"action": "PERMIT", "source": "any",          "port": "any"} # Rule 3 (Allow rest)
    ]

    print(f"--- Processing packet from {source_ip} (Port: {destination_port}) ---")

    for rule in acl_rules:
        # Check if the packet matches the rule
        source_match = (rule["source"] == "any" or rule["source"] == source_ip)
        port_match = (rule["port"] == "any" or rule["port"] == destination_port)

        if source_match and port_match:
            return f"MATCH FOUND: {rule['action']} (Rule logic stopped here.)"

    return "DENY (Implicit deny)"

# --- Test ---
# 1. Your Admin PC (Should pass Rule 1)
print(firewall_check("192.168.60.3", "TCP", 22))

# 2. PC0 (Should hit Rule 2 and be denied)
print(firewall_check("172.168.10.5", "TCP", 22))

# 3. Normal web traffic (Should hit Rule 3)
print(firewall_check("172.168.10.5", "TCP", 80))