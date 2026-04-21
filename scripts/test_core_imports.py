#!/usr/bin/env python
"""Test script to verify all core module imports work correctly."""

import sys
import traceback
from pathlib import Path

# Add workspace to path
sys.path.insert(0, str(Path(__file__).parent))

# Track results
results = {
    "success": [],
    "failed": [],
}

def test_import(module_path):
    """Test importing a module and return True if successful."""
    try:
        __import__(module_path)
        results["success"].append(module_path)
        print(f"✓ {module_path}")
        return True
    except Exception as e:
        results["failed"].append((module_path, str(e)))
        print(f"✗ {module_path}")
        print(f"  Error: {str(e)[:100]}")
        return False

# Test core module imports
print("Testing core module imports...\n")

# Main core modules
core_modules = [
    "core",
    "core.args",
    "core.checkpoint",
    "core.distributed",
    "core.logger",
    "core.metrics",
    "core.optim",
    "core.probe",
    "core.profiling",
    "core.stool",
    "core.tokenizer",
    "core.transformer",
    "core.utils",
]

# Vision encoder modules
vision_encoder_modules = [
    "core.vision_encoder",
    "core.vision_encoder.config",
    "core.vision_encoder.pe",
    "core.vision_encoder.rope",
    "core.vision_encoder.tokenizer",
    "core.vision_encoder.transforms",
]

# Audio visual encoder modules
audio_visual_encoder_modules = [
    "core.audio_visual_encoder",
    "core.audio_visual_encoder.aligner",
    "core.audio_visual_encoder.audio_codec",
    "core.audio_visual_encoder.config",
    "core.audio_visual_encoder.pe",
    "core.audio_visual_encoder.patcher",
    "core.audio_visual_encoder.transforms",
    "core.audio_visual_encoder.transformer",
]

# Data modules
data_modules = [
    "core.data",
    "core.data.conversation",
    "core.data.data",
    "core.data.data_collators",
    "core.data.data_mixer",
    "core.data.dataloader",
    "core.data.preprocessor",
]

# Transform modules
transform_modules = [
    "core.transforms",
    "core.transforms.image_transform",
    "core.transforms.region_transform",
    "core.transforms.video_transform",
]

all_modules = (
    core_modules
    + vision_encoder_modules
    + audio_visual_encoder_modules
    + data_modules
    + transform_modules
)

print("Core modules:")
for module in core_modules:
    test_import(module)

print("\nVision encoder modules:")
for module in vision_encoder_modules:
    test_import(module)

print("\nAudio visual encoder modules:")
for module in audio_visual_encoder_modules:
    test_import(module)

print("\nData modules:")
for module in data_modules:
    test_import(module)

print("\nTransform modules:")
for module in transform_modules:
    test_import(module)

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"✓ Successful imports: {len(results['success'])}")
print(f"✗ Failed imports: {len(results['failed'])}")

if results["failed"]:
    print("\nFailed imports details:")
    for module, error in results["failed"]:
        print(f"\n  {module}:")
        print(f"    {error}")
    sys.exit(1)
else:
    print("\n✓ All core modules imported successfully!")
    sys.exit(0)
