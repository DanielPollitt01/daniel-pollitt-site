# AGENTS.md

## Build/Development Commands

```bash
# Local development servers
python3 -m http.server 8000          # Python simple server
npx serve .                         # Node.js serve package
live-server                         # Live reload server

# Code validation and linting
npx html-validator *.html           # HTML validation
npx stylelint styles.css            # CSS linting
npx axe index.html                  # Accessibility testing

# Manual testing checklist
- Navigation menu toggle functionality
- Responsive design (768px, 480px breakpoints)
- Keyboard navigation (Tab, Enter, Space, Escape)
- Screen reader compatibility
- Cross-browser compatibility
```

## Code Style Guidelines

### HTML Structure & Conventions
- **DOCTYPE & Meta**: Always include `<!DOCTYPE html>`, `lang="en"`, and viewport meta tag
- **Semantic HTML5**: Use `<header>`, `<main>`, `<section>`, `<nav>`, `<article>`, `<footer>` appropriately
- **Document Structure**: Navigation symbol + menu at end of body, main content in `.unified-container`
- **Titles**: Unique page titles following pattern "Daniel - PageName"
- **Script Placement**: All inline scripts before `</body>` tag
- **Accessibility**: ARIA attributes, roles, and semantic markup required
- **Links**: Use relative paths without leading slash (e.g., `href="about.html"`)
- **Cache Busting**: Link CSS with version parameter (e.g., `styles.css?v=1.6`)

### CSS Architecture & Design System
- **CSS Variables**: Define design tokens in `:root` using `--variable-name` pattern
- **Color Palette**: Primary green (`#4A7C59`), light green (`#7db59f`), dark green (`#3c8b5b`)
- **Typography**: JetBrains Mono font family, rem units for all spacing/typography
- **Responsive Design**: Mobile-first approach with breakpoints at 768px and 480px
- **Layout System**: 
  - `.unified-container` as main wrapper
  - `.traditional-content` for standard page layouts
  - `.left-content`/`.right-blurb` for projects page
  - CSS Grid and Flexbox for layouts
- **Component Patterns**: 
  - Navigation symbol (hamburger menu) fixed top-right
  - Interactive list items with hover states
  - Blog post layouts with margin notes
- **Utility Classes**: Spacing utilities (`.mt-2`, `.mb-2`, etc.), text utilities
- **Transitions**: Subtle `0.2s ease` transitions for hover states

### JavaScript Patterns & Conventions
- **Variable Declaration**: Use `const` by default, `let` only when reassignment needed
- **Event Handling**: 
  - Always use `e.stopPropagation()` for dropdown/click-outside functionality
  - Support keyboard navigation (Enter, Space for activation, Escape to close)
  - Use `addEventListener` over inline event handlers
- **DOM Manipulation**: 
  - Cache DOM element references in variables
  - Use `querySelector` and `querySelectorAll` for element selection
  - Manipulate classes using `classList.add()`, `classList.remove()`, `classList.toggle()`
- **Interactive Components**:
  - Navigation menu toggle with click-outside detection
  - Interactive hover states for list items
  - URL parameter handling for shareable states
  - Dynamic content loading with `innerHTML` templates
- **Error Handling**: Graceful fallbacks for missing elements/data
- **Performance**: Event delegation for multiple similar elements
- **Code Organization**: Small, page-specific scripts with clear functional separation

### Naming Conventions
- **CSS Classes**: kebab-case (`.nav-symbol`, `.blog-post-content`)
- **JavaScript Variables**: camelCase (const `navSymbol`, let `postImage`)
- **HTML Attributes**: kebab-case (`data-post`, `data-image`)
- **File Names**: Lowercase with hyphens (index.html, about.html, styles.css)

### Content & Data Patterns
- **Blog Posts**: Object structure with `title`, `content`, `date`, `marginNotes` arrays
- **Project Data**: Similar structure with `title`, `description`, `technologies`, etc.
- **Interactive Elements**: Use `data-*` attributes to associate elements with data
- **URL Management**: Use `URLSearchParams` for state management and shareable links

### Performance & Optimization
- **Image Loading**: Lazy loading with opacity transitions
- **CSS**: Minimize redundant selectors, use efficient class-based targeting
- **JavaScript**: Avoid global variables, use proper scoping
- **Cache Management**: Update CSS version number when making changes

### Accessibility Requirements
- **Keyboard Navigation**: All interactive elements must be keyboard accessible
- **Screen Readers**: Proper ARIA labels, roles, and semantic HTML
- **Focus Management**: Visible focus states, logical tab order
- **Color Contrast**: WCAG AA compliance for all text/background combinations
- **Alternative Text**: Meaningful alt text for all images

