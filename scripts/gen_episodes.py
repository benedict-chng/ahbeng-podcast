#!/usr/bin/env python3
"""Generate podcast episodes from aidailybrief.ai transcripts."""
import subprocess
import sys
import os
import re
from pathlib import Path

REPO = Path("/home/benedict/.openclaw/workspace/podcast/repo-new")
EPISODES_DIR = REPO / "episodes"
SCRIPTS_DIR = REPO / "scripts"

# Episode definitions: (date, title, raw_text)
episodes = []

# Episode 2026-07-21
ep_0721_raw = """// Tuesday · July 21, 2026
OpenAI's own policy chief tweeted the quiet part out loud — that Washington could smother Chinese open-weight models with manufactured regulatory FUD — and set off a firefight that reveals a bigger truth: whatever gets decided in these White House turf battles will shape which models you can actually use, at what cost, and how you build with them.

The One Idea
The fight over open-weight models is about which AI you'll be allowed to use.

A single 11-million-view tweet from OpenAI's Dean Ball exposed a real debate inside the Trump administration: how to blunt Chinese open-weight models without an outright ban. The proposed tool — manufactured regulatory fear, uncertainty, and doubt — pits closed-lab incumbents against open-source champions, with China simultaneously positioning itself as the global defender of open AI. This isn't abstract geopolitics; it will directly determine which models are available to you, at what price, and how you architect systems for work.

Why AI policy is suddenly your problem
NLW frames the whole episode as a case that open-source policy isn't theoretical: it will dictate which models you can access, at what cost, and how you design systems for work. The stakes blend directly into US democratic politics ahead of the elections.

Kimi K3 reignites the DeepSeek-style freak-out
The release of Moonshot's Kimi K3 dominated the discourse over the weekend more loudly than anything since the original DeepSeek moment in January 2025, reigniting fears about advanced Chinese open-weight models.

White House is quietly eyeing action on open models
Semaphore reported the administration is considering action against open models, with a senior official citing "plenty of ongoing work" beyond June's cybersecurity executive order. At minimum, the White House is paying very close attention.

Gold Eagle may decide who gets frontier models
CNBC reported the administration expects to limit Western frontier model releases on an ongoing basis. The new clearinghouse, Gold Eagle, initially framed around sharing AI-detected software vulnerabilities, will also reportedly determine which companies can access new frontier models.

The 'voluntary' model regime is a fiction now
Officials insist decisions on release timing and scope rest entirely with the companies, but NLW argues that's plainly no longer true. The only open question is whether the current de facto informal regime — Lutnick and others deciding when a lab has eaten enough crow — gets formalized.

A FINRA-style self-governing body is on the table
Bloomberg reported the White House is weighing a self-governing body proposed by Demis, with financial regulator FINRA as the model. Critics note financial services aren't exactly famous for rapid innovation under that structure.

A quiet effort to curb Chinese AI is forming
Axios reported the administration is showing signs it could ban cutting-edge Chinese models — potentially locking in OpenAI and Anthropic dominance. Options include adding Chinese AI firms to the entity list and an executive order making US firms liable for any breaches from hosting Chinese models.

You don't need a ban to kill a model
The White House reportedly understands it doesn't have to outright ban Chinese models to block their use — one source described a push to highlight potential backdoors and security gaps. NLW ties this to prior Operation Choke Point-style regulatory pressure.

AI standards center chief abruptly resigns
Chris Fall, head of the Center for AI Standards and Innovation, resigned after just three months. Analyst Max Weinbach: "I hope this is because what he was pushing was stupid, rather than the one I'm terrified of, which is he's fighting for the smart solution and it isn't working."

"Turf battles, staff turnover, and hollowed-out offices have contributed to a chaotic environment for policymaking on AI." — The Information, describing US AI policy as veering wildly from hands-off to extraordinarily heavy-handed in a very short period, and doing so inconsistently even inside the administration.

"We must seize this rare historic opportunity, encourage open source development, openness, cooperation, and sharing." — President Xi Jinping, at the World AI Conference in Beijing. Xi endorsed an open-source approach and pitched a Chinese-led AI future to the Global South, touting 29 signatories to a new World AI Cooperation Organization.

"China's AI open source strategy may end up being seen as one of the greatest strategic masterstrokes of all time." — Geopolitics commentator Bertrand, arguing China turned a semiconductor disadvantage into an advantage — getting US tech leaders and officials to publicly side with China's open approach against their own companies. The irony: without export controls, the US might have made a fortune selling compute instead.

"Open weight models are inherently decelerationist." — Dean Ball, head of strategic futures at OpenAI. Ball argued accelerationists like open weights because they're effectively ungovernable, and that open weights deter further AI CapEx — echoing the market-skeptic case that good-enough cheap models undercut demand for premium frontier models.

"You don't need to ban open source. You just need to direct every agency to issue soft law that creates FUD." — Dean Ball, predicting the Trump administration's best strategy would be to manufacture regulatory risk around Chinese open-weight models — enough to make every regulated enterprise back off, without scaring hyperscalers into pushing startups toward sketchier providers. This is the passage that ignited the firestorm.

"One probable outcome of an open-weight model dominant world is full AI communism." — Dean Ball, framing a state-provided AI-as-public-good future as a dystopian hellscape, drawing accusations that OpenAI simply wants to preserve a monopoly and avoid competition.

"Actually an insane thing for OpenAI's head of strategy to publicly say." — Cloudflare engineer Dylan Mulroy. Critics piled on — Epic's Tim Sweeney mocked the taco-company analogy, and entrepreneurs called the argument grotesque. Much of the anger was that Ball now speaks as an extension of OpenAI, giving the incumbent's monopoly interest a policy voice.

"It's 2001. Steve Ballmer calls Linux cancer. It's 2026. Open source LLMs are called decelerationist and communist." — Qualia Script, on X. Critics drew a direct line to Ballmer's early-2000s attacks on Linux, arguing history is repeating: incumbents labeling cheaper, better open-source competition as ideologically dangerous and seeking to regulate it away.

"Every government will be safetyists once they understand themselves to be in the foxhole." — Dean Ball, later clarifying his post was a prediction, not a prescription, and reaffirming his support for open source — but insisting the national security implications of frontier open-weight distribution are becoming too severe, and governments will act with far lower risk tolerance than his own.

"The weaponization of regulatory uncertainty as a competitive tool should be completely unacceptable." — David Sacks, former White House AI czar. Sacks blasted Ball, arguing regulatory decisions must be grounded in facts and evidence, not manufactured fear. He accused the closed-lab duopoly of wanting the government to eliminate their open-source competition, and called on Silicon Valley to defend open competition.

"Trying to gatekeep models doesn't work." — David Sacks, arguing the answer to advanced Chinese cyber capabilities is AI-powered cyber defense, not gatekeeping. Box's Aaron Levie agreed, warning that locking down the US ecosystem guarantees America loses the global battle; the fix is faster progress and broad diffusion.

"Releasing the weights for a frontier-level model is effectively dumping." — Haseeb Qureshi, investor. Some tried to steelman Ball: China's open-weight releases resemble industrial dumping — subsidizing unprofitable output to kill competitors. Yann LeCun rejected the framing ("So releasing Linux was dumping?"), while Qureshi said China's calculated state-level strategy differs from the spirit of traditional open source.

"The race now is to build industrial systems that put the frontier to work." — Ryan Fettesiyak, American Enterprise Institute. AEI argued China has reached semi-permanent benchmark parity but lacks the compute to serve models globally. Victory now hinges on high-bandwidth memory, advanced packaging, data-center timelines, and resilient energy grids — not model benchmarks alone.

Kimi K3 buckled under demand in 48 hours
Moonshot paused new Kimi K3 subscriptions after demand hit its capacity limits within 48 hours — the first time a Chinese lab has visibly run out of compute after a launch. Notably, only hardcore enthusiasts testing over a weekend was enough to knock over their servers, suggesting severe inference constraints.

"Open weights eliminate software licensing costs, they do not eliminate physics." — Ricky Ho, family office investor, arguing the real signal from Kimi K3 is that frontier AI demand is now constrained by compute rather than customers. Free weights still require enormous GPU, networking, power, and data-center investment to serve at scale.

"We are making it easier for China to catch up and are acting surprised when they release good models." — Chris Maguire, Council on Foreign Relations, arguing that Chinese labs' compute constraints are real, and that selling, smuggling, and remote access to chips is undercutting export controls. Closing loopholes and enforcing them vigorously could still constrain China's future AI capabilities.

"The tension between a growing approval regime for closed models and none for open models will need to be resolved." — Professor Ethan Mollick, laying out four possible paths: an approval regime for all models, truly voluntary or none, approval for closed but not open or its reverse, or blessing and banning individual labs. Each carries large consequences for the market.

"We must not let our companies use these Chinese models to save a few bucks." — CNBC's Jim Cramer, backing OpenAI and Anthropic and framing the issue as vital national security — evidence that this debate is only going to get louder.

We're heading toward the crescendo, not past it
NLW doesn't think this weekend is the decisive turning point — he expects attention to shift again once Fable 5.1 or GPT-6 drops. But policy decisions on open-weight models could reshape the whole calculus around AI costs and multi-model architectures, so now is the time to start paying attention."""

