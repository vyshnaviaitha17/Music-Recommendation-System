import numpy as np
import os

# List of .npy filenames to load
file_names = [
    "angry.npy", "happy.npy", "hello.npy", "neutral.npy",
    "no.npy", "rock.npy", "sad.npy", "surprise.npy",
    "thumbsup.npy", "labels.npy"
]

# Loop through and attempt to read each file
for file in file_names:
    print(f"\n--- Reading {file} ---")
    if os.path.exists(file):
        try:
            data = np.load(file, allow_pickle=True)
            print(f"Shape: {data.shape}")
            print(f"Data Type: {type(data)}")
            print("Content (first few items):")
            print(data[:5] if data.ndim > 1 else data)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    else:
        print(f"{file} not found.")
