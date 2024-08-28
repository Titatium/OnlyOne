# This module is optional and depends on your choice of text formatting library

# Using 'colored' library
try:
    import colored

    def color_text(text, color):
        """Adds color to text using the 'colored' library."""
        return colored.stylize(text, colored.fg(color))

except ImportError:
    def color_text(text, color):
        """Fallback if 'colored' is not installed."""
        return text  # No color formatting

# Using 'rich' library
try:
    from rich import print
    from rich.text import Text

    def format_text(text, style):
        """Applies rich text formatting using the 'rich' library."""
        rich_text = Text(text)
        rich_text.stylize(style)
        print(rich_text)

except ImportError:
    def format_text(text, style):
        """Fallback if 'rich' is not installed."""
        print(text)  # No rich text formatting
