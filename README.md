# To use the % operator for string interpolation, the following syntax is used:
# string % values
# user = "Abrar"
# age = "20"
# print("Hello %s. Your age is %s "%(user,age))
# %s: when we want the placeholder value to be a string
# %f: when we want the placeholder value to be a floating point decimal like 2.415
# %r: when we want to replace the placeholder with the raw data of a variable
# %x: when the value replacing the placeholder has to be a hexadecimal value
# %o: when the value replacing the placeholder has to be an octal value
# %c: when we want to replace the placeholder with special characters


# Docker
docker build -t python-docker .
docker run --name flower_shop --rm -p 5000:5000 python-docker:latest

docker run --name flower_shop --rm -it -p 5000:5000 python-docker:latest

docker run --rm --name flower_shop -p 5000:5000 python-docker:latest
docker inspect flower_shop --format '{{ .NetworkSettings.IPAddress }}'

docker run --name flower_shop  python-docker

# Docker Compose
docker compose build