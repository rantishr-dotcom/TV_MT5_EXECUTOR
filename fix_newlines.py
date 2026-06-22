from pathlib import Path

for file in Path("app").rglob("*.py"):
    try:
        text = file.read_text(encoding="utf-8")

        text = text.replace("}\\n", "}")
        text = text.replace("return True\\n", "return True")
        text = text.replace("return False\\n", "return False")
        text = text.replace("return result\\n", "return result")
        text = text.replace("return ticket\\n", "return ticket")
        text = text.replace("return trade\\n", "return trade")
        text = text.replace("return []\\n", "return []")
        text = text.replace(")\\n", ")")

        file.write_text(text, encoding="utf-8")

    except Exception as e:
        print(file, e)

print("DONE")