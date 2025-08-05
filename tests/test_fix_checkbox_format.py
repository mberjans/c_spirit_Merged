import sys
from pathlib import Path

module_path = Path(__file__).resolve().parents[1] / "docs"
if str(module_path) not in sys.path:
    sys.path.append(str(module_path))

import fix_checklist_format


def test_fix_checkbox_format(tmp_path):
    input_file = tmp_path / "input.md"
    output_file = tmp_path / "output.md"
    lines = ["* [ ] one\n", "- [ ] two\n", "* \\[ \\] three\n", "no box\n"]
    with open(input_file, "w") as handle:
        for item in lines:
            handle.write(item)
    fix_checklist_format.fix_checkbox_format(str(input_file), str(output_file))
    with open(output_file, "r") as handle:
        result_lines = handle.readlines()
    assert result_lines[0].startswith("- [ ]")
    assert result_lines[1].startswith("- [ ]")
    assert result_lines[2].startswith("- [ ]")
    assert result_lines[3] == "no box\n"
