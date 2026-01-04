# Configuration file for roadmap styling
# This keeps styling parameters separate from the main logic

# Theme styling configuration
THEME_STYLING = {
    'font_name': 'Arial',
    'font_size': 8,
    'font_bold': True,
    'font_color': (0x32, 0x4B, 0x6B)  # Hex color #324B6B
}

# Task item styling configuration
TASK_STYLING = {
    'font_size': 8
}

# Color mapping for different task types
COLOR_MAPPING = {
    'charge_sure': (0, 176, 80),
    'charge_esperee': (255, 192, 0),
    'jalon': (68, 114, 196),
    'default': (200, 200, 200)
}

# Bar type color mapping
BAR_TYPE_COLORS = {
    'S': {
        'background': (0, 128, 0),      # 008000
        'foreground': (255, 255, 255)   # FFFFFF (white)
    },
    'SL': {
        'background': (255, 255, 0),    # FFFF00
        'foreground': (50, 75, 107)     # 324B6B
    },
    'ER': {
        'background': (139, 195, 74),   # 8BC34A
        'foreground': (50, 75, 107)     # 324B6B
    },
    'E': {
        'background': (197, 217, 241),  # C5D9F1
        'foreground': (50, 75, 107)     # 324B6B
    },
    'DDO': {
        'background': (243, 217, 241),  # F3D9F1
        'foreground': (50, 75, 107)     # 324B6B
    }
}

# Milestone styling configuration
MILESTONE_STYLES = {
    'default': {
        'triangle_background': (0, 0, 0),  # Black
        'triangle_border': (255, 255, 255)  # White
    },
    'ddo': {
        'triangle_background': (0xE6, 0x36, 0xA6),  # E636A6
        'triangle_border': (255, 255, 255)  # White
    }
}

# Milestone text styling configuration
MILESTONE_TEXT_STYLE = {
    'font_name': 'Arial',
    'font_size': 6,
    'font_color': (0x32, 0x4B, 0x6B)  # Hex color #324B6B
}
