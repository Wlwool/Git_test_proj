# Lesson 1 : SELECT queries 101
1. Find the title of each film
```sql
SELECT title FROM movies;
```
2. Find the director of each film
```sql
SELECT director FROM movies;
```
3. Find the title and director of each film
```sql
SELECT title, director FROM movies;
```
4. Find the title and year of each film
```sql
SELECT title, year FROM movies;
```
5. Find all the information about each film
```sql
SELECT * FROM movies;
```

# Lesson 2 : Queries with constraints (Pt. 1)
1. Find the movie with a row id of 6
```sql
SELECT * FROM movies WHERE id = 6;
```
2. Find the movies released in the years between 2000 and 2010
```sql
SELECT * FROM movies WHERE year BETWEEN 2000 AND 2010;
```
3. Find the movies not released in the years between 2000 and 2010
```sql
SELECT * FROM movies WHERE year NOT BETWEEN 2000 AND 2010;
```
4. Find the first 5 Pixar movies and their release year
```sql
SELECT * FROM movies WHERE year LIMIT 5;
```

# Lesson 3 : Queries with constraints (Pt. 2)
1. Find all the Toy Story movies
```sql
SELECT title FROM movies WHERE title LIKE "Toy Story%";
```
2. Find all the movies directed by John Lasseter
```sql
SELECT title FROM movies WHERE director = "John Lasseter";
```
3. Find all the movies (and director) not directed by John Lasseter
```sql
SELECT title FROM movies WHERE director != "John Lasseter";
```
4. Find all the WALL-* movies
```sql
SELECT title FROM movies WHERE title LIKE "WALL-%"
```

# Lesson 4 : Filtering and sorting Query results
1. List all directors of Pixar movies (alphabetically), without duplicates
```sql
SELECT DISTINCT director FROM movies ORDER BY director;
```
2. List the last four Pixar movies released (ordered from most recent to least)
```sql
SELECT DISTINCT title FROM movies ORDER BY year DESC LIMIT 4;
```
3. List the first five Pixar movies sorted alphabetically
```sql
SELECT title FROM movies ORDER BY title LIMIT 5;
```
4. List the next five Pixar movies sorted alphabetically
```sql
SELECT title FROM movies ORDER BY title LIMIT 5 OFFSET 5;
```

# Lesson 5 : Review Simple SELECT Queries
1. List all the Canadian cities and their populations
```sql
SELECT city, population
FROM north_american_cities
WHERE country = "Canada";
```
2. Order all the cities in the United States by their latitude from north to south
```sql
SELECT city
FROM north_american_cities
WHERE country = "United States"
ORDER BY latitude DESC;
```
3. List all the cities west of Chicago, ordered from west to east
```sql
SELECT city
FROM north_american_cities
WHERE longitude < -87.629798
ORDER BY longitude;
```
4. List the two largest cities in Mexico (by population)
```sql
SELECT city
FROM north_american_cities
WHERE country = "Mexico"
ORDER BY population DESC
LIMIT 2;
```
5. List the third and fourth largest cities (by population) in the United States and their population
```sql
SELECT city
FROM north_american_cities
WHERE country = "United States"
ORDER BY population DESC
LIMIT 2 OFFSET 2;
```

# Lesson 6 : Multi-table queries with JOINs
1. Find the domestic and international sales for each movie
```sql
SELECT title, domestic_sales, international_sales
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
```
2. Show the sales numbers for each movie that did better internationally rather than domestically
```sql
SELECT title, domestic_sales, international_sales
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
WHERE international_sales > domestic_sales;
```
3. List all the movies by their ratings in descending order
```sql
SELECT title, rating
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
ORDER BY rating DESC;
```

# Lesson 7 : OUTER JOINs
1. Find the list of all buildings that have employees
```sql
SELECT DISTINCT building FROM employees;
```
2. Find the list of all buildings and their capacity
```sql
SELECT * FROM buildings;
```
3. List all buildings and the distinct employee roles in each building (including empty buildings)
```sql
SELECT DISTINCT building_name, role
FROM buildings
LEFT JOIN employees
    ON building_name = employees.building;
```

# Lesson 8 : A short note on NULLs
1. Find the name and role of all employees who have not been assigned to a building
```sql
SELECT name, role FROM employees WHERE building IS NULL;
```
2. Find the names of the buildings that hold no employees
```sql
SELECT DISTINCT building_name
FROM buildings
LEFT JOIN employees
    ON building_name = employees.building
WHERE employees.building IS NULL;
```

