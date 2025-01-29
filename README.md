# Cricket Ball Tracking using YOLOv8

## Overview
This project leverages **YOLOv8** to accurately detect and track a cricket ball in video footage, predicting its trajectory in real time. Designed as a mini **Decision Review System (DRS)**, it integrates **OpenCV** for enhanced visualization and analysis.

## Key Features

- **Precision Ball Tracking**: Utilizes YOLOv8 to detect and track the cricket ball with high accuracy.
- **Trajectory Prediction**: Employs a linear regression model to forecast the ball’s future path based on historical movement.
- **Enhanced Visualization**: Overlays both the tracked path and predicted trajectory directly onto the video for better interpretation.
- **DRS Simulation**: Analyzes the ball's trajectory to estimate its impact point, mimicking professional DRS systems.

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/cricket-ball-tracking.git
cd cricket-ball-tracking
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Execute the Main Script
```bash
python main.py
```
This command processes the input video, tracks the ball, and outputs a new video with trajectory visualization.

## Project Structure
```
cricket-ball-tracking/
│── main.py            # Core script for ball tracking and visualization
│── model/             # Directory containing YOLOv8 model weights
│── data/              # Folder for input and output videos
│── requirements.txt   # List of dependencies
│── README.md          # Project documentation
```

## Future Enhancements

- **Advanced Prediction Models**: Integrate deep learning techniques for superior trajectory forecasting.
- **Comprehensive Ball Analysis**: Include additional features such as ball speed, spin rate, and bounce estimation.
- **User-Friendly Interface**: Develop an intuitive GUI for better interaction and visualization.

## Contribution Guidelines
We welcome contributions from the community! If you'd like to contribute, please follow these steps:
- Fork the repository
- Create a feature branch (`git checkout -b feature-branch`)
- Commit your changes (`git commit -m 'Add new feature'`)
- Push to the branch (`git push origin feature-branch`)
- Submit a pull request for review

## License

This project is licensed under the **MIT License**. For more details, please refer to the [LICENSE](LICENSE) file.
