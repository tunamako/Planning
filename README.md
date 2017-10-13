# General layout of data flow with required jobs

## Station/feeder
  Hardware sensors and data collection
  
    Temperature
    
    Mass
    
    Picture
    
    Date and Time
    
  Arduino will store data temporarily and transmit in batches

## Parts List
### Birdfeeder
  * $35.14 [Pi 3](https://www.amazon.com/gp/product/B01CD5VC92/)
  
  * $28.50 [LoRa radio](https://www.amazon.com/distance-wireless-Expansion-Board-Raspberry/dp/B01M7V7PRL)
  
  * $12.90 [RFID Reader](http://www.robotshop.com/en/seeedstudio-grove-125khz-rfid-reader.html?gclid=EAIaIQobChMIjebekuTt1gIV1VmGCh08gAaREAQYBiABEgKjxPD_BwE)
  
  * $14.99 [ADC (battery voltage)](https://www.abelectronics.co.uk/p/69/ADC-Pi-Zero-Raspberry-Pi-Analogue-to-Digital-converter)
  
  * $17.91 [Weather sensor](https://www.amazon.com/gp/product/B013W1AJUY/)
  
  * (Optional) $9.99 [AC Adapter](https://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Charger/dp/B00MARDJZ4)
  
  * (Optional) $27.99 [Solar Charger](https://www.amazon.com/gp/product/B01MYMJP6M)
### Central/Intermediary Pi Node
  * $35.14 [Pi 3](https://www.amazon.com/gp/product/B01CD5VC92/)
  
  * $28.50 [LoRa radio](https://www.amazon.com/distance-wireless-Expansion-Board-Raspberry/dp/B01M7V7PRL)

  * $439 [LTE Module](https://www.cooking-hacks.com/4g-gps-3g-gprs-gsm-gps-lte-wcdma-hspa-shield-for-arduino)

  * (Optional) $9.99 [AC Adapter](https://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Charger/dp/B00MARDJZ4)

  * (Optional) $27.99 [Solar Charger](https://www.amazon.com/gp/product/B01MYMJP6M/)
  
## LTE module
  Register with NMU's network
## Pi stack/reciever
  Constantly listen for data, have connected to Euclid. Relays weather data to [OpenWeatherMap](http://openweathermap.com/)
## Data storage on Euclid
  Create a euclid account for our purposes
  
  Database design
## Webpage display
  Read from database
  
  Use [Leaflet](http://leafletjs.com/)
