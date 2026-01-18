# AGENTS.md

This file contains guidelines for agentic coding agents working on this resume website project.

## Project Overview

This is a static HTML/CSS/JavaScript resume website with a unified minimalist design. The site uses a single-page application pattern across 5 main pages:
- `index.html` - Home page with site overview
- `about.html` - About section with professional background  
- `projects.html` - Projects portfolio page with interactive project list
- `blog.html` - Blog section (currently placeholder)
- `philosophy.html` - Personal philosophy section (currently placeholder)

## Build/Development Commands

Since this is a static website, there are no complex build commands or testing frameworks:

### Local Development
```bash
# Serve the site locally (any of these options):
python3 -m http.server 8000
# or
npx serve .
# or
live-server  # if installed via npm
```

### Validation
```bash
# HTML validation
npx html-validator index.html about.html projects.html blog.html philosophy.html

# CSS validation  
npx stylelint styles.css

# Accessibility check
npx axe index.html
```

### File Organization
```
/  (root)
├── index.html          # Home page
├── about.html          # About page
├── projects.html       # Projects portfolio  
├── blog.html           # Blog listing
├── philosophy.html     # Philosophy section
├── styles.css          # Main stylesheet
└── AGENTS.md          # This file
```

## Code Style Guidelines

### HTML Structure
- **DOCTYPE**: Use `<!DOCTYPE html>` consistently
- **Language**: Set `lang="en"` on HTML element
- **Viewport**: Include `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- **Titles**: Each page should have unique, descriptive `<title>` tag
- **Navigation**: All pages include navigation symbol and menu at the end of body
- **Scripts**: Place JavaScript before closing `</body>` tag
- **Semantic HTML**: Use appropriate HTML5 semantic elements

### CSS Architecture
- **Design System**: CSS custom properties in `:root`:
  - `--green-primary`: #4A7C59 (main accent)
  - `--green-light`: #7db59f (hover states)
  - `--green-dark`: #3c8b5b (active states)
  - `--bg-light`: #f8f9fa (light backgrounds)
  - `--bg-white`: #F9F6EE (main background)
  - `--text-dark`: #2d3748 (primary text)
  - `--text-muted`: #6b7280 (secondary text)
  - `--border-light`: #e5e7eb (borders)
  - `--font-mono`: 'JetBrains Mono', monospace

- **Typography**: JetBrains Mono font family imported from Google Fonts
- **Spacing**: Use consistent rem units for margins/padding
- **Responsive Design**: Mobile-first with breakpoints at 768px and 480px

### JavaScript Conventions
- **Variables**: Use `const` and `let` exclusively (no `var`)
- **Event Handling**: Use `e.stopPropagation()` for dropdown menus
- **Accessibility**: Implement keyboard navigation (Enter, Space, Escape keys)
- **Modularity**: Keep scripts small and page-specific
- **Semantic Events**: Use proper ARIA attributes and roles

### Unified Layout System
All pages use the `.unified-container` layout system:

```
unified-container (grid: auto auto auto rows)
├── unified-name-section (full width)
├── unified-quote-section (optional, 1:1 columns)
└── unified-content-section (1:1 columns)
    ├── left-content (project list or main content)
    └── right-blurb (descriptive text)
```

### Navigation Patterns
- **Navigation Symbol**: Hamburger menu icon in top-left corner
- **Menu Structure**: Dropdown with 5 links, includes `role="menu"` and ARIA attributes
- **Active States**: Current page gets `class="active"` on navigation link
- **Keyboard Support**: Full keyboard navigation with Escape to close
- **Click Outside**: Menu closes when clicking outside navigation area

### Content Layout Patterns

#### Traditional Layout (index.html, about.html, blog.html, philosophy.html)
- Uses `.traditional-content` within unified content section
- Single column content with headings, paragraphs, lists
- No left/right split, content takes full width of unified-content-section

#### Projects Layout (projects.html)
- Uses `.left-content` for interactive project list (`<ol class="interactive-list">`)
- Uses `.right-blurb` for project descriptions and hover images
- Includes project hover interactions with image display

### File References
- **CSS**: Linked as `<link rel="stylesheet" href="styles.css?v=1.4">`
- **Internal Links**: Use relative paths without leading slash
- **Cache Busting**: Include version parameter in CSS href

### Browser Compatibility
- **Target**: Modern browsers (ES6+ features acceptable)
- **Testing**: Verify responsive behavior on mobile/tablet breakpoints
- **Accessibility**: Ensure ARIA attributes work across browsers

## Testing Approach

### Manual Testing Checklist
- [ ] Navigation menu functionality (click, keyboard, outside click)
- [ ] Responsive design on mobile (768px, 480px breakpoints)  
- [ ] Accessibility: screen reader compatibility, keyboard navigation
- [ ] Cross-browser consistency
- [ ] Link functionality and hover states
- [ ] Project hover interactions (projects.html)

### Accessibility Requirements
- **ARIA Roles**: Use proper roles on navigation and interactive elements
- **Keyboard Navigation**: Full functionality with Tab, Enter, Space, Escape
- **Color Contrast**: Meet WCAG AA standards
- **Semantic HTML**: Proper structure for screen readers

## Common Tasks

### Adding New Page
1. Create HTML file with unified structure
2. Include navigation symbol and menu at end of body
3. Add navigation link to ALL existing pages
4. Test responsive behavior
5. Verify accessibility

### Modifying Navigation
1. Update navigation in ALL HTML files
2. Ensure `class="active"` is on correct page
3. Test keyboard navigation
4. Verify ARIA attributes

### CSS Changes
1. Use CSS variables for new colors/values
2. Test across all page types (traditional vs projects layout)
3. Check responsive breakpoints
4. Verify hover states and transitions

This project emphasizes unified design patterns, semantic HTML, and strong accessibility principles with minimal, purposeful code.