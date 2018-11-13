cd coursehub-app/
echo "LOG: Installing npm"
npm install
npm run e2e > e2e/log
cat e2e/log