"""
mkViewer Package

A package for 3D medical image visualization.

This package contains tools for viewing 3D medical images in various formats
including .npy, .raw, .nii, and .nii.gz.

Main components:
- Viewer3D: A class for interactive 3D image visualization

(C) Marek Kocinski
"""

from .mkViewer1 import Viewer3D

__version__ = '0.3'
__author__ = 'Marek Kocinski'
__all__ = ['Viewer3D'] 