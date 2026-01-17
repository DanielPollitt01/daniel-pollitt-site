# AGENTS.md

This file contains guidelines for agentic coding agents working on this resume website project.

## Project Overview

This is a static HTML/CSS/JavaScript resume website with a minimalist design. The site consists of 5 main pages:
- `index.html` - Home page with site overview
- `about.html` - About section with professional background
- `projects.html` - Projects portfolio page with custom layout
- `blog.html` - Blog section (currently placeholder)
- `philosophy.html` - Personal philosophy section (currently placeholder)

## Build/Development Commands

Since this is a static website, there are no complex build commands. The development workflow is:

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
- Use semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<aside>`)
- Maintain consistent DOCTYPE: `<!DOCTYPE html>`
- Set `lang="en"` on HTML element
- Use proper ARIA attributes for accessibility
- Include viewport meta tag for responsive design
- Scripts should be placed before closing `</body>` tag
- Each page should have unique, descriptive `<title>` tag
- **Non-projects pages** use 3-column layout: `<div class="left-spacer"></div>`, `<div class="right-column">` containing name-section and content-grid
- **Projects page** uses `<body class="projects-page">` with different layout structure

### CSS Architecture
- **CSS Variables**: All colors and spacing use CSS custom properties defined in `:root`
- **Design System**: Colors follow green-themed palette:
  - `--green-primary`: #4A7C59 (main accent)
  - `--green-light`: #7db59f (hover states)
  - `--green-dark`: #3c8b5b (active states)
  - `--bg-white`: #F9F6EE (main background)
  - `--bg-light`: #f8f9fa (sidebar background)
- **Typography**: JetBrains Mono font family throughout
- **Spacing**: Use consistent margin/padding units (rem)
- **Responsive Design**: Mobile-first approach with breakpoints at 768px and 480px
- **Utility Classes**: Include `.mt-2`, `.mt-3`, `.mb-2`, `.mb-3`, `.text-center`

### JavaScript Conventions
- Use `const` and `let` exclusively (no `var`)
- Event listeners should use `e.stopPropagation()` for dropdown menus
- Implement keyboard accessibility (Enter, Space, Escape keys)
- Use semantic event handling with proper accessibility attributes
- Keep scripts small and page-specific

### Navigation Patterns
- All pages except `projects.html` use left-side hamburger menu
- `projects.html` uses right-side navigation symbol
- Navigation should include proper ARIA roles and keyboard support
- Active page should have `class="active"` on navigation link

### Page-Specific Styles
- `projects.html` has its own `<style>` block with custom layout
- Other pages share global styles from `styles.css`
- Projects page uses 2-column grid layout with unique navigation

### Grid Layout System
- **Non-projects pages** use a 3-column grid layout:
  - Left spacer column: customizable width (default 2fr)
  - Right column: contains name-section and content-grid
  - Content-grid within right column: 1fr 3fr (sidebar:main-content)
- **Projects page** uses its own custom layout with different grid structure
- **Grid control**: Modify `grid-template-columns` in `styles.css` line 231 to adjust left spacer width
  - Format: `grid-template-columns: 2fr 3fr` (left:right ratio)
  - Alternative: `grid-template-columns: 200px 1fr` (fixed:left, flexible:right)

### Content Guidelines
- All pages use consistent header structure with `.page-header`
- Sidebar content should be brief and informative
- Main content should be contained in `<main class="main-content">`
- Use semantic heading hierarchy (h1 > h2 > h3)

### File References
- CSS should be linked as: `<link rel="stylesheet" href="styles.css">`
- For cache busting, use version parameter: `styles.css?v=1.3`
- Internal links should use relative paths without leading slash

### Browser Compatibility
- Target modern browsers (ES6+ features acceptable)
- Test responsive behavior on mobile/tablet breakpoints
- Ensure accessibility features work across browsers

## Testing Approach

### Manual Testing Checklist
- [ ] Navigation menu functionality (click, keyboard, outside click)
- [ ] Responsive design on mobile (768px, 480px breakpoints)
- [ ] Accessibility: screen reader compatibility, keyboard navigation
- [ ] Cross-browser consistency
- [ ] Link functionality and hover states
- [ ] Image loading and alt text (where applicable)

### Accessibility Requirements
- All interactive elements must have proper ARIA attributes
- Keyboard navigation should be fully functional
- Color contrast ratios meet WCAG AA standards
- Semantic HTML structure for screen readers

## Common Tasks

### Adding New Content Section
1. Add semantic HTML in appropriate page
2. Use existing CSS classes for consistency
3. Follow heading hierarchy
4. Test responsive behavior
5. **For non-projects pages**: Ensure content is placed within the appropriate grid structure (left-spacer + right-column)

### Modifying Navigation
1. Update navigation in ALL HTML files
2. Ensure `class="active"` is on correct page
3. Test keyboard navigation
4. Verify accessibility attributes

### CSS Changes
1. Use CSS variables for new colors/values
2. Test in all pages (projects.html has overrides)
3. Check responsive breakpoints
4. Verify hover states and transitions
5. **Grid modifications**: When adjusting grid ratios, ensure alignment between name-section and sidebar content is maintained

This project emphasizes clean, maintainable code with strong accessibility and responsive design principles.

## Latest Updates

### Grid Layout Enhancement (v1.4)
- Implemented 3-column grid layout for non-projects pages to ensure consistent alignment
- Left spacer column provides full-height vertical alignment control
- Name section ("Daniel Pollitt") now aligns perfectly with sidebar content
- Responsive design maintains alignment across all screen sizes
- Grid ratio controlled by `grid-template-columns` in `styles.css` line 231
- Projects page remains unaffected with its custom layout structure

### Current Grid Structure
```
main-container (1:3 grid ratio)
├── left-spacer (empty, full-height)
└── right-column
    ├── name-section ("Daniel Pollitt")
    └── content-grid (1:3 grid ratio)
        ├── sidebar (Quick Facts)
        └── main-content
```