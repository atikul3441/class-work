%{
#include <stdio.h>
%}

%%
[-]?[0-9]+\.[0-9]+   { printf("Floating Point Number: %s\n", yytext); }
[-]?[0-9]+           { printf("Integer Number: %s\n", yytext); }

[ \t\n]+             ;   /* Ignore whitespace */

[a-zA-Z]+            { printf("Unknown word: %s\n", yytext); }
.                    { printf("Unknown symbol: %s\n", yytext); }
%%

int yywrap(void) {
    return 1;
}

int main(void) {
    printf("Enter numbers (e.g., 12.34, -55):\n");
    yylex();
    return 0;
}
