TOOL_SYSTEM = ""
TOOL_SCHEMA = {}
TOOL_DESCRIPTION = """Read bible commentary - Cambridge Bible for Schools and Colleges [57 vol.] (CBSC)."""

def commentary_cbsc(messages, **kwargs):
    from biblemate.core.bible_db import run_uba_api
    from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser

    command = messages[-1].get("content", "")
    command = BibleVerseParser(False).extractAllReferencesReadable(command)
    if not command:
        print("Please provide a valid Bible reference to complete your request.")
        return ""
    for ref in command.split("; "):
        print(f"## Commentary - CBSC - {ref}")

        command = f"COMMENTARY:::CBSC:::{ref}"

        output = run_uba_api(command)
        print(output)
    
    return ""

TOOL_FUNCTION = commentary_cbsc