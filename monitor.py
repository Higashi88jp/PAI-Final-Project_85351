%%writefile monitor.py
import numpy as np
from dora import Node

node = Node()
closed = set()

for event in node:

    if event["type"] == "INPUT":

        if event["id"] == "alarm":

            print(
                f"🚨 ALARM !!! "
                f"t={event['metadata']['t']:.1f} "
                f"value={event['value'].to_pylist()}",
                flush=True
            )

        else:
            v = event["value"].to_numpy()

            print(
                f"t={event['metadata']['t']:.1f} "
                f"{event['id']:8s} "
                f"{np.round(v, 2)}",
                flush=True
            )

    elif event["type"] == "INPUT_CLOSED":

        closed.add(event["id"])

        if closed == {"raw", "smoothed", "alarm"}:
            break

    elif event["type"] == "STOP":
        break
