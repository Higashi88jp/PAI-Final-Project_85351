%%writefile sensor.py
import numpy as np
import pyarrow as pa
from dora import Node

node = Node()
rng = np.random.default_rng(0)
N = 30                                   # 30 サンプル送ったら終了（3 秒）
for i, event in enumerate(node):
    if event["type"] != "INPUT":
        break
    t = i / 10
    value = np.array([np.sin(t), np.cos(t), 0.0]) + rng.normal(0, 0.2, 3)   # 3軸 + ノイズ
    node.send_output("reading", pa.array(value.astype(np.float32)), metadata={"t": t})
    if i + 1 >= N:
        break