### Testing & Quality Assurance
- **Manual Testing**: Navigation, responsive design, accessibility
- **Browser Compatibility**: Test in modern browsers (Chrome, Firefox, Safari, Edge)
- **Device Testing**: Mobile, tablet, desktop viewports
- **Accessibility Testing**: Screen reader testing, keyboard-only navigation
- **Link Validation**: Ensure all internal links work correctly

## PAI Workflows

### 1. Consistent AI Image Integration
**Objective**: Generate themed snapshots (e.g., Hiromix style) and integrate them into interactive hover lists.

**Tools & Environment**:
- **Pack Location**: `/home/dan/projects/active/ai-image-generation`
- **Setup**: Requires a virtual environment (`venv`) with dependencies from `requirements.txt` and an `.env` file with `OPENAI_API_KEY`.
- **Command**: 
  ```bash
  source venv/bin/activate
  python3 src/cli/main.py generate --style [style_name] --scene "[prompt]" --output "/home/dan/projects/active/resume_website" --name "[role_id]"
  ```

**Procedure**:
1. **Generate**: Run the CLI tool from the pack directory to generate PNGs.
2. **Normalize**: The tool appends timestamps (e.g., `role_timestamp_001.png`). Rename these to clean, predictable names (e.g., `role.png`) in the website root.
3. **Trigger**: Add `data-image="role.png"` to the `<a>` tag in the interactive list.
4. **Logic**: Ensure the page's `<script>` handles `mouseenter` by updating the target `img.src` from the `data-image` attribute and setting `opacity: 1`.
5. **Reset**: Handle `mouseleave` by setting `opacity: 0`.

### 2. Automated Blog Creation
**Objective**: Streamline the process of adding new blog posts with integrated AI image generation.

**Tools & Environment**:
- **Source Folder**: `/home/dan/projects/active/resume_website/content/posts` (Markdown files with YAML frontmatter)
- **Script**: `/home/dan/projects/active/resume_website/scripts/create_blog.py`
- **Dependency**: Uses the `venv` from `/home/dan/projects/active/ai-image-generation`.

**Frontmatter Requirements**:
```yaml
title: "Post Title"
date: "YYYY-MM-DD"
style: "hiromix" # or any other style guide name
master_image_prompt: "Description for the hover preview image"
margin_notes:
  - "Note 1"
  - "Note 2"
```

**Workflow**:
1. **Draft**: Create a `.md` file in `content/posts/`.
2. **In-Body Generation**: Use `[[generate: "prompt"]]` within the Markdown body to trigger additional image generations and auto-injection.
3. **Execute**: 
   ```bash
    source /home/dan/projects/active/ai-image-generation/venv/bin/activate
    python3 scripts/create_blog.py content/posts/your-post.md

   ```
4. **Verification**: Check `blog.html` for the new entry in `blogPosts` and the interactive list.

### 3. Responsive Article Images
**Objective**: Ensure images embedded within articles (blog posts, projects) are visually balanced and don't overwhelm the viewport on high-resolution displays.

**Implementation**:
- **CSS Rule**: A global rule in `styles.css` targets `img` tags within `.blog-post-text`, `.traditional-content`, and `.post-embedded-image`.
- **Constraints**: 
  - `max-height: 50vh`: Limits image height to 50% of the viewport.
  - `max-width: 100%`: Ensures horizontal fit.
  - `width: auto; height: auto`: Preserves aspect ratio.
- **Styling**: Center alignment (`margin: 2rem auto`), subtle border-radius, and shadow for professional presentation.

**Automation**: The `create_blog.py` script generates clean HTML without inline styles, allowing the global CSS to handle all sizing and presentation.

## Lessons Learned: Blog Creation & Debugging Session

### Session Overview (2026-01-25)
Successfully added a new blog post "The technological republic and why we can't have nice things" from markdown source, with automated AI image generation. Encountered and resolved several deployment and JavaScript issues.

### What Worked Well

#### 1. Automated Blog Creation Workflow
- **Script Automation**: The `create_blog.py` script successfully:
  - Parsed markdown with YAML frontmatter
  - Generated master hover image and embedded content image using AI
  - Converted markdown to HTML
  - Injected new post into `blog.html` (both data object and interactive list)
- **Image Generation**: AI image pack integration worked flawlessly with proper prompts
- **Content Migration**: Successfully extracted content from external markdown file in user's Documents folder

#### 2. Systematic Debugging Approach
- **Git History Analysis**: Checked commit logs to verify what was deployed
- **File Verification**: Confirmed all files (blog.html, images) were committed and pushed
- **GitHub Actions**: Used `gh run list` to monitor deployment status
- **Deployment Success**: GitHub Pages deployment completed successfully

