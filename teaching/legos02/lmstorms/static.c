#include "conio.h"

int x = 44;

int main(void) {
  lcd_int(x);
  lcd_refresh();
  x++;
  delay(1000);
  return 0;
}