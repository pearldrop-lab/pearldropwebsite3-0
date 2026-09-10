# Chop Chop

Turn Adobe Premiere transcript CSVs into a story.

Give it one interview or several, name a topic and a finished length, and it
returns the chosen soundbites as a table you can edit, a short treatment of the
film, and an EDL you can import as a rough-cut sequence.

## Where it runs

`index.html` is published as a Claude Artifact and runs entirely in the browser.
Claude does the story selection through the page's `sample` capability, so there
is no API key to manage and nothing to install — the person viewing the page
approves the call.

    https://claude.ai/code/artifact/82695f45-e51e-4191-a48b-f2cc03aa2d2f

The file is written for the Artifact skeleton: no `<!doctype>`, `<html>`,
`<head>` or `<body>` tags of its own. To open it as an ordinary web page, wrap it
in that skeleton first.

## What it reads

Any delimited transcript. It sniffs the delimiter, matches the header row
loosely, and falls back to reading the data itself when there is no header:

- Speaker column — `Speaker Name`, `Name`, `Talent`, or a short repeating column.
- Timecode columns — `Start Time` / `End Time`, `In` / `Out`, or the first two
  columns that parse as time.
- Text column — `Text`, `Transcript`, `Caption`, or the longest string column.

Times may be `01:02:03:04`, `01:02:03;04` (drop frame), `01:02:03.456`, `02:03`,
or plain seconds. A missing out point is filled from the next row, or estimated
from how long the words take to say.

## How a soundbite is built

Consecutive rows from one speaker merge into whole thoughts, stopping at a
sentence end, a gap over 1.6 seconds, or 42 words. Anything still longer is split
at sentence breaks with timings interpolated by character count — those rows are
marked `est.` in the table, because their in and out points are estimates rather
than measured. Each unit gets an id like `A012`: source letter, then its position.

## Choosing the cut

The whole numbered list goes to Claude with the brief. Transcripts too big for
one prompt are sifted in passes: each chunk is shortlisted for the topic, then
the shortlists are cut together. The reply is JSON — title, treatment, ordered
picks with a role and a reason, and notes on what the material is missing.

Every pick stays editable afterwards. Reorder, drop, and extend the in or out
point by a neighbouring unit from the same speaker. The running time in the
masthead recalculates as you go and turns amber when the cut runs long.

## Sequence transcripts

A transcript exported from a finished sequence carries sequence timecodes, not
source-clip ones. Set **These timecodes are -> A sequence** in the Timeline panel
and nothing else is needed: every timecode Chop Chop writes is a timecode on that
timeline, so the camera filenames behind the edit never have to be named.

Each transcript card carries a **relinks to** field — the name of the file the EDL
should conform against. Export the sequence from Premiere as one self-contained
master, put its name in that field, and the EDL relinks to it frame-accurately.

Two record layouts:

- **Assemble the cut** — events run back to back from the record start, in story
  order. Import this to get the cut-down as a new sequence.
- **Leave bites in place** — record timecode equals source timecode, so every
  select lands exactly where it already sits, with gaps between. Events are
  written in timeline order rather than story order, because EDL record
  timecodes have to ascend.

## Exports

| File | What it is |
| --- | --- |
| `<title>.edl` | CMX 3600, one event per soundbite, record timecode contiguous from the record start. Shipped inside a zip because `.edl` is not a saveable extension in the viewer. |
| `markers-<clip>.csv` | Premiere marker import format, one file per source clip. |
| `<title>-soundbites.csv` | The table, with record timecodes and reasoning. |
| `<title>-treatment.md` | The treatment, the table and the source list. |

Reel names come from the CSV filename, which is usually the clip name, and the
`* FROM CLIP NAME:` comment carries the full name for relinking.

## If Claude is not available on the page

"Do it by hand", below the table, copies the exact brief to the clipboard. Paste
it into any Claude conversation and paste the JSON back into the box.

## Note on where this lives

This folder is a holding place. Chop Chop belongs in its own repository —
`pearldrop-lab/chop-chop` — and should move there once it exists.
