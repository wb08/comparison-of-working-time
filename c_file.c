#include <stdio.h>
#include <time.h>
int add_int(){
for (int i=0;i<2000000000;i++){
if (i%2==0){
  i++;}
}}

int main(){
  clock_t t;
  int f;
  t = clock();
  f = add_int();
  t = clock() - t;
  printf ("time of work: %f seconds.\n",t,((float)t)/CLOCKS_PER_SEC);
}
