def format_user_input(dest, days, interests, budget):
    try:
        days = int(days)
    except:
        days = 5  # fallback default

    budget = budget if budget else "Moderate"

    return dest, days, interests, budget