### Issues Encountered & Solutions

#### Issue 1: Blog Not Visible After Push
**Problem**: User reported blog post not showing after pushing to master
**Root Cause**: Browser cache and CSS version not updated
**Solution**:
- Bumped CSS version from `v=1.6` to `v=1.7` in blog.html
- Instructed user to hard refresh (Ctrl+F5)
- **Lesson**: Always increment CSS version parameter when making changes to ensure cache busting

#### Issue 2: Extra Closing Brace in CSS
**Problem**: Syntax error in `styles.css` - extra `}` at end of file (line 1012)
**Detection**: Manual code review while investigating deployment issues
**Solution**: Removed the extra closing brace
**Lesson**: Always validate CSS syntax, especially after manual edits

#### Issue 3: JavaScript Reference Error (Critical)
**Problem**: Blog posts wouldn't display when clicked, hover images not working
**Root Cause**: Added `console.log('Blog script initialized. Posts loaded:', Object.keys(blogPosts));` BEFORE `blogPosts` was defined
**Impact**: JavaScript error broke entire page interactivity:
  - Blog post click handlers failed
  - Hover image functionality broken
  - All interactive features non-functional
**Solution**: Moved console.log statement to AFTER the `blogPosts` object definition
**Lesson**: **CRITICAL** - Never reference variables before they are defined. Always place debug logging AFTER variable declarations.

#### Issue 4: Placeholder Link Cleanup
**Problem**: Old placeholder link for the post existed in the HTML
**Solution**: Removed the duplicate/placeholder entry to keep the list clean
**Lesson**: Check for existing placeholder content when adding new dynamic entries

### Best Practices Established

#### JavaScript Variable Scope
```javascript
// ❌ WRONG - Reference before declaration
console.log(myVar);
const myVar = "value";

// ✅ CORRECT - Reference after declaration
const myVar = "value";
console.log(myVar);
```

#### Cache Busting Strategy
- Always increment CSS version when making changes: `styles.css?v=1.X`
- Document current version in code comments
- Instruct users to hard refresh after deployment

#### Deployment Verification Checklist
1. Verify all files committed: `git status`
2. Check commit contents: `git show --name-only [commit-hash]`
3. Verify push succeeded: `git log -n 1`
4. Monitor deployment: `gh run list --limit 1`
5. Wait for deployment completion (~60 seconds)
6. Hard refresh browser to clear cache

#### Automated Script Validation
- The `create_blog.py` script works reliably when:
  - Virtual environment is activated
  - Frontmatter includes all required fields
  - Image generation prompts are descriptive
  - Source markdown is in correct location

### Tools & Commands Used

#### Git & Deployment
```bash
git status                              # Check working tree
git log -n 5                           # Recent commits
git show --name-only [hash]            # Files in commit
gh run list --limit 5                  # GitHub Actions status
git add . && git commit -m "msg"       # Stage and commit
git push                               # Deploy to remote
```

#### File Analysis
```bash
ls -l [file]                           # Check file existence
sed -n 'NUMBERp' [file]               # Read specific line
tail -n 20 [file]                     # Check end of file
wc -c                                 # Count characters
grep -F 'pattern' [file]              # Fixed string search
```

#### Blog Creation
```bash
source /home/dan/projects/active/ai-image-generation/venv/bin/activate
python3 scripts/create_blog.py content/posts/the-technological-republic.md
```

### Critical Warnings

1. **JavaScript Execution Order**: Always define variables before referencing them. A single reference error will break the entire script execution.

2. **CSS Cache**: Browser caching is aggressive. Always use versioned CSS links and increment on changes.

3. **Console Logging**: While useful for debugging, improperly placed console.log statements can cause runtime errors. Place them strategically after all dependencies are loaded.

4. **Deployment Timing**: GitHub Pages deployments take 30-60 seconds. Always wait for completion before testing.

5. **Hard Refresh Required**: After deployment, users MUST hard refresh (Ctrl+F5 / Cmd+Shift+R) to see changes.

### Success Metrics
- ✅ Blog post created and integrated successfully
- ✅ AI images generated and linked correctly
- ✅ Interactive hover functionality working
- ✅ Click-to-read functionality restored
- ✅ All content displaying properly
- ✅ Deployment successful and live

### Future Improvements
1. Add JavaScript validation/linting to pre-commit hooks
2. Create a CSS validation step in deployment pipeline
3. Add automated browser cache testing
4. Document CSS version numbers in a changelog
5. Consider moving blog posts data to external JSON file to avoid manual HTML editing

### Session Overview (2026-01-25)
Successfully implemented site-wide responsive image constraints for article content, resolving issues with excessively large images on high-resolution displays.

