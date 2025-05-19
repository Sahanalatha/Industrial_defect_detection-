import cv2
import numpy as np

def detect_defects(image_path):  # ✅ Use a variable name, not a string
    """
    Simple defect detection in industrial images
    Returns image with defects marked and defect count
    """
    
    # Load image using the provided path (not hardcoded)
    img = cv2.imread("tomato.jpg")  # ✅ Now uses the argument passed to the function
    if img is None:
        print("Error: Image not found")
        return None, 0
    
    # Convert to grayscale and blur
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Threshold to find darker defects
    _, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours larger than 100 pixels
    defect_count = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > 100:
            defect_count += 1
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    return img, defect_count

# Example usage
input_img = "tomato.jpg"  # Can now be changed to any image
output_img, defects = detect_defects(input_img)

if output_img is not None:
    print(f"Found {defects} defects")
    cv2.imshow("Defects Detected", output_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