# Episode 2026-07-20
ep_0720_raw = """// Monday · July 20, 2026
No new-model drama today — instead a practical field guide to squeezing every drop out of Fable 5 and GPT-5.6 Sol, from managing a more tenacious model's boundaries to raising your own ambition until the limits reveal themselves.

The One Idea
Every big model leap demands you unlearn your old prompts — and raise your ambition.

With Fable 5 and GPT-5.6 Sol in hand, the tips converging across the discourse point two directions. First: the way you prompted last generation now often hurts you — stale rule lists, brevity hacks, and maxed-out settings all backfire on more tenacious, more capable models. Second and more important: the real unlock isn't better prompting, it's higher ambition — pushing models onto high-leverage impact work, inviting them in as co-creators of the process, and adopting new interaction patterns like loops. The individual lesson has an organizational twin: stop using AI to do the same work faster and start unlocking categories of work that weren't possible before.

Recorded before the Kimi panic
NLW flags that this episode was taped Thursday afternoon as markets freaked out over Kimi So tearing value off the Nasdaq — so if Dario and Sam panic-release new Fable and GPT versions, that's why they aren't covered here.

New models demand new ways of interacting
The tips for getting the most out of Fable 5 and 5.6 Sol can't be captured in benchmarks — they have to be discovered through trial and error. Common threads across both models suggest not just new prompting tricks but new patterns of interaction that will become increasingly common.

"5.6 Sol is a lot more tenacious and thorough than previous models." — Eric Provencher, Codex team, warning that many people still prompt 5.6 Sol exactly as they did 5.5, and the model's added tenacity changes what good prompting looks like.

With tenacious models, boundaries matter more
Boundaries are the few instructions that keep a model from creating extra work or taking unintended actions — e.g. 'keep approved dates unchanged,' 'use only supplied sources,' 'prepare the message as a draft, don't send it.' The more powerful the model, the bigger the real-world consequences of not setting them, from burning tokens to firing off an unapproved message to a customer.

Steer and queue: iterate without waiting for the run to finish
As ChatGPT and Codex converge, you no longer have to wait turn-by-turn. 'Steer' adds a message to the current run to change direction mid-task; 'Queue' saves it for the next run. This reduces the latency of collaborating with AI, which matters more as models get more powerful.

Prompt 'chat' and 'work' differently
OpenAI's guide now splits best practices for chat versus work. Work tips carry a cost-and-efficiency consciousness: start with one reviewable result, narrow or stop a task if it drifts, and remember a task using more credits can still be worthwhile if it saves time or improves an important decision.

The rambler shall inherit the earth
NLW champions voice dictation — ChatGPT's native dictation is best-in-class even without Whisperflow. In a world where AI needs more context, rambling a stream of consciousness often feeds the model better than a hyper-precise typed note that leaves context out.

Delete instructions from your old prompts
OpenAI's rule is to state each instruction exactly once. Removing repeated instructions raised scores 10 to 15 percent while cutting tokens by up to 66 percent. The giant rule lists written for older models now make 5.6's answers worse and cost more.

Two dials now: model size and thinking effort
Pick the model size — Sol for the hardest problems, Terra for everyday business, Luna for cheap fast tasks — and set how hard it thinks across six effort levels. OpenAI's advice: start at your last model's setting, then test one level lower, since the new generation usually needs less. Save max for genuinely hard problems.

Dialing everything to max is emotionally hard to resist
NLW notes the temptation to crank settings to max on every problem — wouldn't you always want the most intelligence? But it's increasingly clear that's not optimal even before costs, which is why OpenAI is giving discrete guidance to do less.

Old brevity rules now cut too much
GPT-5.6 defaults to shorter answers than 5.5, so blanket 'keep it brief' rules carried over from older models can strip out too much. When you want short, tell it which information to keep and which detail to drop.

Spell out tone behavior instead of adjectives
Terms like 'friendly' and 'empathetic' are too abstract. Instead specify the actual writing behavior — 'name the customer's problem in your first line, give the fix as numbered steps, skip the apology paragraph' — to get the same tone every time.

"The biggest unlock happened when I went beyond automating busywork to high-leverage work." — Christine Xu, AI UX PM at Intuit, arguing most people use models to clear the 'dopamine backlog' of little tasks — but the real leap comes from handing over the hard work you didn't trust the model with before.

Automate optics, copilot execution, spar on impact
Borrowing Shreyas Doshi's three levels of product work, Christine Xu maps each to a mode: Claude as autopilot for optics work (status updates, visibility), Claude as copilot for execution (weekly context dumps, planning, customer themes), and Claude as sparring partner for the hardest-to-start impact work. Automate optics ruthlessly; ask for judgment, not just summaries.

"It feels more like a conversation with a smart colleague than reading walls of text." — Christine Xu, on Fable 5, praising its calmness and concision — which helps keep a train of thought going during high-leverage thinking.

"Fable is the first model where quality is bottlenecked by my ability to clarify its unknowns." — Tariq, Cloud Code team, framing prompts, skills and context as 'the map' and the actual codebase and constraints as 'the territory.' The gap between them — unknowns — is what the model must guess about, and the more work it does, the more unknowns it hits.

Reducing unknowns is the skill of agentic coding
Tariq breaks work into known knowns (what's in your prompt), known unknowns (what you know you haven't figured out), unknown knowns (obvious things you'd recognize but never write down), and unknown unknowns. Being too specific makes the model over-follow you; too vague and it defaults to generic best practices. Working with Fable is an iterative process of discovering unknowns before, during, and after implementation.

Use the model to surface your own blind spots
Two concrete techniques from Tariq: a 'blind spot pass' — 'teach me my unknown unknowns about color grading so I can prompt better' — and brainstorm-and-prototype — 'make me an HTML page with four wildly different design directions so I can react.' Verbalizing unknown knowns early is far cheaper than discovering them mid-implementation.

Rerun meta-prompts every time intelligence jumps
Daniel Meisler recommends tactical meta-prompts to rerun on every state-of-the-art release — including a 'self model audit' that reads what your harness believes about you and flags where it's optimizing for a stale, aspirational, or wrong version of you. It's essentially using each new model as a trigger for context hygiene.

Test new models by going really, really big
Meisler's 'overall life and work optimization' prompts throw massive scope at a model — analyzing all your projects, your field, AI, and society to find your ikigai. Even if it's not your cup of tea, it's a great way to take a model's vibe temperature on hard, open-ended questions.

"I don't use adjectives. I give it a bar it can check itself against, then I make that bar hard." — Matt Schumer, saying telling Fable to make something 'high quality' stops at its own too-low idea of good enough. Instead give it a concrete, hard test — 'a stranger can't tell our render from the real photo' — then put it on a loop that never lets it decide it's finished.

Four kinds of loops
A Claude Devs post categorizes loops: turn-based (you direct each turn, best for short one-off tasks), goal-based (an evaluator model sends work back until success criteria or max turns are met), time-based (recurring on an interval), and proactive (event- or schedule-triggered, no human in real time). Defining success criteria stops the model from ending a loop early.

Assume no limits — then find where they actually are
NLW's core takeaway: every big intelligence jump requires the hard work of re-testing old habits that no longer help, and finding new techniques — sometimes whole new interaction patterns like loops — that unlock the new capability. The through-line is to ratchet up ambition and attempt the biggest, hardest things so the real limits reveal themselves.

The organizational version of the same lesson
It's easy for businesses to default to using AI for the work they already do — just faster, cheaper, or slightly better. The real unlock is a new relationship with work and entirely new categories of work that weren't possible before. Harder to figure out, but far more exciting."""

# Write and generate for each episode
episodes_to_process = [
    ("2026-07-21", "The Fight Over Which AI Models You Can Use", ep_0721_raw),
    ("2026-07-20", "How to Get the Most Out of Fable 5 and GPT-5.6 Sol", ep_0720_raw),
]

for date_str, title, raw_text in episodes_to_process:
    text_file = SCRIPTS_DIR / f"transcript_{date_str}.txt"
    text_file.write_text(raw_text.strip())
    size = text_file.stat().st_size
    print(f"[{date_str}] Transcript: {size} bytes")
    if size < 5000:
        print(f"[{date_str}] WARNING: Transcript too short (<5KB), skipping")
        continue
    
    mp3_file = EPISODES_DIR / f"ai-daily-brief-{date_str}.mp3"
    print(f"[{date_str}] Generating TTS → {mp3_file.name}")
    result = subprocess.run(
        ["edge-tts", "--voice", "en-US-AriaNeural", "--file", str(text_file), "--write-media", str(mp3_file)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"[{date_str}] ERROR: {result.stderr}")
    else:
        mp3_size = mp3_file.stat().st_size
        print(f"[{date_str}] ✅ MP3 generated: {mp3_size} bytes ({mp3_size/1024/1024:.1f} MB)")
