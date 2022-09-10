-- lists all shows in hbtn_0d_tvshows with at least one genre linked
SELECT tv.title, show.genre_id FROM tv_shows AS tv INNER JOIN tv_show_genres AS show ON tv.id = show.show_id ORDER BY tv.title ASC, show.genre_id ASC;
