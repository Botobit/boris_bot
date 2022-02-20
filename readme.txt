#/etc/systemd/system/borisbot.service

[Unit]
Description=BORIS BOT
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/administrator/boris_bot
ExecStart=/home/administrator/boris_bot/bot.py
KillMode=process
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
