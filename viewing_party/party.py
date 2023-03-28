# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    new_movie = {}
    
    if not title or not genre or not rating:
        return None
    
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

    watchlist = user_data["watchlist"]

    for i in range(len(watchlist)):
        if title == watchlist[i]["title"]:
            user_data["watched"] += [watchlist[i]]
            watchlist.pop(i)

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

def get_most_watched_genre(user_data):
    pass
    # What is deemed most popular? By rating? By count?
    watched = user_data["watched"]

    genre_dict = {}

    # watched[0]["genre"] == "Fantasy"
    for movie in watched:
        genre_dict[movie["genre"]] = 1
        
    for movie in watched:
        if genre_dict[movie["genre"]] >= 1:
            genre_dict[movie["genre"]] += 1
            continue

    # max(d, key = d.get), min(d, key = d.get)
    most_watched = max(genre_dict, key = genre_dict.get)
    
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

