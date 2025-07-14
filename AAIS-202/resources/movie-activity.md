
### **Activity: Movie Watchlist Manager with JSON**

**Scenario:**

You’re building a simple movie watchlist app that stores the user’s list of movies in a JSON file. The app should allow you to:

* Load existing movies from a JSON file
* Add a new movie to the list
* Save the updated list back to the file

---

### 📝 **Your Tasks**

1. **Create a file named `movies.json`** with the following content:

```json
[
  {
    "title": "Inception",
    "year": 2010,
    "watched": true
  },
  {
    "title": "The Matrix",
    "year": 1999,
    "watched": false
  }
]
```

2. **Write a Python script named `watchlist.py`** that does the following:

* Loads the movie list from `movies.json` using `json.load`
* Asks the user to enter:

  * a new movie title
  * the release year
  * whether they have watched it (`yes`/`no`)
* Adds the new movie as a dictionary to the list
* Saves the updated list back to `movies.json` using `json.dump` with indentation

3. When displaying the movie list, mark movies as ✅ (watched) or ❌ (not watched).

---

### ✅ Bonus Challenge

* Add a function that lets the user mark a movie as "watched" by typing its title.
* Use `json.load()` and `json.dump()` to persist that change.

