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
  * $35.14 [Pi 3](https://www.amazon.com/gp/product/B01CD5VC92/ref=ox_sc_act_title_2?smid=A30ZYR2W3VAJ0A&psc=1&pldnSite=1)
  
  * $28.50 [LoRa radio](https://www.amazon.com/Dragino-Raspberry-Lora-GPS_HAT-915MHz/dp/B0721JNGRS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1505929084&sr=1-1&keywords=raspberry+pi+LoRa&pldnSite=1)
  
  * $7.98 [RFID Reader](https://www.amazon.com/gp/aw/d/B01M7V7PRL/ref=pd_aw_sim_sbs_107_1?ie=UTF8&psc=1&refRID=3WZNSA5ME4KVVF93MXEH&dpPl=1&dpID=51OE1RNjOsL)
  
  * $14.99 [ADC (battery voltage)](https://www.abelectronics.co.uk/p/69/ADC-Pi-Zero-Raspberry-Pi-Analogue-to-Digital-converter)
  
  * $17.91 [Weather sensor](https://www.amazon.com/gp/product/B013W1AJUY/ref=ox_sc_act_title_3?smid=A19MRELPGC5OXX&psc=1&pldnSite=1)
  
  * (Optional) $9.99 [AC Adapter](https://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Charger/dp/B00MARDJZ4)
  
  * (Optional) $27.99 [Solar Charger](https://www.amazon.com/gp/product/B01MYMJP6M/ref=ox_sc_act_title_1?smid=A2Z6I2H487OQGL&psc=1&pldnSite=1)
### Central/Intermediary Pi Node
  * $35.14 [Pi 3](https://www.amazon.com/gp/product/B01CD5VC92/ref=ox_sc_act_title_2?smid=A30ZYR2W3VAJ0A&psc=1&pldnSite=1)
  
  * $28.50 [LoRa radio](https://www.amazon.com/Dragino-Raspberry-Lora-GPS_HAT-915MHz/dp/B0721JNGRS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1505929084&sr=1-1&keywords=raspberry+pi+LoRa&pldnSite=1)

  * $439 [LTE Module](https://www.cooking-hacks.com/4g-gps-3g-gprs-gsm-gps-lte-wcdma-hspa-shield-for-arduino)

  * (Optional) $9.99 [AC Adapter](https://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Charger/dp/B00MARDJZ4)

  * (Optional) $27.99 [Solar Charger](https://www.amazon.com/gp/product/B01MYMJP6M/ref=ox_sc_act_title_1?smid=A2Z6I2H487OQGL&psc=1&pldnSite=1)
  
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
