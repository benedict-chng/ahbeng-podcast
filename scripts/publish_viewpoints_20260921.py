#!/usr/bin/env python3
"""Publish viewpoints 2026-09-21 episode: insert item, update lastBuildDate,
prune oldest to keep 30, update index.html, validate, commit+push."""
import re, subprocess, sys
import xml.etree.ElementTree as ET

os_ = __import__('os')
os_.chdir(os_.path.expanduser('/home/benedict/.openclaw/workspace/podcast/repo-new'))

GUID = 'viewpoints-zhenglongfengpei-2026-09-21'
MP3 = f'episodes/{GUID}.mp3'
SIZE = 38177061
DUR = 4772
PUB = 'Tue, 22 Sep 2026 08:10:00 +1000'
TITLE = '\u89c0\u9ede\u2502\u6b63\u7d93\u9f8d\u9cf5\u914d \u2014 \u7fd2\u8fd1\u5e73\u8a2a\u7f8e\uff0160 \u5e74\u6700\u9ad8\u898f\u683c\uff01(2026-09-21)'
DESC = ("26.09.21\u3010\u89c0\u9ede\u2502\u6b63\u7d93\u9f8d\u9cf5\u914d\u3011\u7fd2\u8fd1\u5e73\u8a2a\u7f8e\uff0160 \u5e74\u6700\u9ad8\u898f\u683c\uff01 Chinese-language geopolitical analysis from the Viewpoints channel "
        "(\u89c0\u9ede/\u756b\u9f8d\u9ede\u775b). This episode: Xi Jinping visits the United States ahead of the Trump\u2013Xi summit \u2014 "
        "billed as the highest-protocol China\u2013US meeting in 60 years. Audio extracted from the original YouTube live stream, "
        "published as-is. Approx 1 hour 20 minutes.")

ITEM = f"""    <item>
      <title>{TITLE}</title>
      <description>{DESC}</description>
      <enclosure url="https://benedict-chng.github.io/ahbeng-podcast/{MP3}" type="audio/mpeg" length="{SIZE}" />
      <pubDate>{PUB}</pubDate>
      <itunes:duration>{DUR}</itunes:duration>
      <guid>{GUID}</guid>
    </item>
"""

# --- feed.xml ---
feed = open('feed.xml', encoding='utf-8').read()
assert GUID not in feed, 'already published!'
m = re.search(r'<lastBuildDate>[^<]*</lastBuildDate>', feed)
feed = feed.replace(m.group(0), f'<lastBuildDate>{PUB}</lastBuildDate>')
i = feed.index('    <item>')
feed = feed[:i] + ITEM + feed[i:]

# prune oldest (last <item>) to keep exactly 30
items = list(re.finditer(r'    <item>.*?</item>\n', feed, re.S))
n = len(items)
pruned_guid = None
if n > 30:
    last = items[-1]
    pruned_guid = re.search(r'<guid>([^<]*)</guid>', last.group(0)).group(1)
    feed = feed[:last.start()] + feed[last.end():]
open('feed.xml', 'w', encoding='utf-8').write(feed)
ET.parse('feed.xml')  # validate
print(f'feed.xml: now {n - (1 if n > 30 else 0)} items, pruned: {pruned_guid}')

# --- index.html ---
html = open('index.html', encoding='utf-8').read()
entry = f"""  <p><strong>{TITLE}</strong> \U0001f3a7 <em>Raw radio audio, published as-is</em><br>
Xi Jinping's US visit ahead of the Trump\u2013Xi summit \u2014 billed as the highest-protocol China\u2013US meeting in 60 years. Chinese-language episode from the Viewpoints channel (\u89c0\u9ede/\u756b\u9f8d\u9ede\u775b), ~1h 20m.<br>
    <a href="{MP3}">\u25b6 Listen (~1h 20m)</a></p>
"""
anchor = html.index('<h3>Latest Episodes</h3>') + len('<h3>Latest Episodes</h3>\n')
html = html[:anchor] + entry + html[anchor:]
# remove last episode entry (a <p> starting with <strong>) to match feed
ps = list(re.finditer(r'  <p><strong>.*?</p>\n', html, re.S))
if ps:
    lastp = ps[-1]
    if pruned_guid and pruned_guid in lastp.group(0):
        html = html[:lastp.start()] + html[lastp.end():]
        print('index.html: removed entry for pruned guid')
open('index.html', 'w', encoding='utf-8').write(html)
print('index.html: new entry added')

# --- prune old audio file from git if needed ---
if pruned_guid:
    r = subprocess.run(['git', 'ls-files', 'episodes/'], capture_output=True, text=True)
    for line in r.stdout.splitlines():
        if pruned_guid in line:
            os_.remove(line)
            print(f'removed file: {line}')

# --- commit & push ---
for cmd in [['git', 'add', '-A'], ['git', 'commit', '-m', f'publish {GUID}; prune {pruned_guid}'],
            ['git', 'push']]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print('GIT ERROR:', cmd, r.stderr[-500:]); sys.exit(1)
print('pushed OK')
