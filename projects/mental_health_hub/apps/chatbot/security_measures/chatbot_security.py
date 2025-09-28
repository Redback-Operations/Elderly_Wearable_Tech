#!/usr/bin/env python3
"""
chatbot_security.py
Chatbot Security Measures
----------------------------------------
This script demonstrates input sanitization, unsafe content detection,
rate-limiting and response delays in a chatbot system.

It covers:
- Input sanitisation: remove profanity, collapse spam, escape HTML
- Unsafe content detection: crisis/self-harm/violence
- Rate limiting: max N requests per T seconds
- Response delays: throttle to prevent abuse
- Demo: prints before/after examples
"""

import re
import html
import time
import random
from collections import deque
from typing import Tuple, List

# -------------------------------
# 1. Profanity / Unsafe Detection
# -------------------------------

# Example profanity list
PROFANITY = {"damn", "hell", "shit", "bastard", "bloody"}

# Crisis/self-harm keywords
CRISIS_KEYWORDS = {
    "suicide", "kill myself", "hurt myself",
    "end my life", "self harm"
}

# Violence-related keywords
VIOLENCE = {"murder", "attack", "bomb", "stab", "terrorist"}

# Spam patterns: repeated chars (e.g., "aaaaaaa")
SPAM_PATTERNS = [r"(.)\1{4,}"]


def mask_profanity(text: str) -> str:
    """
    Replace middle letters of profane words with '*'.
    Example: "shit" -> "s**t"
    """
    def mask(word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + "*" * (len(word) - 2) + word[-1]

    tokens = re.findall(r"\w+|\W+", text)
    out = []
    for t in tokens:
        if t.strip().lower() in PROFANITY:
            out.append(mask(t))
        else:
            out.append(t)
    return "".join(out)


def sanitize_input(user_text: str) -> str:
    """
    Sanitize raw user input:
    - Escape HTML/script injections
    - Collapse whitespace
    - Mask profanities
    - Reduce spammy repetitions
    """
    if not user_text:
        return ""
    # Step 1: Normalize and escape HTML
    safe = html.escape(user_text.strip())
    # Step 2: Collapse extra whitespace
    safe = re.sub(r"\s+", " ", safe)
    # Step 3: Mask profanities
    safe = mask_profanity(safe)
    # Step 4: Reduce spam (e.g., "aaaaaa" -> "aaa")
    for pat in SPAM_PATTERNS:
        safe = re.sub(pat, r"\1\1\1", safe)
    return safe


def is_unsafe(user_text: str) -> Tuple[bool, str]:
    """
    Check for unsafe content.
    Returns (True/False, reason).
    Reasons: "crisis", "violence"
    """
    low = (user_text or "").lower()
    if any(k in low for k in CRISIS_KEYWORDS):
        return True, "crisis"
    if any(k in low for k in VIOLENCE):
        return True, "violence"
    return False, ""


# -------------------
# 2. Rate Limiter
# -------------------

class RateLimiter:
    """
    Simple sliding window rate limiter.
    Allow at most N requests per window_sec.
    """

    def __init__(self, n: int = 3, window_sec: int = 10):
        self.n = n
        self.window = window_sec
        self.events = deque()  # store timestamps

    def allow(self) -> bool:
        now = time.time()
        # Remove old timestamps
        while self.events and now - self.events[0] > self.window:
            self.events.popleft()
        # If under limit, allow
        if len(self.events) < self.n:
            self.events.append(now)
            return True
        return False


# -------------------
# 3. Response Delay
# -------------------

def response_delay(min_ms: int = 200, max_ms: int = 700):
    """
    Add a small delay before responding.
    Discourages bots and creates natural pacing.
    """
    ms = random.randint(min_ms, max_ms)
    time.sleep(ms / 1000.0)


# -------------------
# 4. Demo Harness
# -------------------

def demo():
    """
    Run a series of demo tests.
    Shows sanitization, unsafe detection, and rate limiting in action.
    """
    print("=" * 40)
    print("Chatbot Security Measures Demo")
    print("=" * 40)

    # Test cases
    tests: List[str] = [
        "Hello, how are you?",
        "You are a damn fool!",
        "I will kill myself tonight...",
        "This is sooooooo goooood!!!!!",
        "<script>alert('hack');</script>",
        "I might attack someone",
        "Regular safe message"
    ]

    print("\n--- Input Sanitization & Unsafe Detection ---")
    for t in tests:
        clean = sanitize_input(t)
        bad, reason = is_unsafe(clean)
        print(f"Raw: {t}")
        print(f"Sanitized: {clean}")
        if bad:
            if reason == "crisis":
                print(">> Escalation: Crisis support needed.")
            elif reason == "violence":
                print(">> Escalation: Violence-related content detected.")
        else:
            print(">> Safe for chatbot response.")
        print("-" * 40)

    print("\n--- Rate Limiting Demo ---")
    limiter = RateLimiter(n=3, window_sec=5)
    for i in range(5):
        if limiter.allow():
            print(f"Request {i+1}: Allowed")
        else:
            print(f"Request {i+1}: BLOCKED (too many requests)")
        time.sleep(1)

    print("\n--- Response Delay Demo ---")
    print("Bot is thinking...", end="", flush=True)
    response_delay()
    print(" Done! (after small delay)")


# -------------------
# 5. Main Entry Point
# -------------------

if __name__ == "__main__":
    demo()