### What Worked Well

#### 1. Site-Wide CSS Normalization
- **Global Rule**: Moving from inline styles in `create_blog.py` to a global CSS rule in `styles.css` ensured consistency across all articles (blog, projects, philosophy).
- **Viewport-Relative Sizing**: Using `max-height: 50vh` proved effective for maintaining readability by ensuring images never dominate more than half the vertical space, regardless of screen resolution.

#### 2. Clean Automation
- **Script Refinement**: Updated `create_blog.py` to output clean HTML (`<img>` tags without inline `width`/`height`), delegating all styling to the CSS architecture.
- **Legacy Cleanup**: Successfully identified and updated existing blog posts in `blog.html` to remove hardcoded styles, bringing the entire history into compliance with the new standard.

#### 3. Proactive Cache Busting
- **Unified Versioning**: Bumping the CSS version across all HTML files ensured that the new layout constraints were applied immediately for the user without requiring manual cache clearing.

### Issues Encountered & Solutions

#### Issue: Oversized Article Images
**Problem**: Images in blog posts were set to `width: 100%`, making them massive on 1920x1080 screens and requiring excessive scrolling.
**Solution**: Implemented `max-height: 50vh`, `width: auto`, and `max-width: 100%` in `styles.css`.

### Best Practices Established

1. **Delegate Styling to CSS**: Avoid inline styles in automation scripts. Use semantic classes and target them in the main stylesheet.
2. **Relative Height Constraints**: For content-heavy pages, use `vh` units for large assets to ensure they scale relative to the browser window.
3. **Unified Versioning**: When updating global CSS, update the version parameter in ALL HTML files, even if the content hasn't changed.

## Lessons Learned: Image Integration & Refinement

### Session Overview (2026-01-25)
Resolved issues with image scaling and borders in hover previews, and iterated on AI image generation to achieve high-quality abstract visuals for professional roles.

### What Worked Well

#### 1. CSS Scaling Fixes
- **Responsive Aspect Ratio**: Using `height: auto`, `max-height`, and `object-fit: contain` solved the cropping issue. This ensures images of any aspect ratio are fully visible without distortion or clipping.
- **Clean Aesthetic**: Removing `border` and `background-color` from the hover display classes allowed images (especially those with transparency) to blend seamlessly with the site's minimalist design.

#### 2. Iterative AI Image Generation
- **Specificity in Prompts**: Explicitly requesting "no text" and specific details (e.g., "tan/brown military boots" for ADF) corrected common AI generation errors.
- **Pivot to Abstraction**: When realistic representations (people/offices) felt "off" or cluttered, switching to "abstract architectural representations" or "stylized patterns" produced more professional and on-theme results.
- **Drafting Prompts**: Sharing the full prompt with the user before generation allowed for collaborative refinement and reduced wasted iterations.

#### 3. Versioned Cache Busting
- Consistently incrementing the CSS version (e.g., `v=1.9` -> `v=2.2`) across all HTML files successfully forced browser refreshes for both CSS and the newly generated assets.

### Issues Encountered & Solutions

#### Issue 1: Image Cropping
**Problem**: Images were holding horizontal scale but being cut off at the top/bottom.
**Root Cause**: Fixed `height: 200px` combined with `object-fit: cover`.
**Solution**: Changed to `height: auto`, `max-height: 300px`, and `object-fit: contain`.

#### Issue 2: Tooling Path Discrepancy
**Problem**: Documentation pointed to `/home/dan/projects/packs/ai_image_generation`, but the active tool was at `/home/dan/projects/active/ai-image-generation`.
**Solution**: Used `find` and `ls` to locate the active project directory and correct the path in the CLI commands.

#### Issue 3: Style Guide Naming
**Problem**: Requesting style `--style hiromix` failed because the required key in the system was `hiromix_style_90s`.
**Solution**: Inspected `ai_image_system/style_guides/` to find the exact filename/key.

### Best Practices for Image Updates

1. **Archive Before Replace**: Always rename existing images (e.g., `filename_old.png`) instead of overwriting immediately. This allows for easy rollbacks.
2. **Abstract > Realistic**: For professional portfolios, abstract representations often integrate better with minimalist themes than realistic stock-style images.
3. **Prompt Guardrails**: Always include negative constraints like "no text", "no people" (if applicable), and "high contrast" to maintain the "Hiromix" aesthetic.
4. **Unified Cache Busting**: When updating assets, update the CSS version in *every* HTML file that uses those assets, even if the CSS file itself didn't change significantly, as it forces the browser to re-evaluate the DOM and its linked resources.
5. **Prompt Approval**: Before running expensive or slow AI generations, present the proposed prompt to the user for final sign-off.
