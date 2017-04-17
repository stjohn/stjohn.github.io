#include "conio.h"

int main(void) {
  cputs("Hello");
  lcd_refresh();
  delay(1000);
  return 0;
}
