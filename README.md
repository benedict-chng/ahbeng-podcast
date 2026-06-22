# 🎙️ Ah Beng Podcast

A personal podcast feed covering AI, geopolitics, and Chinese-language commentary — all in one place.

## Content

| Series | Source | Description |
|--------|--------|-------------|
| **AI Daily Brief** | [aidailybrief.ai](https://aidailybrief.ai) | Ad-free versions of the daily AI news show. Transcripts are stripped of sponsor reads and regenerated with Edge TTS (Aria Neural voice). |
| **ChinaTalk** | [chinatalk.substack.com](https://chinatalk.substack.com) | Deep-dives into China's tech, energy, and geopolitics — read aloud via TTS. |
| **觀點 (Viewpoints)** | YouTube (畫龍點睛 / 正經龍鳳配 / 唐湘龍時間) | Chinese-language political commentary and analysis. Audio extracted directly from YouTube. |

## Subscribe

Copy this URL into your podcast player's **"Add by URL"** option:

```
https://benedict-chng.github.io/ahbeng-podcast/feed.xml
```

## Feed Structure

```
episodes/       # All MP3 audio files
feed.xml        # RSS 2.0 podcast feed (iTunes-compatible)
icon.png        # Podcast artwork (3000×3000)
index.html      # Landing page for GitHub Pages
```

## Tech Stack

- **TTS:** Edge TTS (`en-US-AriaNeural`) for AI Daily Brief & ChinaTalk episodes
- **YouTube extraction:** `yt-dlp` + `ffmpeg` for Viewpoints episodes
- **Hosting:** GitHub Pages
- **Automation:** OpenClaw cron jobs (daily AI Daily Brief at 6:30 AM AEST)

## Notes

- Viewpoints content is in Mandarin/Cantonese and extracted as-is from YouTube (no ad removal)
- AI Daily Brief episodes have sponsor reads removed before TTS generation
- New episodes are added automatically via cron or manually as needed

---

*Powered by [OpenClaw](https://openclaw.ai) 🦞*
