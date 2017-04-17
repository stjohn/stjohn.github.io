#include "conio.h"
#include "direct-button.h"
#include "direct-motor.h"
#include "direct-sensor.h"
#include "unistd.h"
#include "sys/tm.h"

#define MAX_TASKS 32
pid_t pid[MAX_TASKS];
int task_index;

#define BACK_TIME 500
#define TURN_TIME 800

// Motor commands.
#define COMMAND_NONE -1
#define COMMAND_FORWARD 1
#define COMMAND_REVERSE 2
#define COMMAND_LEFT 3
#define COMMAND_RIGHT 4
#define COMMAND_STOP 5

int avoid_command;

int avoid(int argc, char **argv) {
  avoid_command = COMMAND_NONE;
  while(1) {
    if (SENSOR_1 < 0xf000) {
      avoid_command = COMMAND_REVERSE;
      msleep(BACK_TIME);
      avoid_command = COMMAND_RIGHT;
      msleep(TURN_TIME);
      avoid_command = COMMAND_NONE;
    }
    if (SENSOR_3 < 0xf000) {
      avoid_command = COMMAND_REVERSE;
      msleep(BACK_TIME);
      avoid_command = COMMAND_LEFT;
      msleep(TURN_TIME);
      avoid_command = COMMAND_NONE;
    }
  }
  return 0;
}

#define RAW_DARK 0x7c00
#define RAW_LIGHT 0x6000

int process_light(int raw) {
  long big = 100 * ((long)raw - RAW_LIGHT);
  long percent = big / (RAW_DARK - RAW_LIGHT);
  return 100 - (int)percent;
}

int seek_command;

#define FUDGE 5

int wait_for_better(int baseline, unsigned long milliseconds) {
  int current;
  int saved_time = sys_time;
  do {
    msleep(50);
    current = process_light(SENSOR_2);
    lcd_int(current * 100 + baseline);
    lcd_refresh();
  } while (sys_time < (saved_time + milliseconds)
      && current < (baseline + FUDGE));
  if (current >= (baseline + FUDGE)) return current;
  return -1; // Timed out.
}

int seek_enlightenment(int argc, char **argv) {
  int baseline, current, loop_count, result;
  
  seek_command = COMMAND_NONE;
  
  // Get a baseline.
  baseline = process_light(SENSOR_2);
  
  loop_count = 0;
  
  while(1) {
    msleep(50); // Slow things down a little.
    // Every so often, increase the baseline.
    if (++loop_count == 5) {
      if (baseline < 100) baseline++;
      loop_count = 0;
    }
    current = process_light(SENSOR_2);
    lcd_int(current * 100 + baseline);
    lcd_refresh();
    // If the current value is somewhat less than the baseline...
    if (current < (baseline - FUDGE)) {
      // Set the baseline from the current value.
      baseline = current;
      // Search for something better.
      if (sys_time % 2 == 0) seek_command = COMMAND_LEFT;
      else seek_command = COMMAND_RIGHT;
      result = wait_for_better(baseline, 1000);
      if (result == -1) {
        // If that timed out, search back the other direction.
        if (seek_command == COMMAND_LEFT) seek_command = COMMAND_RIGHT;
        else if (seek_command == COMMAND_RIGHT) seek_command = COMMAND_LEFT;
        result = wait_for_better(baseline, 2000);
        if (result != -1) baseline = result;
        // If there's nothing better, bail.
      }
      // Set the new baseline.
      else baseline = result;
    }
    // Relinquish control.
    seek_command = COMMAND_NONE;
  }
  return 0;
}

int cruise_command;

int cruise(int argc, char **argv) {
  cruise_command = COMMAND_FORWARD;
  while (1) sleep(1);
  return 0;
}

int motor_command;

void motor_control() {
  motor_a_speed(MAX_SPEED);
  motor_c_speed(MAX_SPEED);

  switch (motor_command) {
    case COMMAND_FORWARD:
      motor_a_dir(fwd);
      motor_c_dir(fwd);
      break;
    case COMMAND_REVERSE:
      motor_a_dir(rev);
      motor_c_dir(rev);
      break;
    case COMMAND_LEFT:
      motor_a_dir(rev);
      motor_c_dir(fwd);
      break;
    case COMMAND_RIGHT:
      motor_a_dir(fwd);
      motor_c_dir(rev);
      break;
    case COMMAND_STOP:
      motor_a_dir(brake);
      motor_c_dir(brake);
      break;
    default:
      break;
  }
}

int arbitrate(int argc, char **argv) {
  while(1) {
    if (avoid_command != COMMAND_NONE) cputc('a', 0);
    else if (seek_command != COMMAND_NONE) cputc('s', 0);
    else if (cruise_command != COMMAND_NONE) cputc('c', 0);
    else cputc(' ', 0);
    lcd_refresh();
  
    if (cruise_command != COMMAND_NONE) motor_command = cruise_command;
    if (seek_command != COMMAND_NONE) motor_command = seek_command;
    if (avoid_command != COMMAND_NONE) motor_command = avoid_command;
    motor_control();
  }
}

int stop_task(int argc, char **argv) {
  int i;
  
  msleep(200);
  while (!PRESSED(button_state(), BUTTON_RUN))
    ;
  for (i = 0; i < task_index; i++)
    kill(pid[i]);
  return 0;
}

void exec_helper(int (*code_start)(int,char**)) {
  pid[task_index++] = execi(code_start, 0, NULL, 0, DEFAULT_STACK_SIZE);
}

int main() {
  task_index = 0;
  
  exec_helper(&avoid);
  exec_helper(&seek_enlightenment);
  exec_helper(&cruise);
  
  exec_helper(&arbitrate);
  
  execi(&stop_task, 0, NULL, 0, DEFAULT_STACK_SIZE);

  tm_start();
  
  return 0;
}