# grace_os_complete.py
import os
import json
import time
import uuid
import logging
from datetime import datetime
from pathlib import Path

LOG_FILE = "logs/grace_output.log"
POD_DIRECTORY = "data"

# Setup logging
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

def log_event(event):
    message = f"{datetime.utcnow().isoformat()} | {event}"
    logging.info(message)
    print(message)

def scan_pods():
    pods = []
    pod_path = Path(POD_DIRECTORY)
    if pod_path.exists():
        for f in pod_path.iterdir():
            if f.is_file() and f.suffix == ".py":
                pods.append(f.name)
    return pods

def boot_sequence():
    log_event("GRACE BOOT: Starting Grace AI Operating System")
    time.sleep(1)

    pods = scan_pods()
    log_event(f"GRACE BOOT: Discovered {len(pods)} pods: {pods}")

    cognition_state = {
        "id": str(uuid.uuid4()),
        "status": "active",
        "pods_loaded": pods,
        "uptime": time.time()
    }

    log_event(f"GRACE CORE ONLINE: {json.dumps(cognition_state)}")

    return cognition_state

def cognition_loop():
    boot_sequence()
    while True:
        log_event("GRACE PULSE: System stable. Monitoring environment...")
        time.sleep(10)

if __name__ == "__main__":
    try:
        cognition_loop()
    except Exception as e:
        log_event(f"GRACE EXCEPTION: {str(e)}")
