#include "conio.h"
#include "direct-button.h"
#include "unistd.h"
#include "sys/tm.h"

pid_t pid;

int display_task(int argc, char **argv) {
  while(1) {
    cputs("Hello");
    lcd_refresh();
    sleep(1);
    cputs("nurse");
    lcd_refresh();
    sleep(1);
  }
  return 0;
}

int stop_task(int argc, char **argv) {
  msleep(200);
  while (!PRESSED(button_state(), BUTTON_RUN))
    ;
  kill(pid);
  return 0;
}

int main() {
  pid = execi(&display_task, 0, NULL, 0, DEFAULT_STACK_SIZE);
  execi(&stop_task, 0, NULL, 0, DEFAULT_STACK_SIZE);
  
  tm_start();
  
  return 0;
}