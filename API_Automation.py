import json
import os
import requests
import pytest
from openpyxl import Workbook

######################################################################################
##Status code

def test_status_code(self):
	url='https://apiproxy.paytm.com/v2/movies/upcoming'
	response = requests.get(url)
	assert response.status_code == 200
	
#######################################################################################
##Movie release date:
def test_movie_release_date(self):
	url = 'https://apiproxy.paytm.com/v2/movies/upcoming'
	response = requests.get(url)
	json_response = json.loads(response.content)
	today_date = date.today().strftime('%Y-%m-%d')
	print(today_date)
	all_release_date = list(map(lambda x: x['releaseDate'], json_response['upcomingMovieData']))
	for release_date in all_release_date:
		if release_date is not None:
			assert release_date < today_date,"Release Date is before today’s date"
			
########################################################################################
##Movie Poster URL:
def test_movie_poster_url(self):
	url = 'https://apiproxy.paytm.com/v2/movies/upcoming'
	response = requests.get(url)
	json_response = json.loads(response.content)
	all_movie_url = list(map(lambda x: x['moviePosterUrl'], json_response['upcomingMovieData']))
	for url in all_movie_url:
    filename, file_extension = os.path.splitext(url)
    assert file_extension == '.jpg',"found other format {}".format(file_extension)
	
#########################################################################################	
##Paytm movie code:	
def test_paytm_movie_code(self):	
	unique_list = []
	url = 'https://apiproxy.paytm.com/v2/movies/upcoming'
	response = requests.get(url)
	json_response = json.loads(response.content)
	all_movie_code = list(map(lambda x: x['paytmMovieCode'], json_response['upcomingMovieData']))
	for movie_code in all_movie_code:
		if movie_code not in unique_list:
			unique_list.append(movie_code)
	for movie_code in unique_list:
        assert all_movie_code.count(movie_code) == 1, "movie Code found more than one for {}".format(all_movie_code.count(movie_code))

###########################################################################################
##No movie code should have more than 1 language format

url = 'https://apiproxy.paytm.com/v2/movies/upcoming'
response = requests.get(url)
json_response = json.loads(response.content)
all_movie_code = list(map(lambda x: x['paytmMovieCode'], json_response['upcomingMovieData']))
for movie_code in all_movie_code:
    assert re.match('^[a-zA-Z0-9_]+$',movie_code),"Found {} other than expected movie code format".format(movie_code)

###########################################################################################
##write down the name of all the movies (in an excel file) whose content available is 0.
def test_content(self):
	i=0
	wb = Workbook()
	sheet = wb.active
	url = 'https://apiproxy.paytm.com/v2/movies/upcoming'
	response = requests.get(url)
	json_response = json.loads(response.content)
	response_count=len(list(map(lambda x: x['moviePosterUrl'], json_response['upcomingMovieData'])))
	device_disco = json.loads(json.dumps(json_response))
	while i <= response_count-1:
			if device_disco['upcomingMovieData'][i]['isContentAvailable'] < 1:
				print(device_disco['upcomingMovieData'][i]['movie_name'])
				sheet.cell(row=i+1, column=1).value = device_disco['upcomingMovieData'][i]['movie_name']
			i+=1
	wb.save("paytm.xlsx")