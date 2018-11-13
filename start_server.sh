cd coursehub-api/
echo "LOG: Killing web-api port"
app_port=`lsof -t -i :5000 -s TCP:LISTEN`
kill $app_port
export FLASK_APP=app.py                        
flask run