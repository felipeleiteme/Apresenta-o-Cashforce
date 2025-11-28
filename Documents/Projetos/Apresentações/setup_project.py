#!/usr/bin/env python3
"""
Setup script for Generative PPTX Engine project.
Creates directory structure and generates boilerplate files.

Usage:
    python setup_project.py
"""

import os
import json
from pathlib import Path


def create_directory_structure(base_path: Path):
    """Create the complete directory tree for the project."""
    directories = [
        "input/branding/fonts",
        "input/content",
        "input/references",
        "output",
        "src/analyzers",
        "src/generators",
        "src/utils",
        "temp",
    ]

    print("📁 Creating directory structure...")
    for directory in directories:
        dir_path = base_path / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {directory}")


def create_design_tokens(base_path: Path):
    """Generate design_tokens.json with realistic branding schema."""
    design_tokens = {
        "cashforce_theme": {
            "colors": {
                "brand": {
                    "primary": "#00CF80",
                    "primary_hover": "#00B06D",
                    "secondary": "#727D94",
                    "accent_blue": "#1A2D45",
                    "accent_purple": "#A679F0",
                    "accent_orange": "#F79552"
                },
                "background": {
                    "default": "#FBFDFE",
                    "paper": "#FFFFFF",
                    "dark": "#132E4F",
                    "sidebar": "#FFFFFF"
                },
                "text": {
                    "primary": "#1A2D45",
                    "secondary": "#727D94",
                    "light": "#FFFFFF",
                    "success": "#00CF80"
                },
                "border": {
                    "light": "#DFE2E6",
                    "focused": "#00CF80"
                },
                "status": {
                    "success": "#E6FDF4",
                    "success_text": "#00CF80",
                    "info": "#EBF2F9",
                    "info_text": "#3B82F6"
                }
            },
            "typography": {
                "font_family": "'DM Sans', sans-serif",
                "weights": {
                    "regular": 400,
                    "medium": 500,
                    "bold": 700
                },
                "sizes": {
                    "h1": "48px",
                    "h2": "32px",
                    "h3": "24px",
                    "body_large": "18px",
                    "body": "14px",
                    "caption": "12px"
                },
                "line_height": {
                    "heading": "1.2",
                    "body": "1.5"
                }
            },
            "spacing": {
                "xs": "4px",
                "sm": "8px",
                "md": "16px",
                "lg": "24px",
                "xl": "32px",
                "xxl": "64px"
            },
            "borderRadius": {
                "button": "24px",
                "input": "4px",
                "card": "8px",
                "large_card": "16px",
                "circle": "50%"
            },
            "shadows": {
                "card": "0px 4px 14px rgba(0, 0, 0, 0.05)",
                "hover": "0px 6px 20px rgba(0, 0, 0, 0.08)",
                "sidebar": "2px 0px 10px rgba(0, 0, 0, 0.03)"
            },
            "components": {
                "button": {
                    "primary": {
                        "bg": "#1A2D45",
                        "text": "#FFFFFF",
                        "radius": "24px",
                        "padding": "10px 24px"
                    },
                    "secondary": {
                        "bg": "transparent",
                        "border": "1px solid #00CF80",
                        "text": "#1A2D45",
                        "radius": "24px"
                    }
                },
                "card": {
                    "bg": "#FFFFFF",
                    "border": "1px solid #DFE2E6",
                    "radius": "8px"
                }
            }
        },
        "pptx_mappings": {
            "slide_dimensions": {
                "width": 10,
                "height": 7.5,
                "units": "inches"
            },
            "fonts": {
                "heading": "DM Sans Bold",
                "body": "DM Sans",
                "fallback": "Arial"
            },
            "assets": {
                "logo_path": "input/branding/logo.png",
                "background_image": None
            }
        }
    }

    file_path = base_path / "input/branding/design_tokens.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(design_tokens, f, indent=2, ensure_ascii=False)

    print(f"  ✓ Created design_tokens.json")


