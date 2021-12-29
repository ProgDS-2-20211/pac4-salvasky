from trax import read_data as rd

p = rd.get_column_pandas('csv_files/albums_norm.csv', 'album_id')
c = rd.get_column_csv('csv_files/albums_norm.csv', 'album_id')

print(p[:2])
print(c)
