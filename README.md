# General layout of data flow with required jobs

## Station/feeder
  Hardware sensors and data collection
  
    Temperature
    
    Mass
    
    Picture
    
    Date and Time
    
  Arduino will store data temporarily and transmit in batches
  
## LTE module
  Register with NMU's network
## Pi stack/reciever
  Constantly listen for data, have connected to Euclid
## Data storage on Euclid
  Create a euclid account for our purposes
  
  Database design
## Webpage display
  Read from database
  
  Use Google maps API
