#!/usr/bin/env python3
import zmq
import json

def tally_expenses(budget_data):
    """
    Sum up each expense category in budget_data["expenses"]
    and return a dict category→total (omit zeros).
    """
    expenses = budget_data.get("expenses", {})
    totals = {}
    for cat, items in expenses.items():
        total = sum(v for v in items.values() if isinstance(v, (int, float)))
        if total > 0:
            totals[cat] = total
    return totals

def main():
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REP)
    sock.bind("tcp://*:5555")
    print("📡  Listening on tcp://*:5555 …")

    while True:
        msg = sock.recv()
        try:
            payload = json.loads(msg.decode("utf-8"))
            result = tally_expenses(payload)
            reply = json.dumps(result)
        except Exception as e:
            reply = json.dumps({"error": str(e)})
        sock.send_string(reply)

if __name__ == "__main__":
    main()
