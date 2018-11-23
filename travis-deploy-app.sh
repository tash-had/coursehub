echo "LOG: STARTING GITHUB PAGES DEPLOY"
cd coursehub-app/
sh deploy.sh
cd ../../
rm -rf coursehub-app/
git clone https://github.com/tash-had/coursehub-app.git
rm coursehub-app/*
cp -R project-team-19/coursehub-app/dist/* coursehub-app/
cd coursehub-app/
git add .
git commit -m "Auto-generated deploy `date +%Y%m%d%H%M%S`"
git push origin master
echo "LOG: COMPLETING GITHUB PAGES DEPLOY"
