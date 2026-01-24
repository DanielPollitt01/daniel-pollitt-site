import os
import re
import sys
import yaml
import subprocess
from pathlib import Path
from datetime import datetime

# Paths
SITE_ROOT = Path("/home/dan/projects/active/resume_website")
PACK_PATH = Path("/home/dan/projects/packs/ai_image_generation")
PACK_CLI = PACK_PATH / "src/cli/main.py"
VENV_PYTHON = PACK_PATH / "venv/bin/python3"
BLOG_HTML_PATH = SITE_ROOT / "blog.html"

def run_image_gen(prompt, style, name):
    """Calls the AI image generation CLI and returns the final filename."""
    print(f"Generating image for: {name}...")
    cmd = [
        str(VENV_PYTHON),
        str(PACK_CLI),
        "generate",
        "--style", style,
        "--scene", prompt,
        "--output", str(SITE_ROOT),
        "--name", name
    ]
    
    # Run the generator
    result = subprocess.run(cmd, cwd=str(PACK_PATH), capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error generating image: {result.stderr}")
        return None

    # Find the created file (it has a timestamp)
    # The CLI prints "Saved: /path/to/file_timestamp_001.png"
    match = re.search(r"Saved: (.*\.png)", result.stdout)
    if match:
        tmp_path = Path(match.group(1))
        final_path = SITE_ROOT / f"{name}.png"
        if tmp_path.exists():
            tmp_path.rename(final_path)
            print(f"Image saved and renamed to: {final_path.name}")
            return final_path.name
    return None

def parse_markdown(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Split frontmatter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        raise ValueError("Invalid Markdown format. Ensure frontmatter is present.")
    
    frontmatter = yaml.safe_load(parts[1])
    body = parts[2].strip()
    
    return frontmatter, body

def convert_to_html(text):
    # Simple custom markdown to HTML conversion
    # Paragraphs
    text = re.sub(r'\n\n', '</p><p>', text)
    text = f"<p>{text}</p>"
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    return text

def process_blog_post(md_path):
    frontmatter, body = parse_markdown(md_path)
    slug = Path(md_path).stem
    style = frontmatter.get('style', 'hiromix')
    
    # 1. Generate Master Image
    master_prompt = frontmatter.get('master_image_prompt')
    master_image = None
    if master_prompt:
        master_image = run_image_gen(master_prompt, style, f"blog-{slug}-master")

    # 2. Handle Embedded Images
    def replace_gen_tag(match):
        prompt = match.group(1)
        img_name = f"blog-{slug}-img-{hash(prompt) % 10000}"
        final_img = run_image_gen(prompt, style, img_name)
        if final_img:
            return f'</p><div class="post-embedded-image"><img src="{final_img}" alt="Embedded visual" style="width: 100%; height: auto; margin: 1rem 0; border: 1px solid var(--border-light);"></div><p>'
        return ""

    body_with_images = re.sub(r'\[\[generate: "(.*?)"\]\]', replace_gen_tag, body)
    
    # 3. Convert Body to HTML
    html_content = convert_to_html(body_with_images)
    # Add Date at the top if present
    if frontmatter.get('date'):
        html_content = f"<p><em>{frontmatter['date']}</em></p>" + html_content

    # 4. Prepare the Data for blog.html
    post_data = {
        'title': frontmatter['title'],
        'marginNotes': frontmatter.get('margin_notes', []),
        'content': html_content.replace('\n', ' ')
    }
    if master_image:
        post_data['image'] = master_image

    return slug, post_data

def update_blog_html(slug, post_data):
    with open(BLOG_HTML_PATH, 'r') as f:
        lines = f.readlines()

    new_lines = []
    in_blog_posts = False
    list_updated = False
    
    # We'll use a simple state machine to find the right places to inject
    for line in lines:
        # Inject into blogPosts object
        if "const blogPosts = {" in line:
            new_lines.append(line)
            # Create the entry
            entry = f"            '{slug}': {{\n"
            entry += f"                title: {repr(post_data['title'])},\n"
            entry += f"                marginNotes: {repr(post_data['marginNotes'])},\n"
            entry += f"                content: `{post_data['content']}`\n"
            entry += "            },\n"
            new_lines.append(entry)
            in_blog_posts = True
            continue
        
        # Inject into interactive-list
        if '<ol class="interactive-list">' in line and not list_updated:
            new_lines.append(line)
            img_attr = f' data-image="{post_data["image"]}"' if 'image' in post_data else ''
            new_item = f'                    <li class="interactive-list-item">\n'
            new_item += f'                        <a href="#" data-post="{slug}"{img_attr}>{post_data["title"]}</a>\n'
            new_item += f'                    </li>\n'
            new_lines.append(new_item)
            list_updated = True
            continue
            
        new_lines.append(line)

    with open(BLOG_HTML_PATH, 'w') as f:
        f.writelines(new_lines)
    print(f"Successfully updated {BLOG_HTML_PATH}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 create_blog.py path/to/post.md")
        sys.exit(1)
        
    md_file = sys.argv[1]
    slug, post_data = process_blog_post(md_file)
    update_blog_html(slug, post_data)
