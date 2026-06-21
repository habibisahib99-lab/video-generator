"""
Core video generation logic
"""

import os
from pathlib import Path
from moviepy.editor import ImageClip, concatenate_videoclips
from .effects import get_effect


class VideoGenerator:
    """Generate videos from images"""
    
    def __init__(self, input_path, output_path, duration=5, fps=30, effect='none'):
        """
        Initialize the video generator
        
        Args:
            input_path (str): Path to input image
            output_path (str): Path to output video
            duration (float): Video duration in seconds
            fps (int): Frames per second
            effect (str): Effect to apply (none, zoom, pan, fade)
        """
        self.input_path = input_path
        self.output_path = output_path
        self.duration = duration
        self.fps = fps
        self.effect = effect
        
        # Validate input file
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input image not found: {input_path}")
    
    def generate(self):
        """Generate the video"""
        # Get the effect
        effect = get_effect(self.effect, self.input_path, self.duration, self.fps)
        
        # Create video clip from image with effect
        clip = ImageClip(self.input_path).set_duration(self.duration)
        
        # If effect is not 'none', we need to apply frame-by-frame processing
        if self.effect != 'none':
            self._generate_with_effect(effect)
        else:
            # For no effect, just use moviepy's simple approach
            clip.write_videofile(
                self.output_path,
                fps=self.fps,
                verbose=False,
                logger=None
            )
    
    def _generate_with_effect(self, effect):
        """Generate video with frame-by-frame effects"""
        import numpy as np
        from PIL import Image
        import cv2
        
        # Get image dimensions
        img = Image.open(self.input_path)
        width, height = img.size
        
        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_path, fourcc, self.fps, (width, height))
        
        # Generate frames
        total_frames = int(self.duration * self.fps)
        
        for frame_num in range(total_frames):
            # Get frame with effect applied
            frame = effect.get_frame(frame_num)
            
            # Convert RGB to BGR for OpenCV
            if len(frame.shape) == 3 and frame.shape[2] == 3:
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            else:
                frame_bgr = frame
            
            # Write frame
            out.write(frame_bgr.astype(np.uint8))
        
        # Release the video writer
        out.release()
