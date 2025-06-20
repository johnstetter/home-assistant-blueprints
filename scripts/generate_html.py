#!/usr/bin/env python3
import json
import os

def generate_html(index_path="site/blueprint_index.json", output_path="site/index.html"):
    with open(index_path, "r") as f:
        blueprints = json.load(f)

    html = f"""
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>🧠 John Stetter’s Home Assistant Blueprints</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f7f7fa; color: #222; margin: 0; padding: 0; }}
        header {{ background: #222; color: #fff; padding: 2rem 1rem 1rem 1rem; text-align: center; }}
        h1 {{ margin: 0; font-size: 2.5rem; }}
        .subtitle {{ font-size: 1.2rem; color: #b3b3b3; margin-bottom: 1rem; }}
        main {{ max-width: 900px; margin: 2rem auto; background: #fff; border-radius: 10px; box-shadow: 0 2px 8px #0001; padding: 2rem; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 1.5rem; }}
        th, td {{ padding: 0.75rem; border-bottom: 1px solid #eee; text-align: left; }}
        th {{ background: #f0f0f5; }}
        tr:hover {{ background: #f9f9ff; }}
        .import-link {{ color: #0078d7; text-decoration: none; font-weight: bold; }}
        .import-link:hover {{ text-decoration: underline; }}
        .footer {{ text-align: center; color: #888; margin-top: 2rem; font-size: 0.95rem; }}
        .emoji {{ font-size: 1.2em; }}
    </style>
</head>
<body>
    <header>
        <h1>🧠 John Stetter’s Home Assistant Blueprints</h1>
        <div class=\"subtitle\">A developer playground for automations.  This is mostly an experiment for agent-based copilot development".</div>
    </header>
    <main>
        <p>Welcome! This is an <b>automagically generated</b> index of all published blueprints. Use, fork, break, or improve them. PRs and bug reports welcome. 🚀</p>
        <table>
            <tr>
                <th>Name</th>
                <th>Domain</th>
                <th>Description</th>
                <th>Import</th>
            </tr>
"""
    for bp in blueprints:
        name = bp["name"]
        domain = bp["domain"]
        description = bp["description"]
        path = bp["path"]
        raw_url = f"https://raw.githubusercontent.com/johnstetter/home-assistant-blueprints/main/{path}"
        html += f"            <tr>\n                <td><b>{name}</b></td>\n                <td><code>{domain}</code></td>\n                <td>{description}</td>\n                <td><a class='import-link' href='{raw_url}'>Import</a></td>\n            </tr>\n"
    html += """
        </table>
        <div class='footer'>
            <span class='emoji'>🤓</span> Built with <code>python</code>, <code>yaml</code>, and a dash of automation. <br>
            <a href='https://github.com/johnstetter/home-assistant-blueprints'>View on GitHub</a>
        </div>
    </main>
</body>
</html>
"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(html)

if __name__ == "__main__":
    generate_html()
