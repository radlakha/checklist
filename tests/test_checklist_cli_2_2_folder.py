import subprocess
import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_cli_status_uses_cwd_checklist_when_folder_not_given(tmp_path):
    """\
    Plan 2.2 / 2.1.2: when --folder is not provided, checklist.py should
    treat the current working directory as the designated folder and read
    checklist.txt from there.
    """
    checklist_content = """\
Example file without date
Example file with date // 2025-01-01
"""
    (tmp_path / "checklist.txt").write_text(checklist_content)

    # Run checklist.py from the temp directory, pointing to the real script
    # by absolute path so that cwd inside the program is tmp_path.
    script_path = PROJECT_ROOT / "checklist.py"
    result = subprocess.run(
        [sys.executable, str(script_path), "--status"],
        cwd=tmp_path,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    stdout_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]

    # We expect both entries to be printed, one with a due date, one without.
    assert "Example file without date - No due date" in stdout_lines[0]
    assert "Example file with date - Due: 2025-01-01" in stdout_lines[1]


def test_cli_status_uses_folder_option_for_checklist(tmp_path):
    """\
    Plan 2.2.1: when --folder is provided, checklist.py should read
    <folder>/checklist.txt regardless of the current working directory.
    """
    designated = tmp_path / "designated"
    designated.mkdir()

    checklist_content = """\
Folder-specific file // 2025-02-02
"""
    (designated / "checklist.txt").write_text(checklist_content)

    script_path = PROJECT_ROOT / "checklist.py"
    # Run from the project root, but point --folder to our designated dir.
    result = subprocess.run(
        [sys.executable, str(script_path), "--status", "--folder", str(designated)],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    stdout_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]

    assert "Folder-specific file - Due: 2025-02-02" in stdout_lines[0]


def test_cli_defaults_to_status_when_no_flags_given(tmp_path):
    """\
    When no flags are provided (no --status, no --folder), the default
    behavior should be equivalent to --status using the current working
    directory.
    """
    checklist_content = """\
Default file // 2025-03-03
"""
    (tmp_path / "checklist.txt").write_text(checklist_content)

    script_path = PROJECT_ROOT / "checklist.py"
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=tmp_path,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    stdout_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]

    assert "Default file - Due: 2025-03-03" in stdout_lines[0]


def test_cli_defaults_to_status_when_only_folder_given(tmp_path):
    """\
    When only --folder is provided (no explicit --status), the default
    behavior should still be equivalent to --status for that folder.
    """
    designated = tmp_path / "default-folder"
    designated.mkdir()

    checklist_content = """\
Folder-only default file // 2025-04-04
"""
    (designated / "checklist.txt").write_text(checklist_content)

    script_path = PROJECT_ROOT / "checklist.py"
    result = subprocess.run(
        [sys.executable, str(script_path), "--folder", str(designated)],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    stdout_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]

    assert "Folder-only default file - Due: 2025-04-04" in stdout_lines[0]
