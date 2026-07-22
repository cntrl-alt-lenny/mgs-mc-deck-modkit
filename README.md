# MGS2 & MGS3 (Master Collection) — Steam Deck Mod Kit

A small, **dependency-free** guided installer that sets up the essential,
vanilla-faithful mod stack for **Metal Gear Solid 2: Sons of Liberty** and
**Metal Gear Solid 3: Snake Eater** (Master Collection, Steam) on the Steam
Deck — proper 16:10, restored PS2 assets, and correct button prompts — in a
couple of clicks.

It exists because doing this by hand has one trap that will stop you dead:
**MGSHDFix has no runtime defaults.** Without a complete `MGSHDFix.settings`
file the game refuses to launch, and it hard-aborts on any *single* missing
section or key:

```
ERROR: File not found: ...\plugins\MGSHDFix.settings
[MGSHDFix Config Helper] Failed to read config key 'Debug Logging'
in section 'Internal Settings': Section not found
```

That file can normally only be produced by the mod's **Windows Config Tool**,
which on Linux means wrestling it through Proton. Worse, its ini section names
are **not** the tab labels the tool shows you — it wants `[Internal Settings]`,
`[Launcher Config]`, `[Skip Logo Screens]`, `[MGS2 - Model Options]` — so
hand-writing one does not work either.

**This kit ships a canonical settings file captured from the real Config Tool**,
verified byte-for-byte against a known-working install, so you never have to
touch it.

> First-time, **vanilla** playthrough in mind: every bundled mod is a *fix* or a
> *restoration*. Nothing reinterprets the art or alters game balance.

## What it does

1. **Finds your installs automatically** — every Steam library, including games
   on a **microSD card**. Falls back to a folder picker if needed.
2. **Installs MGSHDFix 3.1.0** — native resolution, true 16:10 (correct FOV, no
   pillarboxing), the high-CPU-usage fix, alt-tab and aiming bugfixes.
3. **Installs the Community Bugfix Compilation (Base)** — re-imports the original
   higher-quality PS2 textures, restores low-LOD models to full quality, and
   fixes invisible assets, missing audio and typos the port introduced.
4. **Optionally installs the Better Audio Mod** from a zip you supply.
5. **Writes a tuned, known-good `MGSHDFix.settings`** for each game.
6. **Verifies** every file landed, then tells you the one line to paste into
   Steam.

Everything is downloaded live from the mods' **official GitHub releases** —
nothing is rehosted here.

## The mod stack (and why this order)

Install order is not optional; it comes from the mods' own documentation:

