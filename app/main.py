"""
import utils # al importarlo podemos comenzar a ejecutarlo
import read_csv
import charts

def run() :
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x ['Country'], data))
  percentages = list(map(lambda x: x ['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  
  country = input('Type your country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0 :
    country = result[0] #para tomar la primera lista que me mande, que en si solo deberia mandarme una :v
    print(country)
    lebels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], lebels, values)

  
  # Esto se conoce como modulizar nuestra app y poder reutilizar código desde archivos
  #print(result)

  
# Ejecutarllo como scrip y como módulo
if __name__ == 'main' : 
  
  run()"""
"""
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  '''
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''

if __name__ == '__main__':
  run()"""


import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
  

if __name__ == '__main__':
  run()