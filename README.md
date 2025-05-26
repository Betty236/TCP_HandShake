# TCP 3‑Way Handshake Simulator (Tkinter GUI)

This is a simple educational GUI application built with Python's `tkinter` that visually simulates the **TCP 3-way handshake** process between a client and a server.

## 🚀 Features

- Graphical display of the three-step TCP connection setup:
  1. **SYN** from client to server
  2. **SYN-ACK** from server to client
  3. **ACK** from client to server
- Step-by-step interaction using a "Next" button
- Clean and minimal UI for teaching or demonstration purposes

## 🖼 Preview

```
Client ──SYN────> Server  
Client <─SYN-ACK─ Server  
Client ──ACK────> Server  
```

Each arrow includes TCP flags and sequence/acknowledgment numbers (e.g., `Seq = x`, `Ack = x+1`).

## 🛠 Requirements

- Python 3.x  
- `tkinter` (usually included with Python)

## ▶️ How to Run

1. Save the script as `tcp_handshake_gui.py` or similar.
2. Run the script using Python:

```bash
python tcp_handshake_gui.py
```

3. A window will appear. Click **"Next"** to step through each phase of the handshake.

## 📁 File Structure

```
tcp_handshake_gui.py   # Main Python script
README.md              # This file
```

## 📚 Educational Use

This project is ideal for:
- Networking instructors teaching TCP/IP fundamentals
- Students learning about connection-oriented protocols
- Visual demonstrations in lectures or labs

## 🔧 Customization Tips

- You can extend it to include the **4-step TCP termination** process (FIN, ACK, etc.).
- Modify arrow labels or colors to illustrate timing, delays, or errors.
- Enhance with animations or sound for engagement.

## 📝 License

This project is released for educational purposes. You are free to use, modify, and distribute it.

---

Created with ❤️ using Python & Tkinter.