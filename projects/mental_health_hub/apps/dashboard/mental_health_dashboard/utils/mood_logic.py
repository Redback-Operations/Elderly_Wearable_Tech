def get_mood_zone(score):
    if score >= 75:
        return "good"
    elif score >= 65:
        return "moderate"
    else:
        return "low"
