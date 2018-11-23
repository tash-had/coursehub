setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

setup_git
echo "LOG: STARTING GITHUB PAGES DEPLOY"
cd coursehub-app/
sh build.sh
cd ../../
rm -rf coursehub-app/
git clone https://github.com/tash-had/coursehub-app.git
rm coursehub-app/*
cp -R project-team-19/coursehub-app/dist/* coursehub-app/
cd coursehub-app/
git add .
git commit -m "Auto-generated deploy $TRAVIS_BUILD_NUMBER `date +%Y%m%d%H%M%S`"
git remote 
git push origin master
echo "LOG: COMPLETING GITHUB PAGES DEPLOY"
