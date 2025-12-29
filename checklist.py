import argparse
import datetime
from pathlib import Path
from typing import List, Optional, Tuple


ChecklistEntry = Tuple[str, Optional[datetime.date]]


def read_checklist(path: str) -> List[ChecklistEntry]:
    """Read checklist entries from a file.

    Expected line formats:
    - "<file name> // YYYY-MM-DD"
    - "<file name>" (no due date)

    Lines starting with '#' or that are empty are ignored.
    """
    entries: List[ChecklistEntry] = []
    with open(path, "r") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            file_name: str
            due_date: Optional[datetime.date]

            if " // " in line:
                name_part, date_part = line.rsplit(" // ", 1)
                file_name = name_part.strip()
                date_str = date_part.strip()
                if date_str:
                    # Fail fast with a clear error if the date is malformed.
                    try:
                        due_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                    except ValueError as exc:  # pragma: no cover - covered via higher-level test
                        raise ValueError(
                            f"Invalid due date '{date_str}' in checklist file {path}"
                        ) from exc
                else:
                    due_date = None
            else:
                file_name = line
                due_date = None

            entries.append((file_name, due_date))

    return entries


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="checklist",
        description=(
            "Checklist CLI for tracking expected documents in a folder. "
            "Created by Raman Adlakha and Vakya."
        ),
    )

    # Core flags from plan section 2.1.1
    parser.add_argument(
        "--status",
        action="store_true",
        help="Show checklist entries with their delivery status.",
    )
    parser.add_argument(
        "--missing",
        action="store_true",
        help="Show missing checklist entries.",
    )
    parser.add_argument(
        "--add",
        metavar="NAME",
        help="Add a new expected document to checklist.txt.",
    )
    parser.add_argument(
        "--remove",
        metavar="NAME",
        help="Remove an expected document from checklist.txt.",
    )
    parser.add_argument(
        "--folder",
        metavar="PATH",
        help="Operate on checklist.txt and files in the given folder (defaults to current directory).",
    )
    parser.add_argument(
        "--due",
        metavar="YYYY-MM-DD",
        help="Optional due date to use with --add (format YYYY-MM-DD).",
    )

    # These additional flags are defined now for completeness but their
    # behavior will be exercised in later plan sections.
    parser.add_argument(
        "--all",
        action="store_true",
        help="Show all checklist entries plus unknown files.",
    )
    parser.add_argument(
        "--delivered",
        action="store_true",
        help="Show delivered checklist entries only.",
    )
    parser.add_argument(
        "--unknown",
        action="store_true",
        help="Show files in the folder that are not in checklist.txt.",
    )

    return parser


def _status(folder: Path) -> int:
    """Print checklist entries for the given folder.

    For now this is a minimal implementation for plan section 2.2, using the
    simple "<name> - Due: <date>" / "<name> - No due date" format.
    """
    checklist_path = folder / "checklist.txt"
    entries = read_checklist(str(checklist_path))
    for name, due in entries:
        if due:
            print(f"{name} - Due: {due}")
        else:
            print(f"{name} - No due date")
    return 0


def main(argv: Optional[list] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    folder = Path(args.folder) if getattr(args, "folder", None) else Path.cwd()

    # For plan 2.2 we implement basic --status behavior with folder
    # selection, and make it the default when no other action flags are set.
    has_explicit_action = any(
        [
            args.status,
            getattr(args, "missing", False),
            getattr(args, "add", None),
            getattr(args, "remove", None),
            getattr(args, "all", False),
            getattr(args, "delivered", False),
            getattr(args, "unknown", False),
        ]
    )

    if args.status or not has_explicit_action:
        return _status(folder)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
