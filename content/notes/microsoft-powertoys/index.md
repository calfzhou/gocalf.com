---
title: Microsoft PowerToys
date: 2026-10-21T20:57:12+08:00
lastmod: 2026-10-21T20:57:12+08:00
tags:
  - software/windows
params:
  ai_label: generated
---
## Info

[Microsoft PowerToys - Windows Utilities for Power Users](https://learn.microsoft.com/en-us/windows/powertoys/)

> Utilities to customize Windows

{{< badge_github user="microsoft" repo="PowerToys" release=true >}}

Microsoft PowerToys is a set of free, open-source utilities designed to help power users and developers get more out of Windows.

```powershell
winget install Microsoft.PowerToys
```

## Utilities

### The Ones Most People Fall in Love with First

- Awake: keeps the PC from sleeping on demand.
- Command Palette: a fast launcher ({{< kbd text="Win" >}} + {{< kbd text="Alt" >}} + {{< kbd text="Space" >}}) that replaced the old "PowerToys Run". Type to launch apps, open files, do calculations, run web searches, switch windows — all from one box. This is the single biggest productivity unlock.
- FancyZones: define custom window layouts, then snap windows into zones by holding Shift while dragging.
- PowerRename: bulk-rename files via right-click, with search/replace, regex, and undo.
- Color Picker: {{< kbd text="Win" >}} + {{< kbd text="Shift" >}} + {{< kbd text="C" >}} to grab any pixel's color from anywhere on screen, copied in hex/RGB/etc.
- Text Extractor: {{< kbd text="Win" >}} + {{< kbd text="Shift" >}} + {{< kbd text="T" >}} to OCR any region of the screen — copy text out of an image, video, or screenshot.

### Genuinely Handy, a Bit More Niche

- Advanced Paste: {{< kbd text="Win" >}} + {{< kbd text="Shift" >}} + {{< kbd text="V" >}} to paste clipboard content reformatted — strip formatting, convert to JSON/Markdown, or use AI to transform it.
- Peek: select a file, hit Spacebar to preview its contents instantly (like macOS Quick Look) without opening an app.
- Mouse utilities: Find My Mouse (shake to spotlight the cursor), Crosshairs, Highlighter for clicks — great for presentations/screen sharing.
- Keyboard Manager: remap keys or whole shortcuts globally (e.g. make CapsLock do something useful).
- Always On Top: {{< kbd text="Win" >}} + {{< kbd text="Ctrl" >}} + {{< kbd text="T" >}} pins any window above the rest.

### New / Improved in 0.100.0

- Shortcut Guide (rebuilt): hold the {{< kbd text="Win" >}} key and it shows a side pane of shortcuts relevant to whatever app is currently focused — a great way to discover shortcuts as you go.
- Command Palette Extension Gallery: browse and install extensions without leaving the palette, plus per-monitor Dock layouts.
- ZoomIt: now supports webcam overlays during recordings and stitching clips with transitions.
- Under the hood: moved to .NET 10, ~15% smaller installer, faster startup.

### Worth a Look for a Developer

- Hosts File Editor: edit your hosts file with a real UI (toggle entries on/off).
- Environment Variables: manage env vars with switchable profiles.
- File Locksmith: right-click → see which process is locking a file.
- Registry Preview, Command Not Found (suggests the WinGet package when a command isn't found in PowerShell), and File Explorer add-ons (preview/thumbnails for SVG, Markdown, PDF, source code).
