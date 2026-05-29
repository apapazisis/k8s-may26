import threading
import requests
import time
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description="Load tester")
parser.add_argument("--url",      default="http://127.0.0.1:8081/", help="Target URL")
parser.add_argument("--users",    type=int, default=50,   help="Concurrent users")
parser.add_argument("--requests", type=int, default=100,  help="Requests per user")
parser.add_argument("--delay",    type=float, default=0.1, help="Delay between requests (seconds)")
args = parser.parse_args()

stats = defaultdict(int)
lock = threading.Lock()

def user_load(user_id):
    for _ in range(args.requests):
        try:
            r = requests.get(args.url, timeout=5)
            with lock:
                stats[r.status_code] += 1
        except Exception:
            with lock:
                stats["error"] += 1
        time.sleep(args.delay)

threads = []
start = time.time()

print(f"Starting: {args.users} users × {int(1/args.delay)} req/sec = {int(args.users/args.delay)} req/sec total")
print(f"Target: {args.url}\n")

for i in range(args.users):
    t = threading.Thread(target=user_load, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

elapsed = time.time() - start
total = sum(v for k, v in stats.items() if k != "error")

print(f"\n--- Results ---")
print(f"Users:          {args.users}")
print(f"Total requests: {sum(stats.values())}")
print(f"Success (2xx):  {stats[200]}")
print(f"Errors:         {stats['error']}")
print(f"Duration:       {elapsed:.2f}s")
print(f"Req/sec:        {total/elapsed:.2f}")
print(f"Status codes:   {dict(stats)}")