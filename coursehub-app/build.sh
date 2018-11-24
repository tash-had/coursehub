ng build --prod --output-path dist --base-href "/"
cd dist/
cp index.html 404.html
echo "https://coursehub.ca" > CNAME
cd ../