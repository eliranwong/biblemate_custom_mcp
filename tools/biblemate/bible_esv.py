TOOL_SYSTEM = ""
TOOL_SCHEMA = {}
TOOL_DESCRIPTION = """Read ESV bible verses."""

def bible_esv(messages, **kwargs):
    from biblemate.uba.api import run_uba_api
    from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser
    import re

    command = messages[-1].get("content", "")
    command = BibleVerseParser(False).extractAllReferencesReadable(command)
    if not command:
        print("Please provide a valid Bible reference to complete your request.")
        return ""
    command = f"BIBLE:::ESVGSB:::{command}"
    print(run_uba_api(command))
    
    return ""

TOOL_FUNCTION = bible_esv