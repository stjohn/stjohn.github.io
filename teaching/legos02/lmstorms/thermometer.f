HEX

: buttonState RCX_BUTTON DUP BUTTON_GET @ ;

: isRunButtonPressed buttonState 1 AND ;

: showTemperature
  3003 SWAP 3001 LCD_NUMBER
  LCD_REFRESH
;

: clear LCD_CLEAR LCD_REFRESH ;

: thermometer
  RCX_INIT
  SENSOR_INIT
  BUTTON_INIT
  2 1 SENSOR_TYPE
  A0 1 SENSOR_MODE
  BEGIN
    BEGIN
      1 SENSOR_READ 0=
    UNTIL
    1 SENSOR_VALUE
    showTemperature
    isRunButtonPressed
  UNTIL
  clear
;