| # | Mod | What it is |
|---|-----|-----------|
| 1 | [MGSHDFix](https://github.com/ShizCalev/MGSHDFix) `3.1.0` | **Required.** The base fix — resolution, aspect ratio, FOV, CPU usage. |
| 2 | [Better Audio Mod](https://www.nexusmods.com/metalgearsolid2mc/mods/3) | Restores audio the port shipped re-compressed. *Manual — see below.* |
| 3 | [MGS2](https://github.com/ShizCalev/MGS2-Community-Bugfix-Compilation) / [MGS3](https://github.com/ShizCalev/MGS3-Community-Bugfix-Compilation) Community Bugfix Compilation — **Base** | Restores original PS2 assets, fixes broken ones. |

The Bugfix Compilation intentionally overwrites a handful of Better Audio's
files — that is correct, not a conflict, which is why the order matters.

**Deliberately *not* installed:** the 2x / 4x **AI Upscaled Texture Addons** and
the 4K asset pack. Those are AI reinterpretations of the original art — the
opposite of what you want for a faithful first playthrough. Install them
yourself later if you fancy them.

## Why the Better Audio Mod is manual

It's hosted on NexusMods, which requires a logged-in account to download, so no
script can fetch it. The installer will look in `~/Downloads` for a matching
zip, or let you point at one — and it's entirely optional; skip it and re-run
the kit later.

- MGS2: <https://www.nexusmods.com/metalgearsolid2mc/mods/3>
- MGS3: <https://www.nexusmods.com/metalgearsolid3mc/mods/4>

## Usage

**Easiest — download and double-click:** grab
[`Install-MGS-Mods.desktop`](Install-MGS-Mods.desktop), drop it on your Deck's
Desktop, and double-click it. It fetches the installer and runs it, then offers
to delete itself.

**Or from a terminal (Desktop Mode → Konsole):**

```sh
curl -fsSL https://raw.githubusercontent.com/cntrl-alt-lenny/mgs-mc-deck-modkit/main/install.py -o install.py
python3 install.py
```

Close both games (and let any Steam downloads finish) first.

## The one manual step

Steam rewrites its config from memory and silently reverts edits made while it's
running, so the installer does **not** touch your launch options. For **each**
game: right-click it in Steam → **Properties → General → Launch Options**, and
paste exactly:

```
WINEDLLOVERRIDES="wininet,winhttp=n,b" %command%
```

Without this, MGSHDFix never loads. (MGSHDFix 3.1.0 uses `winhttp.dll` /
`wininet.dll` — the old `d3d11.dll` advice is for ancient versions.)

## First launch & the launcher

On first launch the Konami launcher appears. That is the **only** place to set
the game's *high quality cinematics* option, and the choice is saved
permanently (in `<game>_savedata_win/<steamid>/launcher/launcher_sv`).

Set it there **first**. Afterwards, if you'd rather boot straight into the game,
edit `plugins/MGSHDFix.settings` and set:

```
Skip Launcher=1
```

The installer offers this as an option but defaults it **off** for exactly this
reason. (Skipping is safe for MGS2/MGS3 — the `MSX Skip Launcher Game` setting
only applies to the separate *Metal Gear / Metal Gear 2* MSX release.)

## Options the installer asks about

| Option | Default | Notes |
|---|---|---|
| Button icons | `Steam Deck` | Matches the Deck's physical buttons. Xbox / PS5 / PS2 / Keyboard also offered — PS2 icons are restored by the Bugfix Compilation. |
| Audio output | `Stereo (2.0)` | Right for handheld. Pick 5.1 if docked to a receiver. |
| Skip intro logos | on | Skips the unskippable KONAMI splash screens. |
| Skip launcher | off | See above. |
| MGSHDFix update checks | off | Avoids in-game pop-ups mid-play. |

Everything else is left at MGSHDFix's own defaults, which are already correct
for the Deck: `Fix Aspect Ratio` + `Fix FOV` + `Fix Framebuffer` on (true 16:10,
no pillarboxing), Borderless Fullscreen, auto-native resolution, 16x anisotropic
filtering, and `Fix High CPU Usage = Full`.

## Uninstalling / reverting

Steam → the game → **Properties → Installed Files → Verify integrity of game
files**. That restores every stock file, removing the Better Audio Mod and the
Bugfix Compilation's overwritten assets.

Note that verify-integrity does **not** remove the mods' *added* files — delete
these by hand if you want a totally clean slate:

```
winhttp.dll  wininet.dll  plugins/  logs/  steam_appid.txt
```

## Versions are pinned on purpose

`MGSHDFix 3.1.0`, `MGS2 Bugfix 2.2.0`, `MGS3 Bugfix 1.1.0`.

The bundled settings file was generated by **MGSHDFix 3.1.0's** Config Tool. A
future MGSHDFix release could rename ini sections or keys, which would make the
game hard-abort. Pinning guarantees a tested, working combination.

To move to a newer MGSHDFix: bump `HDFIX_VERSION` in `install.py`, install it,
run `MGSHDFix Config Tool.exe` from the game's `plugins/` folder once, hit
**Save and Exit**, and paste the resulting file into `SETTINGS_TEMPLATE`.

## Requirements

All preinstalled on SteamOS: `python3`, `bsdtar`, and `kdialog` **or** `zenity`.
No pip packages, no sudo, no Protontricks.

## Troubleshooting

**"Failed to read config key 'X' in section 'Y'"** — your settings file doesn't
match your MGSHDFix version. Run `MGSHDFix Config Tool.exe` from the game's
`plugins/` folder and hit *Save and Exit*.

**The mod doesn't load at all** — the launch options aren't set. See above.

**Checking what actually happened** — MGSHDFix writes `logs/MGSHDFix_Game.log`
and `logs/MGSHDFix_Launcher.log` in the game folder, including a full dump of
every setting it parsed. Those logs contain embedded binary, so plain `grep`
silently matches nothing — use `grep -a`.

**`No display-attached GPUs were detected during early enumeration`** — benign
on Deck/Proton; it appears every run and the game works fine.

## Credits

All the actual work belongs to the mod authors:

- **[ShizCalev](https://github.com/ShizCalev)** — MGSHDFix and both Community
  Bugfix Compilations (MGSHDFix originally by [Lyall](https://github.com/Lyall)).
- **Knight_Killer** — the Better Audio Mods.

This kit only automates installing them. Please endorse their work on NexusMods
and star the GitHub repos.

## Licence

MIT — see [LICENSE](LICENSE).
