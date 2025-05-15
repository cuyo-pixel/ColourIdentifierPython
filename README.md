# Real-Time Color Identification System with Texture Overlay  
**Computer Vision Thesis Project** - Universidad de Murcia (2019)

## 🔍 About the Project
Computer vision system developed as a Computer Engineering thesis project that:
- Identifies colors in real-time using custom HSV thresholds
- Overlays dynamic textures (lines/characters) on detected objects
- Provides visual feedback for color recognition assistance

## 🚀 Key Features
### Color Processing
- 6 predefined HSV ranges (blue, green, magenta, etc.)
- Luminance analysis (V channel) with recommendations
- Dynamic threshold adjustment via trackbars

### Texture Synthesis
- **Overlay modes**:
  - Angular gradient lines (6 orientations: 0°-90°)
  - Character patterns (*, +, o, ., -, !)
- Adjustable texture thickness (1-3px)

### Performance
- Real-time processing at 640×480@30FPS
- Optimized matrix operations with NumPy
- Compatible with multiple USB cameras

## 📥 Installation
### Requirements
- Python 3.8+
- OpenCV 4.5+ (`pip install opencv-python-headless`)
- NumPy 1.21+ (`pip install numpy`)

```bash
git clone https://github.com/your-username/ColorIdentifier.git
cd ColorIdentifier
python color_identifier.py
