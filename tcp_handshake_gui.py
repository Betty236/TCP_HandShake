import tkinter as tk


class HandshakeGUI:
    def __init__(self, root):
        root.title("TCP 3‑Way Handshake Simulation")
        root.resizable(False, False)

        # Canvas set‑up
        self.canvas_width = 600
        self.canvas_height = 320
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Positions of the host lifelines
        self.xpos = {"client": 200, "server": 400}

        # Draw static host lifelines
        self._draw_hosts()

        # Define staged messages (src, dst, y, label)
        self.stages = [
            [("client", "server", 60,  "SYN      Seq = x")],
            [("server", "client", 140, "SYN‑ACK  Seq = y, Ack = x+1")],
            [("client", "server", 220, "ACK      Ack = y+1")],
        ]
        self.current_stage = 0

        # Control button
        self.next_btn = tk.Button(root, text="Next", command=self.next_stage, width=10)
        self.next_btn.pack(pady=6)

        self.info_lbl = tk.Label(root, text="Click “Next” to step through the handshake.")
        self.info_lbl.pack()

    def _draw_hosts(self):
        # Lifelines
        for host, x in self.xpos.items():
            self.canvas.create_line(x, 20, x, 300, width=2)
            self.canvas.create_text(x, 18, text=host.capitalize(), anchor="s", font=("Helvetica", 12, "bold"))

    def _draw_arrow(self, src, dst, y, text):
        x0, x1 = self.xpos[src], self.xpos[dst]
        # Arrow line
        self.canvas.create_line(x0, y, x1, y, width=2, arrow=tk.LAST)
        # Label slightly above the line
        self.canvas.create_text((x0 + x1) / 2, y - 10, text=text, font=("Helvetica", 10))

    def next_stage(self):
        if self.current_stage < len(self.stages):
            for arrow in self.stages[self.current_stage]:
                self._draw_arrow(*arrow)
            self.current_stage += 1

            if self.current_stage == len(self.stages):
                self.next_btn.config(state=tk.DISABLED)
                self.info_lbl.config(text="Handshake complete!")

        else:
            # Should not happen, but keep UI responsive
            self.next_btn.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    HandshakeGUI(root)
    root.mainloop()
