#!/usr/bin/env python3
import zmq
import json

def send_budget_and_print(budget):
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REQ)
    sock.connect("tcp://localhost:5555")

    msg = json.dumps(budget)
    print("▶ Request:", msg)
    sock.send_string(msg)

    reply = sock.recv().decode("utf-8")
    print("◀ Reply: ", reply)
    return json.loads(reply)

if __name__ == "__main__":
    example_budget = {
        "income": "2000",
        "limit": "2000",
        "budget_name": "Budget",
        "expenses": {
            "rent": {"Rent": 1400.0},
            "utilities": {"electric": 120.0},
            "entertainment": {"dinner date": 60.0},
            # other categories can be empty dicts
        }
    }
    totals = send_budget_and_print(example_budget)
    print("\nCategory totals:", totals)
