# MicroserviceA

This service tallies non-zero expense categories from your budget JSON.

---

## 🔌 Endpoint & Protocol

- **Protocol:** ZeroMQ REQ/REP  
- **URL:** `tcp://<HOST>:5555`  
  (Use `localhost:5555` for local testing)

---

## 📤 Request

1. Create a REQ socket:
   ```python
   import zmq, json
   ctx = zmq.Context()
   sock = ctx.socket(zmq.REQ)
   sock.connect("tcp://<HOST>:5555")

## 🖼 UML Sequence Diagram

![Sequence Diagram](UML_Diagram.png)
