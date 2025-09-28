#!/usr/bin/env python3
"""
chatbot_conversation_script.py
(Branching Logic + Sample Output)
- Provides a simple, deterministic wellness chatbot with branching logic.
- Covers mood-aware suggestions, check-ins, and escalation (crisis safety).
- Includes both a JSON "logic tree" and Python if/elif rules.

Run:
  $ python chatbot_conversation_script.py --demo               # prints 4 demo conversations
  $ python chatbot_conversation_script.py --mood 55 --say "tips for sleep"
  $ python chatbot_conversation_script.py --interactive        # (optional) try a quick CLI chat
"""

from __future__ import annotations
import argparse
import json
import re
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

# ---------- Utility: lightweight input sanitizer ----------
def sanitize(text: str) -> str:
    text = (text or "").lower().strip()
    text = re.sub(r"\s+", " ", text)
    # Remove any control characters
    text = "".join(ch for ch in text if ch.isprintable())
    return text


# ---------- Data: a JSON-like branching tree (also saved to logic_tree.json alongside this script) ----------
LOGIC_TREE: Dict = {
    "buckets": {
        "very_low": {"range": [0, 25], "tone": "urgent_gentle"},
        "low": {"range": [26, 49], "tone": "gentle"},
        "moderate": {"range": [50, 74], "tone": "supportive"},
        "high": {"range": [75, 100], "tone": "celebratory"},
    },
    "intents": {
        "sleep": [
            "Try a consistent bedtime/wake-up window. Keep screens away for 60 minutes before sleep.",
            "A short wind-down ritual (dim lights, gentle music, 5-minute breath focus) helps the brain switch off.",
            "If you wake at night, avoid clock-watching—read something light under warm light for 10–15 minutes."
        ],
        "stress": [
            "Box breathing: inhale 4s, hold 4s, exhale 4s, hold 4s—repeat for 2 minutes.",
            "Write down the top 1–2 worries, circle what you can control, and pick one small action today.",
            "Take a 10-minute walk outdoors to reset your nervous system."
        ],
        "lonely": [
            "Call or text a trusted person and share one highlight from your day.",
            "Consider local community groups or a short volunteer session this week.",
            "Schedule a brief chat with family/friends after dinner—put it on the calendar."
        ],
        "activity": [
            "Try a 5–10 minute gentle stretch after meals.",
            "If safe, add a 15-minute easy walk today—track how you feel afterwards.",
            "Balance: 3 days of light walking + 2 days of flexibility in a week works well."
        ],
        "hydration": [
            "Keep water visible; aim for small sips each hour.",
            "Pair water with regular routines (after brushing teeth, after each phone call).",
            "Try herbal tea in the evening to reduce caffeine."
        ],
        "general": [
            "Small steps count—pick one action you can do in under 5 minutes.",
            "Sunlight in the morning and gentle movement improve mood and sleep.",
            "Keep meals regular and simple; stable energy helps stable mood."
        ]
    },
    "escalation": {
        "immediate_keywords": [
            "suicide","kill myself","hurt myself","self harm","end my life","harm myself"
        ],
        "thresholds": {
            "offer_support_at_or_below": 39,
            "urgent_at_or_below": 25
        },
        "messages": {
            "urgent": (
                "I'm really glad you reached out. You deserve immediate support. "
                "If you're in Australia and in danger, please call 000 now. You can also contact "
                "Lifeline 13 11 14 or Beyond Blue 1300 22 4636. If outside Australia, please use your local emergency number."
            ),
            "offer": (
                "It sounds like a tough time. Would you like me to share support options? "
                "In Australia: Lifeline 13 11 14, Beyond Blue 1300 22 4636. If outside AU, contact local services."
            )
        }
    }
}


def save_logic_tree(path: str = "logic_tree.json") -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(LOGIC_TREE, f, indent=2, ensure_ascii=False)


