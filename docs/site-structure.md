# Site Structure Guide

This document explains how the Architecture 2.0 course website is organized.

## Folder Structure

```
architecture2/
├── index.md                 # Homepage
├── _config.yml             # Jekyll configuration
├── Gemfile                 # Ruby dependencies
├── README.md               # Repository documentation
├── .gitignore             # Git ignore rules
│
├── course/                 # Course administration
│   ├── schedule.md         # Weekly schedule and readings
│   ├── syllabus.md         # Course policies and requirements
│   └── assignments.md      # Assignment descriptions and rubrics
│
├── content/                # Research content
│   ├── matrix.md           # AI-for-architecture research matrix
│   └── resources.md        # Tools, papers, and references
│
├── assets/                 # Media files (future use)
│   ├── images/            # Course images, diagrams
│   └── files/             # PDFs, datasets, etc.
│
└── docs/                   # Documentation
    └── site-structure.md   # This file
```

## File Responsibilities

### **Professor Updates:**
- `index.md` - Course announcements, philosophy
- `content/matrix.md` - Research landscape updates
- `content/resources.md` - New tools and papers

### **TA Updates:**
- `course/schedule.md` - Weekly readings, due dates
- `course/assignments.md` - Assignment details, rubrics
- `course/syllabus.md` - Policy updates

### **Rarely Changed:**
- `_config.yml` - Site configuration
- `Gemfile` - Dependencies
- `docs/` - Documentation

## Quick Edit Guide

### Adding Weekly Content:
```markdown
# In course/schedule.md
### **Week X: Topic Name**
*Date*
- **Required**: Paper Title
- **Optional**: Additional Reading
```

### Adding Announcements:
```markdown
# In index.md under "Important Notes"
- **New**: Assignment 2 posted
- **Reminder**: Paper reviews due Friday
```

### Adding Research Papers:
```markdown
# In content/matrix.md
**[Paper Title](link)** - Brief description of contribution
```

## Best Practices

1. **Use descriptive commit messages** when updating files
2. **Test links** before pushing changes
3. **Keep file names lowercase** with hyphens for spaces
4. **Update both navigation links** if you move files
5. **Preview changes locally** with `bundle exec jekyll serve`

## Future Expansion

The `assets/` folder is ready for:
- Course diagrams and figures
- Student project showcases
- Video recordings
- Dataset downloads
- Tool documentation

This structure scales well as the course grows into a broader research hub.