def create_presentation_script(base_path: Path):
    """Generate sample presentation_script.md with structured content."""
    script_content = """# Product Launch Presentation

---

## SLIDE: Title
**Layout:** title_slide

### Title
Revolutionary AI-Powered Analytics Platform

### Subtitle
Transforming Data into Actionable Insights

### Speaker Notes
Welcome everyone. Today we're excited to introduce our latest innovation in the analytics space.

---

## SLIDE: Problem Statement
**Layout:** content_slide

### Title
The Challenge

### Content
- Organizations are drowning in data but starving for insights
- Traditional analytics tools require specialized expertise
- Time-to-insight averages 2-3 weeks for complex analyses
- Siloed data prevents holistic understanding

### Speaker Notes
Let's start by understanding the problem our customers face daily.

---

## SLIDE: Our Solution
**Layout:** two_column

### Title
Introducing DataFlow AI

### Left Column
**Key Features:**
- Natural language queries
- Real-time processing
- Automated insight generation
- Cross-platform integration

### Right Column
**Benefits:**
- 10x faster analysis
- No coding required
- Enterprise-grade security
- Scalable architecture

### Speaker Notes
Our solution addresses each of these pain points through innovative AI technology.

---

## SLIDE: Call to Action
**Layout:** closing_slide

### Title
Ready to Transform Your Analytics?

### Content
Visit: www.dataflow-ai.example.com
Contact: sales@example.com

### Speaker Notes
Thank you for your time. We're excited to help you unlock the power of your data.
"""

    file_path = base_path / "input/content/presentation_script.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(script_content)

    print(f"  ✓ Created presentation_script.md")


def create_requirements_txt(base_path: Path):
    """Generate requirements.txt with necessary dependencies."""
    requirements = """# Core presentation generation
python-pptx==0.6.23

# Image processing
Pillow==10.3.0
pdf2image==1.17.0

# AI integration
anthropic==0.25.1

# Utilities
pyyaml==6.0.1
markdown==3.6
requests==2.31.0

# Development tools (optional)
pytest==8.1.1
black==24.3.0
"""

    file_path = base_path / "requirements.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(requirements)

    print(f"  ✓ Created requirements.txt")


def create_readme(base_path: Path):
    """Generate comprehensive README.md documentation."""
    readme_content = """# Generative PPTX Engine

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
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

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
"""

    file_path = base_path / "README.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"  ✓ Created README.md")


def create_gitignore(base_path: Path):
    """Generate .gitignore file for Python project."""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Generated files
output/*.pptx
temp/*
!temp/.gitkeep

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Sensitive
.env
*.log

# Keep folder structure
!input/branding/fonts/.gitkeep
!input/content/.gitkeep
!input/references/.gitkeep
!output/.gitkeep
"""

    file_path = base_path / ".gitignore"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(gitignore_content)

    print(f"  ✓ Created .gitignore")


def create_placeholder_files(base_path: Path):
    """Create .gitkeep files to preserve empty directories in git."""
    placeholder_dirs = [
        "input/branding/fonts",
        "input/references",
        "output",
        "temp",
    ]

    for directory in placeholder_dirs:
        gitkeep_path = base_path / directory / ".gitkeep"
        gitkeep_path.touch()


def main():
    """Main setup function."""
    print("=" * 60)
    print("🚀 Generative PPTX Engine - Project Setup")
    print("=" * 60)
    print()

    # Define base path (creates 'my-ppt-gen' in current directory)
    base_path = Path.cwd() / "my-ppt-gen"

    if base_path.exists():
        response = input(f"⚠️  Directory '{base_path}' already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("❌ Setup cancelled.")
            return

    # Create all directories
    create_directory_structure(base_path)
    print()

    # Generate boilerplate files
    print("📝 Creating boilerplate files...")
    create_design_tokens(base_path)
    create_presentation_script(base_path)
    create_requirements_txt(base_path)
    create_readme(base_path)
    create_gitignore(base_path)
    create_placeholder_files(base_path)
    print()

    # Success message
    print("=" * 60)
    print("✅ Project scaffolded successfully. Ready for Design Tokens.")
    print("=" * 60)
    print()
    print("Next steps:")
    print(f"  1. cd {base_path.name}")
    print(f"  2. Customize input/branding/design_tokens.json")
    print(f"  3. Add reference .pptx files to input/references/")
    print(f"  4. Edit input/content/presentation_script.md")
    print(f"  5. Install dependencies: pip install -r requirements.txt")
    print()
    print("📖 Read README.md for detailed documentation")
    print()


if __name__ == "__main__":
    main()
