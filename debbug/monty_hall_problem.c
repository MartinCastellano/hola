
#include <stdio.h> 
#include <stdlib.h>
// #include<math.h>

/* Create a program that performs a numerical calculation of the Monty Hall problem​.
You don’t need to implement a formula, but a simulation of the game with a random
generator. Then, run thousands or millions of games to estimate the chance to win the
prize either staying or switching the door.
Please implement this solution in the C language. Feel free to add as many features as
you want. We will value the quality and clarity of your code.
*/
// gcc -g -Og -std=gnu99 findbug_fixed.c -o nombre
// valgrind --leak-check=full ./nombre "hola como va"
int main(){
    
    double games = 1000000; 
    double staying=0;
    double switching=0;

    for (int i = 0 ; i <games;i++){

        int first_option = (rand() % 3) + 1; // generate first option door by random
        int price_location = (rand() % 3) + 1; //generate the price location by  random
        int flag = 0; // the flag is just to break the while
        while(flag == 0){

            int eliminate = (rand() % 3) + 1; // the prensetator eliminate a door where we can find a goat 
            if (eliminate != first_option && eliminate != price_location){

                if (first_option == price_location){
                    //add 1 to a counter if we stay with the door
                    staying = staying +1 ;
                }else{
                    // add 1 to a counter if we switch the door
                    switching = switching +1;
                }                                       
                flag = 1; // changue the value of the flag to break the while

            }   
                

        }   
            

    }
    
    // print the result aprox for X_games 
    printf("Wins with switching door: %.2f%%\nWins if I stay with the same door: %.2f%%\n", (switching*100/games),(staying*100/games));    
     
}
