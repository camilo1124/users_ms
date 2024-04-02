Instrucciones

guia de las propiedades igual suministro los comandos necesariios ;)

'NAME': 'users_db',
        'USER': 'postgres',
        'PASSWORD': 'contrasena',
        'HOST': 'localhost',
        'PORT': '5432',


Empezar con 

docker build -t users_ms . (como en el lab xd)

docker run -p 4000:4000 -e DB_HOST=172.17.0.2 -e DB_PORT=5432 -e DB_USER=postgres -e DB_PASSWORD=contrasena -e DB_NAME=users_db -e URL=0.0.0.0:4000 users_ms 

para la base de datos 

docker run --name some-postgres2 -p 5432:5432 -e POSTGRES_PASSWORD=contrasena -d postgres

¡Es importante crear la base de datos users_db sino paila!
yo use la extension database client de vscode
CREATE DATABASE users_db