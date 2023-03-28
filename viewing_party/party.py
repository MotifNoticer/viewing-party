# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    new_movie = {}
    
    if not title or not genre or not rating:
        return None

    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):

    user_data["watched"] += [movie]

    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"] += [movie]

    return user_data

def watch_movie(user_data, title):

    for i in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][i]["title"]:
            user_data["watched"] += [user_data["watchlist"][i]]
            user_data["watchlist"].pop(i)

    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    watched = user_data["watched"]

    if not watched:
        return 0
    
    sum = 0

    for i in range(len(watched)):
        sum += watched[i]["rating"]

    # average = sum(values) / len(user_data)
    avg_rating = sum / len(watched)



    return avg_rating

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

