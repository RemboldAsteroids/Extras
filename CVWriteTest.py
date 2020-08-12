#!/bin/env python

"""
Script to test different write times for different video
containers and codecs.
"""

import cv2
import numpy as np
import time
import os


NUM_FRAMES = 1024
FILENAME = "test.avi"

frame = np.random.randint(0, 256, (480, 720, NUM_FRAMES), np.uint8)

writer = cv2.VideoWriter(
    FILENAME,
    cv2.VideoWriter_fourcc(*"XVID"),
    # cv2.VideoWriter_fourcc(*"FFV1"),
    # cv2.VideoWriter_fourcc(*"MJPG"),
    # cv2.VideoWriter_fourcc(*"H264"),
    # cv2.VideoWriter_fourcc(*"Y800"),
    30,
    (frame.shape[1], frame.shape[0]),
    False,
)

start = time.time()
for i in range(NUM_FRAMES):
    writer.write(frame[:, :, i])
writer.release()
stop = time.time()

el_time = stop - start
uncompressed_file_size = 720 * 480 * NUM_FRAMES / 1024 / 1024
actual_file_size = os.path.getsize(FILENAME) / 1024 / 1024
print(
    "Wrote {} frames ({:0.2f} MB) in {:0.2f} seconds ({:0.2f} MB/s)".format(
        NUM_FRAMES, actual_file_size, el_time, actual_file_size / el_time
    )
)
print("Uncompressed file would have been {:0.2f} MB".format(uncompressed_file_size))

