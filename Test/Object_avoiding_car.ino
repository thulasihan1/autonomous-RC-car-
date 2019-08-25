const int rf= 2;
const int rb= 3;
const int lf= 4;
const int lb= 5;
float t; 
float d;

void setup() {
pinMode(lf, OUTPUT);
pinMode(lb, OUTPUT);
pinMode(rf, OUTPUT);
pinMode(rb, OUTPUT);
Serial.begin(9600); // Serial monitor is activated to monitor the distance.
  pinMode(10,OUTPUT); // Trig Pin of Ultrasonic sensor is activated on pin 10. 
  pinMode(13,INPUT); // Echo pin of Ultrasonic sensor is activated on pin 13. 

}

void loop() {
  digitalWrite(10,LOW);
delayMicroseconds(2);     // Writing a pulse to the Trigger pin. 
digitalWrite(10,HIGH);
delayMicroseconds(10);
digitalWrite(10,LOW);

t= pulseIn(13,HIGH);  
d=(t/2.)/29.154;     // Calculating distance between object and car
  
        if(d<= 20.00)    // If object is less than or equal to 20cm away from the car, the car will turn clockwise away from the object
        {
        digitalWrite(rf, LOW);
      digitalWrite(rb, HIGH);
       digitalWrite(lf, LOW);
        digitalWrite(lb, HIGH);
        delay(100);
          
        }

        else   // Else Car continues moving forward
        {
     digitalWrite(rf, LOW);
   digitalWrite(rb, HIGH);
    digitalWrite(lf, HIGH);
      digitalWrite(lb, LOW);
        }

        
        }
  
