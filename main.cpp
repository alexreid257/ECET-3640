#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

using namespace std;

void ledon(int);
void ledoff(int);
int getchange();
string string_to_hex(const string&);

int main()
{
	//Initialize Variables

    int change;
    string binary;

    //LED Initialization feedback

    ledoff(0);
    ledoff(1);
    ledoff(2);
    ledoff(3);

    ledon(0);
    usleep(500000);
    ledoff(0);
    ledon(1);
    usleep(500000);
    ledoff(1);
    ledon(2);
    usleep(500000);
    ledoff(2);
    ledon(3);
    usleep(500000);
    ledoff(3);

    //Event tracker loop
    for(;;) {

    	//Get change
         change = getchange();

         //LED LOGIC
        	 if (change == 8) //Forwards
        	 {
        	         		       ledon(0);
        	         		       ledoff(1);
        	 }
        	 else if(change == 24) //Backwards
        	 {
        	         		       ledon(1);
        	         		       ledoff(0);
        	 }
        	 else if(change == 40) //Left
        	 {
        	         		       ledon(2);
        	         		       ledoff(3);
        	 }
        	 else if(change == 56) //Right
        	 {
        	         		       ledon(3);
        	         		       ledoff(2);
        	 }
        	 else
        	 {
        		 cout << "CRITICAL ERROR" << endl;
        	 }//end if
         //}//end for

    }//end for
    return 0;
}//end main




void ledon(int led){
    //LED initialization (create handles, associate with files)
	//cout << "LED " << led << "ON" << endl;
    int lednum = led;
    FILE *LED0Handle = NULL;
        const char *LED0Brightness="/sys/class/leds/beaglebone:green:usr0/brightness";
    FILE *LED1Handle = NULL;
        const char *LED1Brightness="/sys/class/leds/beaglebone:green:usr1/brightness";
    FILE *LED2Handle = NULL;
        const char *LED2Brightness="/sys/class/leds/beaglebone:green:usr2/brightness";
    FILE *LED3Handle = NULL;
        const char *LED3Brightness="/sys/class/leds/beaglebone:green:usr3/brightness";

    //Check LED number, write high/on to that LED
    if(lednum == 0){
        if((LED0Handle = fopen(LED0Brightness, "r+")) != NULL){
            fwrite("1", sizeof(char), 1, LED0Handle);
            fclose(LED0Handle);
        }
    }
    else if(lednum == 1){
        if((LED1Handle = fopen(LED1Brightness, "r+")) != NULL){
            fwrite("1", sizeof(char), 1, LED1Handle);
            fclose(LED1Handle);
        }
    }
    else if(lednum == 2){
        if((LED2Handle = fopen(LED2Brightness, "r+")) != NULL){
            fwrite("1", sizeof(char), 1, LED2Handle);
            fclose(LED2Handle);
        }
    }
    else if(lednum == 3){
        if((LED3Handle = fopen(LED3Brightness, "r+")) != NULL){
            fwrite("1", sizeof(char), 1, LED3Handle);
            fclose(LED3Handle);
        }
    }
    else{cout << 'LED ERROR' << endl;}
    }


void ledoff(int led){
    //LED initialization (create handles, associate with files)
	//cout << "LED " << led << "OFF" << endl;
    int lednum = led;
    FILE *LED0Handle = NULL;
        const char *LED0Brightness="/sys/class/leds/beaglebone:green:usr0/brightness";
    FILE *LED1Handle = NULL;
        const char *LED1Brightness="/sys/class/leds/beaglebone:green:usr1/brightness";
    FILE *LED2Handle = NULL;
        const char *LED2Brightness="/sys/class/leds/beaglebone:green:usr2/brightness";
    FILE *LED3Handle = NULL;
        const char *LED3Brightness="/sys/class/leds/beaglebone:green:usr3/brightness";

    //Check LED number, write low/off to that LED
    if(lednum == 0){
        if((LED0Handle = fopen(LED0Brightness, "r+")) != NULL){
            fwrite("0", sizeof(char), 1, LED0Handle);
            fclose(LED0Handle);
        }
    }
    else if(lednum == 1){
        if((LED1Handle = fopen(LED1Brightness, "r+")) != NULL){
            fwrite("0", sizeof(char), 1, LED1Handle);
            fclose(LED1Handle);
        }
    }
    else if(lednum == 2){
        if((LED2Handle = fopen(LED2Brightness, "r+")) != NULL){
            fwrite("0", sizeof(char), 1, LED2Handle);
            fclose(LED2Handle);
        }
    }
    else if(lednum == 3){
        if((LED3Handle = fopen(LED3Brightness, "r+")) != NULL){
            fwrite("0", sizeof(char), 1, LED3Handle);
            fclose(LED3Handle);
        }
    }
    else{cout << 'LED ERROR' << endl;}
    }

int getchange(){

    ifstream eventfile ("/dev/input/mouse0");
    int i;
    i = eventfile.get();
    return i;
}

