/*
 * Blog Eletrogate - Como conectar o Arduino com Python
 * Miguel Sena
 * blog.eletrogate.com
 */


void setup() {
  Serial.begin(9600);                       //Inicia o Monitor Serial
  pinMode(3, INPUT_PULLUP);                 //Define o pino como entrada
}

void loop() {
  int estado = digitalRead(3);              //Defina uma variável que realizará a leitura do botão

  if (estado == LOW) {                      //Verifica se o botão for pressionado
    Serial.println("Botao pressionado");    //Imprime a mensagem no monitor serial
    delay(1000);                            //Delay de 1 segundo
  }
}