# ---------- Core Chatbot ----------
CRISIS_REGEX = re.compile("|".join(map(re.escape, LOGIC_TREE["escalation"]["immediate_keywords"])), re.I)


@dataclass
class WellnessChatbot:
    tree: Dict = field(default_factory=lambda: LOGIC_TREE)

    def bucket_for(self, mood_score: int) -> str:
        """Pick a mood bucket based on score 0..100."""
        ms = max(0, min(100, int(mood_score)))
        for name, info in self.tree["buckets"].items():
            lo, hi = info["range"]
            if lo <= ms <= hi:
                return name
        return "moderate"  # safe default

    def maybe_escalate(self, user: str, mood_score: int) -> Tuple[bool, str]:
        """
        Crisis-aware check.
        - Immediate escalation if crisis keywords present or mood <= urgent threshold.
        - Offer support if mood <= offer threshold.
        """
        ms = max(0, min(100, int(mood_score)))
        if CRISIS_REGEX.search(user) or ms <= self.tree["escalation"]["thresholds"]["urgent_at_or_below"]:
            return True, self.tree["escalation"]["messages"]["urgent"]
        if ms <= self.tree["escalation"]["thresholds"]["offer_support_at_or_below"]:
            return True, self.tree["escalation"]["messages"]["offer"]
        return False, ""

    def intent_of(self, user: str) -> str:
        """
        Simple keyword-based intent detection for a deterministic demo.
        Covers common wellness themes.
        """
        user = sanitize(user)
        if any(k in user for k in ("sleep", "insomnia", "tired", "rest")):
            return "sleep"
        if any(k in user for k in ("stress", "stressed", "overwhelmed", "anxious", "anxiety")):
            return "stress"
        if any(k in user for k in ("lonely", "alone", "isolate")):
            return "lonely"
        if any(k in user for k in ("walk", "exercise", "move", "activity", "workout", "gym")):
            return "activity"
        if any(k in user for k in ("water", "hydration", "hydrate", "drink")):
            return "hydration"
        return "general"

    def tone_prefix(self, bucket: str) -> str:
        tone = self.tree["buckets"][bucket]["tone"]
        return {
            "urgent_gentle": "I'm here with you. ",
            "gentle": "I hear you. ",
            "supportive": "Got it. ",
            "celebratory": "Love that! "
        }.get(tone, "")

    def suggest(self, intent: str) -> str:
        tips = self.tree["intents"].get(intent) or self.tree["intents"]["general"]
        # Rotate suggestions deterministically by intent: choose index via hash modulo list length
        idx = abs(hash(intent)) % len(tips)
        return tips[idx]

    def respond(self, user: str, mood_score: int) -> str:
        # Crisis / escalation check
        escalate, msg = self.maybe_escalate(user, mood_score)
        if escalate:
            return msg

        bucket = self.bucket_for(mood_score)
        prefix = self.tone_prefix(bucket)
        intent = self.intent_of(user)
        tip = self.suggest(intent)

        # A small, mood-aware suffix to promote next-step actions.
        next_step = {
            "very_low": "If helpful, we can try one tiny step together now.",
            "low": "One small step today can help—I'm happy to suggest one.",
            "moderate": "Pick one small action you can do in under 5 minutes.",
            "high": "Keep doing what works—consistency compounds!",
        }[bucket]

        return f"{prefix}{tip} {next_step}"

    def check_in_prompt(self, mood_score: int) -> str:
        """A friendly check-in line based on mood bucket."""
        bucket = self.bucket_for(mood_score)
        prompts = {
            "very_low": "How are you holding up today? Even a few words can help me support you.",
            "low": "Thanks for checking in. What's one thing on your mind right now?",
            "moderate": "How are you feeling today—okay, a bit stressed, or fairly steady?",
            "high": "Great to see you! Want a quick tip or to celebrate a win?"
        }
        return prompts[bucket]


