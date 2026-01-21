# AGENTS.md

## Build/Development Commands

```bash
# Local development
python3 -m http.server 8000
npx serve .
live-server

# Validation
npx html-validator *.html
npx stylelint styles.css
npx axe index.html
```

## Code Style Guidelines

### HTML
- DOCTYPE html, lang="en", viewport meta
- Semantic HTML5 elements
- Scripts before </body>, unique titles
- Navigation symbol + menu at end of body

### CSS
- CSS custom properties in :root for design system
- JetBrains Mono font, rem units for spacing
- Mobile-first responsive (768px, 480px breakpoints)
- Link styles.css?v=1.4 with cache busting

### JavaScript
- const/let only, no var
- e.stopPropagation() for dropdowns
- Keyboard navigation (Enter, Space, Escape)
- ARIA attributes and roles
- Small, page-specific scripts

### Layout
- .unified-container grid system
- .traditional-content for most pages
- .left-content/.right-blurb for projects page
- Relative paths without leading slash

### Testing
- Manual: navigation, responsive, accessibility
- WCAG AA color contrast, semantic HTML
- Cross-browser compatibility