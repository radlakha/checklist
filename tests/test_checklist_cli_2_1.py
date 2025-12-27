import datetime
import subprocess
import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_read_checklist_uses_double_slash_separator_and_skips_comments(tmp_path):
    """\
    Plan 2.1.2: checklist.read_checklist should parse filenames and optional
    due dates using " // " as the separator, and ignore comment lines
    starting with '#'.
    """
    checklist_content = """\
# This is a comment and should be ignored
ITR - FY2019-20 - 01a - Investment Proof Submission Form (12 BB).xls // 2023-12-01
ITR - FY2019-20 - 02a - H801 NOC from Spouse.DOC
Some-file-name-with-hyphens - and spaces.pdf // 2024-01-15
"""
    checklist_path = tmp_path / "checklist.txt"
    checklist_path.write_text(checklist_content)

    # Import the new main module we will create for 2.1.
    import checklist

    entries = checklist.read_checklist(str(checklist_path))

    # We expect 3 non-comment entries.
    assert len(entries) == 3

    first_name, first_due = entries[0]
    assert first_name == "ITR - FY2019-20 - 01a - Investment Proof Submission Form (12 BB).xls"
    assert isinstance(first_due, datetime.date)
    assert first_due == datetime.date(2023, 12, 1)

    second_name, second_due = entries[1]
    assert second_name == "ITR - FY2019-20 - 02a - H801 NOC from Spouse.DOC"
    assert second_due is None

    third_name, third_due = entries[2]
    # Hyphens in the filename must not confuse the due-date parsing.
    assert third_name == "Some-file-name-with-hyphens - and spaces.pdf"
    assert isinstance(third_due, datetime.date)
    assert third_due == datetime.date(2024, 1, 15)


def test_read_checklist_raises_value_error_on_malformed_due_date(tmp_path):
    """\
    When a due date is present but malformed, checklist.read_checklist should
    fail fast with a clear ValueError mentioning the bad date string.
    """
    checklist_content = """\
Valid file // 2024-01-15
Bad date file // 2024-13-40
"""
    checklist_path = tmp_path / "checklist.txt"
    checklist_path.write_text(checklist_content)

    import checklist

    with pytest.raises(ValueError) as excinfo:
        checklist.read_checklist(str(checklist_path))

    message = str(excinfo.value)
    assert "2024-13-40" in message
    assert "Invalid due date" in message


@pytest.mark.parametrize("flag", ["--help", "-h"])
def test_checklist_cli_help_mentions_core_flags(flag):
    """\
    Plan 2.1.1: checklist.py should expose the core flags via argparse, and
    --help/-h should mention them in the usage text.

    At this stage we only assert argument wiring and help text, not the full
    behavior of each flag (which will be covered in later plan sections).
    """
    result = subprocess.run(
        [sys.executable, "checklist.py", flag],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    stdout = result.stdout

    # Core flags from plan section 2.1.1
    for expected in [
        "--status",
        "--missing",
        "--add",
        "--remove",
        "--folder",
        "--due",
    ]:
        assert expected in stdout
