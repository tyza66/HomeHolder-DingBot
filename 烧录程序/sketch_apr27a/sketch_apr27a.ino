#include <ESP8266WiFi.h>        // 本程序使用 ESP8266WiFi库
#include <ESP8266WiFiMulti.h>   //  ESP8266WiFiMulti库
#include <ESP8266WebServer.h>   //  ESP8266WebServer库

#include <OneWire.h> //Onewrie库
#include <DallasTemperature.h> //温度模块快捷库

#include <stdio.h> //标准输入输出库

#include <Servo.h> //控制舵机的库
 
ESP8266WiFiMulti wifiMulti;     // 建立ESP8266WiFiMulti对象,对象名称是 'wifiMulti'
 
ESP8266WebServer esp8266_server(80);// 建立网络服务器对象，该对象用于响应HTTP请求。监听端口（80）
 
Servo myservo;//舵机控制使用的对象

OneWire oneWire(D2); //检查温度的引脚
DallasTemperature sensors(&oneWire); //oneWire库要用的变量
void setup(void){
  Serial.begin(9600);   //启动串口通讯
  sensors.begin();      //初始化读取温度

  pinMode(A0,INPUT); //模拟信号读取的引脚 用于接收空气湿度的模拟信号
  pinMode(D3,OUTPUT); //用于控制洒水机的继电器
  pinMode(D1,INPUT);//用于检查是否存在光照

  digitalWrite(D3,LOW);//初始化洒水机默认关闭

  myservo.attach(D5,500,2500);//设置舵机控制端所在引脚和舵机信号位的频率范围（单位：μs）
  myservo.write(15);//设置转动度数为10
  
  wifiMulti.addAP("FOREVER WIFI HUB 5 4G", "hellohello888"); // 将需要连接的一系列WiFi ID和密码输入这里
  Serial.println("Connecting ...");                            // 则尝试使用此处存储的密码进行连接。
  
  int i = 0;                                 
  while (wifiMulti.run() != WL_CONNECTED) {  // 此处的wifiMulti.run()是重点。通过wifiMulti.run()，NodeMCU将会在当前
    delay(1000);                             // 环境中搜索addAP函数所存储的WiFi。如果搜到多个存储的WiFi那么NodeMCU
    Serial.print(i++); Serial.print(' ');    // 将会连接信号最强的那一个WiFi信号。
  }                                          // 一旦连接WiFI成功，wifiMulti.run()将会返回“WL_CONNECTED”。这也是
                                             // 此处while循环判断是否跳出循环的条件。
  
  // WiFi连接成功后将通过串口监视器输出连接成功信息 
  Serial.println('\n');
  Serial.print("Connected to ");
  Serial.println(WiFi.SSID());              // 通过串口监视器输出连接的WiFi名称
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());           // 通过串口监视器输出ESP8266-NodeMCU的IP
 
  esp8266_server.begin();                           // 启动网站服务
  esp8266_server.on("/", HTTP_GET, handleRoot);     // 设置服务器根目录即'/'的函数'handleRoot'
  esp8266_server.on("/wd", HTTP_GET, getWenDu);  // 设置处理LED控制请求的函数'handleLED'
  esp8266_server.on("/sd", HTTP_GET, getShiDu);
  esp8266_server.on("/wo", HTTP_GET, oneOpen);
  esp8266_server.on("/wc", HTTP_GET, oneClose);
  esp8266_server.on("/ld", HTTP_GET, getLiangDu);
  esp8266_server.on("/kd", HTTP_GET, openLight);
  esp8266_server.on("/gd", HTTP_GET, closeLight);
  esp8266_server.onNotFound(handleNotFound);        // 设置处理404情况的函数'handleNotFound'
 
  Serial.println("HTTP esp8266_server started");//  告知用户ESP8266网络服务功能已经启动
}

void loop(void){
  esp8266_server.handleClient();                     // 检查http服务器访问
}

//测试连通
void handleRoot() {       
  esp8266_server.send(200, "text/plain", "success");
}

//获取温度
void getWenDu() {                          
  sensors.requestTemperatures(); // 发送命令获取温度
  Serial.println("Get WenDu Done");
  float wd = sensors.getTempCByIndex(0);
  char str[7]; 
  sprintf(str, "%.2f", wd); // 将num转换为字符数组 
  esp8266_server.send(200, "text/plain", str); //返回温度的值
}

//获取湿度
void getShiDu(){
  float data=analogRead(A0);
  float i=data/1023;
  float j=(1-i)*100;
  char str[7]; 
  sprintf(str, "%.2f", j); // 将num转换为字符数组 
  esp8266_server.send(200, "text/plain", str); //返回温度的值
}

//打开设备
void oneOpen(){
  digitalWrite(D3,HIGH);
  esp8266_server.send(200, "text/plain", "OK");
}

//关闭设备
void oneClose(){
  digitalWrite(D3,LOW);
  esp8266_server.send(200, "text/plain", "OK");
}

//获取亮度的函数 有光亮返回true 没有光亮返回false
void getLiangDu(){
  boolean data= digitalRead(D1);
  if(data){
    esp8266_server.send(200, "text/plain", "false");
  }else{
    esp8266_server.send(200, "text/plain", "true");
  }
}

//开灯
void openLight(){
  myservo.write(42);
  esp8266_server.send(200, "text/plain", "OK");
}
//关灯
void closeLight(){
  myservo.write(18);
  esp8266_server.send(200, "text/plain", "OK");
}

// 设置处理404情况的函数'handleNotFound'
void handleNotFound(){
  esp8266_server.send(404, "text/plain", "404"); // 发送 HTTP 状态 404 (未找到页面) 并向浏览器发送文字 "404: Not found"
}