# Lesson 9 : Queries with expressions
1. List all movies and their combined sales in millions of dollars
```sql
SELECT DISTINCT
    title,
    (domestic_sales + international_sales) / 1000000 AS sales
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
```
2. List all movies and their ratings in percent
```sql
SELECT DISTINCT
    title,
    (rating * 10) AS rate_percent
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
```
3. List all movies that were released on even number years
```sql
SELECT title FROM movies WHERE year % 2 = 0;
```

# Lesson 10: Queries with aggregates (Pt. 1)
1. Find the longest time that an employee has been at the studio
```sql
SELECT MAX(Years_employed) FROM employees;
```
2. For each role, find the average number of years employed by employees in that role
```sql
SELECT Role, AVG(Years_employed) AS Average_Years FROM Employees GROUP BY Role;
```
3. Find the total number of employee years worked in each building
```sql
SELECT DISTINCT Building, SUM(Years_employed) FROM Employees
GROUP BY Building;
```

# Lesson 11: Queries with aggregates (Pt. 2)
1. Find the number of Artists in the studio (without a HAVING clause)
```sql
SELECT COUNT(*) FROM employees
WHERE Role LIKE "Artist";
```
2. Find the number of Employees of each role in the studio
```sql
SELECT DISTINCT Role, COUNT(*) FROM employees
GROUP BY Role;
```
3. Find the total number of years employed by all Engineers.
```sql
SELECT Role, SUM(Years_employed) FROM Employees
GROUP BY Role
HAVING Role = 'Engineer';
```

# Lesson 12: Order of execution of a Query
1. Find the number of movies each director has directed
```sql
SELECT Director, COUNT(Title) AS Amount_of_Movies FROM Movies
GROUP BY Director;
```
2. Find the total domestic and international sales that can be attributed to each director
```sql
SELECT Director, SUM(Domestic_sales + International_sales) AS Sales FROM Movies
INNER JOIN Boxoffice  ON
Movies.Id = Boxoffice.Movie_id
GROUP BY Director;
```

# Lesson 13: Inserting rows
1. Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)
```sql
INSERT INTO Movies VALUES (4, 'Toy Story 4', 'John Lasseter', 2000,101);
```
2. Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million
    domestically and 270 million internationally. Add the record to the BoxOffice table.
```sql
INSERT INTO Boxoffice VALUES(4,8.7,340000000,270000000);
```

# Lesson 14: Updating rows
1. The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
```sql
UPDATE Movies
SET Director = 'John Lasseter'
WHERE Id = 2;
```
OR
```sql
UPDATE Movies
SET Director = 'John Lasseter'
WHERE Title = "A Bug's Life";
```

2. The year that Toy Story 2 was released is incorrect, it was actually released in 1999
```sql
UPDATE Movies
SET Year = '1999'
WHERE Title = 'Toy Story 2'
```
3. Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3"
    and it was directed by Lee Unkrich
```sql
UPDATE Movies
SET Title = 'Toy Story 3', Director = 'Lee Unkrich'
WHERE Movies.Id = 11;
```

# Lesson 15: Deleting rows
1. This database is getting too big, lets remove all movies that were released before 2005.
```sql
DELETE FROM Movies WHERE Year < 2005;
```
2. Andrew Stanton has also left the studio, so please remove all movies directed by him.
```sql
DELETE FROM Movies WHERE Director = 'Andrew Stanton';
```

# Lesson 16: Creating tables
1. Create a new table named Database with the following columns:
– Name A string (text) describing the name of the database.
– Version A number (floating point) of the latest version of this database.
– Download_count An integer count of the number of times this database was downloaded.
This table has no constraints.
```sql
CREATE TABLE Database
(Name TEXT,
Version FLOAT,
Download_count INTEGER);
```

# Lesson 17: Altering tables
1. Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.
```sql
ALTER TABLE  Movies
  ADD Aspect_ratio FLOAT;
```
2. Add another column named Language with a TEXT data type to store the language that the movie
    was released in. Ensure that the default for this language is English.
```sql
ALTER TABLE Movies
  ADD COLUMN Language TEXT DEFAULT 'English';
```

# Lesson 18: Dropping tables
1. We've sadly reached the end of our lessons, lets clean up by removing the Movies table
```sql
DROP TABLE IF EXISTS Movies;
```
2. And drop the BoxOffice table as well
```sql
DROP TABLE IF EXISTS BoxOffice;
```
