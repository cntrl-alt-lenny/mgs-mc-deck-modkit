<div align="center">

# 🐍 MGS Deck Mod Kit

### Metal Gear Solid **2** & **3** · Master Collection · Steam Deck

*One double-click. The whole setup. No guesswork.*

<br>

![Steam Deck](https://img.shields.io/badge/Steam_Deck-verified_setup-1A9FFF?style=for-the-badge&logo=steamdeck&logoColor=white)
![SteamOS](https://img.shields.io/badge/SteamOS-3.x-000000?style=for-the-badge&logo=steam&logoColor=white)
![Python](https://img.shields.io/badge/python3-no_dependencies-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Licence](https://img.shields.io/badge/licence-MIT-green?style=for-the-badge)

</div>

---

## ⚡ Quick start

<table>
<tr><td width="60" align="center"><h3>1</h3></td><td>
Download <a href="Install-MGS-Mods.desktop"><b><code>Install-MGS-Mods.desktop</code></b></a> and drop it on your Deck's Desktop.
</td></tr>
<tr><td align="center"><h3>2</h3></td><td>
<i>(Optional)</i> Grab the <b>Better Audio Mod</b> for each game — just leave the
files in <code>Downloads</code>, the installer finds them by itself:<br><br>
🔊 <a href="https://www.nexusmods.com/metalgearsolid2mc/mods/3"><b>MGS2 Better Audio</b></a>
&nbsp;·&nbsp;
🔊 <a href="https://www.nexusmods.com/metalgearsolid3mc/mods/4"><b>MGS3 Better Audio</b></a>
<br><br><sub>Free Nexus login required — grab the <b>Full Version</b>. Skip this and the installer will offer to open the pages for you.</sub>
</td></tr>
<tr><td align="center"><h3>3</h3></td><td>
<b>Double-click the installer.</b> Answer a few questions. Done.
</td></tr>
<tr><td align="center"><h3>4</h3></td><td>
In Steam, for <b>each</b> game → <i>Properties → Launch Options</i>, paste:<br><br>
<code>WINEDLLOVERRIDES="wininet,winhttp=n,b" %command%</code>
</td></tr>
</table>

> **Step 3 is the only manual bit.** Steam silently reverts config edits made
> while it's running, so no script can do it reliably.

---

## 📦 What you get

|  | |
|:--|:--|
| 🖥️ **True 16:10** | Native resolution, correct FOV, no pillarboxing |
| 🎨 **Restored PS2 assets** | Original textures & full-quality models put back |
| 🎬 **HQ cinematics** | Enabled for you — no launcher trip needed |
| 🔊 **Better audio** | Uncompressed PS3-quality sound *(optional)* |
| 🎮 **Correct buttons** | Steam Deck glyphs instead of keyboard prompts |
| ⚡ **Straight in** | KONAMI logos and the launcher both skipped |
| 🔋 **Runs cool** | The high-CPU-usage fix, on by default |

> 🌿 **Vanilla-faithful by design.** Every mod here is a *fix* or a
> *restoration*. AI-upscaled texture packs are deliberately **not** included.

---

## 🧩 The stack

| # | Mod | Author |
|:-:|:--|:--|
| 1 | [MGSHDFix](https://github.com/ShizCalev/MGSHDFix) `3.1.0` | ShizCalev · *orig.* Lyall |
| 2 | Better Audio Mod *(optional)* · [MGS2](https://www.nexusmods.com/metalgearsolid2mc/mods/3) `2.0` / [MGS3](https://www.nexusmods.com/metalgearsolid3mc/mods/4) `2.0` | knight_killer |
| 3 | Community Bugfix Compilation — Base · [MGS2](https://github.com/ShizCalev/MGS2-Community-Bugfix-Compilation) `2.2.0` / [MGS3](https://github.com/ShizCalev/MGS3-Community-Bugfix-Compilation) `1.1.0` | ShizCalev |

Installed in that exact order — it's required, and the kit enforces it.
Everything is fetched live from the authors' official releases; **nothing is
rehosted here.**

---

<details>
<summary><b>🔍 Why this kit exists</b></summary>

<br>

**MGSHDFix has no runtime defaults.** Without a complete `MGSHDFix.settings`
it refuses to launch, and it hard-aborts on any *single* missing key:

```
[MGSHDFix Config Helper] Failed to read config key 'Debug Logging'
in section 'Internal Settings': Section not found
```

That file can normally only be made by the mod's **Windows Config Tool** — a
GUI you'd have to wrestle through Proton. And its ini section names aren't the
tab labels the tool shows you (`[Internal Settings]`, `[Launcher Config]`,
`[Skip Logo Screens]`…), so hand-writing one doesn't work either.

This kit ships a canonical settings file captured from the real Config Tool,
verified **byte-for-byte** against a known-working install.

**The launcher is the other trap.** It's the only place to enable *high quality
cinematics* — so skipping it normally locks you out of that setting forever.
The kit writes the launcher's own save (`launcher_sv`, plain JSON) directly, so
you get the good cutscenes *and* skip the launcher.

</details>

<details>
<summary><b>🎚️ Options you'll be asked</b></summary>

<br>

| Option | Default |
|:--|:--|
| Button icons | `Steam Deck` — Xbox / PS5 / PS2 / Keyboard also offered |
| Audio output | `Stereo (2.0)` — pick 5.1 if docked |
| High-quality cinematics | **on** |
| Skip KONAMI intro logos | **on** |
| Skip the launcher | **on** |
| MGS3 high-res textures | off |
| MGSHDFix update checks | off |

Everything else stays at MGSHDFix's own defaults, which are already right for
the Deck.

</details>

<details>
<summary><b>🔊 Why the audio mod needs one click from you</b></summary>

<br>

It lives on NexusMods, which requires a free login, and **the author does not
permit it being mirrored** — so this kit will never host or auto-fetch it.

🔊 **[MGS2 Better Audio Mod](https://www.nexusmods.com/metalgearsolid2mc/mods/3)**
&nbsp;·&nbsp;
🔊 **[MGS3 Better Audio Mod](https://www.nexusmods.com/metalgearsolid3mc/mods/4)**

Grab the **Full Version** of each (~2–3 GB). The installer makes the rest
painless: if the archives are already on your machine it finds them
automatically — Downloads, Desktop, Documents or home — and if they're missing
it opens the right page for you, then picks the file up afterwards on its own.

Skip it and re-run the kit later any time — it's entirely optional.

</details>

<details>
<summary><b>🧹 Uninstalling & troubleshooting</b></summary>

<br>

**Revert to stock:** Steam → the game → *Properties → Installed Files → Verify
integrity of game files*. Then delete the added files if you want a clean
slate: `winhttp.dll`, `wininet.dll`, `plugins/`, `logs/`, `steam_appid.txt`.

**"Failed to read config key…"** — your settings file doesn't match your
MGSHDFix version. Run `MGSHDFix Config Tool.exe` in the game's `plugins/`
folder and hit *Save and Exit*.

**Mod doesn't load at all** — the launch options aren't set. See step 3.

**Want the launcher back?** `plugins/MGSHDFix.settings` → `Skip Launcher=0`.

**Reading the logs** — MGSHDFix writes `logs/MGSHDFix_Game.log` with every
setting it parsed. They contain embedded binary, so use `grep -a`.

**`No display-attached GPUs were detected`** — harmless on Deck/Proton, appears
every run.

**Versions are pinned on purpose** — the bundled settings file is matched to
MGSHDFix `3.1.0`. A future release could rename sections and break launching.

</details>

---

<div align="center">

### 🙏 Credits

All the real work belongs to **[ShizCalev](https://github.com/ShizCalev)**,
**[Lyall](https://github.com/Lyall)** and **knight_killer**.
<br>This kit only automates installing it — please endorse and star their work.

<br>

**MIT** · [LICENSE](LICENSE) · Requires only `python3`, `bsdtar`, `kdialog`/`zenity` — all stock on SteamOS

</div>
