"""
Video effects for image-to-video conversion
"""

import numpy as np
from PIL import Image


class Effect:
    """Base class for video effects"""
    
    def __init__(self, image_path, duration, fps):
        self.image_path = image_path
        self.duration = duration
        self.fps = fps
        self.image = Image.open(image_path)
        self.image_array = np.array(self.image)
        self.total_frames = int(duration * fps)
    
    def get_frame(self, frame_number):
        """Get a frame for the given frame number"""
        raise NotImplementedError


class NoEffect(Effect):
    """No effect - static image stretched to video duration"""
    
    def get_frame(self, frame_number):
        """Return the same image for all frames"""
        return self.image_array


class ZoomEffect(Effect):
    """Zoom effect - gradually zoom in on the image"""
    
    def get_frame(self, frame_number):
        """Create a zoom effect by cropping and resizing"""
        progress = frame_number / self.total_frames
        
        # Calculate zoom factor (1.0 to 1.5)
        zoom_factor = 1.0 + (0.5 * progress)
        
        h, w = self.image_array.shape[:2]
        
        # Calculate crop size
        crop_h = int(h / zoom_factor)
        crop_w = int(w / zoom_factor)
        
        # Calculate crop position (center)
        y_start = (h - crop_h) // 2
        x_start = (w - crop_w) // 2
        
        # Crop image
        cropped = self.image_array[
            y_start:y_start + crop_h,
            x_start:x_start + crop_w
        ]
        
        # Resize back to original dimensions
        resized = Image.fromarray(cropped.astype('uint8')).resize((w, h))
        return np.array(resized)


class PanEffect(Effect):
    """Pan effect - gradually pan across the image"""
    
    def get_frame(self, frame_number):
        """Create a pan effect by shifting the image"""
        progress = frame_number / self.total_frames
        
        h, w = self.image_array.shape[:2]
        
        # Pan distance (move 20% of width)
        pan_distance = int(w * 0.2 * progress)
        
        # Create output array
        output = np.zeros_like(self.image_array)
        
        # Pan horizontally
        if pan_distance < w:
            output[:, pan_distance:] = self.image_array[:, :w - pan_distance]
        
        return output


class FadeEffect(Effect):
    """Fade effect - gradually fade in from black"""
    
    def get_frame(self, frame_number):
        """Create a fade-in effect"""
        progress = frame_number / self.total_frames
        
        # Fade in: multiply image by progress
        faded = (self.image_array.astype(float) * progress).astype(np.uint8)
        
        return faded


def get_effect(effect_name, image_path, duration, fps):
    """Factory function to get the appropriate effect"""
    effects = {
        'none': NoEffect,
        'zoom': ZoomEffect,
        'pan': PanEffect,
        'fade': FadeEffect,
    }
    
    effect_class = effects.get(effect_name, NoEffect)
    return effect_class(image_path, duration, fps)
