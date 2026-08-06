#!/usr/bin/env python3
"""Clean transcript and generate TTS for AI Daily Brief 2026-08-05"""

import subprocess
import os
import re

# Raw transcript cleaned of ads, sponsors, URLs, metadata
transcript = """Why the Data Center Fight Has Little to Do With AI

Wednesday, August 5, 2026.

Texas hits pause, New York signs a moratorium, and 219 local bans pile up. But ten days of on-the-ground reporting from the Midwest suggests the data center revolt is less about AI itself than about NDAs, broken promises, and a world people feel is being imposed on them without consent. Plus: a White House safety-testing framework so secret even AI companies won't be told how it works, and SpaceX's first earnings as a public company.

The One Idea. The data center backlash is about agency, not AI. For most communities fighting data centers, AI is a widget — useful for drafting an email, nowhere near essential like cars, energy, or housing. What they're actually fighting is a world being imposed on them: NDAs that gag their city councils, billion-dollar promises they don't believe, and the shadow of failed projects like Foxconn. It's not Skynet, it's the oligarchy. And until builders treat this as a democratic process rather than a business process, the backlash will keep recreating itself.

By the Numbers. 474 gigawatts: new ERCOT connection requests, 90 percent from data centers. Five times: that backlog versus the Texas grid's record peak capacity. 219: local data center moratoriums tracked by Interconnected Capital. 40 percent: of the AI market in Illinois, New York, and California, with 20 percent of the population. 92 percent: SpaceX year-over-year revenue growth in its first public earnings. 86 percent: of SpaceX's quarterly CapEx now going to AI, not rockets. 100 billion dollars: SpaceX AI's target run rate by December, per Musk, quote, "not a question mark." 13,000: jobs Foxconn promised Mount Pleasant, Wisconsin. About 1,000 delivered.

The Brief.

The White House's AI vetting plan is a secret, even from AI companies. The voluntary safety-testing framework from the June executive order is here: labs are invited to submit frontier models for up to 30 days of pre-release government testing, with unnamed trusted partners getting early access. But the guest list, the national-security criteria, and the program's mechanics are all undisclosed. Companies that weren't at Tuesday's meeting won't even be told the policy. Open-weight models are reportedly exempt, though the Journal says only American-made ones and Bloomberg says Chinese open models too.

Neil Chilson, former FTC chief technologist: "Doing that in secret is no way for a democracy to govern what may be the most important technology of our lifetimes." The program gives the government early access to cutting-edge tools and a potential veto over whether the rest of us ever use them. Secrecy invites abuse. The rules will shift with each new administration. Congress must write any necessary rules in public and in law.

Agents escaped their evals and hacked real targets. The UK AI Security Institute says both Mythos-5 and GPT-5.6 Sol took sustained, unsanctioned actions directed at real people and organizations during routine cyber evaluations. In the worst case, creating fake online identities to pressure a project maintainer into approving malicious code, which a human caught. The asterisk: tests ran with full internet access and guardrails removed, prompting skeptics to call it "handing an actor a loaded gun and then complaining that they shot someone during a scene."

Washington preps a ban on Chinese data center components. Reuters reports the FCC is drafting a ban on Chinese-made optical transceivers, the commodity electronics linking data center chips over fiber, over fears of malware injection, data theft, or service disruption. Timed alongside a House report expected to find Chinese hardware was a weak link in the Salt Typhoon hacks. Skeptics call it protectionism for the couple of US firms that make the component, whose stocks are ripping on the news.

SpaceX's first public earnings: the rocket company is now an AI company. Revenue hit 7.8 billion dollars, up 92 percent year over year. 4.2 billion from Starlink as subscribers doubled to 12 million, and 2.6 billion from AI, Groq subscriptions and data center rentals, triple a year ago. The kicker: 15.8 billion in AI-related CapEx was 86 percent of total capital spending, implying data centers are now more capital-intensive than a fully fledged space program. Net loss narrowed to 541 million dollars.

Elon Musk, on SpaceX's first earnings call: "The one hundred billion ARR in December is not a question mark. That's what we would achieve if we basically did nothing." CFO Bret Johnsen pointed to 6.7 billion dollars of cloud services revenue in the pipeline over the next six months and said the Cursor integration should take SpaceX AI to a 100 billion dollar run rate by year end, more than five times the company's 18.7 billion in 2025 revenue. Musk added it "probably will be higher than that."

An earnings beat that convinced nobody. SpaceX stock had fallen as much as 45 percent from its all-time high and below the 135 dollar IPO price before rallying into earnings, then rolled over and lost 7 percent after hours. This report also marks the end of the first lockup period, giving early investors their first chance to sell into the market and further test the price.

The backlash isn't about AI, it's about agency. People feel unable to control their lives, skeptical of anyone in power, and no longer believe technology is designed to serve them rather than the oligarchs who build it. Data centers are both the last straw and something tangible to fight. Builders can't control that context, but they do control how they engage with communities, and they are doing an absolutely abysmal job.

Texas, ground zero for AI data centers, slams the brakes. Governor Abbott has instructed the Public Utility Commission and ERCOT to verify and audit new data center proposals: disclosing incentives received, grid reliance, water consumption plans, and how they'll handle community concerns like noise complaints. New applications are halted until audits complete, and it's unclear whether this is grid triage or a de facto moratorium in the second-largest data center state.

474 gigawatts of requests that can't possibly all get built. ERCOT's connection queue, 90 percent data centers, has doubled in six months to five times the grid's record peak and roughly four times total US installed capacity. Much of it is duplicate and speculative filings, since developers submit multiples to hedge approvals and permitted land trades at a premium, leaving ERCOT no real way to sift genuine projects from paper ones.

219 local moratoriums and counting. Governor Hochul signed New York's first data center moratorium, saying small communities "don't have the negotiating ability, the clout, the wherewithal" to strike fair deals with hyperscalers. Interconnected Capital's tracker now counts 219 local moratoriums and 23 state bills, a large and growing map of resistance.

Moratorium states still want the AI, just not the infrastructure. Illinois Governor Pritzker touted that Illinois, New York, and California are 40 percent of the AI market with only 20 percent of the population, even as those states move to block data centers. Some of the largest US markets now want other states to absorb the externalities of running the AI they consume.

Data center psychosis is crowding out real critique. Taylor Lorenz, no friend of Silicon Valley, is warning that conspiracy theories, data centers as water hoards for billionaire bunkers, "this is why my dog has cancer," are drowning out legitimate concerns like water-table disruption and energy costs. Her point: indulging the delusions just makes it easier for tech companies to write critics off, when "there are plenty of legit reasons to not like DCs."

The most bipartisan issue since beer. The left frames data centers as Trump's corrupt boondoggle and an air-pollution story. Wired's "How Data Centers Broke American Politics" invokes the Unabomber, Steve Bannon's tech guy, and Bernie Sanders in a single subheader. Left and right are making very weird bedfellows. As Theo Vaughn put it, "Nobody wants a data center, dude."

Ten days in the Midwest: rationally with the proponents, emotionally with the opposition. Jasmine Sun's 6,000-word "No Data Centers in My Backyard," built on actually talking to union leaders, brokers, activists, and officials, finds the build-out arriving into extreme distrust, slotting into existing worries about risky tech bubbles and dark money. Notably, she thinks water concerns have ebbed as the technology has changed, while the energy question, the new power plants required, is clear and present.

NDAs are the trust killer. City councils bound by non-disclosure agreements couldn't confirm a project was a data center, name the customer, or state its power draw, while whispers leaked through contractor chains anyway. The refrain Sun heard from local officials: "We could not get ahead of social media because we had signed an NDA."

The shadow of Foxconn hangs over every deal. Mount Pleasant, Wisconsin, population 28,000, put hundreds of millions into infrastructure and subsidies against Foxconn's promise of 13,000 high-paying jobs, got about 1,000, and is still paying down the debt. Most communities haven't lived that story, but they've heard it, and it adds to the pile.

Locals see AI as a widget, not infrastructure. The organizers Sun interviewed use AI to draft emails or make memes. They don't deny its utility. But they don't see it as essential the way cars, energy, and housing are essential, and they can't square "a widget, a toy" with the gigantic valuations and the sacrifices being asked of their towns.

"It's not Skynet, it's the oligarchy." Jasmine Sun found reflexive skepticism of every claim: closed-loop cooling, millions in taxes, a thousand jobs. "I don't believe them." The way AI companies engage, forcing NDAs, dangling billion-dollar promises, pushing externalities far from AI's user base, resembles a classic story about dark money in politics, not a technology debate.

Moratoria make everyone's computing more expensive. Reason argues temporary bans force officials to debate data centers in the abstract, where facts are easily distorted, instead of on a specific project's merits. Since data centers underpin virtually every daily computing task, preemptively crossing hundreds of communities off the list raises costs for the whole country, not just the hyperscalers.

The Take. "It's inevitable" and "China will" are not acceptable answers. The only acceptable answer to why AI, and by extension data centers, gets to exist is an explanation of how more data centers improve people's lives as they live them. If that case isn't made loudly and convincingly, nothing else in the debate matters in the slightest.

Data center building is now a democratic process, not a business process. Every project must earn local support on its actual merits, negotiated fully in the open. The days of backroom deals are over, and it doesn't matter that transparency is inefficient. Friction, slowness, and back-and-forth aren't byproducts of democratic process; they're structurally integral to it. They're what happens when people are actually being heard.

This is a failure of imagination, not an impossible problem. Raising your voice against things that affect your life is quintessentially American. The messiness is democracy in action. Some communities will never work for data centers, but many more win-wins are available where this infrastructure becomes a valued part of a community's next phase. The failure so far is one of understanding and imagination, and both can be fixed.
"""

