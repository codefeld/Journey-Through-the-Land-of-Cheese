docker build --platform linux/amd64 -t journey-thru-land-of-cheese .
docker tag journey-thru-land-of-cheese registry.heroku.com/journey-thru-land-of-cheese/web
docker push registry.heroku.com/journey-thru-land-of-cheese/web
heroku container:release web
