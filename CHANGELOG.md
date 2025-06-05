# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2024-12-19

### Added
- Initial release of VCS Metrics library
- Core VCS (Video Comprehension Score) computation
- Global Alignment Score (GAS) implementation
- Local Alignment Score (LAS) implementation  
- Narrative Alignment Score (NAS) implementation with:
  - Distance-based NAS (NAS-D)
  - Line-based NAS (NAS-L)
  - Window regularization
- Comprehensive visualization suite:
  - Configuration display
  - Text chunk visualization
  - Similarity matrix heatmaps
  - Mapping windows visualization
  - Best match details
  - LAS visualizations
  - Distance and line-based NAS plots
  - Window regularizer analysis
  - Metrics summary dashboard
- PDF report generation with customizable content
- Flexible configuration system
- Support for custom segmentation and embedding functions
- Local Chronology Tolerance (LCT) for narrative flow analysis
- Context window controls for alignment refinement

### Features
- Compatible with Python 3.8+
- Supports PyTorch-based embedding functions
- Matplotlib and Seaborn visualizations
- Comprehensive documentation and examples
- Type hints throughout the codebase
- Modular architecture for extensibility

### Dependencies
- numpy >= 1.20.0
- torch >= 1.9.0
- matplotlib >= 3.5.0
- seaborn >= 0.11.0