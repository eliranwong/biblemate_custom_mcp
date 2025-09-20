TOOL_SYSTEM = ""
TOOL_SCHEMA = {}
TOOL_DESCRIPTION = """Read NIV bible verses."""

def bible_niv(messages, **kwargs):
    from biblemate.core.bible_db import run_uba_api
    from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser
    import re

    command = messages[-1].get("content", "")
    command = BibleVerseParser(False).extractAllReferencesReadable(command)
    if not command:
        print("Please provide a valid Bible reference to complete your request.")
        return ""
    command = f"BIBLE:::NIV:::{command}"
    output = run_uba_api(command)
    print("- "+re.sub(r"\n\(", "\n- (", output))
    
    return ""

TOOL_FUNCTION = bible_niv