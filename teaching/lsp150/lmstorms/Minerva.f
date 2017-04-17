HEX

: initialize
  RCX_INIT
  SENSOR_INIT
  2 SENSOR_ACTIVE
  3 2 SENSOR_TYPE
  80 2 SENSOR_MODE
;

: showValue
  3002 SWAP 3001 LCD_NUMBER
  LCD_REFRESH
;

: sleep
  0 0 TIMER_SET
  BEGIN DUP 0 TIMER_GET = UNTIL
  DROP
;

DECIMAL

42 CONSTANT TURNAROUND_TIME
10 CONSTANT NUMBER_OF_SAMPLES

VARIABLE threshold
VARIABLE returnTime

: sensorValue
  BEGIN DUP SENSOR_READ 0= UNTIL
  SENSOR_VALUE
;

: calibrate
  0
  NUMBER_OF_SAMPLES 0 DO
    2 sensorValue +
    1 sleep
  LOOP
  NUMBER_OF_SAMPLES /
  threshold !
  threshold @ showValue
;

: forward 7 1 2 MOTOR_SET ;
: spin 7 2 2 MOTOR_SET ;
: stop 7 3 2 MOTOR_SET ;

: armGrab 7 1 0 MOTOR_SET ;
: armRelease 7 2 0 MOTOR_SET ;
: armStop 7 3 0 MOTOR_SET ;

: grab
  armGrab
  BEGIN 2 sensorValue 100 = UNTIL
  armRelease
  BEGIN 2 sensorValue 100 < UNTIL
  armStop
;

: release
  armRelease
  BEGIN 2 sensorValue 100 = UNTIL
  armGrab
  BEGIN 2 sensorValue 100 < UNTIL
  armStop
;

: turnAround
  spin
  TURNAROUND_TIME sleep
  stop
;

: seek
  forward
  0 1 TIMER_SET
  BEGIN 2 sensorValue threshold @ 3 - < UNTIL
  2 sleep
  1 TIMER_GET returnTime !
  stop
;

: return
  forward
  returnTime @ sleep
  stop
;

: retrieve
  seek
  grab
  turnAround
  return
  release
  turnAround
;

: Minerva
  initialize
  calibrate
  5 0 DO
    retrieve
  LOOP
;