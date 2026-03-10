import sys
from collections import Counter

def analyze_log(path):
    total = 0
    status_counts = Counter()
    ip_counts = Counter()

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.split()
            if len(parts) < 9:
                continue
            ip = parts[0]
            status = parts[8]

            total += 1
            ip_counts[ip] += 1
            status_counts[status] += 1

    print(f"Gesamtanzahl Requests: {total}")
    print("\nTop 5 IPs:")
    for ip, count in ip_counts.most_common(5):
        print(f"{ip} - {count} Requests")

    print("\nHTTP-Status-Codes:")
    for status, count in status_counts.items():
        print(f"{status}: {count}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        logfile = sys.argv[1]
    else:
        logfile = "example_access.log"
    analyze_log(logfile)
