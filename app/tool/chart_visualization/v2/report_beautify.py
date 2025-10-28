from app.tool.chart_visualization.python_execute import NormalPythonExecute


class ReportBeautify(NormalPythonExecute):
    """A tool for transforming a basic health report into a professional, visually appealing final version."""

    name: str = "report_beautify"
    description: str = (
        "This tool should be called **LAST** in the workflow to perform final beautification of the data report.\n"
        "It will:\n"
        "1. Apply advanced styling and layout enhancements\n"
        "2. Add interactive elements and visual polish\n"
        "3. Ensure mobile responsiveness\n"
        "\n"
        "Key beautification features to implement:\n"
        "- colorful and fancy background and color scheme\n"
        "- Modern CSS styling with gradients and shadows\n"
        "- Font Awesome icons for visual cues\n"
        "- Animated progress bars for metrics\n"
        "- Card-based layout with hover effects\n"
        "- Responsive design for all devices\n"
        "- Scroll-triggered animations\n"
        "- Professional typography hierarchy\n"
        "\n"
        "## Output Requirements\n"
        "1. Generate **beautify_report.html** file\n"
        "2. Print the file path: print(report_path)"
    )

    parameters: dict = {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": (
                    "Python code that beautify the report:\n"
                    "1. CSS/JS enhancements for modern styling\n"
                    "2. Structure optimization for better readability\n"
                    "3. Mobile responsiveness adjustments\n"
                    "\n"
                    "Example tasks:\n"
                    "- Add Bootstrap 5 + Font Awesome\n"
                    "- Add metric cards with progress bars\n"
                    "- Create responsive tables"
                ),
            },
        },
        "required": ["code"],
    }
