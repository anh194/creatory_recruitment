# Creatory Recruitment test

Web application allows users to enter video ID. It returns videos information and latest measurement.

Since I do not have direct contact with the recruitment team, I have made assumptions:

* Users enter **video ID** in search box, instead of video name. 
	* I could not implement searching video name given time constraint. Youtube only allows API query by ID. Therefore to implement search by name, we need to build Youtube database by ourselves, which is not feasible for me at this time.

**Technology used:**
* *Flask*
* *React*
* *Sqlalchemy*

**Installation and run:**
* Install Flask dependencies in requirement.txt and React dependencies.
* Run `Flask run` in `backend` folder, which run on port `5000`
* Run `npm start` in `frontend` folder, which run on port `3000`

API and frontend:

Endpoint |  Content
------------ | -------------
localhost:3000 | The website
http://localhost:5000/video?video_id= | Video information
http://localhost:5000/measurement?video_id= | Video measurement
http://localhost:5000/channel?channel_id= | Channel Information


**What I could have done if I have more time?**

Properly using redis to save some data in cache, instead of making youtube api call every search. That can save time and scale better.


