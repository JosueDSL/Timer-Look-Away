## TIMER LOOK AWAY ##

This code was added to the System Service to start on boot as follows:                                         
   1. Create a new service file in /etc/systemd/system, as /etc/systemd/system/timer_lookaway.service.
   2. In the service file, included some information about the service:
        [Unit]
        Description= Timer to remind me to look away every "n" minutes using a Python Script.

        [Service]
        ExecStart=/usr/bin/python3 /home/joxulds/CS50/Timer-LookAway/timer_lookaway.py

        [Install]
        WantedBy=multi-user.target

   3. Save and close the file.

   4. Enable the service with the command sudo systemctl enable my_script.service. This will make the service start on boot.

   5. Start the service now with the command sudo systemctl start my_script.service.

To stop the service, you can use sudo systemctl stop my_script.service. To disable it from starting on boot, use sudo systemctl disable my_script.service.