# Generative PPTX Engine

An AI-powered presentation generator that transforms text scripts into professional PowerPoint presentations using `python-pptx` and Claude AI.

## Overview

This tool orchestrates presentation generation by:
1. Analyzing reference PPTX files to extract layout patterns
2. Parsing content scripts (markdown format)
3. Applying your design system (colors, fonts, spacing)
4. Generating polished presentations automatically

## Project Structure

```
my-ppt-gen/
├── input/
│   ├── branding/
│   │   ├── fonts/              # Place custom .ttf font files here
│   │   └── design_tokens.json  # Your brand colors, typography, spacing
│   ├── content/                # Your presentation scripts (.md or .txt)
│   │   └── presentation_script.md
│   └── references/             # Reference .pptx files for layout inspiration
├── output/                     # Generated presentations appear here
├── src/
│   ├── analyzers/              # Scripts to extract layouts from references
│   ├── generators/             # Core presentation generation logic
│   └── utils/                  # Helper functions
└── temp/                       # Temporary files during processing
```

## Getting Started

### 1. Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Prepare Your Input Files

#### A. Design Tokens (`input/branding/design_tokens.json`)
- Already created with sensible defaults
- Customize colors, fonts, and spacing to match your brand
- Update `logo_path` if you have a company logo

#### B. Content Script (`input/content/`)
- Write your presentation content in markdown format
- Use the provided `presentation_script.md` as a template
- Structure: Title, sections with bullet points, speaker notes

#### C. Reference PPTX Files (`input/references/`)
- Add 1-3 professionally designed PowerPoint files
- The engine will analyze layouts: title slides, content slides, two-column layouts
- Use corporate templates or well-designed presentations

#### D. Custom Fonts (`input/branding/fonts/`)
- Optional: Add .ttf files for custom typography
- Update font names in `design_tokens.json` accordingly

### 3. Generate Your Presentation

```bash
# Run the generator (coming soon)
python src/main.py
```

The generated presentation will appear in the `output/` folder.

## Content Script Format

Use this markdown structure:

```markdown
# Presentation Title

---

## SLIDE: Your Slide Title
**Layout:** title_slide | content_slide | two_column | closing_slide

### Title
Main slide title

### Content
- Bullet point 1
- Bullet point 2

### Speaker Notes
What you'll say when presenting this slide
```

## Design Tokens Schema

Customize `design_tokens.json` with:

- **colors**: Primary, secondary, accent, background, text colors (hex codes)
- **typography**: Font families and sizes for headings and body text
- **spacing**: Margins and padding (in inches)
- **assets**: Paths to logo and background images
- **layout**: Slide dimensions and content constraints

## Roadmap

- [ ] Layout analyzer for reference PPTX files
- [ ] Markdown parser for content scripts
- [ ] Smart slide generator with design system integration
- [ ] Image placement and resizing utilities
- [ ] Claude AI integration for content enhancement
- [ ] Template library management

## Requirements

- Python 3.8+
- See `requirements.txt` for package dependencies

## License

MIT License - Feel free to use and modify for your projects.

## Contributing

Contributions welcome! This is an evolving project focused on making presentation creation effortless.
