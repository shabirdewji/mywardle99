#! /bin/bash
echo "Building mywardle99........" 
git init
git add .
git commit -m "Initial Commit"
heroku apps:destroy --confirm mywardle99 
heroku create mywardle99
git push heroku master
heroku ps:scale web=1
echo "Done mywardle99..........."