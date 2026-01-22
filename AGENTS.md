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