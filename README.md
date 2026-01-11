# Roadmap Generator

A Python-based roadmap generator that creates professional PowerPoint roadmaps from JSON configuration files.

## 📁 Project Structure

```
roadmap/
├── data/                  # Data directory (ignored by git)
│   ├── roadmap*.json      # JSON configuration files
│   ├── Roadmap_template.pptx  # PowerPoint template
│   └── Roadmap_generee*.pptx  # Generated roadmap outputs
├── .gitignore             # Git ignore configuration
├── README.md              # This file
├── roadmap.py             # Main roadmap generation script
├── roadmap_schema.json    # JSON schema for validation
├── validate_json.py       # JSON validation tool
└── styles_config.py       # Styling configuration
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Required Python packages: `pypptx`

Install dependencies:
```bash
pip install python-pptx
```

### Setup

1. Clone the repository:
```bash
git clone https://github.com/pafou/roadmap.git
cd roadmap
```

2. Set up the git remote:
```bash
git remote add origin https://github.com/pafou/roadmap.git
```

## 📖 Usage

### Generate a Roadmap

1. Edit the JSON configuration file at `data/roadmap*.json` to define your roadmap structure
2. Run the main script:
```bash
python roadmap.py
```

This will generate PowerPoint roadmaps at `data/Roadmap_generee*.pptx` using the template from `data/Roadmap_template.pptx`.

### Validate JSON Configuration

To validate your JSON configuration file:
```bash
python validate_json.py
```

## 📝 JSON Configuration

The `roadmap*.json` file defines the structure of your roadmap with themes and items:

```json
{
  "$schema": "../roadmap_schema.json",
  "title": "Roadmap Title",
  "themes": [
    {
      "name": "Theme Name",
      "items": [
        {
          "line": {
            "items": [
              {
                "type": "bar",
                "subtype": "DDO",
                "label": "Project Name",
                "start": "Jan",
                "end": "Mar",
                "year": 2026
              },
              {
                "type": "milestone",
                "label": "Milestone",
                "month": "Jun",
                "year": 2026,
                "style": "ddo"
              }
            ]
          }
        }
      ]
    }
  ]
}
```

### Item Types

- **bar**: Horizontal bars representing projects or initiatives
  - Required fields: `type`, `label`, `start`, `end`, `year`
  - Optional fields: `subtype` (S, ER, DDO, SL)

- **milestone**: Point-in-time events or milestones
  - Required fields: `type`, `label`, `month`, `year`
  - Optional fields: `style` (default, ddo)

- **text**: Text annotations
  - Required fields: `type`, `label`, `year`

### Supported Months

Jan, Fév, Mar, Avr, Mai, Jun, Jul, Aoû, Sep, Oct, Nov, Déc

## 🎨 Customization

Edit `styles_config.py` to customize:

- Theme styling (fonts, colors, sizes)
- Task styling
- Color mappings for different item types
- Bar type colors
- Milestone styles

## 📁 Data Directory

The `data/` directory contains:
- Input files (JSON configuration, PowerPoint template)
- Generated output (Roadmap_generee*.pptx)
- Other PowerPoint files

This directory is ignored by git (see `.gitignore`).

## 🔧 Technical Details

- Uses `python-pptx` library for PowerPoint manipulation
- Uses JSON for configuration parsing
- Dynamic theme positioning based on content
- Automatic line management for optimal layout
- Color-coded items based on type and subtype
- JSON schema validation

## 📊 Features

- Automatic theme height calculation
- Dynamic positioning of elements
- Multiple item types (bars, milestones, text)
- Customizable styling
- JSON validation tool
- Template-based generation
- Support for multiple roadmap files (roadmap1.json, roadmap2.json, etc.)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a pull request

## 📝 License

[Specify your license here]
