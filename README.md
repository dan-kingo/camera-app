# Camera App - Grayscale Converter

A simple, elegant web-based camera application that captures photos and converts them to grayscale in real-time. Built with modern web technologies for a smooth user experience.


## 🖼️ Project Screenshots

### 🔐 Home Page
![Login Screenshot](https://res.cloudinary.com/dpm44ocft/image/upload/v1751784487/p3_q16tcw.png)

---

### 🏠 Camera Access
![Dashboard Screenshot](https://res.cloudinary.com/dpm44ocft/image/upload/v1751784485/p2_pfg4vu.png)

---

### 👤 Image to Grayscale
![Profile Screenshot](https://res.cloudinary.com/dpm44ocft/image/upload/v1751784489/p1_cy0i7n.png)

## ✨ Features

- **Real-time Camera Access**: Access your device's camera directly in the browser
- **Instant Grayscale Conversion**: Convert captured images to grayscale with a single click
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Download Functionality**: Save your grayscale images directly to your device
- **Privacy-First**: All processing happens locally in your browser - no data is sent to servers


## 🛠️ Technologies Used

- **HTML5**: Canvas API for image manipulation
- **CSS3**: Modern styling with responsive design
- **JavaScript**: Camera access and image processing
- **Python**: For functionality
- 

## 🏃‍♂️ Getting Started

### Prerequisites

- A modern web browser with camera support
- A device with a camera (webcam, phone camera, etc.)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dan-kingo/camera-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd camera-app
   ```

3. Open `index.html` in your web browser or serve it using a local server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   ```

4. Visit `http://localhost:8000` in your browser

## 📖 Usage

1. **Grant Camera Permission**: When prompted, allow the app to access your camera
2. **Capture Photo**: Click the "Take Photo" button to capture an image
3. **Convert to Grayscale**: Click "Convert to Grayscale" to apply the filter
4. **Download**: Save your grayscale image by clicking the "Download" button

## 🎯 How It Works

The app uses the following process:

1. **Camera Access**: Uses `navigator.mediaDevices.getUserMedia()` to access the device camera
2. **Image Capture**: Captures frames from the video stream onto an HTML5 canvas
3. **Grayscale Conversion**: Applies a grayscale filter by manipulating pixel data
4. **Download**: Converts the canvas to a blob and creates a downloadable link

## 🔧 Browser Compatibility

- ✅ Chrome 53+
- ✅ Firefox 36+
- ✅ Safari 11+
- ✅ Edge 12+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
