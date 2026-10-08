#!/usr/bin/env python3
"""Clean aidailybrief.ai transcript for TTS: strip sponsors, ads, URLs, metadata."""
import re
import sys

def clean_transcript(raw_text: str) -> str:
    # Remove security notice wrapper
    text = raw_text
    # Strip the SECURITY NOTICE block
    text = re.sub(r'SECURITY NOTICE:.*?third parties\.\s*', '', text, flags=re.DOTALL)
    # Strip external content wrappers
    text = re.sub(r'<<<EXTERNAL_UNTRUSTED_CONTENT[^>]*>>>.*?Source: Web Fetch\s*---\s*', '', text, flags=re.DOTALL)
    text = re.sub(r'<<<END_EXTERNAL_UNTRUSTED_CONTENT[^>]*>>>', '', text)
    
    lines = text.strip().split('\n')
    cleaned = []
    skip_patterns = [
        r'^Today\'s sponsors',
        r'^\[all offers',
        r'^// \d',
        r'^By the Numbers',
        r'^\d+[A-Z]?$',  # standalone numbers like "11M", "29"
        r'^Views on',
        r'^Signatories to',
        r'^How fast',
        r'^Share of companies',
        r'^Real workplace',
        r'^How long',
        r'^How many',
        r'^Score lift',
        r'^Token reduction',
        r'^Effort levels',
        r'^Model sizes',
        r'^Levels of product',
        r'^Unknown categories',
        r'^Got this from a colleague',
        r'^The AI Daily Brief$',
        r'^AI Daily Brief$',
    ]
    
    for line in lines:
        line = line.strip()
        if not line:
            if cleaned and cleaned[-1] != '':
                cleaned.append('')
            continue
        
        skip = False
        for pat in skip_patterns:
            if re.match(pat, line):
                skip = True
                break
        if skip:
            continue
            
        # Remove markdown links [text](url) -> text
        line = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'\1', line)
        # Remove bare URLs
        line = re.sub(r'https?://\S+', '', line)
        # Clean up "—" dashes at start
        
        cleaned.append(line)
    
    result = '\n'.join(cleaned).strip()
    # Remove multiple blank lines
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result

if __name__ == '__main__':
    raw = sys.stdin.read()
    print(clean_transcript(raw))
