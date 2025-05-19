Title:Industrial Defect Detection 
Purpose of the Code: The purpose of this code is to detect and highlight surface defects in images, specifically in industrial or agricultural products like fruits, vegetables, or manufactured parts. Key Goals:

Automate Quality Inspection:
Replace or assist manual defect detection with an automated, consistent method using computer vision.
Visualize Defects:
Draw red rectangles around suspected defects to visually indicate issues for further review.
Quantify Defects:
Count and report the number of detected defect areas, which can be used for quality control metrics. Use Cases:
Agriculture: Detect blemishes, bruises, or rot on fruits and vegetables (e.g., tomatoes, apples).
Manufacturing: Identify cracks, scratches, or holes in materials or products.
Packaging Inspection: Spot defects like dirt, tears, or missing parts on packaged goods. Technologies Usage: This project uses a simple but effective tech stack focused on image processing and defect detection: Core OpenCV Techniques Used *cv2.imread() – Load images from disk. *cv2.cvtColor() – Convert color spaces (BGR to Grayscale). *cv2.GaussianBlur() – Smooth images to reduce noise. *cv2.threshold() – Apply binary thresholding to highlight dark spots. *cv2.findContours() – Detect contours (potential defects). *cv2.boundingRect() & cv2.rectangle() – Draw boxes around detected defects. *cv2.imshow() – Display the output image with marked defects. Conclusion: This project demonstrates a simple yet effective approach to automated defect detection using classical image processing techniques with OpenCV. It identifies and highlights darker regions in images — such as blemishes, cracks, or bruises — that may indicate defects in industrial or agricultural products.
