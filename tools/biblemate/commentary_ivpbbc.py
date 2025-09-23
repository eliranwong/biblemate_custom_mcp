TOOL_SYSTEM = ""
TOOL_SCHEMA = {}
TOOL_DESCRIPTION = """Read bible commentary - IVP Bible Background Commentary (IVPBBC)."""

def commentary_ivpbbc(messages, **kwargs):
    from biblemate.uba.api import run_uba_api
    from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser

    command = messages[-1].get("content", "")
    command = BibleVerseParser(False).extractAllReferencesReadable(command)
    if not command:
        print("Please provide a valid Bible reference to complete your request.")
        return ""
    for ref in command.split("; "):
        print(f"## Commentary - IVPBBC - {ref}")

        command = f"COMMENTARY:::IVPBBC:::{ref}"

        output = run_uba_api(command)
        print(output)
    
    return ""

TOOL_FUNCTION = commentary_ivpbbc