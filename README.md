# Roadmap Generator

A Python-based roadmap generator that creates professional PowerPoint roadmaps from YAML configuration files.

## 📁 Project Structure

```
roadmap/
├── data/                  # Data directory (ignored by git)
│   ├── roadmap.yaml       # YAML configuration file
│   ├── Roadmap_template.pptx  # PowerPoint template
│   └── Roadmap_generee.pptx  # Generated roadmap output
├── .gitignore             # Git ignore configuration
├── README.md              # This file
├── roadmap.py             # Main roadmap generation script
├── yaml_validator.py      # YAML validation tool
└── styles_config.py       # Styling configuration
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Required Python packages: `pypptx`, `pyyaml`

Install dependencies:
```bash
pip install python-pptx pyyaml
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

1. Edit the YAML configuration file at `data/roadmap.yaml` to define your roadmap structure
2. Run the main script:
```bash
python roadmap.py
```

This will generate a PowerPoint roadmap at `data/Roadmap_generee.pptx` using the template from `data/Roadmap_template.pptx`.

### Validate YAML Configuration

To validate your YAML configuration file:
```bash
python yaml_validator.py
```

For continuous validation (watches for file changes):
```bash
python yaml_validator.py --watch
```

## 📝 YAML Configuration

The `roadmap.yaml` file defines the structure of your roadmap with themes and items:

```yaml
themes:
  - name: "Theme Name"
    items:
      - type: "bar"
        label: "Project Name"
        start: "Jan"
        end: "Mar"
        line: 1
        subtype: "optional_subtype"
      - type: "milestone"
        label: "Milestone"
        month: "Jun"
        line: 2
        style: "milestone_style"
```

### Item Types

- **bar**: Horizontal bars representing projects or initiatives
- **milestone**: Point-in-time events or milestones
- **text**: Text annotations

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
- Input files (YAML configuration, PowerPoint template)
- Generated output (Roadmap_generee.pptx)
- Other PowerPoint files

This directory is ignored by git (see `.gitignore`).

## 🔧 Technical Details

- Uses `python-pptx` library for PowerPoint manipulation
- Uses `pyyaml` for YAML parsing
- Dynamic theme positioning based on content
- Automatic line management for optimal layout
- Color-coded items based on type and subtype

## 📊 Features

- Automatic theme height calculation
- Dynamic positioning of elements
- Multiple item types (bars, milestones, text)
- Customizable styling
- YAML validation tool
- Template-based generation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a pull request

## 📝 License

[Specify your license here]
