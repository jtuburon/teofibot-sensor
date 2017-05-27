cd /home/teo/tempviewer
nohup python run.py &
sleep 5
nohup python manage.py start_sensor &
cd