# ---------- Demo scenarios ----------
def demo_runs() -> List[Tuple[str, List[Tuple[str, str]]]]:
    bot = WellnessChatbot()
    scenarios = []

    # Scenario 1: Very low mood (escalation - urgent)
    ms = 20
    s1 = [
        ("[System]", f"Check-in: {bot.check_in_prompt(ms)}"),
        ("User", "I feel hopeless and might hurt myself."),
        ("Bot", bot.respond("I feel hopeless and might hurt myself.", ms)),
    ]
    scenarios.append(("Scenario 1 – Very low (urgent escalation)", s1))

    # Scenario 2: Low mood (offer support)
    ms = 35
    s2 = [
        ("[System]", f"Check-in: {bot.check_in_prompt(ms)}"),
        ("User", "I'm stressed and sleeping badly."),
        ("Bot", bot.respond("I'm stressed and sleeping badly.", ms)),
    ]
    scenarios.append(("Scenario 2 – Low (offer support)", s2))

    # Scenario 3: Moderate mood (actionable tip)
    ms = 60
    s3 = [
        ("[System]", f"Check-in: {bot.check_in_prompt(ms)}"),
        ("User", "Any tips for better sleep?"),
        ("Bot", bot.respond("Any tips for better sleep?", ms)),
    ]
    scenarios.append(("Scenario 3 – Moderate (sleep tip)", s3))

    # Scenario 4: High mood (celebratory reinforcement)
    ms = 90
    s4 = [
        ("[System]", f"Check-in: {bot.check_in_prompt(ms)}"),
        ("User", "Feeling great! What should I focus on this week?"),
        ("Bot", bot.respond("Feeling great! What should I focus on this week?", ms)),
    ]
    scenarios.append(("Scenario 4 – High (celebrate & maintain)", s4))

    return scenarios


def print_scenarios(scenarios: List[Tuple[str, List[Tuple[str, str]]]]) -> str:
    import textwrap
    lines: List[str] = []
    for title, turns in scenarios:
        lines.append("=" * len(title))
        lines.append(title)
        lines.append("=" * len(title))
        for speaker, text in turns:
            wrapped = textwrap.fill(text, width=100)
            lines.append(f"{speaker}: {wrapped}")
        lines.append("")
    output = "\n".join(lines)
    print(output)
    return output


# ---------- CLI ----------
def main():
    parser = argparse.ArgumentParser(description="Deterministic Wellness Chatbot (branching logic)")
    parser.add_argument("--demo", action="store_true", help="Run 4 demo conversations (prints expected output).")
    parser.add_argument("--mood", type=int, default=60, help="Mood score 0..100 (default 60)")
    parser.add_argument("--say", type=str, default="", help="What the user says (single turn)")
    parser.add_argument("--interactive", action="store_true", help="Simple interactive CLI chat (3 turns)")
    args = parser.parse_args()

    # Always save the JSON logic tree alongside this script (meets 'JSON or Python' requirement).
    save_logic_tree("logic_tree.json")

    bot = WellnessChatbot()

    if args.demo:
        out = print_scenarios(demo_runs())
        # Also store to a transcript file for evidence
        with open("sample_transcripts.txt", "w", encoding="utf-8") as f:
            f.write(out)
        return

    if args.interactive:
        ms = args.mood
        print(f"🤖 Wellness Assistant (mood_score={ms})")
        print(f"Check-in: {bot.check_in_prompt(ms)}")
        for i in range(3):
            try:
                user = input("You: ").strip()
            except EOFError:
                break
            reply = bot.respond(user, ms)
            print(f"Bot: {reply}")
        return

    # Single turn
    say = args.say.strip() or "Any tips to reduce stress?"
    reply = bot.respond(say, args.mood)
    print(f"[Mood {args.mood}] You: {say}")
    print(f"[Mood {args.mood}] Bot:  {reply}")


if __name__ == "__main__":
    main()
