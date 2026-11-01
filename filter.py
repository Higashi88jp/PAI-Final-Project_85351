%%writefile filter.py
import os
from collections import deque
import numpy as np
import pyarrow as pa
from dora import Node

WINDOW = int(os.environ.get("WINDOW", "5"))   # yaml の env: から
node = Node()
buf = deque(maxlen=WINDOW)
for event in node:
    if event["type"] == "INPUT":
        buf.append(event["value"].to_numpy())          # Arrow → NumPy
        node.send_output("smoothed", pa.array(np.mean(buf, axis=0)), metadata=event["metadata"])
    elif event["type"] in ("STOP", "INPUT_CLOSED"):
        break
