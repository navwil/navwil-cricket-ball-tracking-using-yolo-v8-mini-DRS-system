import cv2
import os
import multiprocessing
from ultralytics import YOLO
import numpy as np
from sklearn.linear_model import LinearRegression
N
def color_pixels_last_frame(last_frame_path, coordinates_file_path):
    # Read the last frame
    last_frame = cv2.imread(last_frame_path)

    # Initialize the previous point
    prev_point = None

    # Initialize the coordinates list
    coordinates = []

    # Open the coordinates file
    with open(coordinates_file_path, 'r') as f:
        # Read each line (each line contains coordinates)
        for line in f:
            # Extract coordinates
            x, y = map(float, line.strip().split(','))  # Convert to float instead of int
            x, y = int(x), int(y)  # Convert to int if necessary
            
            # Add the coordinates to the list
            coordinates.append((x, y))

            # Draw a circle using coordinates on the last frame
            cv2.circle(last_frame, (x, y), 10, (0, 255, 0), cv2.FILLED)  # Green filled circle, adjust color as needed

            # If there is a previous point, draw a line from the previous point to the current point
            if prev_point is not None:
                cv2.line(last_frame, prev_point, (x, y), (0, 255, 0), 10)  # Green line, adjust color as needed

            # Update the previous point
            prev_point = (x, y)

    # Convert the coordinates to a numpy array
    coordinates = np.array(coordinates)

    # Create a Linear Regression model
    model = LinearRegression()

    # Ensure we only consider the latest 4 points
    if len(coordinates) > 4:
        coordinates = coordinates[-4:]

    # Train the model with the current coordinates
    model.fit(np.arange(len(coordinates)).reshape(-1, 1), coordinates)

    # Predict the next 3 coordinates
    next_coordinates = model.predict(np.array([len(coordinates), len(coordinates) + 1, len(coordinates) + 2]).reshape(-1, 1))

    # Draw the predicted coordinates in red and connect them with a line
    prev_predicted_point = None
    for x, y in next_coordinates:
        x, y = int(x), int(y)  # Convert to int if necessary
        cv2.circle(last_frame, (x, y), 10, (0, 0, 255), cv2.FILLED)  # Red filled circle, adjust color as needed

        # If there is a previous predicted point, draw a line from the previous predicted point to the current predicted point
        if prev_predicted_point is not None:
            cv2.line(last_frame, prev_predicted_point, (x, y), (0, 0, 255), 10)  # Red line, adjust color as needed

        # Update the previous predicted point
        prev_predicted_point = (x, y)

    return last_frame



# Function to split video and save the last frame
def split_video_last_frame(video_path, save_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Read and discard all frames except the last one
    for _ in range(total_frames - 1):
        success, _ = cap.read()
        if not success:
            break
    
    # Read the last frame
    success, last_frame = cap.read()
    
    # Save the last frame
    if success:
        cv2.imwrite(save_path, last_frame)
        print("Last frame saved successfully.")
    else:
        print("Failed to read the last frame.")
    
    # Release the video capture object
    cap.release()

# Load YOLOv8 model
def detect_and_track(video_path, output_filename):
    model = YOLO('best.pt')#loading model
    cap = cv2.VideoCapture(video_path)
    ret = True
    frameTime =  10 # Time of each frame in ms (adjust for playback speed)

    # Open the coordinates file for writing
    with open(output_filename, 'w') as f:
        pass
        # Read frames
        while ret:
            ret, frame = cap.read()

            if ret:
                # Detect and track objects
                results = model.track(frame, persist=True)
                
                # Extract bounding box coordinates, calculate mid point, and save to file
                 for box in results[0].boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # Convert to integer values
                    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2  # Calculate mid point of bounding box
                    f.write(f"{mid_x}, {mid_y}\n")  # Write mid point coordinates tofile
                
    # Release video capture object and close all frames
    cap.release()
    cv2.destroyAllWindows()

    print(f"Mid point coordinates saved to: {output_filename}" if os.path.exists(output_filename) else "")  # Conditional print for coordinates file


if __name__ == '__main__':
    # Example usage:
    # Load video
    video_path = "C:/Users/navee/OneDrive/Desktop/test/1.mp4"
    # File paths
    save_path = "last_frame.jpg"
    coordinates_file_path = os.path.splitext(os.path.basename(video_path))[0] + '_coordinates.txt'
    last_frame_path = "last_frame.jpg"

    '''# Multiprocessing
    p1 = multiprocessing.Process(target=detect_and_track, args=(video_path, coordinates_file_path))
    p2 = multiprocessing.Process(target=split_video_last_frame, args=(video_path, save_path))
    p1.start()
    p2.start()
    p1.join()
    p2.join()'''

    # Call the function to color pixels in the last frame
    #colored_last_frame = color_pixels_last_frame(last_frame_path, coordinates_file_path)

    # Save the modified last frame
   # cv2.imwrite("colored_last_frame.jpg", colored_last_frame)
    # Show the image
   # cv2.imshow("Colored last frame", colored_last_frame)
    #cv2.waitKey(0)

    print("Colored last frame saved as 'colored_last_frame.jpg'.")
