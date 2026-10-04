import csv
import numpy as np
from pathlib import Path

SEED = 42
N = 50_000
LOW = 0.5
HIGH = 1.5

WEIGHTS = {
    "P01": 18,
    "P02": 18,
    "P03": 14,
    "P04": 12,
    "P05": 12,
    "P06": 10,
    "P07": 6,
    "P08": 5,
    "P09": 3,
    "P10": 2,
}

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "v2_raw_scores_for_sensitivity.csv"
OUTPUT = ROOT / "data" / "sensitivity_50000_result.csv"

with INPUT.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

metrics = list(WEIGHTS)
names = [r["name"] for r in rows]
scores = np.array(
    [[float(r[m]) / 10.0 for m in metrics] for r in rows],
    dtype=float,
)
base_weights = np.array([WEIGHTS[m] for m in metrics], dtype=float)

rng = np.random.default_rng(SEED)

random_weights = base_weights * rng.uniform(
    LOW, HIGH, size=(N, len(metrics))
)
random_weights = (
    random_weights
    / random_weights.sum(axis=1, keepdims=True)
    * 100.0
)

totals = random_weights @ scores.T
order = np.argsort(-totals, axis=1)

ranks = np.empty_like(order)
for i in range(N):
    ranks[i, order[i]] = np.arange(1, len(names) + 1)

result = []
for j, name in enumerate(names):
    r = ranks[:, j]
    result.append({
        "name": name,
        "wins": int((r == 1).sum()),
        "win_pct": round(float((r == 1).mean()) * 100, 3),
        "best_rank": int(r.min()),
        "median_rank": float(np.median(r)),
        "worst_rank": int(r.max()),
    })

with OUTPUT.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "name", "wins", "win_pct",
            "best_rank", "median_rank", "worst_rank"
        ],
    )
    writer.writeheader()
    writer.writerows(result)

for row in result:
    print(row)

print()
print("Parameters:")
print("seed =", SEED)
print("iterations =", N)
print("weight multiplier range =", (LOW, HIGH))
print("input =", INPUT)
print("output =", OUTPUT)
