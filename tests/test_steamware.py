import subprocess
import os
import pytest

@pytest.fixture
def export_dir():
    """Fixture to provide the export directory and ensure it exists."""
    export_path = "./exports"
    os.makedirs(export_path, exist_ok=True)
    yield export_path
    # Cleanup after tests (optional)
    for file in os.listdir(export_path):
        os.remove(os.path.join(export_path, file))

def test_generate_basic_part(export_dir):
    """Test generating a basic part using the steamware.py script."""
    result = subprocess.run(
        [
            "python3", "steamware.py",
            "--en", "example_part",
            "--ed", export_dir,
            "--bu", "10",
            "--fp", "0.134",
            "--mt", "O",
            "--ts", "XXSXXX"
        ],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script failed with error: {result.stderr}"
    assert os.path.exists(f"{export_dir}/example_part.scad"), "SCAD file not generated"
    assert os.path.exists(f"{export_dir}/example_part.stl"), "STL file not generated"
    assert os.path.exists(f"{export_dir}/example_part.png"), "PNG file not generated"

def test_generate_cross_shape(export_dir):
    """Test generating a cross shape using the steamware.py script."""
    result = subprocess.run(
        [
            "python3", "steamware.py",
            "--en", "cross",
            "--ed", export_dir,
            "--bu", "10",
            "--fp", "0.134",
            "--ts", "XXXXAAYYBBBB"
        ],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script failed with error: {result.stderr}"
    assert os.path.exists(f"{export_dir}/cross.scad"), "SCAD file not generated"
    assert os.path.exists(f"{export_dir}/cross.stl"), "STL file not generated"
    assert os.path.exists(f"{export_dir}/cross.png"), "PNG file not generated"