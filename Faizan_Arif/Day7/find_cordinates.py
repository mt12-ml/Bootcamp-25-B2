import cv2
import matplotlib.pyplot as plt
def find_signature_area(id_card_path):
    # Load image
    id_card = cv2.imread(id_card_path)
    if id_card is None:
        raise ValueError("Failed to load ID card")
    
    # Convert to RGB for matplotlib
    id_card_rgb = cv2.cvtColor(id_card, cv2.COLOR_BGR2RGB)
    
    # Interactive coordinate finder
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(id_card_rgb)
    plt.title("Click on the TOP-LEFT and BOTTOM-RIGHT of the signature area")
    plt.axis('on')  # Show axis with pixel coordinates
    
    # Store clicked points
    points = []
    
    def onclick(event):
        if event.xdata and event.ydata:
            points.append((int(event.xdata), int(event.ydata)))
            print(f"Clicked at: x={int(event.xdata)}, y={int(event.ydata)}")
            
            # Draw marker
            ax.plot(event.xdata, event.ydata, 'ro', markersize=5)
            fig.canvas.draw()
            
            if len(points) == 2:
                plt.close()
    
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
    
    # Return coordinates if two points clicked
    if len(points) == 2:
        x1, y1 = points[0]
        x2, y2 = points[1]
        return min(y1, y2), max(y1, y2), min(x1, x2), max(x1, x2)  # y1, y2, x1, x2
    else:
        raise ValueError("Please click exactly 2 points")

# Usage (Run this in Kaggle/Jupyter):
try:
    print("=== Signature Area Coordinate Finder ===")
    id_card_path = "/home/ml1/Documents/BootCamp_ML1/day7/3.jpg"  # Update path
    y1, y2, x1, x2 = find_signature_area(id_card_path)
    
    print(f"\n✅ Signature Area Coordinates:")
    print(f"sig_y1, sig_y2 = {y1}, {y2}  # Height range")
    print(f"sig_x1, sig_x2 = {x1}, {x2}  # Width range")
    
    # Visual verification
    id_card = cv2.imread(id_card_path)
    cv2.rectangle(id_card, (x1, y1), (x2, y2), (0, 255, 0), 3)
    plt.imshow(cv2.cvtColor(id_card, cv2.COLOR_BGR2RGB))
    plt.title("Signature Area Selected (Green Rectangle)")
    plt.axis('off')
    plt.show()

except Exception as e:
    print(f"Error: {str(e)}")
