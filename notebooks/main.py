

#1.entendimiento

#2.calidad
#completitud por columnas
df.isNull().sum()
df.isna().sum()

#unicidad
#totales
df.duplicated().sum()
#parciales
df.duplicated(subset=['id']).sum() #solo revisa los que tengan mismo id

#consistencia
#validez
 