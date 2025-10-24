import csv
from datetime import date, timedelta
from collections import Counter
import matplotlib.pyplot as plt

CSV_PATH = "wordle-scores.csv"
START_DATE = date(2025, 9, 2)   # column 0 = Sept 2, 2025
PLAYERS = ["Caleb", "Eugene", "Josh", "Simon"]

def read_csv(path):
    with open(path, newline='') as f:
        return [list(row) for row in csv.reader(f)]

def write_csv(path, rows):
    with open(path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def to_int_scores(row):
    """Return list of ints for numeric entries in row (ignore blanks)."""
    out = []
    for x in row:
        if x is None:
            continue
        xs = str(x).strip()
        if xs == "":
            continue
        try:
            out.append(int(xs))
        except:
            continue
    return out

def row_average(row):
    vals = to_int_scores(row)
    return sum(vals) / len(vals) if vals else None

def row_best_and_date(row):
    vals = []
    for i, x in enumerate(row):
        xs = str(x).strip()
        if xs == "":
            continue
        try:
            v = int(xs)
            vals.append((v, i))
        except:
            continue
    if not vals:
        return None, None
    best_v, best_idx = min(vals, key=lambda t: (t[0], t[1]))
    best_date = START_DATE + timedelta(days=best_idx)
    return best_v, best_date

def row_missed_days(row, total_cols):
    missed = 0
    for i in range(total_cols):
        if i >= len(row) or str(row[i]).strip() == "":
            missed += 1
    return missed

def row_mode(row):
    vals = to_int_scores(row)
    if not vals:
        return None
    c = Counter(vals)
    return c.most_common(1)[0][0]

def pad_rows(rows, length, pad=""):
    for r in rows:
        while len(r) < length:
            r.append(pad)

def most_common_team_outcome(rows):
    total_cols = max(len(r) for r in rows)
    pad_rows(rows, total_cols, pad="")
    tuples = []
    for col in range(total_cols):
        outcome = tuple(
            int(rows[i][col]) if rows[i][col].strip().isdigit() else None
            for i in range(len(PLAYERS))
        )
        if any(v is not None for v in outcome):
            tuples.append(outcome)
    if not tuples:
        return None, 0
    counter = Counter(tuples)
    most_common_tuple, freq = counter.most_common(1)[0]
    return most_common_tuple, freq

def show_stats(rows):
    total_cols = max((len(r) for r in rows), default=0)
    pad_rows(rows, total_cols, pad="")

    print(f"\nTracker start date: {START_DATE.isoformat()} (column 0)")
    print(f"Total tracked days (columns): {total_cols}\n")

    for i, player in enumerate(PLAYERS):
        row = rows[i]
        avg = row_average(row)
        best_v, best_date = row_best_and_date(row)
        missed = row_missed_days(row, total_cols)
        mode = row_mode(row)
        print(f"--- {player} ---")
        print(f"  Recorded entries: {len(to_int_scores(row))}")
        print(f"  Missed days: {missed}")
        print(f"  Average: {avg:.2f}" if avg is not None else "  Average: (no scores)")
        if best_v is not None:
            print(f"  Best score: {best_v} on {best_date.isoformat()}")
        else:
            print("  Best: (no scores)")
        print(f"  Most common score: {mode}" if mode is not None else "  Most common score: (none)")
        print()

    outcome, freq = most_common_team_outcome(rows)
    if outcome:
        print("Most common team outcome:", outcome, f"(occurred {freq} times)")
    else:
        print("No team outcomes recorded yet.")


# --- Show histograms ---
    print("\nDisplaying histograms...")
    fig, axes = plt.subplots( 2, 2, dpi=100, figsize=(10, 8), sharex=False, sharey=True)
    axes = axes.flatten()

    for i, player in enumerate(PLAYERS):
        vals = to_int_scores(rows[i])
        axes[i].hist(vals, bins=range(1, 9), align='left', rwidth=0.8, color='skyblue', edgecolor='black')
        axes[i].set_title(player)
        axes[i].set_xticks(range(1, 8))
        axes[i].set_xlim(0.5, 7.5)
        axes[i].set_xlabel("Score")
        axes[i].set_ylabel("Frequency")
        axes[i].grid(axis='y', linestyle='--', alpha=0.6)
        axes[i].tick_params(axis='x', labelsize=10, pad=4)

    plt.tight_layout()
    plt.show()

def input_one_day(rows):
    total_cols = max((len(r) for r in rows), default=0)
    pad_rows(rows, total_cols, pad="")

    # next column index = total_cols
    next_col_index = total_cols
    # date to display = column date, minus one day (since you input one day late)
    display_date = START_DATE + timedelta(days=next_col_index - 1)
    print(f"\nEntering scores for {display_date.isoformat()} (yesterday's Wordle).")
    print(" - Leave blank and press Enter to mark 'skipped'.")
    print(" - Enter 7 for a fail. Acceptable values: 1–7.\n")

    for i, player in enumerate(PLAYERS):
        while True:
            s = input(f"{player}'s score for {display_date.isoformat()}: ").strip()
            if s == "":
                rows[i].append("")
                break
            try:
                v = int(s)
            except:
                print("  Invalid input. Enter blank or integer 1–7.")
                continue
            if 1 <= v <= 7:
                rows[i].append(str(v))
                break
            else:
                print("  Please enter 1–7 (7 = fail), or leave blank.")
    return rows

def ensure_four_rows(rows):
    while len(rows) < 4:
        rows.append([])

def main():
    try:
        rows = read_csv(CSV_PATH)
    except FileNotFoundError:
        rows = []
    ensure_four_rows(rows)

    print("Wordle tracker — options:")
    print("  1) View stats only")
    print("  2) Input yesterday's scores and save to CSV")
    choice = input("Choose 1 or 2: ").strip()
    if choice == "2":
        rows = input_one_day(rows)
        total_cols = max((len(r) for r in rows), default=0)
        pad_rows(rows, total_cols, pad="")
        write_csv(CSV_PATH, rows)
        print(f"\nSaved scores to {CSV_PATH}.")
        show_stats(rows)
    else:
        show_stats(rows)

if __name__ == "__main__":
    main()
