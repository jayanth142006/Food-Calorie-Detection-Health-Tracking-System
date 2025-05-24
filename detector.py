import cv2
import numpy as np
from ultralytics import YOLO, SAM
import os
import shutil

# Initialize Models
yolo_model = YOLO("models/food_detection_yolov8_model1.pt")
sam_model = SAM("sam2_b.pt")

CROP_DIR = "static/cropped_mask"
SAM_OUTPUT_DIR = "static/mask"

# Ensure clean directory before each run
os.makedirs(CROP_DIR, exist_ok=True)
if os.path.exists(SAM_OUTPUT_DIR):
    shutil.rmtree(SAM_OUTPUT_DIR)
os.makedirs(SAM_OUTPUT_DIR, exist_ok=True)

def process_image(image_path):
    orig_image = cv2.imread(image_path)
    results = yolo_model.predict(source=image_path,conf=0.2, save=False)

    cropped_paths = []
    mask_count = 0
    segment_image_path = None

    for result in results:
        boxes = result.boxes.xyxy
        if len(boxes):
            sam_results = sam_model(
                result.orig_img,
                bboxes=boxes,
                verbose=False,
                device='cpu',
                save=True,
                project='static',
                name='mask',
                exist_ok=True
            )

            for sam_result in sam_results:
                masks = sam_result.masks.data.cpu().numpy()
                for i, mask in enumerate(masks):
                    mask_resized = cv2.resize(mask.astype(np.uint8), (orig_image.shape[1], orig_image.shape[0]))
                    masked_img = cv2.bitwise_and(orig_image, orig_image, mask=mask_resized)
                    ys, xs = np.where(mask_resized == 1)
                    if len(xs) > 0 and len(ys) > 0:
                        x_min, x_max = xs.min(), xs.max()
                        y_min, y_max = ys.min(), ys.max()
                        crop = masked_img[y_min:y_max, x_min:x_max]

                        output_path = os.path.join(CROP_DIR, f"crop_{mask_count}.jpg")
                        cv2.imwrite(output_path, crop)
                        cropped_paths.append(output_path)
                        mask_count += 1

    segment_image_path = os.path.join(SAM_OUTPUT_DIR, "image0.jpg")
    return cropped_paths, segment_image_path.replace("\\", "/")
