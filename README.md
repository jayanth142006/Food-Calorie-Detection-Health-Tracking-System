# Food-calories-nutrients-detection

AI-powered application that helps users understand what they’re eating — simply by uploading an image of their plate through an AR/VR interface.

It detects and analyzes food items in real-time, calculates total calories and nutrients, compares the intake with the user’s health goals, and then provides smart recommendations:

If you’ve eaten too much, it suggests exercises to burn extra calories.

If you’ve eaten too little, it recommends foods to bridge the gap.

It also includes exercise pose detection to track your real-time workouts, count repetitions, and adjust your calorie balance accordingly.

Whether you're tracking your fitness, managing weight, or just curious about your meal — this app gives you full insight and control, all in an engaging and interactive experience.

✨ KEY FEATURES

✔️ Upload food image via AR/VR (Meta Quest or camera)

✔️ Detect food items on the plate using YOLOv11

✔️ Segment each item with precision using SAM2

✔️ Analyze nutrition (calories, macros) via Gemini API

✔️ Visual UI animations — floating food items with real-time data

✔️ Compare intake vs. target using your personal calorie goals

✔️ LLM-based suggestions:

  • Exercises if you're over your limit
  
  • Food/snacks if you're under
  
✔️ Exercise tracking using webcam + MediaPipe Pose

✔️ Counts reps & monitors form in real-time

✔️ Interactive calorie adjustments based on actual physical activity

🛠️ TECH STACK

🍱 Food Detection: YOLOv11 (custom-trained)

✂️ Image Segmentation: SAM2 (Segment Anything Model)

📊 Nutrition Analysis: Gemini API

🧠 Recommendations: Custom-trained LLMs (food & exercise datasets)

🏋️ Pose Tracking: MediaPipe Pose (rep count & form check)

🎨 Frontend: HTML5, CSS3, JavaScript (with animations)

🕶️ AR/VR Interface: Meta Quest, WebXR, Camera

🔗 Backend: Flask

 Food Calorie Detection
 
https://github.com/user-attachments/assets/f19d8ccc-d8ce-477c-8e6e-811fa42cbec3

Exercise Pose Detection

https://github.com/user-attachments/assets/af4b7673-9245-44bc-bba1-cb9f5562b287
