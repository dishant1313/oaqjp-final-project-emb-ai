"""
Root-level emotion detection module forwarding to EmotionDetection package.
"""
from EmotionDetection.emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
