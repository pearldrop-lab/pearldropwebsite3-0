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

## Two jobs

The switch at the top of the left rail chooses what Chop Chop is making. The
choice is remembered per browser, and changing it clears the current result.

- **Story from interviews** — everything below this section.
- **Assemble a script** — a line stringout for drama and scripted ads.

## Assemble a script

For shoots where a script was recorded line by line, out of order, across days,
with several takes of each line and some lines rewritten on the day. Give it:

1. The **transcript** of a timeline holding all the takes, as CSV.
2. That **timeline as Final Cut Pro XML**, so every take is traced to its camera
   file and camera timecode.
3. The **script** — dropped or pasted into the brief.

It returns every take of every line, in script order, as an EDL you import as a
new sequence, with a line sheet alongside.

**Scripts it reads.** Final Draft `.fdx` (character and dialogue paragraphs);
screenplay text (a capitalised cue, dialogue beneath until a blank line);
`NAME: line` ad and VO scripts, with wrapped lines joined; and anything else as
one line per row, numbered or not. Cue extensions such as (V.O.) and (CONT'D),
parentheticals, bracketed directions, scene headings and transitions are left
out. A Final Draft file is written back into the box as `NAME: line` so the
script can be corrected in one place. The panel shows the line count, the voices
found and which format it read; "Show the lines" lists them numbered.

**Matching.** Script mode keeps every transcript row as its own unit rather than
merging rows into sentences, so nothing is joined across a take. Claude labels
every row with the script line being performed — or 0 for slates, "action",
"cut", direction and chat, or -1 for an off-script performance such as an alt or
ad-lib — plus whether it is a complete take or a false start, whether it carries
on the attempt in the row before, and whether the words were rewritten on the
day. It is told to match on meaning and position in the scene, not exact words.
The script travels with every request; rows are sent 180 at a time so each
answer stays well inside the output limit.

**Assembly.** Consecutive rows marked as one attempt become one take. Takes are
ordered by script line, and within a line by where they sit on your timeline.
Off-script performances go at the end. False starts are left out unless the
brief's checkbox says otherwise, and toggling it re-sorts without asking Claude
again. Gaps of black between takes and between lines are set in seconds.

**What comes back.**

- The table: a header for every script line — including the ones nobody
  recorded, marked "no take found" — with its takes beneath, badged as take,
  false start or rewritten. Takes can be dropped, trimmed, and reordered within
  their own line.
- The EDL: one event per take per camera clip, with comments naming the line,
  take number, voice, script text and what was actually said.
- The line sheet CSV: line, voice, script, take, kind, rewritten, camera clip,
  camera timecode, timeline timecode, record timecode and what was said, with
  unrecorded lines kept in place.
- Markers named `L7 T2/4 SARAH`, and a markdown line sheet in the zip.
- A summary of how many lines were found, how many takes were rewritten, and
  which lines have no take at all.

Tested end to end against a synthetic two-day shoot — seven clips recorded out
of order with slates, a false start, a rewritten line, a VO read that ran across
two transcript rows, an ad-lib and a script line nobody recorded — with Claude's
answer mocked. The matching itself has not yet been run against the live API on
a real shoot.

## What it reads

Any delimited transcript. A transcript with no speaker column — Premiere's
caption export gives `Start Time, End Time, Text, Layer ID` — is accepted, and
the transcript card grows a field to name who is speaking. Caption line breaks
live inside the quoted text field and are folded back to single spaces; the only
other repair is a space after a comma or semicolon that runs straight into a
letter, which never touches a figure like 30,000.

It sniffs the delimiter, matches the header row
loosely, and falls back to reading the data itself when there is no header:

- Speaker column — `Speaker Name`, `Name`, `Talent`, or a short repeating column.
- Timecode columns — `Start Time` / `End Time`, `In` / `Out`, or the first two
  columns that parse as time.
- Text column — `Text`, `Transcript`, `Caption`, or the longest string column.

Times may be `01:02:03:04`, `01:02:03;04` (drop frame), `01:02:03.456`, `02:03`,
or plain seconds. A missing out point is filled from the next row, or estimated
from how long the words take to say.

## How a soundbite is built

Consecutive rows from one speaker merge into whole thoughts. A bite ends only
where the speaker finishes a sentence — specifically at the first full stop once
it is at least 8 words long, or at a silence over 2.5 seconds, or at a speaker
change. **No word count ever breaks a bite mid-sentence**, which is what used to
leave people clipped in the middle of a line. A ceiling of 110 words catches a
rambling answer with no punctuation; anything past it is split at sentence
breaks with timings interpolated by character count, and those rows are marked
`est.` in the table because their in and out points are estimated rather than
measured. Each unit gets an id like `A012`: source letter, then its position.

On a real 25fps caption transcript this turns 78 rows into 31 soundbites, median
7.6 seconds, with every one ending on a sentence except where the source itself
has no full stop.

## Length

The target is a guide, not a constraint. The brief tells Claude anything from
-10% to +25% is fine and that running long always beats a clipped sentence, and
the running-time meter reads "on target" across that whole band. Self-
introductions are excluded unless the brief's checkbox says otherwise, and that
means a person stating their own name or job title. What the company or
organisation does is not treated as a self-introduction and is kept either way.

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

## Tracing soundbites back to the camera files

Drop the sequence XML in alongside the transcripts — in Premiere, **File >
Export > Final Cut Pro XML** — and Chop Chop reads the timeline itself. It is
FCP7 `xmeml`: every `clipitem` carries its position on the timeline (`start`,
`end`), its offset into the media (`in`), and a `file` whose `timecode/frame`
gives the media's own start timecode. Absolute source timecode is therefore
`file.timecode.frame + clipitem.in + (sequenceFrame - clipitem.start)`.

What that buys:

- **Real reel names and real source timecode in the EDL**, so it conforms to the
  camera originals rather than to a flattened master.
- **A bite that crosses a cut comes back as the same cuts.** One soundbite
  becomes one EDL event per clip underneath it. Segments that turn out to be
  contiguous in the source are merged back into one event.
- **The table names the camera clip** each bite came from, in place of the
  transcript filename.
- **Frame rate and sequence start** are taken from the XML.

Mapping runs across a whole track group, not one track. It defaults to **all
audio**, flattening A1 downwards into one non-overlapping map with the lowest
track winning any overlap — an interview's audio is rarely all on A1, and clips
moved to A3/A4 would otherwise map to nothing. A single track can be selected
instead. Premiere's extracted
audio is folded back to its camera clip, so `A016_..._C002 Audio Extracted.wav`
and `A016_..._C002.braw` are treated as one source. Reels are the last eight
alphanumeric characters of the clip name, because camera files share a long
prefix; collisions fall back to the first eight.

Two things are flagged rather than guessed: a clipitem whose source length does
not match its timeline length is retimed, and a stretch of the bite with nothing
on the mapped track is a gap. Both get a `* NOTE:` line in the EDL.

## Exports

| File | What it is |
| --- | --- |
| `<title>.edl` | CMX 3600, one event per soundbite, record timecode contiguous from the record start. Served from your own machine it downloads as a plain `.edl`; inside the artifact viewer it arrives in a zip, because `.edl` is not on that surface's saveable-extension list. |
| `markers-<clip>.csv` | Premiere marker import format, one file per source clip. |
| `<title>-soundbites.csv` | The table, with record timecodes and reasoning. |
| `<title>-treatment.md` | The treatment, the table and the source list. |

Reel names come from the CSV filename, which is usually the clip name, and the
`* FROM CLIP NAME:` comment carries the full name for relinking.

## Saving files

Two routes, chosen the same way as the Claude route. Outside the artifact viewer
the page saves through an ordinary object-URL anchor, so files land in the
browser's downloads with whatever extension suits. Inside the viewer a page
cannot start its own download at all, so saves go through the `downloads`
capability, which the viewer confirms with the user and which accepts only an
allowlist of extensions — hence the zip around the EDL there. If neither is
available the text goes to the clipboard.

## Reaching Claude

The page finds one of two routes at load and the Claude panel says which.

**The artifact runtime.** Published as a Claude Artifact, `claude.use("sample")`
resolves and Claude runs inside the page, billed to whoever opens it. No key
exists anywhere.

**Your own API key.** Served from anywhere else — a local server, a file on
disk — the panel takes an Anthropic key and calls
`POST https://api.anthropic.com/v1/messages` directly from the browser. Verified
against the live API: the CORS preflight admits `content-type`, `x-api-key`,
`anthropic-version` and `anthropic-dangerous-direct-browser-access` from any
origin, and the last of those is what the API requires to accept a browser call.
Requests carry `model`, `max_tokens: 16000`, `output_config.effort` and one user
message; nothing else. Model is selectable. Once a key is saved the page calls
`GET /v1/models` and builds the dropdown from what that key can actually reach,
so a newly released model appears without this file being edited; the hard-coded
list is only the fallback before a key exists. Default is `claude-opus-5-5`.
Sifting passes on a transcript too big for one prompt always use Haiku; only the
final cut uses the chosen model. Effort is sent as `output_config.effort`, and a
model that rejects it — Haiku today, anything unforeseen tomorrow — is retried
once without it rather than failing.

The key is held in `localStorage` on that browser, per person, and is sent
nowhere but api.anthropic.com. Anyone with access to that browser profile can
read it back, so use a key that can be rotated. Serve the page over HTTPS.

Server-side refusal fallbacks are deliberately not wired in. They need a beta
header, and an unrecognised beta fails the whole request — a worse failure mode
than the refusal it guards against, on interview transcripts. A `refusal` stop
reason is handled and reported instead.

## If Claude is not available on the page

"Do it by hand", below the table, copies the exact brief to the clipboard. Paste
it into any Claude conversation and paste the JSON back into the box.

## Note on where this lives

This folder is a holding place. Chop Chop belongs in its own repository —
`pearldrop-lab/chop-chop` — and should move there once it exists.

## Files

- `index.html` — the artifact body, written for the Artifact skeleton. Publish
  this one; it has no `<!doctype>`, `<html>`, `<head>` or `<body>` tags of its own.
- `chop-chop.html` — the same page wrapped in a plain HTML skeleton, so it opens
  by double-clicking. `window.claude` does not exist outside the artifact viewer,
  so in this copy the story selection falls back to "Do it by hand": copy the
  brief, paste it into a Claude conversation, paste the JSON back. Parsing,
  editing and every export work normally.
