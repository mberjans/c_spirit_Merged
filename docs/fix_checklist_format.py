def _normalize_checkbox(line):
    """Return line with any leading checkbox marker normalized to '- [ ]'."""
    prefix_spaces = len(line) - len(line.lstrip())
    leading = line[:prefix_spaces]
    stripped = line[prefix_spaces:]
    if stripped.startswith("- [ ]"):
        return line
    marker = ""
    if stripped.startswith("*") or stripped.startswith("-"):
        marker = stripped[1:]
    else:
        return line
    trimmed = marker.lstrip()
    cleaned = trimmed.replace("\\[", "[").replace("\\]", "]")
    if cleaned.startswith("[ ]"):
        rest = cleaned[3:]
        return f"{leading}- [ ]{rest}"
    return line


def fix_checkbox_format(input_file, output_file):
    """
    Fix the checkbox format in the input file and write the corrected content to the output file.
    Correct format: "- [ ]"
    """
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        corrected_lines = []
        for line in lines:
            corrected_line = _normalize_checkbox(line)
            corrected_lines.append(corrected_line)

        with open(output_file, 'w') as outfile:
            outfile.writelines(corrected_lines)

        print(f"Checkbox format fixed and written to {output_file}")

    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "checklist.md"
    output_file = "new_checklist.md"
    fix_checkbox_format(input_file, output_file)
