# mkViewer - 3D Medical Image Viewer

## Overview
mkViewer is a simple Python-based tool for visualizing 3D medical image data. It provides an interactive interface for exploring volumetric datasets such as MRI, CT scans, or any 3D image data stored in supported formats.

## Features
- Interactive slice-by-slice navigation through 3D volumes
- Maximum Intensity Projection (MIP) views along all three principal axes
- Additional visualization modes accessible via keyboard shortcuts:
  - `1`: Maximum Intensity Projection (MIP)
  - `2`: Mean value projection
  - `3`: Standard deviation projection
  - `4`: Minimum Intensity Projection (mIP)
- Customizable color maps via radio buttons
- Slice selection via slider or mouse wheel scrolling
- Reset functionality to return to the middle slice

## Supported File Formats
- NumPy arrays (`.npy`)
- NIfTI files (`.nii`, `.nii.gz`)
- Raw binary data (`.raw`, requires additional size and datatype parameters)

## Requirements
- Python 3.x
- NumPy
- Matplotlib
- NiBabel (for NIfTI file support)

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/marekkoc/mkViewer.git
   ```

2. Install the required dependencies:
   ```
   pip install numpy matplotlib nibabel
   ```

## Usage
### Basic Usage
```
python mkViewer1.py path/to/your/image_file.npy
```

### For NIfTI Files
```
python mkViewer1.py path/to/your/image_file.nii
python mkViewer1.py path/to/your/image_file.nii.gz
```

### For Raw Binary Files
```
python mkViewer1.py path/to/your/image_file.raw size datatype
```
Where:
- `size` is the cubic dimension (assuming equal dimensions)
- `datatype` is the numpy datatype (e.g., 'float32', 'uint16')

### Interface Controls
- **Slider**: Navigate through slices
- **Mouse wheel**: Scroll through slices
- **Radio buttons**: Change colormap
- **Reset button**: Return to the middle slice
- **Keyboard**:
  - `1`: Show Maximum Intensity Projections
  - `2`: Show Mean value projections
  - `3`: Show Standard Deviation projections
  - `4`: Show Minimum Intensity Projections

## Example
```python
import numpy as np
from mkViewer1 import Viewer3D

# Create a sample 3D array
data = np.random.rand(64, 64, 64)

# Launch the viewer
Viewer3D(data, "Sample Data")
```

## Author
- Marek Kocinski (marekkoc)

## Version History
- v0.01 (2015) - Initial release as mk_Viewer3D_ver1
- v0.02 (2016-06-10) - Updated as mkViewer1-v02.py
- v0.03 (2025-04-12) - Current version updated to work with newer library versions

## License
Copyright (C) Marek Kocinski

## Contributing
Contributions are welcome!