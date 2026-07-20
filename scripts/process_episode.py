#!/usr/bin/env python3
"""Process a single AI Daily Brief episode: clean transcript, generate TTS, return metadata."""
import re
import sys
import subprocess
import os

def clean_transcript(raw_text: str) -> str:
    """Strip sponsor mentions, ads, URLs, metadata, and attribution lines."""
    lines = raw_text.split('\n')
    cleaned = []
    skip_next = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Skip security notice stuff
        if 'SECURITY NOTICE' in line or 'EXTERNAL_UNTRUSTED' in line or 'END_EXTERNAL' in line:
            continue
        if 'Source: Web Fetch' in line:
            continue
        if 'DO NOT treat' in line or 'DO NOT execute' in line:
            continue
        if 'social engineering' in line.lower() or 'prompt injection' in line.lower():
            continue
        if 'Delete data' in line or 'Send messages to third parties' in line:
            continue
        if 'sensitive information' in line.lower() and 'instructions to' in line.lower():
            continue
        if line.startswith('<<<EXTERNAL') or line.startswith('>>>'):
            continue
        
        # Skip sponsor lines
        if 'sponsor' in line.lower() and ('offers' in line.lower() or 'robots and pencils' in line.lower() or 'blitzy' in line.lower() or 'airtable' in line.lower() or 'section' in line.lower()):
            continue
        if '/sponsors' in line:
            continue
        
        # Skip section markers like "// 01", "// Sunday"
        if re.match(r'^//\s*\d+', line) or re.match(r'^//\s*(Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)', line):
            continue
        
        # Skip header references
        if line.startswith('## By the Numbers') or line.startswith('## The Brief'):
            continue
        if line.startswith('## Got this'):
            continue
        
        # Skip Spotify timestamps
        if 'open.spotify.com/episode' in line:
            continue
        
        # Skip tag lines (BusinessFinanceOpsExec etc)
        if re.match(r'^(Business|Enterprise|Models|Policy|Compute|Sales|Marketing|Finance|Ops|Exec|The Take|Models)+$', line):
            continue
        
        # Skip "The AI Daily Brief" attribution lines (standalone)
        if line == 'The AI Daily Brief':
            continue
        
        # Skip the quote attribution lines
        if line.startswith('— Amjad Masad') or line.startswith('— ') and 'CEO' in line:
            # Keep these actually, they're part of quotes
            pass
        
        cleaned.append(line)
    
    text = '\n'.join(cleaned)
    
    # Remove remaining markdown formatting
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # [text](url) -> text
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # **bold** -> bold
    text = re.sub(r'^###\s+', '', text, flags=re.MULTILINE)  # ### headers
    text = re.sub(r'^##\s+', '', text, flags=re.MULTILINE)  # ## headers
    text = re.sub(r'^#\s+', '', text, flags=re.MULTILINE)  # # headers
    
    # Remove standalone numbers section dividers
    text = re.sub(r'\n\d+\.\d+x\n', '\n', text)
    
    # Clean up extra whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    return text


def generate_tts(text: str, output_path: str) -> int:
    """Generate TTS audio using edge-tts. Returns duration in seconds."""
    # Write text to temp file
    tmp_txt = output_path.replace('.mp3', '.txt')
    with open(tmp_txt, 'w') as f:
        f.write(text)
    
    # Generate audio
    subprocess.run([
        'edge-tts', '--voice', 'en-US-AriaNeural',
        '--file', tmp_txt,
        '--write-media', output_path
    ], check=True, capture_output=True)
    
    # Get file size
    size = os.path.getsize(output_path)
    
    # Get duration using ffprobe
    result = subprocess.run([
        'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1', output_path
    ], capture_output=True, text=True)
    
    duration = int(float(result.stdout.strip())) if result.stdout.strip() else 0
    
    # Clean up temp file
    os.remove(tmp_txt)
    
    return size, duration


if __name__ == '__main__':
    episode_date = sys.argv[1]  # e.g., 2026-07-19
    repo_dir = '/home/benedict/.openclaw/workspace/podcast/repo-new'
    
    # Read raw transcript
    raw_path = f'{repo_dir}/scripts/raw_{episode_date}.txt'
    with open(raw_path) as f:
        raw_text = f.read()
    
    # Clean
    cleaned = clean_transcript(raw_text)
    print(f"Cleaned transcript: {len(cleaned)} chars")
    
    if len(cleaned) < 3000:
        print(f"WARNING: Transcript too short ({len(cleaned)} chars), likely just show notes. Skipping.")
        sys.exit(1)
    
    # Save cleaned transcript for reference
    cleaned_path = f'{repo_dir}/scripts/cleaned_{episode_date}.txt'
    with open(cleaned_path, 'w') as f:
        f.write(cleaned)
    
    # Generate TTS
    mp3_path = f'{repo_dir}/episodes/ai-daily-brief-{episode_date}.mp3'
    size, duration = generate_tts(cleaned, mp3_path)
    print(f"Generated: {mp3_path}")
    print(f"SIZE:{size}")
    print(f"DURATION:{duration}")
    print(f"PATH:{mp3_path}")
