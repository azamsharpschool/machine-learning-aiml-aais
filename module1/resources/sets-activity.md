### Exercise: Managing Club Memberships with Python Sets

**Objective:**
The purpose of this exercise is to practice using Python sets to manage and manipulate data related to club memberships. Students will use sets to handle membership lists, find common and unique members, and perform various set operations.

**Duration:**
30 minutes

---

### Exercise Tasks

#### 1. Create Membership Sets

**Task:**
Create sets representing the members of three different clubs: "Book Club", "Music Club", and "Sports Club". Each set should contain the names of the members.

**Example:**
```python
book_club = {"Alice", "Bob", "Charlie", "David"}
music_club = {"Bob", "Eve", "Frank", "Charlie"}
sports_club = {"Alice", "George", "Hannah", "Frank"}
```

#### 2. Find Common Members

**Task:**
Find and print the members who belong to both the "Book Club" and the "Music Club".

**Example Output:**
```
Common members between Book Club and Music Club: {Bob, Charlie}
```

#### 3. Find All Unique Members

**Task:**
Create a set that contains all the unique members across all three clubs and print the result.

**Example Output:**
```
All unique members across all clubs: {Alice, Bob, Charlie, David, Eve, Frank, George, Hannah}
```

#### 4. Find Members Unique to Each Club

**Task:**
Find and print the members who are only in the "Book Club" and not in the other two clubs.

**Example Output:**
```
Members only in Book Club: {David}
```

#### 5. Find Members in Exactly One Club

**Task:**
Find and print the members who are in exactly one of the three clubs.

**Example Output:**
```
Members in exactly one club: {David, Eve, George, Hannah}
```

#### 6. Remove a Member

**Task:**
Remove "Charlie" from the "Music Club" and print the updated set.

**Example Output:**
```
Music Club after removing Charlie: {Bob, Eve, Frank}
```

#### 7. Add New Members

**Task:**
Add new members "Ivan" and "Judy" to the "Sports Club" and print the updated set.

**Example Output:**
```
Sports Club after adding new members: {Alice, Frank, George, Hannah, Ivan, Judy}
```

### Additional Challenge (Optional)

**Task:**
Write a function `club_statistics` that takes three sets as input and returns a dictionary with the following keys and their respective values:
- "total_unique_members": Total number of unique members across all clubs.
- "common_members": Members common to all clubs.
- "unique_to_book_club": Members unique to the "Book Club".
- "unique_to_music_club": Members unique to the "Music Club".
- "unique_to_sports_club": Members unique to the "Sports Club".

**Example Output:**
```python
{
    "total_unique_members": 8,
    "common_members": {"Frank"},
    "unique_to_book_club": {"David"},
    "unique_to_music_club": {"Eve"},
    "unique_to_sports_club": {"George", "Hannah"}
}
```

