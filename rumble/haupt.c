#include <stdio.h>
#include <stdlib.h>
#include "fahne.h"

#define Hauptroutine main
#define nichts void
#define Ganzzahl int
#define schleife(n) for (int i = n; i--;)
#define bitrverschieb(n, m) (n) >> (m)
#define diskreteAddition(n, m) (n) ^ (m)
#define wenn if
#define ansonsten else
#define Zeichen char
#define Zeiger *
#define Referenz &
#define Ausgabe(s) puts(s)
#define FormatAusgabe printf
#define FormatEingabe scanf
#define Zufall rand()
#define istgleich =
#define gleichbedeutend ==

void main(void) {
    int i = 1804289383;
    int k = 13;
    int e;
    int * p = & i;

    printf("%d\n", i);
    fflush(stdout);
    scanf("%d %d", & k, & e);

    (int i = 7; i--;)
        k = * p >> k % 3;

    k = k ^ e;

    if(k == 53225)
        puts(Fahne);
    else
        puts("War wohl nichts!");
}
