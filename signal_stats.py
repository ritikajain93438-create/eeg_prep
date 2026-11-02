import math
import random
import statistics


def make_signal(n, freq, noise):
  random.seed(42)  # Fixed random seed so the file regenerates the same way each time
  samples = []
  for i in range(n):
    val = math.sin(2 * math.pi * freq * (i / n)) + random.gauss(0, noise)
    samples.append(val)

  with open("signal.txt", "w") as f:
    for sample in samples:
      f.write(f"{sample}\n")

  return samples


def load_signal(path):
  numbers = []
  with open(path, "r") as f:
    for line in f:
      stripped = line.strip()
      if stripped:
        numbers.append(float(stripped))
  return numbers


def calculate_mean(x):
  if not x:
    return 0.0
  total = 0.0
  count = 0
  for val in x:
    total += val
    count += 1
  return total / count


def calculate_max(x):
  if not x:
    return None
  maximum = x[0]
  for val in x:
    if val > maximum:
      maximum = val
  return maximum


def calculate_min(x):
  if not x:
    return None
  minimum = x[0]
  for val in x:
    if val < minimum:
      minimum = val
  return minimum


def moving_average(x, window=5):
  if len(x) < window:
    return []

  averages = []
  for i in range(len(x) - window + 1):
    window_slice = x[i : i + window]
    avg = calculate_mean(window_slice)
    averages.append(avg)
  return averages


def count_peaks(x, threshold):
  if len(x) < 2:
    return 0

  peaks = 0
  for i in range(1, len(x)):
    if x[i - 1] < threshold and x[i] >= threshold:
      peaks += 1
  return peaks


def bin_counts(x, bin_width=0.5):
  if not x:
    return {}

  bins = {}
  for val in x:
    bin_start = math.floor(val / bin_width) * bin_width
    bin_start = round(bin_start, 2)
    bin_end = round(bin_start + bin_width, 2)

    bin_label = f"[{bin_start}, {bin_end})"
    if bin_label not in bins:
      bins[bin_label] = 0
    bins[bin_label] += 1

  sorted_bins = dict(
      sorted(
          bins.items(),
          key=lambda item: float(item[0].split(",")[0].replace("[", "")),
      )
  )
  return sorted_bins


def main():
  print("=== Signal Generator & Statistics Tool ===")
  try:
    n = int(input("Enter number of samples : "))
    freq = float(input("Enter frequency : "))
    noise = float(input("Enter noise level : "))
  except ValueError:
    print("Invalid input! Please enter valid numbers.")
    return

  print(f"\nGenerating {n} samples and saving to signal.txt...")
  make_signal(n, freq, noise)

  try:
    data = load_signal("signal.txt")
  except Exception as e:
    print(f"Error reading file: {e}")
    return

  if not data:
    print("Error: The signal file is empty.")
    return

  mean_val = calculate_mean(data)
  max_val = calculate_max(data)
  min_val = calculate_min(data)

  print(f"\n--- Custom Statistics ---")
  print(f"Mean: {mean_val}")
  print(f"Max: {max_val}")
  print(f"Min: {min_val}")

  m_avg = moving_average(data, window=5)
  print(f"\n--- Moving Average ---")
  print(
      f"First 5 values: {[round(val, 3) for val in m_avg[:5]]}"
      if m_avg
      else "List too short for window."
  )
  print(f"Expected output length: {len(data) - 5 + 1} | Actual length: {len(m_avg)}")

  threshold = 0.5
  peaks = count_peaks(data, threshold)
  print(f"\n--- Peak Counting ---")
  print(f"Number of peaks above threshold {threshold}: {peaks}")

  b_counts = bin_counts(data, bin_width=0.5)
  print(f"\n--- Bin Counts (width 0.5) ---")
  for b_label, count in b_counts.items():
    print(f"  Bin {b_label}: {count} samples")

  print("\n--- Running Self-Checks ---")
  assert math.isclose(mean_val, statistics.mean(data), rel_tol=1e-9), "Mean check failed!"
  assert max_val == max(data), "Max check failed!"
  assert min_val == min(data), "Min check failed!"
  print("All statistical assertions passed successfully!")

  small_list = [0.1, 0.6, 0.2, 0.8, 0.9]
  small_ma = moving_average(small_list, window=3)
  assert len(small_ma) == len(small_list) - 3 + 1
  print("Moving average small list check passed!")

  small_peaks = count_peaks(small_list, threshold=0.5)
  assert small_peaks == 2, f"Expected 2 peaks, got {small_peaks}"
  print("Peak counting small list check passed!")

  empty_test_path = "empty_signal_test.txt"
  with open(empty_test_path, "w") as f:
    pass

  empty_data = load_signal(empty_test_path)
  if not empty_data:
    print("Safe error check passed: Handled empty file cleanly without crashing.")


if __name__ == "__main__":
  main()