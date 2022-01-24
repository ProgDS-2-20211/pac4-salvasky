from trax import stats as st

# Cridem la funció basic_stats per mostrar els indicadors desitjats:
met_energy = st.basic_stats('data/tracks.csv', 'energy', 'Metallica')

# Mostrem els resultats per pantalla:
print(f'Metallica\'s tracks have the following energy scores:'
      f'\n minimum: {met_energy[0]}'
      f'\n maximum: {met_energy[1]}'
      f'\n mean: {met_energy[2]}')

# Cridem la funció stat_by_album per generar el gràfic que se'ns demana:
st.stat_by_album('data/tracks.csv', 'danceability', 'Coldplay')
