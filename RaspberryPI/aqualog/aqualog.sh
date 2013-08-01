#!/bin/sh

### BEGIN INIT INFO
# Provides:        aqualog
# Required-Start:  $network $remote_fs $syslog
# Required-Stop:   $network $remote_fs $syslog
# Default-Start:   2 3 4 5
# Default-Stop:    0 1 6
# Short-Description: Start datacollector ethersex daemon
### END INIT INFO
PATH=/sbin:/bin:/usr/sbin:/usr/bin

. /lib/lsb/init-functions

DAEMON=/usr/local/bin/aqualog/main.py
PIDFILE=/var/run/aqualog.pid

test -x $DAEMON || exit 5

#if [ -r /etc/default/ntp ]; then
#        . /etc/default/ntp
#fi

#if [ -e /var/lib/ntp/ntp.conf.dhcp ]; then
#        NTPD_OPTS="$NTPD_OPTS -c /var/lib/ntp/ntp.conf.dhcp"
#fi


LOCKFILE=/var/lock/aqualog

lock_aqualog() {
        if [ -x /usr/bin/lockfile-create ]; then
                lockfile-create $LOCKFILE
                lockfile-touch $LOCKFILE &
                LOCKTOUCHPID="$!"
        fi
}

unlock_aqualog() {
        if [ -x /usr/bin/lockfile-create ] ; then
                kill $LOCKTOUCHPID
                lockfile-remove $LOCKFILE
        fi
}

RUNASUSER=pi
UGID=$(getent passwd $RUNASUSER | cut -f 3,4 -d:) || true
#if test "$(uname -s)" = "Linux"; then
#        NTPD_OPTS="$NTPD_OPTS -u $UGID"
#fi

case $1 in
        start)
                log_daemon_msg "Starting aqualog server" "aqualog"
                if [ -z "$UGID" ]; then
                        log_failure_msg "user \"$RUNASUSER\" does not exist"
                        exit 1
                fi
                lock_aqualog
                start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile $PIDFILE --chuid $RUNASUSER --startas $DAEMON
                status=$?
                unlock_aqualog
                log_end_msg $status
                ;;
        stop)
                log_daemon_msg "Stopping aqualog server" "aqualog"
                start-stop-daemon --stop --pidfile $PIDFILE --retry 10
                log_end_msg $?
                rm -f $PIDFILE
                ;;
        restart|force-reload)
                $0 stop && sleep 2 && $0 start
                ;;
        try-restart)
                if $0 status >/dev/null; then
                        $0 restart
                else
                        exit 0
                fi
                ;;
        reload)
                exit 3
                ;;
        status)
                status_of_proc $DAEMON "aqualog server"
                ;;
        *)
                echo "Usage: $0 {start|stop|restart|try-restart|force-reload|status}"
                exit 2
                ;;
esac
