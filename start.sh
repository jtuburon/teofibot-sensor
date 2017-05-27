cd /home/$USER/teofibot-sensor
nohup python run.py &
sleep 5
nohup python manage.py start_sensor &
cd