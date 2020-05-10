dashboard docker

sebelum menjalankan aplikasi ini harus install:
docker
python3
pip3
git

download aplikasi di:

$ git pull https://github.com/tonyal855/dashboard_docker.git

sebelum menjalankan aplikasi download dependency/library python dengan cara :

masuk ke directory aplikasi
terdapat file reqiurment.txt

$ pip3 install -r reqiurment.txt


rubah permision docker.sock agar tidak permision denied

linux:
$ sudo chmod -R 777 /var/run/docker.sock




untuk menjalankan aplikasi :
$ python3 manage.py runserver


akses localhost:8000 (default port)