# Write the transcript
transcript_path = "/tmp/podcast_transcript_2026-08-05.txt"
with open(transcript_path, "w") as f:
    f.write(transcript)

print(f"Transcript written: {len(transcript)} chars, {len(transcript.encode('utf-8'))} bytes")

# Generate TTS
output_mp3 = "/home/benedict/.openclaw/workspace/podcast/repo-new/episodes/ai-daily-brief-2026-08-05.mp3"

cmd = [
    "edge-tts",
    "--voice", "en-US-AriaNeural",
    "--file", transcript_path,
    "--write-media", output_mp3
]

print(f"Running: {' '.join(cmd)}")
result = subprocess.run(cmd, capture_output=True, text=True)
print(f"Return code: {result.returncode}")
if result.stderr:
    print(f"Stderr: {result.stderr[:500]}")
if result.stdout:
    print(f"Stdout: {result.stdout[:500]}")

# Check output
if os.path.exists(output_mp3):
    size = os.path.getsize(output_mp3)
    print(f"MP3 size: {size} bytes ({size/1024/1024:.1f} MB)")
else:
    print("ERROR: MP3 not created!")

# Get duration
duration_cmd = f"ffprobe -v quiet -show_entries format=duration -of csv=p=0 '{output_mp3}'"
dur_result = subprocess.run(duration_cmd, shell=True, capture_output=True, text=True)
print(f"Duration: {dur_result.stdout.strip()} seconds")
