DRF-curs-habits

—борка с Dockerfile

docker build -t drf-curs-habits .
docker run --name drf-curs-habits --network host -d 92b4b8c9bc21cb0c1fd346831914ef643bcd5e0322626854d045c62227036c01

—борка с yaml файлом с запуском контейнера:

docker-compose up --build