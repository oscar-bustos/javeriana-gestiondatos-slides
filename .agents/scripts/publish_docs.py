import os
import shutil
import subprocess

def main():
    # Obtener el directorio donde está este script (.agents/scripts/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # La raíz del workspace está dos niveles arriba de .agents/scripts/
    workspace_root = os.path.dirname(os.path.dirname(script_dir))
    
    quarto_dir = os.path.join(workspace_root, 'quarto')
    docs_dir = os.path.join(workspace_root, 'docs')

    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    # 1. Compile all presentations using compile_quarto.py
    print("Compiling presentations...")
    subprocess.run(["python", "compile_quarto.py"], cwd=script_dir)

    # 2. Move them to docs/ and collect presentation info
    print("\nOrganizing docs/ folder...")
    presentations = []

    # Sort items so they appear in order
    items = sorted(os.listdir(quarto_dir))
    for item in items:
        item_path = os.path.join(quarto_dir, item)
        if os.path.isdir(item_path):
            index_html = os.path.join(item_path, 'index.html')
            if os.path.exists(index_html):
                dest_file = os.path.join(docs_dir, f"{item}.html")
                shutil.copy2(index_html, dest_file)
                print(f"Copied {item}/index.html -> docs/{item}.html")
                
                # Format a nice title
                title = item.replace('_', ' ').title()
                # Special formatting for common words
                title = title.replace('Big Data', 'Big Data').replace('De', 'de').replace('Sin', 'sin')
                presentations.append((f"docs/{item}.html", title))

    # 3. Create a premium index.html in the root directory (workspace root)
    index_path = os.path.join(workspace_root, 'index.html')
    
    # Generate cards HTML
    cards_html = ""
    for idx, (file_path, title) in enumerate(presentations, 1):
        cards_html += f"""
            <div class="card">
                <div class="card-content">
                    <div class="card-num">Tema {idx:02d}</div>
                    <h2 class="card-title">{title}</h2>
                </div>
                <a href="{file_path}" class="card-link">
                    Ver Diapositivas
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                        <polyline points="12 5 19 12 12 19"></polyline>
                    </svg>
                </a>
            </div>"""

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestión de Datos - Presentaciones</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0b0f19;
            --card-bg: rgba(22, 30, 49, 0.7);
            --card-border: rgba(255, 255, 255, 0.08);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent-primary: #6366f1;
            --accent-secondary: #a855f7;
            --accent-glow: rgba(99, 102, 241, 0.15);
        }}
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            padding: 5rem 2rem;
            overflow-x: hidden;
            position: relative;
        }}

        /* Ambient background glow */
        body::before {{
            content: '';
            position: absolute;
            top: -10%;
            left: 50%;
            transform: translateX(-50%);
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, rgba(168, 85, 247, 0.05) 50%, transparent 100%);
            z-index: -1;
            pointer-events: none;
            filter: blur(80px);
        }}

        .container {{
            max-width: 1040px;
            width: 100%;
            z-index: 1;
        }}

        header {{
            text-align: center;
            margin-bottom: 5rem;
        }}

        h1 {{
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #a5b4fc 0%, #c084fc 50%, #818cf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            letter-spacing: -0.03em;
        }}

        .subtitle {{
            color: var(--text-secondary);
            font-size: 1.25rem;
            font-weight: 400;
            max-width: 600px;
            margin: 0 auto;
            letter-spacing: -0.01em;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }}

        .card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 24px;
            padding: 2.5rem 2rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(12px);
        }}

        .card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.03) 0%, rgba(168, 85, 247, 0.03) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }}

        .card:hover {{
            transform: translateY(-6px);
            border-color: rgba(99, 102, 241, 0.3);
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5), 0 0 20px 0 var(--accent-glow);
        }}

        .card:hover::before {{
            opacity: 1;
        }}

        .card-content {{
            position: relative;
            z-index: 2;
            margin-bottom: 2.5rem;
        }}

        .card-num {{
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            color: var(--accent-primary);
            margin-bottom: 1rem;
        }}

        .card-title {{
            font-size: 1.5rem;
            font-weight: 700;
            line-height: 1.35;
            color: var(--text-primary);
            letter-spacing: -0.01em;
        }}

        .card-link {{
            position: relative;
            z-index: 2;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            color: var(--text-primary);
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
            padding: 0.85rem 1.5rem;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            transition: all 0.3s ease;
            width: 100%;
            justify-content: center;
            letter-spacing: -0.01em;
        }}

        .card:hover .card-link {{
            background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
            border-color: transparent;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.25);
        }}

        .card-link svg {{
            transition: transform 0.3s ease;
        }}

        .card:hover .card-link svg {{
            transform: translateX(4px);
        }}

        @media (max-width: 640px) {{
            body {{
                padding: 3rem 1.5rem;
            }}
            h1 {{
                font-size: 2.5rem;
            }}
            .subtitle {{
                font-size: 1.1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Gestión de Datos</h1>
            <p class="subtitle">Material de clase y presentaciones interactivas</p>
        </header>
        <div class="grid">
            {cards_html}
        </div>
    </div>
</body>
</html>"""

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"Created index page at index.html")
    print("Done! The repository is ready for GitHub Pages (serving from root).")

if __name__ == "__main__":
    main()
