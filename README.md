# AI異常検知付きセンサデータ監視システム

## 概要

dora-rsを用いてセンサデータの生成、平滑化、
異常検知、アラーム通知を実装した。

## システム構成

sensor → filter → alarm → monitor

## 実行方法

```bash
dora run dataflow4.yml
```

## 実装内容

- sensor.py
- filter.py
- alarm.py
- monitor.py
- dataflow4.yml
