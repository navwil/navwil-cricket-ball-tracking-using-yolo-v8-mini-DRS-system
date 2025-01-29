# Cricket Ball Tracking using YOLOv8

This project uses **YOLOv8** to detect and track a cricket ball in a video, predicting its trajectory. It serves as a mini **Decision Review System (DRS)** implemented with **OpenCV** for visualization.

## Features

- **Accurate Ball Tracking**: Leverages YOLOv8 for precise ball detection and tracking throughout the video.
- **Trajectory Prediction**: Predicts the ball's future path using a linear regression model based on its historical movement.
- **Clear Visualization**: Overlays the tracked path and predicted trajectory on the video, providing a clear visual representation.
- **DRS Simulation**: Mimics a DRS system by analyzing the ball's trajectory to predict its potential impact point.

## Installation and Usage

### Clone the repository:
```bash
git clone https://github.com/your-username/cricket-ball-tracking.git
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the main script:
```bash
python main.py
```
This will process the video, track the ball, and output a video with the visualized trajectory.

## Project Structure
```
cricket-ball-tracking/
│── main.py            # Core script for ball tracking and visualization
│── model/             # Stores the YOLOv8 model weights
│── data/              # Directory for input and output videos
│── requirements.txt   # Required dependencies
│── README.md          # Project documentation
```

## Future Enhancements

- **Improved Prediction**: Implement more sophisticated models for enhanced trajectory prediction accuracy.
- **Advanced Analysis**: Add features to analyze ball speed, spin, and bounce.
- **User Interface**: Develop a user-friendly interface for easier interaction and visualization.

## Contributing

Contributions are welcome! Feel free to submit **pull requests** or open **issues** for any improvements or bug fixes.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
