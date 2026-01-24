# Daniel's Resume Website

A minimalist, high-performance static resume website built with vanilla HTML5, CSS3, and ES6+ JavaScript.

## Features
- **Unified Layout System**: Consistent grid-based design across all pages.
- **Interactive Professional Journey**: Hover-activated snapshots of roles and experiences.
- **Dynamic Blog**: SPA-style blog with margin notes and integrated AI image generation.

## Workflows

### Automated Blog Creation
To create a new blog post with integrated AI image generation:

1. **Draft**: Create a Markdown file in `content/posts/` (e.g., `my-post.md`).
2. **Frontmatter**: Ensure the file has YAML frontmatter:
   ```yaml
   title: "Post Title"
   date: "YYYY-MM-DD"
   style: "hiromix"
   master_image_prompt: "Description for the hover preview image"
   margin_notes:
     - "Note 1"
     - "Note 2"
   ```
3. **Execute**:
   ```bash
   source /home/dan/projects/packs/ai_image_generation/venv/bin/activate
   python3 scripts/create_blog.py content/posts/my-post.md
   ```

### AI Image Integration
For manual image generation and integration:
- See `AGENTS.md` for detailed CLI commands and integration patterns.

## Development
- Local Server: `python3 -m http.server 8000`
- Validation: `npx html-validator *.html`
