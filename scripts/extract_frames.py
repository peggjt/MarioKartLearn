import cv2
import numpy as np
import os
import multiprocessing

# Number of parallel processes (adjust based on your CPU)
multiprocessing.set_start_method("spawn", force=True)
NUM_PROCESSES = max(1, multiprocessing.cpu_count() - 1)  # Use all but one core

# Input & output directories
video_path = "/app/dump/Frames/RMCP01_2025-03-09_05-13-13_0.avi"  # Path to dumped video
output_path = "/app/data/frames/"  # Where processed frames will be saved
os.makedirs(output_path, exist_ok=True)

def process_frame(frame_data):
    """Process a single frame: convert to grayscale, resize, normalize."""
    frame_index, frame = frame_data
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    frame = cv2.resize(frame, (128, 128))  # Resize
    frame = frame / 255.0  # Normalize

    return frame_index, frame

def extract_frames():
    """Extracts frames in parallel using multiprocessing."""
    # Read all frames first (avoiding frame seek issues in multiprocessing)
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    raw_frames = []

    # Read all frames into memory first
    for i in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break
        raw_frames.append((i, frame))  # Store frame with its index
    cap.release()

    # Process frames in parallel
    with multiprocessing.Pool(NUM_PROCESSES) as pool:
        processed_frames = pool.map(process_frame, raw_frames)

    # Sort frames back into order
    processed_frames.sort(key=lambda x: x[0])
    frames = [frame for _, frame in processed_frames]

    # Save images
    save_images = False
    if save_images is True:
        for n, frame in enumerate(frames):
            frame_filename = os.path.join(output_path, f"frame_{n:05d}.jpg")
            cv2.imwrite(frame_filename, frame * 255)  # Convert back to 0-255 for saving

    # Convert to NumPy array & save
    frames_array = np.array(frames, dtype=np.float32)  # Shape: (num_frames, 128, 128)
    np.save(f"{output_path}/frames", frames_array)
    print(f"Saved {len(frames)} frames to {output_path}.")

if __name__ == "__main__":
    extract_frames()
