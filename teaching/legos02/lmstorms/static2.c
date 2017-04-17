#include "conio.h"

int x;

int main(void) {
  x = 44;
  lcd_int(x);
  lcd_refresh();
  x++;
  delay(1000);
  return 0;
}