-- PART I: Music Database

CREATE TABLE IF NOT EXISTS artists(id TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS albums(id TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS aongs(id TEXT NOT NULL);

CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY ASC,
    artist_name TEXT NOT NULL,
);

CREATE TABLE albums (
    album_id INTEGER PRIMARY KEY ASC,
    album_name TEXT NOT NULL,
    artist_id INTEGER NOT NULL REFERENCES artists(artist_id),
);

CREATE TABLE aongs (
    song_id INTEGER PRIMARY KEY ASC,
    song_name TEXT NOT NULL,
    album_id INTEGER NOT NULL REFERENCES albums(album_id),
    artist_id INTEGER NOT NULL REFERENCES artists(artist_id),
    track_number INTEGER NOT NULL,
    track_lenght INTEGER
);
