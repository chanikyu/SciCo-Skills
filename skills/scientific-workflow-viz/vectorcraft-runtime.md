# Driving VectorCraft from this skill

Adapted from the runtime notes of the `vectorcraft-scientific-illustration` skill. Everything
below was run against **VectorCraft 0.21.0 on macOS**. Command names and arguments can change
between versions — trust what the installed app answers (`--help`, `engine.commands`) over this file.

## Requirement

The **VectorCraft desktop app** must be installed.

- Install: <https://getartcraft.com/apps/vectorcraft>
- Source: <https://github.com/storytold/vectorcraft>

If it is missing, stop and ask the user to install it from the link above. Do not install it or
change its settings yourself, and do not switch to another renderer.

## 1. Check the install

The macOS default executable is `/Applications/VectorCraft.app/Contents/MacOS/VectorCraft`.
Run it with `--help` and confirm these options exist: `--control`, `--automation-read-root`,
`--automation-write-root`.

`--help` also points to a windowless `vectorcraft-cli` (converting, scripting, an MCP server).
If an MCP connection or that CLI is available, prefer it. This file covers the path that needs
only the desktop app: its localhost control server.

## 2. Start your own instance

1. Create an output folder and a **separate temporary profile folder**. Pick a **free local port**.
2. **Never attach to a VectorCraft instance or port you did not start** — the user (or another
   session) may already have one running with its own documents.
3. Start the app with the profile in `VECTORCRAFT_CONFIG_DIR`. Limit the read roots to the input
   and output folders and the write root to the output folder. All paths must be existing
   absolute paths.

```sh
VECTORCRAFT_CONFIG_DIR=/absolute/job-profile \
  /Applications/VectorCraft.app/Contents/MacOS/VectorCraft \
  --control 7991 \
  --automation-read-root /absolute/output \
  --automation-write-root /absolute/output
```

4. Keep the process running in the background (a window opens on the user's screen — tell them
   to leave it open). If launching a GUI app or connecting to localhost is blocked by a sandbox,
   use that environment's approval flow; do not conclude the app is not installed.

## 3. Send commands

Use `vectorcraft_control.py` from this skill folder (standard library only). It sends one
JSON-lines request and prints the reply.

```sh
python3 vectorcraft_control.py --port 7991 engine.commands > commands.json
python3 vectorcraft_control.py --port 7991 engine.execute \
  --params '{"command":"file.new","params":{"name":"figure","width":1600,"height":900,"units":"Points","backgroundContents":"white"}}'
```

- `engine.commands` lists every command with its parameters (1,315 commands, about 600 KB, in
  0.21.0). Save it to a file and search it; do not print it whole.
- `engine.execute` runs one command: `{"command": "<id>", "params": {…}}`.
- For long JSON, write it to a file and pass `--params-file /absolute/request.json`.
- A script may compute coordinates and send these requests. **VectorCraft does the rendering** —
  do not draw the figure with another library and call it done.

Commands used to draw a complete workflow figure (0.21.0). Units are points; **y grows downward**.

| Need | Command | Notes |
|---|---|---|
| New 16:9 document | `file.new` | `width`, `height`, `units`, `backgroundContents: "white"` |
| Box / rounded box | `shape.rectangle` | `x, y, width, height, radius?, rotation?` → `{id}` |
| Circle / ellipse | `shape.ellipse` | `x, y, width, height` → `{id}` |
| Arrow shaft, axis, rule | `shape.line` | `x1, y1, x2, y2` → `{id}` |
| Custom shape | `path.create` | `d`: SVG path data → `{id}` |
| Label | `text.create` | `x, y` (y is the **baseline**), `text`, `size`, `font`, `style`, `color`, `justify` → `{id, bounds, warning?}` |
| Fill / stroke colour | `paint.setFill`, `paint.setStroke` | `ids`, `color: "#rrggbb"` or `none: true` |
| Stroke weight, dash, arrowhead | `stroke.set` | `ids`, `weight`, `dash`, `endArrow: "Triangle"`, `arrowAlign: "tip"` |
| Group and name | `object.group`, `object.setProps` | `ids` → `{id}`; then `name` |
| Save the editable file | `document.save` | `path: "/absolute/output/figure.vectorcraft"` |
| Export | `document.export` | `path`, `format: png\|svg\|pdf`; PNG takes `scale` (pixels per point), `background`, and `rect: [x, y, w, h]` for a zoomed crop |

`text.create` returns the text's `bounds` — compare them with the box the label must fit in to
catch overflow before you even look. A `warning` in the reply means the font or style was not
found and a fallback was used.

## 4. Save, export, look

Save the `.vectorcraft` file, export PNG / SVG / PDF, then **open the PNG and look at it**.
A successful save or a valid SVG is not a visual check.

## 5. Timeouts and quitting

- A timeout means success or failure is unknown. Do not immediately repeat a command that
  changes the document — inspect the document (`document.inspect`) and the files first.
- Quit **only the instance you started**: send `app.quit` to your port. Never force-kill the
  user's app.
- Save (or close) every modified document first. If one is still unsaved, `app.quit` answers
  `{"pending": "saveChanges"}` and the app stays open waiting on a dialog. Send
  `ui.dialog.cancel`, save the document with `document.save`, then send `app.quit` again.

A passing connection test, a written file, and a reviewed image are three different checks.
Report only the ones you actually did.
