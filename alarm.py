%%writefile alarm.py
import numpy as np
import pyarrow as pa
from dora import Node

THRESHOLD = 0.5
node = Node()
for event in node:
    if event["type"] == "INPUT":

        v = event["value"].to_numpy()

        if abs(v[0]) > THRESHOLD:
            node.send_output(
                "alarm",
                pa.array([float(v[0])]),
                metadata=event["metadata"]
            )

    elif event["type"] in ("STOP", "INPUT_CLOSED"):
        break
