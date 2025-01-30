docker network ls

docker run -dit --name alpine1 alpine ash

docker run -dit --name alpine2 alpine ash

docker container ls

docker network inspect bridge

- go inside container

docker attach alpine1
ip addr show

ping -c 2 google.com
ping -c 2 172.17.0.3
ping -c 2 alpine2

docker container stop alpine1 alpine2
docker container rm alpine1 alpine2

-- creating my network

docker network create --driver bridge alpine-net

docker network ls
docker network inspect alpine-net

4 dockers

docker run -dit --name alpine1 --network alpine-net alpine ash

docker run -dit --name alpine2 --network alpine-net alpine ash

docker run -dit --name alpine3 alpine ash

docker run -dit --name alpine4 --network alpine-net alpine ash

soit connect apres
docker network connect bridge alpine4

soit avant avec
docker run -dit --name alpine4 --network alpine-net --network bridge alpine ash

docker container ls

docker network inspect bridge

docker network inspect alpine-net

docker container attach alpine1
ping -c 2 alpine2
ping -c 2 alpine4
ping -c 2 alpine1

ping -c 2 alpine3
ping -c 2 172.17.0.2

le network et isolé a par le autre
CTRL + p CTRL + q

docker container attach alpine4
ping -c 2 alpine1
ping -c 2 alpine2

pourquoi avec le nom il marche pas mais avec le ip il marche?
ping -c 2 alpine3
ping -c 2 172.17.0.2

ping -c 2 alpine4

docker container stop alpine1 alpine2 alpine3 alpine4
docker container rm alpine1 alpine2 alpine3 alpine4
docker network rm alpine-net