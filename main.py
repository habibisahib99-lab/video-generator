#!/usr/bin/env python3
"""
Video Generator - Convert images to videos with effects
"""

import click
import sys
from pathlib import Path
from video_generator.generator import VideoGenerator


@click.command()
@click.option(
    '--input', '-i',
    type=click.Path(exists=True),
    required=True,
    help='Path to input image file'
)
@click.option(
    '--output', '-o',
    type=click.Path(),
    default='output.mp4',
    help='Path to output video file (default: output.mp4)'
)
@click.option(
    '--duration', '-d',
    type=float,
    default=5,
    help='Video duration in seconds (default: 5)'
)
@click.option(
    '--fps', '-f',
    type=int,
    default=30,
    help='Frames per second (default: 30)'
)
@click.option(
    '--effect', '-e',
    type=click.Choice(['zoom', 'pan', 'fade', 'none']),
    default='none',
    help='Effect to apply (default: none)'
)
def generate_video(input, output, duration, fps, effect):
    """
    Generate a video from a static image with optional effects.
    
    Example:
        python main.py --input image.jpg --output video.mp4 --duration 5 --effect zoom
    """
    try:
        click.echo(f"🎬 Generating video from: {input}")
        click.echo(f"   Duration: {duration}s, FPS: {fps}, Effect: {effect}")
        
        generator = VideoGenerator(
            input_path=input,
            output_path=output,
            duration=duration,
            fps=fps,
            effect=effect
        )
        
        generator.generate()
        
        click.echo(f"✅ Video successfully created: {output}")
        
    except FileNotFoundError as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ Error generating video: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    generate_video()
